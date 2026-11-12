"""End-to-end tests: a real player on a real 26.2 server, driven through the same triggers the menus use.

    set SLF_MC_SERVER_DIR=<folder with server.jar>
    set SLF_JAVA=<java 25 executable>
    python -m unittest tests.live.test_live -v

See tests/live/README.md. One server is started for the whole module.
"""
import os, sys, time, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import LiveServer, REPO

S = None


def setUpModule():
    global S
    if not os.environ.get("SLF_MC_SERVER_DIR"):
        raise unittest.SkipTest("SLF_MC_SERVER_DIR is not set; live tests need a 26.2 server.jar (see tests/live/README.md)")
    S = LiveServer(datapacks={"SLF": os.path.join(REPO, "data_pack"),
                              "SLF_Weapons": os.path.join(REPO, "weapons", "java_out", "SLF_Weapons_Datapack")}).__enter__()
    S.wait_cycle()


def tearDownModule():
    if S: S.__exit__(None, None, None)


T1 = {"Swordsman": 1, "Warrior": 2, "Bandit": 3, "Priest": 4, "Monk": 5, "Mage": 6, "Fighter": 20, "Mercenary": 30}
# evolution id -> (grant chain to become eligible, required level)
EVOLUTIONS = {
    10: (["swordsman"], 20), 11: (["swordsman"], 20), 14: (["warrior"], 20), 21: (["fighter"], 20), 18: (["priest"], 20),
    60: (["monk"], 20), 70: (["mage"], 20), 50: (["bandit"], 20), 51: (["bandit"], 20), 40: (["swordsman", "sword_master"], 30),
    12: (["swordsman", "sword_master"], 50), 13: (["swordsman", "magic_swordsman"], 50), 15: (["warrior", "barbarian"], 50),
    22: (["fighter", "destroyer"], 50), 19: (["priest", "bishop"], 50), 61: (["monk", "monk_soldier"], 50), 62: (["mage", "sage"], 50),
    16: (["bandit", "thief"], 50), 52: (["bandit", "ninja"], 50), 31: (["mercenary"], 50),
    43: (["swordsman", "sword_master", "knight", "holy_knight"], 70), 44: (["swordsman", "sword_master", "knight", "dark_knight"], 70),
    17: (["bandit", "thief", "assassin"], 80), 53: (["bandit", "ninja", "shinobi"], 80),
}


class Base(unittest.TestCase):
    def setUp(self):
        self.assertIsNone(S.bot.error, "test player lost its connection")
        S.cmd(f"gamemode creative {S.player}"); S.cmd(f"effect clear {S.player}")
        S.as_player("function slf:admin/reset_player"); S.wait_ticks(3)

    def set(self, objective, value): S.cmd(f"scoreboard players set {S.player} {objective} {value}")

    def grant(self, *names):
        for n in names: S.as_player(f"function slf:class/grant/{n}")
        S.wait_ticks(3)

    def click(self, label_part, menu_command):
        """Open a menu as the player, find the button whose label contains label_part, and run what it would run."""
        mark = S.bot.mark(); S.as_player(menu_command); S.wait_ticks(4)
        buttons = S.bot.clicks_since(mark)
        match = [c for l, c in buttons if label_part in l]
        self.assertTrue(match, f"no button containing {label_part!r} in {[l for l, _ in buttons]}")
        mark = S.bot.mark(); S.as_player(match[0].lstrip("/")); S.wait_ticks(4)
        return S.bot.chat_since(mark)


