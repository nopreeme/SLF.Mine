"""
SLF.Mine Datapack Static Analysis Test Suite

Runs without a live Minecraft server. Catches the four categories of bugs
that caused regressions in previous sessions:

  1. Objectives loading  — invalid criteria syntax, missing registrations
  2. Class grant wiring  — ID collisions, missing guards, broken prerequisites
  3. Skill focus wiring  — tick dispatch ↔ focus files ↔ learn_focused ↔ learn files
  4. Menu syntax         — 1.21.5+ click_event format requirement

Usage:
  python3 -m unittest discover tests/        # stdlib runner
  python3 -m pytest tests/                   # once pytest is available
"""

import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data_pack/data/slf/function"
SETUP_F = DATA / "setup.mcfunction"
TICK_F = DATA / "skills/tick.mcfunction"
LEARN_FOCUSED_F = DATA / "skills/learn_focused.mcfunction"
GRANT_DIR = DATA / "class/grant"
FOCUS_DIR = DATA / "skills/focus"
LEARN_DIR = DATA / "skills/learn"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _all_mcfunction_texts() -> list[tuple[Path, str]]:
    return [(f, _read(f)) for f in ROOT.rglob("*.mcfunction")]


def _registered_objectives() -> set[str]:
    text = _read(SETUP_F)
    return {m.group(1) for m in re.finditer(r"scoreboard objectives add (\S+)", text)}


def _tick_class_dispatch() -> dict[int, str]:
    """choose_class trigger value → grant function name."""
    text = _read(TICK_F)
    pattern = re.compile(
        r"execute as @a if score @s slf\.choose_class matches (\d+)\s+run function slf:class/grant/(\w+)"
    )
    return {int(m.group(1)): m.group(2) for m in pattern.finditer(text)}


def _tick_focus_dispatch() -> dict[int, str]:
    """focus_choose trigger value → focus function name."""
    text = _read(TICK_F)
    pattern = re.compile(
        r"execute as @a if score @s slf\.focus_choose matches (\d+)\s+run function slf:skills/focus/(\w+)"
    )
    return {int(m.group(1)): m.group(2) for m in pattern.finditer(text)}


def _learn_focused_dispatch() -> dict[int, str]:
    """focus score value → learn function name."""
    text = _read(LEARN_FOCUSED_F)
    pattern = re.compile(
        r"execute if score @s slf\.focus matches (\d+)\s+run function slf:skills/learn/(\w+)"
    )
    return {int(m.group(1)): m.group(2) for m in pattern.finditer(text)}


def _class_ids() -> dict[str, int]:
    """grant file stem → class ID set by that file."""
    ids: dict[str, int] = {}
    for f in GRANT_DIR.glob("*.mcfunction"):
        m = re.search(r"scoreboard players set @s slf\.class (\d+)", _read(f))
        if m:
            ids[f.stem] = int(m.group(1))
    return ids


def _was_tags_added() -> set[str]:
    """All slf.was_* tags that any grant file adds."""
    tags: set[str] = set()
    for f in GRANT_DIR.glob("*.mcfunction"):
        for m in re.finditer(r"tag @s add (slf\.was_\w+)", _read(f)):
            tags.add(m.group(1))
    return tags


# ---------------------------------------------------------------------------
# 1. Setup / Scoreboard Tests
# ---------------------------------------------------------------------------

