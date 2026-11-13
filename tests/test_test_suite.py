"""
Static checks for the in-game test suite (tools/gen_test_commands.py). No Minecraft needed.

  1. Every item the resource pack has a model for can be spawned with /function slf:give/<item>
  2. Every class has a one-click setup, and every button in /function slf:test/menu points at a real function
  3. The generated files are up to date with the generator (re-run it after adding items or classes)

Run: python -m unittest tests/test_test_suite.py
"""
import json, os, re, subprocess, sys, tempfile, shutil, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FN = ROOT / "data_pack" / "data" / "slf" / "function"
ITEM_DEFS = ROOT / "resource_pack" / "assets" / "minecraft" / "items"


def items():
    out = []
    for f in sorted(ITEM_DEFS.glob("*.json")):
        for c in json.loads(f.read_text(encoding="utf-8"))["model"]["cases"]:
            for w in (c["when"] if isinstance(c["when"], list) else [c["when"]]): out.append((f.stem, w[4:]))
    return out


def function_exists(ref):
    """In the main data pack or the separate weapons data pack (both use the slf namespace)."""
    ns, _, path = ref.partition(":")
    return any((ROOT / pack / "data" / ns / "function" / (path + ".mcfunction")).exists()
               for pack in ("data_pack", "weapons/java_out/SLF_Weapons_Datapack"))


class TestGiveCommands(unittest.TestCase):
    def test_every_item_can_be_given(self):
        missing = []
        for base, name in items():
            f = FN / "give" / f"{name}.mcfunction"
            if not f.exists(): missing.append(name); continue
            text = f.read_text(encoding="utf-8")
            self.assertRegex(text, rf"give @s (minecraft:)?{base}\[", f"give/{name} gives the wrong base item (model is on {base})")
            self.assertIn(f'"slf.{name}"', text, f"give/{name} does not set its custom_model_data string")
        self.assertEqual(missing, [], "items without a give command: run python tools/gen_test_commands.py")

    def test_given_names_are_text_not_json_strings(self):
        """item_name='{...}' (a quoted JSON string) shows up in game as literal JSON since 1.21.5."""
        for f in sorted((FN / "give").glob("*.mcfunction")):
            self.assertNotRegex(f.read_text(encoding="utf-8"), r"item_name\s*=\s*'", f.name)

    def test_kits_cover_every_item_and_fit_an_inventory(self):
        given = {}
        for f in (FN / "test" / "kit").glob("*.mcfunction"):
            names = re.findall(r"function slf:give/([a-z0-9_]+)", f.read_text(encoding="utf-8"))
            self.assertLessEqual(len(names), 36, f"{f.name} gives more items than an inventory holds")
            for n in names: given[n] = f.stem
        self.assertEqual(sorted({n for _, n in items()} - set(given)), [], "items in no kit")


class TestMenu(unittest.TestCase):
    def test_every_class_has_a_setup(self):
        classes = {f.stem for f in (FN / "class" / "grant").glob("*.mcfunction")}
        setups = {f.stem for f in (FN / "test" / "class").glob("*.mcfunction")}
        self.assertEqual(sorted(classes - setups), [])

    def test_every_menu_button_runs_something_real(self):
        text = (FN / "test" / "menu.mcfunction").read_text(encoding="utf-8")
        commands = re.findall(r'"command":"/([^"]+)"', text)
        self.assertGreater(len(commands), 50)
        for c in commands:
            m = re.match(r"function ([a-z0-9_.-]+:[a-z0-9_/.-]+)$", c)
            if m: self.assertTrue(function_exists(m.group(1)), f"menu button runs a missing function: {c}")
            else: self.assertRegex(c, r"^(trigger slf\.|clear @s|scoreboard players set @s slf\.)", f"unexpected menu command: {c}")


class TestGeneratorUpToDate(unittest.TestCase):
    def test_generated_files_match_the_generator(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            for rel in ("data_pack", "resource_pack", "tools"): shutil.copytree(ROOT / rel, tmp / rel)
            subprocess.run([sys.executable, str(tmp / "tools" / "gen_test_commands.py")], check=True, capture_output=True)
            stale = []
            for sub in ("give", "test"):
                for f in (tmp / "data_pack" / "data" / "slf" / "function" / sub).rglob("*.mcfunction"):
                    mine = FN / f.relative_to(tmp / "data_pack" / "data" / "slf" / "function")
                    if not mine.exists() or mine.read_text(encoding="utf-8") != f.read_text(encoding="utf-8"): stale.append(str(mine.relative_to(ROOT)))
            self.assertEqual(stale, [], "generated test commands are out of date: run python tools/gen_test_commands.py")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