class PackLoad(Base):
    def test_objectives_registered(self):
        out = S.cmd("scoreboard objectives list")
        for o in ("slf.class", "slf.level", "slf.exp", "slf.sp_points", "slf.focus", "slf.karma", "slf.menu", "slf.evolve", "slf.mana", "slf.stat.hp"):
            self.assertIn(f"[{o}]", out)

    def test_no_load_errors(self):
        log = S.read_log()
        bad = [l for l in log.splitlines() if ("ERROR" in l or "Failed to load" in l or "Couldn't parse" in l or "Couldn't load" in l)]
        self.assertEqual(bad, [])

    def test_new_player_is_greeted_with_class_menu(self):
        # the test player joined before any test ran: the very first chat lines are the welcome and the class menu
        text = "\n".join(S.bot.chat[:4])
        self.assertIn("Welcome to Shangri-La Frontier", text)
        self.assertIn("Choose Your Class", text)
        self.assertIn("slf.joined", S.tags())


class Menus(Base):
    def test_main_menu_without_class_offers_class_choice(self):
        mark = S.bot.mark(); S.as_player("trigger slf.menu"); S.wait_ticks(4)
        self.assertEqual([c for _, c in S.bot.clicks_since(mark)], ["trigger slf.menu set 2"])

    def test_main_menu_with_class_links_everything(self):
        self.grant("swordsman")
        mark = S.bot.mark(); S.as_player("trigger slf.menu"); S.wait_ticks(4)
        cmds = [c for _, c in S.bot.clicks_since(mark)]
        for n in (7, 4, 3, 5, 9): self.assertIn(f"trigger slf.menu set {n}", cmds)

    def test_menu_trigger_is_reenabled_after_use(self):
        for _ in range(3):
            out = S.as_player("trigger slf.menu"); self.assertIn("Triggered", out); S.wait_ticks(3)

    def test_status_sheet_shows_class_and_numbers(self):
        self.grant("warrior"); self.set("slf.sp_points", 7); S.wait_cycle()
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 7"); S.wait_ticks(4)
        text = "\n".join(S.bot.chat_since(mark))
        self.assertIn("Class: Warrior", text); self.assertIn("Level 1", text); self.assertIn("EXP 0/100", text); self.assertIn("Unspent points 7", text)

    def test_hud_toggle(self):
        self.grant("swordsman")
        S.as_player("trigger slf.menu set 9"); S.wait_ticks(3); self.assertIn("slf.hud_off", S.tags())
        S.as_player("trigger slf.menu set 9"); S.wait_ticks(3); self.assertNotIn("slf.hud_off", S.tags())


class ClassSelection(Base):
    def test_every_starting_class_through_the_menu(self):
        for name, cid in T1.items():
            with self.subTest(name):
                S.as_player("function slf:admin/reset_player"); S.wait_ticks(2)
                chat = self.click(f"[{name}]", "trigger slf.menu set 2")
                self.assertEqual(S.score("slf.class"), cid); self.assertEqual(S.score("slf.level"), 1)
                tags = S.tags()
                self.assertIn("slf.class_chosen", tags); self.assertIn(f"slf.was_{name.lower()}", tags)
                self.assertGreaterEqual(len([t for t in tags if t.startswith("slf.skill.")]), 3)
                self.assertTrue(any(f"You have become a {name}" in c for c in chat), chat)

    def test_second_starting_class_is_refused(self):
        self.grant("mage")
        S.as_player("trigger slf.choose_class set 1"); S.wait_ticks(4)
        self.assertEqual(S.score("slf.class"), 6)
        self.grant("swordsman"); self.assertEqual(S.score("slf.class"), 6)