class TestSetup(unittest.TestCase):
    def setUp(self):
        self.text = _read(SETUP_F)
        self.objectives = _registered_objectives()

    def test_no_duplicate_objectives(self):
        names = re.findall(r"scoreboard objectives add (\S+)", self.text)
        counts = Counter(names)
        dupes = {n: c for n, c in counts.items() if c > 1}
        self.assertFalse(dupes, f"Duplicate scoreboard objectives in setup.mcfunction: {dupes}")

    def test_required_objectives_present(self):
        required = {
            "slf.class", "slf.choose_class", "slf.focus_choose",
            "slf.focus", "slf.focus_stat", "slf.sp", "slf.threshold",
            "slf.timer", "slf.level", "slf.exp", "slf.karma",
            "slf.sp_points", "slf.tmp", "slf.knight_trials",
            "slf.dmg_prev", "slf.move_prev", "slf.evade_prev", "slf.def_prev",
        }
        missing = required - self.objectives
        self.assertFalse(missing, f"Required objectives missing from setup.mcfunction: {missing}")

    def test_no_invalid_stat_criteria_prefix(self):
        # Old bug: 'stat.*' is not a valid scoreboard criterion in 1.21.x.
        # Valid vanilla motion criteria use 'minecraft.custom:minecraft.*'
        bad = re.findall(r"scoreboard objectives add \S+ stat\.\S+", self.text)
        self.assertFalse(bad, f"Invalid 'stat.*' criteria in setup.mcfunction: {bad}")

    def test_vanilla_criteria_use_correct_namespace(self):
        # All non-dummy/trigger criteria must use 'minecraft.custom:minecraft.*'
        lines = [ln for ln in self.text.splitlines()
                 if "scoreboard objectives add" in ln
                 and "dummy" not in ln
                 and "trigger" not in ln]
        for line in lines:
            self.assertIn("minecraft.custom:minecraft.", line,
                          f"Non-dummy/trigger criterion may be malformed: {line.strip()}")

    def test_stat_spend_triggers_registered(self):
        stat_names = ["str", "dex", "vit", "agi", "tec", "lck", "stm"]
        for stat in stat_names:
            trigger_obj = f"slf.stat_{stat}"
            self.assertIn(trigger_obj, self.objectives,
                          f"Stat spend trigger '{trigger_obj}' not registered in setup.mcfunction")

    def test_stat_value_objectives_registered(self):
        stat_names = ["str", "dex", "vit", "agi", "tec", "lck", "stm"]
        for stat in stat_names:
            value_obj = f"slf.stat.{stat}"
            self.assertIn(value_obj, self.objectives,
                          f"Stat value objective '{value_obj}' not registered in setup.mcfunction")


# ---------------------------------------------------------------------------
# 2. Class ID Tests
# ---------------------------------------------------------------------------

class TestClassIDs(unittest.TestCase):
    def setUp(self):
        self.ids = _class_ids()
        self.dispatch = _tick_class_dispatch()

    def test_no_duplicate_class_ids(self):
        counts = Counter(self.ids.values())
        dupes = {
            cid: [name for name, cid2 in self.ids.items() if cid2 == cid]
            for cid, count in counts.items() if count > 1
        }
        self.assertFalse(dupes, f"Duplicate slf.class IDs across grant files: {dupes}")

    def test_all_dispatched_t1_classes_have_ids(self):
        for trigger_val, class_name in self.dispatch.items():
            self.assertIn(class_name, self.ids,
                          f"T1 class '{class_name}' (choose_class={trigger_val}) has no slf.class assignment")

    def test_standard_t1_id_trigger_match(self):
        # The 6 base classes use trigger value == class ID
        expected = {1: "swordsman", 2: "warrior", 3: "bandit",
                    4: "priest", 5: "monk", 6: "mage"}
        for trigger_val, expected_class in expected.items():
            self.assertEqual(
                self.dispatch.get(trigger_val), expected_class,
                f"choose_class={trigger_val} should dispatch to '{expected_class}', "
                f"got '{self.dispatch.get(trigger_val)}'"
            )
            self.assertEqual(
                self.ids.get(expected_class), trigger_val,
                f"'{expected_class}' slf.class should be {trigger_val}, "
                f"got {self.ids.get(expected_class)}"
            )

    def test_brawler_ids(self):
        self.assertEqual(self.ids.get("fighter"), 20)
        self.assertEqual(self.ids.get("mercenary"), 30)
        self.assertEqual(self.dispatch.get(20), "fighter")
        self.assertEqual(self.dispatch.get(30), "mercenary")

    def test_shadow_tree_ids(self):
        # Bandit=3 (T1), Thief=50 (T2) — not colliding with assassin=16
        self.assertEqual(self.ids.get("bandit"), 3)
        self.assertEqual(self.ids.get("thief"), 50)
        self.assertEqual(self.ids.get("ninja"), 51)
        self.assertEqual(self.ids.get("assassin"), 16,
                         "assassin ID should be 16 (was previously colliding with star_shinobi_sei)")

    def test_star_shinobi_sei_id_not_colliding(self):
        # Was previously 16, colliding with assassin — fixed to 53
        sei_id = self.ids.get("star_shinobi_sei")
        assassin_id = self.ids.get("assassin")
        self.assertIsNotNone(sei_id, "star_shinobi_sei has no class ID")
        self.assertNotEqual(sei_id, assassin_id,
                            f"star_shinobi_sei and assassin share class ID {sei_id}")