class Evolution(Base):
    def test_every_evolution_needs_its_level_and_then_works(self):
        for cid, (chain, level) in EVOLUTIONS.items():
            with self.subTest(cid):
                S.as_player("function slf:admin/reset_player"); S.wait_ticks(2); self.grant(*chain)
                before = S.score("slf.class")
                self.set("slf.level", level - 1); mark = S.bot.mark()
                S.as_player(f"trigger slf.evolve set {cid}"); S.wait_ticks(4)
                self.assertEqual(S.score("slf.class"), before, "evolved below the level requirement")
                self.assertTrue(any(f"requires level {level}" in c for c in S.bot.chat_since(mark)), S.bot.chat_since(mark))
                self.set("slf.level", level)
                S.as_player(f"trigger slf.evolve set {cid}"); S.wait_ticks(4)
                self.assertEqual(S.score("slf.class"), cid)
                self.assertEqual(S.score("slf.level"), level, "evolving must not reset the level")

    def test_evolution_menu_lists_only_own_lineage(self):
        self.grant("swordsman"); self.set("slf.level", 20)
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 5"); S.wait_ticks(4)
        cmds = sorted(c for _, c in S.bot.clicks_since(mark) if "slf.evolve" in c)
        self.assertEqual(cmds, ["trigger slf.evolve set 10", "trigger slf.evolve set 11"])

    def test_evolution_through_menu_click(self):
        self.grant("fighter"); self.set("slf.level", 25)
        chat = self.click("[Destroyer]", "trigger slf.menu set 5")
        self.assertEqual(S.score("slf.class"), 21); self.assertTrue(any("Destroyer" in c for c in chat))

    def test_wrong_lineage_is_refused(self):
        self.grant("warrior"); self.set("slf.level", 99); mark = S.bot.mark()
        S.as_player("trigger slf.evolve set 21"); S.wait_ticks(4)   # Destroyer needs Fighter
        self.assertEqual(S.score("slf.class"), 2); self.assertTrue(any("not on your path" in c for c in S.bot.chat_since(mark)))
        S.as_player("trigger slf.evolve set 12"); S.wait_ticks(4)   # Kansei needs Sword Master
        self.assertEqual(S.score("slf.class"), 2)

    def test_no_evolution_without_a_class(self):
        out = S.as_player("trigger slf.evolve set 10"); S.wait_ticks(4)
        self.assertNotIn("Triggered", out); self.assertEqual(S.score("slf.class"), 0)

    def test_knight_trials_lead_to_alignment(self):
        self.grant("swordsman", "sword_master"); self.set("slf.level", 30)
        S.as_player("trigger slf.evolve set 40"); S.wait_ticks(4); self.assertEqual(S.score("slf.class"), 40)
        S.cmd(f"gamemode survival {S.player}")
        for n in (1, 2, 3):
            S.as_player('summon minecraft:witch ~3 ~ ~ {NoAI:1b,Tags:["slf.test"]}'); S.wait_ticks(3)
            S.as_player("damage @e[type=minecraft:witch,tag=slf.test,limit=1] 1000 minecraft:player_attack by @s"); S.wait_ticks(6)
            self.assertEqual(S.score("slf.knight_trials"), n)
        S.wait_ticks(6); mark = S.bot.mark()
        self.assertIn("slf.alignment_offered", S.tags())
        out = S.as_player("trigger slf.choose_class set 41"); self.assertIn("Triggered", out); S.wait_ticks(4)
        self.assertEqual(S.score("slf.class"), 41); self.assertIn("slf.was_holy_knight", S.tags())