# ---------------------------------------------------------------------------
# 3. T1 Grant File Pattern Tests
# ---------------------------------------------------------------------------

class TestT1GrantPattern(unittest.TestCase):
    # choose_class 41/42 (alignment choices) are T2+ — exempt from T1 rules
    ALIGNMENT_TRIGGERS = {41, 42}

    def setUp(self):
        self.dispatch = _tick_class_dispatch()
        self.t1_classes = {
            name for val, name in self.dispatch.items()
            if val not in self.ALIGNMENT_TRIGGERS
        }

    def _read_grant(self, class_name: str) -> str:
        f = GRANT_DIR / f"{class_name}.mcfunction"
        self.assertTrue(f.exists(), f"Grant file missing: {class_name}.mcfunction")
        return _read(f)

    def test_t1_grant_files_exist(self):
        for class_name in self.t1_classes:
            self.assertTrue(
                (GRANT_DIR / f"{class_name}.mcfunction").exists(),
                f"Grant file missing for T1 class '{class_name}'"
            )

    def test_t1_classes_have_class_chosen_guard(self):
        guard = 'execute if entity @s[tag=slf.class_chosen] run return fail'
        for class_name in self.t1_classes:
            text = self._read_grant(class_name)
            self.assertIn(guard, text,
                          f"{class_name}.mcfunction missing class_chosen guard")

    def test_t1_classes_set_class_chosen_tag(self):
        for class_name in self.t1_classes:
            text = self._read_grant(class_name)
            self.assertIn("tag @s add slf.class_chosen", text,
                          f"{class_name}.mcfunction does not add slf.class_chosen tag")

    def test_t1_classes_call_select_cleanup(self):
        for class_name in self.t1_classes:
            text = self._read_grant(class_name)
            self.assertIn("function slf:class/select_cleanup", text,
                          f"{class_name}.mcfunction missing select_cleanup call")

    def test_t2_classes_have_was_prerequisite_guards(self):
        # T2+ grant files that are NOT in the tick dispatch must guard with was_* tags.
        # Skip comment and blank lines to find the first actual command.
        dispatched = set(self.dispatch.values())
        for f in GRANT_DIR.glob("*.mcfunction"):
            if f.stem in dispatched:
                continue  # T1 or alignment — different guard pattern
            text = _read(f)
            first_cmd = next(
                (ln.strip() for ln in text.splitlines()
                 if ln.strip() and not ln.strip().startswith("#")),
                ""
            )
            self.assertIn('unless entity @s[tag=slf.was_', first_cmd,
                          f"{f.name}: T2+ class first command must be a was_* prerequisite guard, "
                          f"got: {first_cmd!r}")


# ---------------------------------------------------------------------------
# 4. Prerequisite Chain Tests
# ---------------------------------------------------------------------------