class Skills(Base):
    def test_focus_then_learn(self):
        self.grant("swordsman")
        chat = self.click("[Megaton Swing]", "trigger slf.menu set 3")
        self.assertEqual((S.score("slf.focus"), S.score("slf.focus_stat"), S.score("slf.threshold")), (2, 1, 500))
        self.assertTrue(any("Focusing: Megaton Swing [0/500]" in c for c in chat), chat)
        self.set("slf.sp", 500); mark = S.bot.mark(); S.wait_cycle()
        self.assertEqual(S.score("slf.focus"), 0); self.assertIn("slf.skill.megaton_swing", S.tags())
        self.assertTrue(any("Skill learned: Megaton Swing" in c for c in S.bot.chat_since(mark)))

    def test_known_skill_cannot_be_focused(self):
        self.grant("swordsman"); mark = S.bot.mark()
        S.as_player("trigger slf.focus_choose set 1"); S.wait_ticks(4)
        self.assertEqual(S.score("slf.focus"), 0); self.assertTrue(any("already know" in c for c in S.bot.chat_since(mark)))

    def test_class_affinity_lowers_threshold(self):
        self.grant("warrior"); S.as_player("trigger slf.focus_choose set 21"); S.wait_ticks(4)   # Gigaton Swing: 2000, Warrior 300
        self.assertEqual(S.score("slf.threshold"), 300)
        S.as_player("function slf:admin/reset_player"); S.wait_ticks(2); self.grant("mage")
        mark = S.bot.mark(); S.as_player("trigger slf.focus_choose set 21"); S.wait_ticks(4)
        self.assertEqual(S.score("slf.focus"), 0); self.assertTrue(any("Requires: Megaton Swing" in c for c in S.bot.chat_since(mark)))
        S.cmd(f"tag {S.player} add slf.skill.megaton_swing")   # with the prerequisite but no Warrior lineage: full price
        S.as_player("trigger slf.focus_choose set 21"); S.wait_ticks(4); self.assertEqual(S.score("slf.threshold"), 2000)

    def test_tec_lowers_threshold(self):
        self.grant("swordsman"); self.set("slf.stat.tec", 20)
        S.as_player("trigger slf.focus_choose set 2"); S.wait_ticks(4); self.assertEqual(S.score("slf.threshold"), 400)
        S.as_player("function slf:admin/reset_player"); S.wait_ticks(2); self.grant("swordsman"); self.set("slf.stat.tec", 90)
        S.as_player("trigger slf.focus_choose set 2"); S.wait_ticks(4); self.assertEqual(S.score("slf.threshold"), 250)   # capped at 50%

    def test_motion_trace_feeds_focus(self):
        self.grant("swordsman"); S.as_player("trigger slf.focus_choose set 2"); S.wait_cycle()
        S.cmd(f"scoreboard players add {S.player} slf.raw.dmg 120"); S.wait_cycle(); S.wait_ticks(10)
        self.assertEqual(S.score("slf.sp"), 120)

    def test_passives_and_titles(self):
        self.grant("swordsman")
        for t in ("slf.skill.iron_skin", "slf.skill.slide_step", "slf.title.apex_crazy_fist"): S.cmd(f"tag {S.player} add {t}")
        S.wait_cycle(); fx = S.effects()
        self.assertEqual(fx.get("resistance"), 1); self.assertEqual(fx.get("speed"), 0); self.assertEqual(fx.get("strength"), 0)

    def test_tantrum_spends_mana_and_counts_kills(self):
        self.grant("bandit"); self.set("slf.stat.mp", 0); S.wait_cycle(); self.set("slf.mana", 20); self.set("slf.bt_kills", 49)
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 8"); S.wait_ticks(4)
        self.assertIn("slf.tantrum_active", S.tags()); self.assertLessEqual(S.score("slf.mana"), 10)
        S.wait_cycle(); self.assertIn("glowing", S.effects())
        S.cmd(f"gamemode survival {S.player}")
        S.as_player('summon minecraft:pig ~3 ~ ~ {NoAI:1b,Tags:["slf.test"]}'); S.wait_ticks(3)
        S.as_player("damage @e[type=minecraft:pig,tag=slf.test,limit=1] 1000 minecraft:player_attack by @s"); S.wait_ticks(6)
        self.assertEqual(S.score("slf.bt_kills"), 50); self.assertIn("slf.skill.grand_tantrum", S.tags())
        self.set("slf.mana", 2); S.wait_cycle(); S.wait_cycle()
        self.assertNotIn("slf.tantrum_active", S.tags()); self.assertGreaterEqual(S.score("slf.mana"), 0)

    def test_tantrum_refused_without_skill_or_mana(self):
        self.grant("swordsman"); mark = S.bot.mark(); S.as_player("trigger slf.menu set 8"); S.wait_ticks(4)
        self.assertNotIn("slf.tantrum_active", S.tags()); self.assertTrue(any("not learned" in c for c in S.bot.chat_since(mark)))
        S.as_player("function slf:admin/reset_player"); S.wait_ticks(2); self.grant("bandit"); S.wait_cycle(); self.set("slf.mana", 3)
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 8"); S.wait_ticks(4)
        self.assertNotIn("slf.tantrum_active", S.tags()); self.assertTrue(any("Not enough mana" in c for c in S.bot.chat_since(mark)))


class Stats(Base):
    def test_spend_each_stat_through_the_menu(self):
        self.grant("swordsman"); self.set("slf.sp_points", 9)
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 4"); S.wait_ticks(4)
        buttons = [(l, c) for l, c in S.bot.clicks_since(mark) if c.startswith("trigger slf.stat_")]
        self.assertEqual(len(buttons), 9, buttons)
        for _, c in buttons: S.as_player(c); S.wait_ticks(3)
        self.assertEqual(S.score("slf.sp_points"), 0)
        for k in "hp mp str dex vit agi tec lck stm".split(): self.assertEqual(S.score(f"slf.stat.{k}"), 1, k)

    def test_cannot_spend_without_points(self):
        self.grant("swordsman"); mark = S.bot.mark(); S.as_player("trigger slf.stat_str"); S.wait_ticks(4)
        self.assertEqual(S.score("slf.stat.str"), 0); self.assertTrue(any("don't have any stat points" in c for c in S.bot.chat_since(mark)))

    def test_stat_menu_needs_a_class(self):
        mark = S.bot.mark(); S.as_player("function slf:stats/menu"); S.wait_ticks(4)
        self.assertFalse([c for _, c in S.bot.clicks_since(mark) if "slf.stat_" in c])

    def test_stat_effects(self):
        self.grant("swordsman")
        for k, v in dict(agi=5, str=10, vit=5, stm=10, dex=5, lck=10).items(): self.set(f"slf.stat.{k}", v)
        S.wait_cycle(); fx = S.effects()
        self.assertEqual((fx.get("speed"), fx.get("strength"), fx.get("absorption"), fx.get("haste")), (0, 0, 0, 0))
        # saturation is an instant effect: it is only present for 3 ticks of every second, so poll for it
        deadline = time.time() + 3; seen = False
        while time.time() < deadline and not seen: seen = "saturation" in S.effects()
        self.assertTrue(seen, "STM 5+ never applied saturation")
        self.assertAlmostEqual(S.attribute("attack_speed", "modifier value get slf:dex_speed"), 0.4, places=2); self.assertEqual(S.attribute("luck"), 1.0)
        for k, v in dict(agi=20, str=20, vit=30, dex=20, lck=60).items(): self.set(f"slf.stat.{k}", v)
        S.cmd(f"effect clear {S.player}"); S.wait_cycle(); fx = S.effects()
        self.assertEqual((fx.get("speed"), fx.get("strength"), fx.get("absorption")), (2, 1, 3))
        self.assertAlmostEqual(S.attribute("attack_speed", "modifier value get slf:dex_speed"), 1.2, places=2); self.assertEqual(S.attribute("luck"), 4.0)

    def test_hp_raises_max_health(self):
        self.grant("swordsman"); self.assertEqual(S.attribute("max_health"), 20.0)
        self.set("slf.stat.hp", 10); S.wait_cycle(); self.assertEqual(S.attribute("max_health"), 25.0)
        self.set("slf.stat.hp", 500); S.wait_cycle(); self.assertEqual(S.attribute("max_health"), 60.0)   # capped at +40
        self.set("slf.stat.hp", 0); S.wait_cycle(); self.assertEqual(S.attribute("max_health"), 20.0)

    def test_mp_builds_a_regenerating_mana_pool(self):
        self.grant("swordsman"); S.wait_cycle(); self.assertEqual(S.score("slf.mana_max"), 20)
        self.set("slf.stat.mp", 30); self.set("slf.mana", 0); S.wait_cycle(); S.wait_cycle()
        self.assertEqual(S.score("slf.mana_max"), 80)
        mana = S.score("slf.mana"); self.assertTrue(4 <= mana <= 16, mana)   # 4 per second at MP 30
        self.set("slf.mana", 500); S.wait_cycle(); self.assertEqual(S.score("slf.mana"), 80)