class TestPrerequisiteChains(unittest.TestCase):
    def setUp(self):
        self.was_tags = _was_tags_added()

    def test_all_guard_prerequisites_are_grantable(self):
        for f in GRANT_DIR.glob("*.mcfunction"):
            text = _read(f)
            for m in re.finditer(r'unless entity @s\[tag=(slf\.was_\w+)\]', text):
                prereq = m.group(1)
                self.assertIn(prereq, self.was_tags,
                              f"{f.name}: guard requires '{prereq}' but no grant file adds it")

    def test_shadow_tree_chain(self):
        # Bandit(T1) → {Thief, Ninja}(T2) → Assassin/Shinobi(T3)
        thief = _read(GRANT_DIR / "thief.mcfunction")
        self.assertIn('unless entity @s[tag=slf.was_bandit] run return fail', thief,
                      "thief.mcfunction must require was_bandit (Bandit → Thief)")

        ninja = _read(GRANT_DIR / "ninja.mcfunction")
        self.assertIn('unless entity @s[tag=slf.was_bandit] run return fail', ninja,
                      "ninja.mcfunction must require was_bandit (Bandit → Ninja)")

        assassin = _read(GRANT_DIR / "assassin.mcfunction")
        self.assertIn('unless entity @s[tag=slf.was_thief] run return fail', assassin,
                      "assassin.mcfunction must require was_thief (Thief → Assassin)")

        shinobi = _read(GRANT_DIR / "shinobi.mcfunction")
        self.assertIn('unless entity @s[tag=slf.was_ninja] run return fail', shinobi,
                      "shinobi.mcfunction must require was_ninja (Ninja → Shinobi)")

    def test_veteran_requires_mercenary(self):
        veteran = _read(GRANT_DIR / "veteran.mcfunction")
        self.assertIn('unless entity @s[tag=slf.was_mercenary] run return fail', veteran,
                      "veteran.mcfunction must require was_mercenary")

    def test_thief_sets_class_chosen(self):
        # Thief is T2 but still sets class_chosen (needed for skill focus/stat triggers)
        thief = _read(GRANT_DIR / "thief.mcfunction")
        self.assertIn("tag @s add slf.class_chosen", thief,
                      "thief.mcfunction must set class_chosen so skill focus triggers activate")

    def test_thief_calls_select_cleanup(self):
        thief = _read(GRANT_DIR / "thief.mcfunction")
        self.assertIn("function slf:class/select_cleanup", thief,
                      "thief.mcfunction must call select_cleanup to clear the menu UI")


# ---------------------------------------------------------------------------
# 5. Skill Focus Dispatch Tests
# ---------------------------------------------------------------------------

class TestSkillFocusDispatch(unittest.TestCase):
    def setUp(self):
        self.tick_focus = _tick_focus_dispatch()
        self.learn_focused = _learn_focused_dispatch()
        self.focus_files = {f.stem for f in FOCUS_DIR.glob("*.mcfunction")}
        self.learn_files = {f.stem for f in LEARN_DIR.glob("*.mcfunction")}

    def test_all_tick_focus_targets_exist(self):
        for trigger_val, focus_name in self.tick_focus.items():
            self.assertIn(focus_name, self.focus_files,
                          f"tick dispatches focus_choose={trigger_val} to '{focus_name}' "
                          f"but skills/focus/{focus_name}.mcfunction not found")

    def test_no_orphan_focus_files(self):
        dispatched = set(self.tick_focus.values())
        for name in self.focus_files:
            self.assertIn(name, dispatched,
                          f"skills/focus/{name}.mcfunction exists but has no tick dispatch entry")

    def test_all_focus_ids_have_learn_entries(self):
        for trigger_val, focus_name in self.tick_focus.items():
            self.assertIn(trigger_val, self.learn_focused,
                          f"focus_choose={trigger_val} ({focus_name}) has no entry in learn_focused.mcfunction")

    def test_all_learn_focused_targets_exist(self):
        for focus_id, learn_name in self.learn_focused.items():
            self.assertIn(learn_name, self.learn_files,
                          f"learn_focused dispatches focus={focus_id} to '{learn_name}' "
                          f"but skills/learn/{learn_name}.mcfunction not found")

    def test_focus_choose_trigger_registered(self):
        registered = _registered_objectives()
        self.assertIn("slf.focus_choose", registered,
                      "slf.focus_choose trigger not registered in setup.mcfunction")

    def test_no_orphan_learn_focused_entries(self):
        # Every learn_focused entry should correspond to a tick-dispatched focus ID
        tick_ids = set(self.tick_focus.keys())
        for focus_id in self.learn_focused:
            self.assertIn(focus_id, tick_ids,
                          f"learn_focused.mcfunction has entry for focus={focus_id} "
                          f"but that ID is not in tick focus dispatch")