class Leveling(Base):
    def kill(self, entity):
        S.cmd(f"gamemode survival {S.player}")
        S.as_player(f'summon minecraft:{entity} ~3 ~ ~ {{NoAI:1b,Tags:["slf.test"]}}'); S.wait_ticks(3)
        out = S.as_player(f"damage @e[type=minecraft:{entity},tag=slf.test,limit=1] 100000 minecraft:player_attack by @s"); S.wait_ticks(6)
        self.assertIn("Applied", out)

    def test_kills_give_exp_by_tier(self):
        self.grant("swordsman")
        for entity, exp in (("pig", 2), ("zombie", 10), ("witch", 40)):
            with self.subTest(entity):
                self.set("slf.exp", 0); self.kill(entity); self.assertEqual(S.score("slf.exp"), exp)
        self.kill("zombie"); self.kill("zombie"); self.assertEqual(S.score("slf.exp"), 60)   # every kill counts, not just the first

    def test_fresh_player_levels_up_from_kills(self):
        """A player who picked a class from the menu (no admin reset) must level up: regression for the standby gate."""
        S.cmd(f"scoreboard players reset {S.player} slf.standby"); S.cmd(f"scoreboard players reset {S.player} slf.awakened")
        self.grant("swordsman"); self.set("slf.exp", 60)
        self.kill("witch"); mark = S.bot.mark(); S.wait_cycle()
        self.assertEqual(S.score("slf.level"), 2); self.assertEqual(S.score("slf.sp_points"), 5)
        self.assertEqual(S.score("slf.exp"), 0)

    def test_surplus_exp_carries_over(self):
        self.grant("swordsman"); self.set("slf.exp", 330); S.wait_cycle(); S.wait_cycle(); S.wait_ticks(10)
        self.assertEqual(S.score("slf.level"), 3); self.assertEqual(S.score("slf.exp"), 30)

    def test_milestone_bonus(self):
        self.grant("swordsman"); self.set("slf.level", 9); self.set("slf.sp_points", 0); S.wait_cycle(); self.set("slf.exp", 4500); S.wait_cycle()
        self.assertEqual(S.score("slf.level"), 10); self.assertEqual(S.score("slf.sp_points"), 7)

    def test_boss_kill_opens_the_gate(self):
        self.grant("swordsman"); self.set("slf.level", 50); self.kill("elder_guardian")   # level 50 needs 5000 EXP, so no level-up interferes
        self.assertEqual(S.score("slf.boss_gate"), 1); self.assertEqual(S.score("slf.boss_kills"), 1); self.assertEqual(S.score("slf.exp"), 2500)
        self.assertEqual(S.score("slf.vorpal_soul"), 1)

    def test_standby_altar_and_awakened_levels(self):
        self.grant("swordsman"); self.set("slf.level", 99); self.set("slf.exp", 12000); S.wait_cycle()
        self.assertEqual((S.score("slf.level"), S.score("slf.standby"), S.score("slf.exp_extend")), (99, 1, 12000))
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 6"); S.wait_ticks(4)
        self.assertEqual(S.score("slf.standby"), 1); self.assertTrue(any("altar is dormant" in c for c in S.bot.chat_since(mark)))
        self.set("slf.boss_gate", 1); S.as_player("trigger slf.menu set 6"); S.wait_ticks(4)
        self.assertEqual((S.score("slf.standby"), S.score("slf.awakened")), (0, 1))
        S.wait_cycle(); S.wait_cycle(); S.wait_cycle()
        self.assertEqual(S.score("slf.level"), 101); self.assertEqual(S.score("slf.standby"), 0)   # 12000 banked EXP = 2 levels, 2000 left
        self.assertEqual(S.score("slf.exp"), 2000)
        self.set("slf.level", 149); self.set("slf.exp", 99999); S.wait_cycle(); S.wait_cycle()
        self.assertEqual(S.score("slf.level"), 150)