# ---------------------------------------------------------------------------
# 6. Menu Syntax Tests (1.21.5+ format)
# ---------------------------------------------------------------------------

class TestMenuSyntax(unittest.TestCase):
    MENU_FILES = [
        DATA / "class/select.mcfunction",
        DATA / "skills/menu.mcfunction",
        DATA / "stats/menu.mcfunction",
    ]

    def test_no_legacy_clickevent_format(self):
        # Old format: "clickEvent":{"action":"...","value":"..."} — rejected in 1.21.5+
        # New format: "click_event":{"action":"...","command":"..."}
        for f in self.MENU_FILES:
            if not f.exists():
                continue
            text = _read(f)
            legacy = re.findall(r'"clickEvent"', text)
            self.assertFalse(legacy,
                             f"{f.name}: uses legacy 'clickEvent' (must be 'click_event' in 1.21.5+)")

    def test_no_legacy_hoverevent_format(self):
        for f in self.MENU_FILES:
            if not f.exists():
                continue
            text = _read(f)
            legacy = re.findall(r'"hoverEvent"', text)
            self.assertFalse(legacy,
                             f"{f.name}: uses legacy 'hoverEvent' (must be 'hover_event' in 1.21.5+)")

    def test_click_event_uses_command_key(self):
        # 1.21.5+ click_event uses "command" not "value"
        for f in self.MENU_FILES:
            if not f.exists():
                continue
            text = _read(f)
            if '"click_event"' not in text:
                continue
            # If click_event is present, it must not use the old "value" key
            legacy_value = re.findall(r'"click_event":\{"action":"[^"]+","value":', text)
            self.assertFalse(legacy_value,
                             f"{f.name}: click_event uses 'value' key (must be 'command' in 1.21.5+)")


# ---------------------------------------------------------------------------
# 7. Give Function Integrity
# ---------------------------------------------------------------------------

class TestGiveFunctions(unittest.TestCase):
    GIVE_DIR = DATA / "give"

    def test_all_referenced_give_functions_exist(self):
        # Grant files that call function slf:give/* — verify those files exist
        give_files = {f.stem for f in self.GIVE_DIR.glob("*.mcfunction")}
        for f in GRANT_DIR.glob("*.mcfunction"):
            text = _read(f)
            for m in re.finditer(r"function slf:give/(\w+)", text):
                give_name = m.group(1)
                self.assertIn(give_name, give_files,
                              f"{f.name}: calls function slf:give/{give_name} "
                              f"but give/{give_name}.mcfunction not found")

    def test_give_functions_use_custom_model_data_strings(self):
        # Custom weapon give functions should use the 1.21.4+ string-based custom_model_data
        weapon_gives = [f for f in self.GIVE_DIR.glob("*.mcfunction")
                        if not f.stem.startswith("armor_")]
        for f in weapon_gives:
            text = _read(f)
            if "custom_model_data" in text:
                self.assertIn('strings:["slf.', text,
                              f"{f.name}: custom_model_data should use strings array format "
                              f"(e.g. strings:[\"slf.item_name\"])")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=2)