class Mask(Base):
    def test_karma_cap_and_bounty_hunter(self):
        self.set("slf.karma", 210); mark = S.bot.mark(); S.wait_cycle()
        self.assertEqual(S.score("slf.karma"), 200); self.assertTrue(any("Bounty Hunter" in c for c in S.bot.chat_since(mark)))
        self.assertEqual(S.cmd("execute store result score #n slf.tmp if entity @e[type=minecraft:pillager,tag=slf.bounty_hunter]").strip()[-1:], "1")
        self.assertEqual(S.cmd("attribute @e[type=minecraft:pillager,tag=slf.bounty_hunter,limit=1] minecraft:max_health base get").split(" is ")[1][:4], "40.0")
        S.cmd("kill @e[type=minecraft:pillager]"); self.set("slf.karma", 0)

    def test_killing_villagers_raises_karma(self):
        self.grant("swordsman"); S.cmd(f"gamemode survival {S.player}")
        S.as_player('summon minecraft:villager ~3 ~ ~ {NoAI:1b,Tags:["slf.test"]}'); S.wait_ticks(3)
        S.as_player("damage @e[type=minecraft:villager,tag=slf.test,limit=1] 1000 minecraft:player_attack by @s"); S.wait_ticks(6)
        self.assertEqual(S.score("slf.karma"), 5)

    def test_death_costs_vorpal_soul(self):
        self.grant("swordsman"); self.set("slf.vorpal_soul", 12); S.cmd(f"gamemode survival {S.player}"); deaths = S.bot.deaths
        S.cmd(f"kill {S.player}"); S.wait_ticks(20)
        self.assertEqual(S.bot.deaths, deaths + 1); self.assertEqual(S.score("slf.vorpal_soul"), 7)


class WeaponsPack(Base):
    """The separate weapons data pack, loaded next to the main one (both add a tick function tag)."""
    TWIN = "*[minecraft:custom_data~{slf:{is_twin:1b}}]"

    def has(self, slot, item): return "passed" in S.cmd(f"execute if items entity {S.player} {slot} {item}")

    def test_give_all_and_models(self):
        S.cmd(f"clear {S.player}"); S.as_player("function slf:weapons/give_all"); S.wait_ticks(4)
        for name in ("wood_staff", "iron_hammer", "iron_sword", "iron_dagger", "marsh_dagger", "mercenary_blade", "vorpal_chopper", "fossil_rod", "wood_shield"):
            self.assertTrue(self.has("container.*", f'*[minecraft:item_model="slf:{name}"]'), name)
        S.cmd(f"clear {S.player}")

    def test_paired_weapon_twin_follows_main_hand(self):
        S.cmd(f"clear {S.player}"); S.wait_ticks(3)
        S.as_player("function slf:weapons/give/marsh_dagger"); S.wait_ticks(4)   # empty inventory: lands in the selected slot
        self.assertTrue(self.has("weapon.mainhand", '*[minecraft:custom_data~{slf:{pair:"marsh_dagger"}}]'))
        self.assertTrue(self.has("weapon.offhand", self.TWIN), "no twin appeared in the off hand")
        S.cmd(f"item replace entity {S.player} weapon.mainhand with minecraft:air"); S.wait_ticks(4)
        self.assertFalse(self.has("weapon.offhand", self.TWIN), "twin stayed after the weapon left the main hand")

    def test_single_weapon_has_no_twin(self):
        S.cmd(f"clear {S.player}"); S.wait_ticks(3); S.as_player("function slf:weapons/give/iron_dagger"); S.wait_ticks(4)
        self.assertFalse(self.has("weapon.offhand", "*")); S.cmd(f"clear {S.player}")

    def test_main_pack_still_ticks_alongside(self):
        self.grant("swordsman"); self.set("slf.exp", 100); S.wait_cycle(); self.assertEqual(S.score("slf.level"), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
