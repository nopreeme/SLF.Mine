"""End-to-end tests: a real player on a real 26.2 server, driven through the same triggers the menus use.

    set SLF_MC_SERVER_DIR=<folder with server.jar>
    set SLF_JAVA=<java 25 executable>
    python -m unittest tests.live.test_live -v

See tests/live/README.md. One server is started for the whole module.
"""
import os, re, sys, time, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import LiveServer, REPO, PORT
from mcbot import Bot

S = None
HOME = None   # where the test player first spawned; every test starts from here


def setUpModule():
    global S
    if not os.environ.get("SLF_MC_SERVER_DIR"):
        raise unittest.SkipTest("SLF_MC_SERVER_DIR is not set; live tests need a 26.2 server.jar (see tests/live/README.md)")
    S = LiveServer(datapacks={"SLF": os.path.join(REPO, "data_pack"),
                              "SLF_Weapons": os.path.join(REPO, "weapons", "java_out", "SLF_Weapons_Datapack")}).__enter__()
    S.wait_cycle()
    global HOME
    HOME = " ".join(str(v) for v in S.bot.pos)


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
        S.cmd(f"tp {S.player} {HOME}"); S.cmd("kill @e[tag=slf.test]"); S.cmd("kill @e[tag=slf.mob]")
        # no altar carried over from an earlier test (an altar still being raised gives up at its next try)
        for k in ("pending", "placed"): S.cmd(f"scoreboard players set #altar_{k} slf.timer 0")
        S.cmd("scoreboard players set #karma_timer slf.karma_timer 0")   # karma decays once a minute: keep that out of the tests
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

    def test_fresh_player_sees_numbers_not_blanks(self):
        """Regression: a player whose scores were never set saw "EXP /100" and stat names without values."""
        S.cmd(f"scoreboard players reset {S.player}"); self.grant("swordsman")
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 7"); S.wait_ticks(4)
        text = "\n".join(S.bot.chat_since(mark))
        self.assertIn("EXP 0/100", text); self.assertIn("Unspent points 0", text)
        for label in ("HP 0", "MP 0", "STR 0", "DEX 0", "VIT 0", "AGI 0", "TEC 0", "LCK 0", "STM 0"): self.assertIn(label, text)
        S.cmd(f"scoreboard players reset {S.player}"); self.grant("warrior"); S.wait_cycle()   # the once-per-second pass covers players who never open a menu
        self.assertEqual((S.score("slf.exp"), S.score("slf.stat.hp"), S.score("slf.vorpal_soul")), (0, 0, 0))

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
        mark = S.bot.mark(); S.as_player("function slf:stats/altar"); S.wait_ticks(4)
        self.assertEqual(S.score("slf.standby"), 1); self.assertTrue(any("altar is dormant" in c for c in S.bot.chat_since(mark)))
        self.set("slf.boss_gate", 1); S.as_player("function slf:stats/altar"); S.wait_ticks(4)
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

    def test_killing_another_player_raises_karma(self):
        victim = Bot("Victim", port=PORT).connect()
        try:
            self.grant("swordsman"); S.cmd("gamemode survival Victim"); S.cmd(f"tp Victim {S.player}"); S.wait_ticks(6)
            out = S.as_player("damage Victim 1000 minecraft:player_attack by @s"); self.assertIn("Applied", out); S.wait_ticks(10)
            self.assertEqual(victim.deaths, 1); self.assertEqual(S.score("slf.karma"), 25)
            self.assertEqual(S.score("slf.exp"), 2)   # a player is not a monster: only the base 2 EXP
        finally:
            victim.close(); S.wait_ticks(10)

    def test_death_costs_vorpal_soul(self):
        self.grant("swordsman"); self.set("slf.vorpal_soul", 12); S.cmd(f"gamemode survival {S.player}"); deaths = S.bot.deaths
        S.cmd(f"kill {S.player}"); S.wait_ticks(20)
        self.assertEqual(S.bot.deaths, deaths + 1); self.assertEqual(S.score("slf.vorpal_soul"), 7)


class RealMotion(Base):
    """The test player really sprints, jumps and swings, so the statistics the pack reads are the game's own."""
    def setUp(self):
        super().setUp(); self.grant("swordsman"); S.platform(); S.bot.sprint(False); S.wait_ticks(2)

    def focus(self, stat):
        """Focus a skill by hand so any statistic can be watched (threshold far out of reach)."""
        self.set("slf.focus", 2); self.set("slf.focus_stat", stat); self.set("slf.threshold", 10000000); self.set("slf.sp", 0); S.wait_cycle()

    def test_sprinting_feeds_move_focus(self):
        self.focus(2); before = S.score("slf.raw.move") or 0
        S.bot.sprint(True); S.bot.walk(6); S.bot.sprint(False); S.wait_cycle(); S.wait_cycle()
        gained = S.score("slf.raw.move") - before
        self.assertTrue(500 <= gained <= 700, f"sprinted 6 blocks, game counted {gained} cm")
        self.assertEqual(S.score("slf.sp"), gained)

    def test_walking_is_not_sprinting(self):
        self.focus(2); before = S.score("slf.raw.move") or 0
        S.bot.walk(4); S.wait_cycle(); S.wait_cycle()
        self.assertEqual((S.score("slf.raw.move") or 0) - before, 0); self.assertEqual(S.score("slf.sp"), 0)

    def test_jumps_feed_evade_focus(self):
        self.focus(3); before = S.score("slf.raw.evade") or 0
        for _ in range(4): S.bot.jump()
        S.wait_cycle(); S.wait_cycle()
        self.assertEqual(S.score("slf.raw.evade") - before, 4); self.assertEqual(S.score("slf.sp"), 4)

    def test_ideal_motion_triples_progress(self):
        ask = f"execute as {S.player} if predicate slf:ideal_motion"
        self.assertNotIn("passed", S.cmd(ask))                      # standing still
        S.bot.sprint(True); S.wait_ticks(2); self.assertNotIn("passed", S.cmd(ask))   # sprinting on the ground
        self.focus(1); S.bot.leave_ground(); S.bot.hold_air(0.15)
        self.assertIn("passed", S.cmd(ask))                         # sprinting and airborne
        S.cmd(f"scoreboard players add {S.player} slf.raw.dmg 100"); S.bot.hold_air(1.5)   # airborne across a whole cycle
        S.bot.land(); S.bot.sprint(False); S.wait_ticks(4)
        self.assertEqual(S.score("slf.sp"), 300)

    def test_melee_hits_feed_damage_focus_and_real_kills_give_exp(self):
        S.cmd(f"gamemode survival {S.player}"); S.cmd(f"clear {S.player}")
        S.cmd(f"item replace entity {S.player} weapon.mainhand with minecraft:netherite_sword"); self.set("slf.exp", 0)
        S.as_player('summon minecraft:zombie ~1.5 ~ ~ {NoAI:1b,Tags:["slf.test"],PersistenceRequired:1b}'); S.wait_ticks(6)
        target = S.entity_uuid("@e[type=minecraft:zombie,tag=slf.test,limit=1]")
        self.assertIn(target, S.bot.entities, "the client never saw the zombie spawn")
        self.focus(1); before = S.score("slf.raw.dmg") or 0
        for _ in range(6):
            if "passed" not in S.cmd("execute if entity @e[type=minecraft:zombie,tag=slf.test]"): break
            S.bot.attack(target); time.sleep(0.75)
        self.assertNotIn("passed", S.cmd("execute if entity @e[type=minecraft:zombie,tag=slf.test]"), "zombie survived six sword hits")
        S.wait_cycle(); S.wait_cycle()
        dealt = S.score("slf.raw.dmg") - before
        # the statistic is in tenths of a health point and is counted after the zombie's armour
        self.assertTrue(150 <= dealt <= 260, f"killing a 20 HP zombie counted {dealt}")
        self.assertEqual(S.score("slf.sp"), dealt)
        self.assertEqual(S.score("slf.exp"), 10)

    def test_damage_taken_feeds_def_focus_and_triggers_ignition(self):
        S.cmd(f"gamemode survival {S.player}"); S.cmd(f"tag {S.player} add slf.skill.ignition"); S.wait_cycle(); S.cmd(f"effect clear {S.player}")
        self.focus(4); before = S.score("slf.raw.def") or 0
        S.cmd(f"damage {S.player} 4 minecraft:generic"); S.wait_cycle(); S.wait_cycle()
        self.assertEqual(S.score("slf.raw.def") - before, 40); self.assertEqual(S.score("slf.sp"), 40)
        fx = S.effects(); self.assertIn("strength", fx); self.assertIn("speed", fx)


class SkillBonuses(Base):
    """Every skill in the generated table really changes the player, and stops when the skill is lost."""
    def modifiers(self):
        path = os.path.join(REPO, "data_pack", "data", "slf", "function", "skills", "attributes.mcfunction"); found = []
        for line in open(path, encoding="utf-8").read().splitlines():
            m = re.match(r"execute as @a\[tag=slf\.skill\.([a-z_]+)\] run attribute @s minecraft:([a-z_]+) modifier add (\S+) (\S+) (\S+)", line)
            if m: found.append((m.group(1), m.group(2), m.group(3), float(m.group(4))))
        return found

    def test_every_skill_modifier_applies_and_is_removed(self):
        mods = self.modifiers(); self.assertGreaterEqual(len(mods), 80)
        for skill in sorted({m[0] for m in mods}): S.cmd(f"tag {S.player} add slf.skill.{skill}")
        S.wait_cycle()
        for skill, attr, mid, amount in mods:
            with self.subTest(skill=skill, attribute=attr):
                self.assertAlmostEqual(S.attribute(attr, f"modifier value get {mid}"), amount, places=3)
        S.as_player("function slf:admin/reset_player"); S.wait_cycle(); S.wait_ticks(5)
        left = [mid for _, attr, mid, _ in mods if S.attribute(attr, f"modifier value get {mid}") is not None]
        self.assertEqual(left, [], "modifiers stayed after the skills were removed")
        self.assertEqual(S.attribute("max_health"), 20.0)

    def test_class_skills_change_real_numbers(self):
        self.grant("warrior"); S.wait_cycle()   # megaton_swing +1 damage, front_position +2 armour, rigid_strength +20% knockback resistance
        S.cmd(f"clear {S.player}"); S.wait_ticks(4)   # empty hands and no armour, so only the skills count
        self.assertEqual(S.attribute("attack_damage"), 2.0); self.assertEqual(S.attribute("armor"), 2.0)
        self.assertAlmostEqual(S.attribute("knockback_resistance"), 0.2, places=3)

    def test_mana_skills(self):
        self.grant("mage"); S.wait_cycle()       # chanting_and_memorizing +20 max mana, tanda_breathing +1 regen
        self.assertEqual(S.score("slf.mana_max"), 40)
        self.set("slf.mana", 0); S.wait_cycle(); S.wait_cycle(); mana = S.score("slf.mana"); self.assertTrue(2 <= mana <= 8, mana)
        self.assertIn("night_vision", S.effects())   # wisdoms_divine_eye


class Altar(Base):
    def tearDown(self): S.as_player("function slf:altar/remove")

    def place(self):
        S.platform(); mark = S.bot.mark(); S.as_player("function slf:altar/place"); S.wait_ticks(4)
        self.assertTrue(any("Altar of Awakening placed" in c for c in S.bot.chat_since(mark)))

    def test_altar_is_built(self):
        self.place()
        for offset, block in (("~ ~ ~4", "gilded_blackstone"), ("~ ~1 ~4", "crying_obsidian"), ("~ ~2 ~4", "end_rod"),
                              ("~2 ~1 ~6", "soul_lantern"), ("~-2 ~ ~2", "polished_blackstone_wall"), ("~ ~-1 ~4", "polished_blackstone_bricks")):
            self.assertIn("passed", S.cmd(f"execute at {S.player} if block {offset} minecraft:{block}"), f"{block} missing at {offset}")
        self.assertIn("passed", S.cmd("execute if entity @e[type=minecraft:marker,tag=slf.altar]"))
        self.assertIn("passed", S.cmd("execute if entity @e[type=minecraft:text_display,tag=slf.altar_label]"))

    def test_walking_up_awakens_only_the_worthy(self):
        self.grant("swordsman"); self.set("slf.level", 99); self.set("slf.exp", 6000); S.wait_cycle()
        self.assertEqual(S.score("slf.standby"), 1)
        mark = S.bot.mark(); self.place(); S.wait_cycle(); S.wait_cycle()          # arrives without a boss kill
        self.assertEqual(S.score("slf.awakened"), 0); self.assertTrue(any("altar is dormant" in c for c in S.bot.chat_since(mark)), S.bot.chat_since(mark))
        self.assertEqual(sum("altar is dormant" in c for c in S.bot.chat_since(mark)), 1, "the altar repeated itself while the player stood there")
        S.as_player("tp @s ~ ~ ~-12"); S.wait_cycle(); self.assertNotIn("slf.at_altar", S.tags())
        self.set("slf.boss_gate", 1); S.as_player("tp @s ~ ~ ~12"); S.wait_cycle(); S.wait_cycle()
        self.assertEqual((S.score("slf.awakened"), S.score("slf.standby")), (1, 0))
        S.wait_cycle(); S.wait_cycle(); self.assertEqual(S.score("slf.level"), 100)

    COMPASS = "minecraft:compass[minecraft:custom_data~{slf_altar_compass:1b}]"

    def compasses(self):
        m = re.search(r"Found (\d+) matching", S.cmd(f"clear {S.player} {self.COMPASS} 0")); return int(m.group(1)) if m else 0

    def test_altar_rises_when_first_needed_and_the_compass_leads_to_it(self):
        S.cmd(f"clear {S.player}"); self.grant("swordsman"); S.cmd(f"clear {S.player}")
        px, _, pz = [float(v) for v in re.findall(r"(-?[\d.]+)d", S.cmd(f"data get entity {S.player} Pos"))]
        self.set("slf.boss_gate", 1); self.set("slf.level", 99); mark = S.bot.mark()
        deadline = time.time() + 90
        while time.time() < deadline and S.score("slf.timer", "#altar_placed") != 1: time.sleep(1)
        self.assertEqual(S.score("slf.timer", "#altar_placed"), 1, f"no altar rose; chat: {S.bot.chat_since(mark)}")
        S.wait_ticks(10); chat = "\n".join(S.bot.chat_since(mark))
        self.assertIn("Standby.", chat); self.assertIn("is rising", chat); self.assertIn("has risen", chat)
        ax, ay, az = (S.score("slf.timer", f"#altar_{k}") for k in "xyz")
        self.assertIn(f"stands at {ax} {ay} {az}", chat)
        d = ((ax - px) ** 2 + (az - pz) ** 2) ** 0.5   # 320 away, or 480 if no spot on the inner ring was dry ground
        ring = 320 if S.score("slf.timer", "#altar_moves") < 8 else 480
        self.assertTrue(ring - 20 <= d <= ring + 20, f"altar at {ax},{az} is {d:.0f} from the player at {px},{pz}, expected about {ring}")
        self.assertEqual(self.compasses(), 1, "no altar compass was given")
        target = S.cmd(f'data get entity {S.player} Inventory[{{components:{{"minecraft:custom_data":{{slf_altar_compass:1b}}}}}}].components."minecraft:lodestone_tracker".target.pos')
        self.assertIn(f"[I; {ax}, {ay}, {az}]", target, target)
        S.cmd(f"tp {S.player} {ax} {ay + 10} {az}"); S.wait_ticks(60)      # let the area load before looking at blocks
        for dy, block in ((-1, "polished_blackstone_bricks"), (0, "gilded_blackstone"), (1, "crying_obsidian"), (2, "end_rod")):
            self.assertIn("passed", S.cmd(f"execute if block {ax} {ay + dy} {az} minecraft:{block}"), f"{block} missing in the raised altar")
        for dx, dz in ((0, 0), (-2, -2), (2, 2), (-2, 2), (2, -2)):             # under the centre and the four corners of the base
            for bad in ("minecraft:air", "minecraft:water", "minecraft:lava", "#minecraft:leaves"):
                self.assertNotIn("passed", S.cmd(f"execute if block {ax + dx} {ay - 2} {az + dz} {bad}"), f"the altar stands on {bad} at offset {dx},{dz}")
        self.assertIn("passed", S.cmd(f"execute positioned {ax} {ay} {az} if entity @e[type=minecraft:text_display,tag=slf.altar_label,distance=..6]"))
        mark = S.bot.mark(); self.click("[Altar of Awakening]", "trigger slf.menu"); S.wait_ticks(4)
        self.assertTrue(any("compass points the way" in c for c in S.bot.chat_since(mark)), S.bot.chat_since(mark))
        self.assertEqual(self.compasses(), 1, "asking again handed out a second compass")
        S.cmd(f"tp {S.player} {ax + 1}.5 {ay + 1} {az + 2}.5"); S.wait_cycle(); S.wait_cycle()
        self.assertEqual((S.score("slf.awakened"), S.score("slf.standby")), (1, 0))
        S.cmd(f"clear {S.player}")

    def test_raised_altar_avoids_water(self):
        """Regression: a real-client check found an altar raised on the open ocean (surface y=63)."""
        S.cmd(f"tp {S.player} {HOME}"); px, _, pz = [int(float(v)) for v in re.findall(r"(-?[\d.]+)d", S.cmd(f"data get entity {S.player} Pos"))]
        found = None                                                            # find ocean somewhere near, then aim the altar at it
        for r in range(150, 1500, 150):
            for dx, dz in ((r, 0), (0, r), (-r, 0), (0, -r)):
                out = S.cmd(f"execute positioned {px + dx} 64 {pz + dz} run locate biome #minecraft:is_ocean")
                m = re.search(r"\[(-?\d+), (?:-?\d+|~), (-?\d+)\]", out)
                if m: found = (int(m.group(1)), int(m.group(2))); break
            if found: break
        self.assertTrue(found, "no ocean near the test spawn")
        ox, oz = found
        # raise as if a player stood 320 blocks north of the ocean point: direction 0 (south, +z) makes it the first candidate
        S.cmd("scoreboard players set #altar_pending slf.timer 1"); S.cmd("scoreboard players set #altar_moves slf.timer 0"); S.cmd("scoreboard players set #altar_dir slf.timer 0")
        S.cmd(f"data modify storage slf:altar px set value {ox}"); S.cmd(f"data modify storage slf:altar pz set value {oz - 320}")
        S.cmd("function slf:altar/create_pick")
        deadline = time.time() + 150
        while time.time() < deadline and S.score("slf.timer", "#altar_placed") != 1 and S.score("slf.timer", "#altar_pending") == 1: time.sleep(1)
        self.assertEqual(S.score("slf.timer", "#altar_placed"), 1, f"no altar rose (moves tried: {S.score('slf.timer', '#altar_moves')})")
        ax, ay, az = (S.score("slf.timer", f"#altar_{k}") for k in "xyz")
        S.cmd(f"tp {S.player} {ax} {ay + 10} {az}"); S.wait_ticks(60)
        self.assertIn("passed", S.cmd(f"execute if block {ax} {ay} {az} minecraft:gilded_blackstone"))
        for dx, dz in ((0, 0), (-2, -2), (2, 2), (-2, 2), (2, -2)):
            for bad in ("minecraft:air", "minecraft:water", "minecraft:lava", "#minecraft:leaves"):
                self.assertNotIn("passed", S.cmd(f"execute if block {ax + dx} {ay - 2} {az + dz} {bad}"), f"the altar stands on {bad}")
        self.assertGreaterEqual(S.score("slf.timer", "#altar_moves"), 1, "the ocean spot was not skipped")
        self.assertTrue(300 <= ((ax - ox) ** 2 + (az - oz + 320) ** 2) ** 0.5 <= 500, "the moved altar left the rings around the player")

    def test_only_one_altar_rises(self):
        self.grant("swordsman"); self.set("slf.level", 99)
        deadline = time.time() + 3
        while time.time() < deadline and S.score("slf.timer", "#altar_pending") != 1: time.sleep(0.05)
        self.assertEqual(S.score("slf.timer", "#altar_pending"), 1, "entering Standby did not start raising an altar")
        mark = S.bot.mark(); S.as_player("trigger slf.menu set 6"); S.wait_ticks(3)       # asking while it may still be rising
        chat = S.bot.chat_since(mark)
        if S.score("slf.timer", "#altar_placed") != 1:                                     # (the far chunk can already exist: then it rises at once)
            self.assertTrue(any("is rising" in c for c in chat), chat)
        S.as_player("function slf:altar/place"); S.wait_ticks(4)                          # an admin-placed altar takes over
        self.assertEqual(S.score("slf.timer", "#altar_pending"), 0)
        placed = [S.score("slf.timer", f"#altar_{k}") for k in "xyz"]; S.wait_ticks(80)
        self.assertEqual([S.score("slf.timer", f"#altar_{k}") for k in "xyz"], placed, "the far altar was still raised after one was placed")

    def test_menu_points_to_the_altar_once_placed(self):
        self.grant("swordsman"); self.set("slf.level", 99); S.wait_cycle(); self.place()   # no boss kill yet: the altar stays dormant
        S.as_player("tp @s ~ ~ ~-12"); S.wait_cycle(); self.set("slf.boss_gate", 1)
        chat = self.click("[Altar of Awakening]", "trigger slf.menu")
        self.assertTrue(any("Altar of Awakening stands at" in c for c in chat), chat)
        self.assertEqual(S.score("slf.awakened"), 0)   # the menu only gives directions: no shortcut past the altar


class TestSuite(Base):
    """The operator test tools (/function slf:test/menu) work in game."""
    def count_slf_items(self):
        out = S.cmd(f"execute if items entity {S.player} container.* *[minecraft:custom_model_data]")
        m = re.search(r"Count: (\d+)", out); return int(m.group(1)) if m else 0

    def item_names(self):
        """Each slot read separately: one reply over RCON is cut off at about 4 KB."""
        return [S.cmd(f'data get entity {S.player} Inventory[{{Slot:{n}b}}].components."minecraft:item_name"') for n in range(36)]

    def test_every_kit_gives_every_item_with_a_real_name(self):
        for kit in ("weapons", "armor", "skill_books", "materials"):
            with self.subTest(kit):
                text = open(os.path.join(REPO, "data_pack", "data", "slf", "function", "test", "kit", f"{kit}.mcfunction"), encoding="utf-8").read()
                expected = len(re.findall(r"function slf:give/", text))
                learn = os.path.join(REPO, "data_pack", "data", "slf", "function", "skills", "learn")
                consumed = {f[:-11]: n for n in re.findall(r"function slf:give/([a-z0-9_]+)", text) for f in os.listdir(learn)
                            if f'"slf.{n}"' in open(os.path.join(learn, f), encoding="utf-8").read()}   # books that teach on first pickup
                S.cmd(f"clear {S.player}"); S.as_player(f"function slf:test/kit/{kit}"); S.wait_ticks(6)
                self.assertEqual(self.count_slf_items(), expected - len(consumed))
                for skill in consumed: self.assertIn(f"slf.skill.{skill}", S.tags(), f"picking up its book did not teach {skill}")
                if consumed:   # once learned, a second kit keeps every book
                    S.cmd(f"clear {S.player}"); S.as_player(f"function slf:test/kit/{kit}"); S.wait_ticks(6)
                    self.assertEqual(self.count_slf_items(), expected)
                bad = [n for n in self.item_names() if "'{" in n or "'\"" in n]
                self.assertEqual(bad, [], "an item name is a quoted JSON string, which shows as raw text")
        S.cmd(f"clear {S.player}")

    def test_boss_drops_have_real_names(self):
        """Regression: loot tables stored names as JSON strings, shown in game as {"translate":...}."""
        for table in ("bilac_drops", "nightclaw_drops", "oriana_drops", "wethermon_drops", "wezaemon_drops", "lycagon_drops"):
            with self.subTest(table):
                for _ in range(8):   # drops are random: roll until the unique item comes
                    S.cmd(f"clear {S.player}"); S.cmd(f"loot give {S.player} loot slf:{table}")
                    out = S.cmd(f'data get entity {S.player} Inventory[{{components:{{"minecraft:custom_model_data":{{}}}}}}].components."minecraft:item_name"')
                    if "translate" in out: break
                self.assertIn("translate:", out, f"no unique item dropped from {table} in 8 rolls: {out}")
                self.assertNotIn("'{", out)
        S.cmd(f"clear {S.player}")

    def test_every_class_setup(self):
        grant = os.path.join(REPO, "data_pack", "data", "slf", "function", "class", "grant")
        for f in sorted(os.listdir(grant)):
            k = f[:-11]; cid = int(re.search(r"slf\.class (\d+)", open(os.path.join(grant, f), encoding="utf-8").read()).group(1))
            with self.subTest(k):
                S.as_player(f"function slf:test/class/{k}"); S.wait_ticks(2)
                self.assertEqual(S.score("slf.class"), cid); self.assertIn("slf.class_chosen", S.tags())

    def test_every_menu_button(self):
        mark = S.bot.mark(); S.as_player("function slf:test/menu"); S.wait_ticks(4)
        buttons = S.bot.clicks_since(mark); self.assertGreater(len(buttons), 50)
        for label, command in buttons:
            with self.subTest(label):
                out = S.as_player(command.lstrip("/"))
                self.assertFalse(re.search(r"Unknown|Incorrect|Expected|Invalid", out), f"{label} -> {command}: {out}")
        S.as_player("function slf:altar/remove"); S.cmd(f"clear {S.player}"); S.cmd("kill @e[type=minecraft:pillager]")


class Mobs(Base):
    """SLF mobs: the Vorpal Bunny. Its level sets its stats, the EXP it gives, and whether killing it earns a Vorpal Soul."""
    BUNNY = "@e[tag=slf.vorpal_bunny,limit=1,sort=nearest]"

    def spawn(self, level=None):
        S.as_player("function slf:test/mob/vorpal_bunny_30" if level == 30 else "function slf:test/mob/vorpal_bunny"); S.wait_ticks(3)

    def kill_bunny(self):
        S.cmd(f"gamemode survival {S.player}")
        out = S.as_player(f"damage {self.BUNNY} 100000 minecraft:player_attack by @s"); self.assertIn("Applied", out); S.wait_ticks(6)

    def test_bunny_stats_follow_its_level(self):
        self.spawn(30)
        self.assertIn("99", S.cmd(f"data get entity {self.BUNNY} RabbitType"))           # vanilla's Killer Bunny: hostile
        self.assertIn("Vorpal Bunny Lv.30", S.cmd(f"data get entity {self.BUNNY} CustomName"))
        self.assertIn("is 36.0", S.cmd(f"attribute {self.BUNNY} minecraft:max_health base get"))   # 6 + level
        self.assertIn("is 7.0", S.cmd(f"attribute {self.BUNNY} minecraft:attack_damage base get"))  # 2 + level/6
        self.assertIn("36.0f", S.cmd(f"data get entity {self.BUNNY} Health"))
        self.assertIn("slf:vorpal_bunny_drops", S.cmd(f"data get entity {self.BUNNY} DeathLootTable"))
        self.assertIn("is 0.38", S.cmd(f"attribute {self.BUNNY} minecraft:movement_speed base get"))   # faster than a rabbit
        tags = S.cmd(f"data get entity {self.BUNNY} Tags")                                 # 30 = 0b11110
        for b in range(8): self.assertEqual(f'"slf.lvb{b}"' in tags, b in (1, 2, 3, 4), (b, tags))

    def test_random_level_is_8_to_30(self):
        for _ in range(5): self.spawn()
        levels = [int(m) for m in re.findall(r'"Vorpal Bunny Lv\.(\d+)"', S.cmd("execute as @e[tag=slf.vorpal_bunny] run data get entity @s CustomName"))]
        self.assertEqual(len(levels), 5, levels); self.assertTrue(all(8 <= v <= 30 for v in levels), levels)

    def test_low_level_player_gets_exp_by_level_and_a_vorpal_soul(self):
        self.grant("swordsman"); self.set("slf.exp", 0); self.set("slf.vorpal_soul", 0)
        self.spawn(30); self.kill_bunny()
        self.assertEqual(S.score("slf.exp"), 32)            # its level + the 2 every kill gives
        self.assertEqual(S.score("slf.vorpal_soul"), 1)     # level 30 >= player level 1 + 20
        self.assertEqual(S.score("slf.kill_lv"), 0)

    def test_no_vorpal_soul_when_the_bunny_is_not_20_levels_higher(self):
        self.grant("swordsman"); self.set("slf.level", 20); self.set("slf.exp", 0); self.set("slf.vorpal_soul", 0)
        self.spawn(30); self.kill_bunny()
        self.assertEqual(S.score("slf.exp"), 30 // 4 + 2)   # a forest monster: a quarter of its level from player level 12
        self.assertEqual(S.score("slf.vorpal_soul"), 0)

    def test_bunny_attacks_players(self):
        S.platform(); S.cmd(f"gamemode survival {S.player}"); S.cmd(f"effect give {S.player} instant_health 1 10"); S.wait_ticks(4)
        S.as_player("scoreboard players set #spawn_lv slf.mob_level 12"); S.as_player("execute positioned ~2 ~ ~ run function slf:mob/vorpal_bunny/spawn")
        health = None
        for _ in range(20):
            S.wait_ticks(10); health = float(re.search(r"([\d.]+)f", S.cmd(f"data get entity {S.player} Health")).group(1))
            if health < 20: break
        S.cmd(f"gamemode creative {S.player}"); S.cmd(f"effect give {S.player} instant_health 1 10")
        self.assertLess(health, 20, "the Vorpal Bunny never hurt the player")

    def test_wild_rabbits_near_players_become_vorpal_bunnies(self):
        S.platform(); S.as_player("fillbiome ~-8 190 ~-8 ~8 210 ~8 minecraft:desert")
        for i in range(10): S.as_player(f'summon minecraft:rabbit ~{i % 5 - 2} ~ ~{i // 5 + 2} {{Tags:["slf.test"]}}')
        S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.test,tag=slf.vorpal_bunny]"), "desert rabbits became Vorpal Bunnies")
        S.cmd("kill @e[tag=slf.test]"); S.as_player("fillbiome ~-8 190 ~-8 ~8 210 ~8 minecraft:forest")
        for i in range(15): S.as_player(f'summon minecraft:rabbit ~{i % 5 - 2} ~ ~{i // 5 + 2} {{Tags:["slf.test"]}}')
        S.as_player('summon minecraft:rabbit ~ ~ ~-3 {Tags:["slf.test","pet"],CustomName:"Thumper"}')
        S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("passed", S.cmd("execute if entity @e[type=minecraft:rabbit,tag=slf.test,tag=slf.vorpal_bunny]"))   # 1 in 3 each: 15 all staying normal is ~0.2%
        self.assertIn("passed", S.cmd("execute if entity @e[type=minecraft:rabbit,tag=slf.test,tag=!slf.vorpal_bunny]"))  # and not all of them
        self.assertIn("failed", S.cmd("execute if entity @e[type=minecraft:rabbit,tag=slf.test,tag=!slf.seen]"))         # every one got its single roll
        self.assertIn("failed", S.cmd("execute if entity @e[tag=pet,tag=slf.vorpal_bunny]"))                           # a named rabbit stays a pet


class Bosses(Base):
    """The five SLF bosses: stats from level, boss bars, the boss kill reward, natural encounters, night bosses leaving at dawn."""
    # id: (body, level, full name, size)
    BOSSES = {"nightclaw": ("spider", 40, "Nightclaw", 2.5), "bilac": ("phantom", 60, "Bilac the Full Moon Fangs", 3.0),
              "oriana": ("evoker", 75, "Oriana the Uncrowned", 1.3), "lycagon": ("wolf", 90, "Lycagon the Nightslayer", 3.0),
              "ctarnidd": ("elder_guardian", 85, "Ctarnidd of the Abyss", 2.0), "siegwurm": ("ghast", 95, "Siegwurm the Sky Ruler", 1.5),
              "wethermon": ("wither_skeleton", 100, "Wethermon the Tombguard", 1.6)}

    def tearDown(self):
        S.cmd("kill @e[tag=slf.mob]"); S.cmd("time set 1000"); S.cmd(f"gamemode creative {S.player}")

    def boss(self, bid): return f"@e[tag=slf.boss_{bid},limit=1]"

    def test_each_boss_has_its_stats_name_and_bar(self):
        for bid, (body, lv, name, scale) in self.BOSSES.items():
            with self.subTest(bid):
                S.cmd("kill @e[tag=slf.mob]"); S.as_player(f"function slf:test/mob/boss_{bid}"); S.wait_ticks(3)
                self.assertIn("passed", S.cmd(f"execute if entity @e[type=minecraft:{body},tag=slf.boss_{bid}]"))
                self.assertIn(f"{name} Lv.{lv}", S.cmd(f"data get entity {self.boss(bid)} CustomName"))
                self.assertIn(f"is {lv * 4}.0", S.cmd(f"attribute {self.boss(bid)} minecraft:max_health get"))
                self.assertIn(f"is {scale}", S.cmd(f"attribute {self.boss(bid)} minecraft:scale base get"))
                health = float(re.search(r"([\d.]+)f", S.cmd(f"data get entity {self.boss(bid)} Health")).group(1))
                self.assertGreater(health, lv * 4 - 10)   # full health, give or take a scrape from the terrain it spawned in
                bar = int(re.search(r"value of (\d+)", S.cmd(f"bossbar get slf:{bid} value")).group(1))
                self.assertGreater(bar, lv * 4 - 10)
                self.assertIn("shown", S.cmd(f"bossbar get slf:{bid} visible"))
        S.cmd("kill @e[tag=slf.mob]"); S.wait_cycle()
        for bid in self.BOSSES: self.assertIn("hidden", S.cmd(f"bossbar get slf:{bid} visible"), bid)

    def test_wethermon_carries_its_scythe_and_does_not_drop_its_gear(self):
        S.as_player("function slf:test/mob/boss_wethermon"); S.wait_ticks(3)
        self.assertIn("slf.wethermon_scythe", S.cmd(f"data get entity {self.boss('wethermon')} equipment.mainhand"))
        self.assertIn("mainhand: 0.0f", S.cmd(f"data get entity {self.boss('wethermon')} drop_chances"))

    def test_boss_kill_gives_exp_soul_and_opens_the_gate(self):
        self.grant("swordsman"); self.set("slf.exp", 0); self.set("slf.vorpal_soul", 0); self.set("slf.boss_gate", 0); self.set("slf.boss_kills", 0)
        self.set("slf.level", 10)   # next level needs 5000 EXP, so the reward can't be spent on a level-up before it is read
        S.as_player("function slf:test/mob/boss_wethermon"); S.wait_ticks(3); S.cmd(f"gamemode survival {S.player}")
        out = S.as_player(f"damage {self.boss('wethermon')} 100000 minecraft:player_attack by @s"); self.assertIn("Applied", out); S.wait_ticks(6)
        self.assertEqual(S.score("slf.exp"), 100 + 2 + 2400)   # its level + every kill's 2 + the boss reward; not also an elite (wither skeleton) kill
        self.assertEqual((S.score("slf.boss_gate"), S.score("slf.boss_kills"), S.score("slf.vorpal_soul")), (1, 1, 1))

    def test_lycagon_keeps_its_health(self):
        S.cmd("time set 1000"); S.as_player("function slf:test/mob/boss_lycagon"); S.wait_cycle(); S.wait_cycle()
        self.assertIn("is 360.0", S.cmd(f"attribute {self.boss('lycagon')} minecraft:max_health get"))
        health = float(re.search(r"([\d.]+)f", S.cmd(f"data get entity {self.boss('lycagon')} Health")).group(1))
        self.assertGreater(health, 300)   # not clamped to a plain wolf's 8 (a scrape from the terrain is fine)

    def test_lycagon_hunts_players(self):
        S.platform(); S.cmd("time set 18000"); S.cmd(f"gamemode survival {S.player}"); S.cmd(f"effect give {S.player} instant_health 1 10"); S.wait_ticks(4)
        S.as_player("execute positioned ~4 ~ ~ run function slf:mob/boss/lycagon/spawn"); S.cmd("tag @e[tag=slf.boss_new] remove slf.boss_new")
        deaths = S.bot.deaths; hurt = False
        for _ in range(20):
            S.wait_ticks(10)
            m = re.search(r"([\d.]+)f", S.cmd(f"data get entity {S.player} Health"))
            if S.bot.deaths > deaths or (m and float(m.group(1)) < 20): hurt = True; break
        S.cmd(f"gamemode creative {S.player}")
        self.assertTrue(hurt, "Lycagon never attacked: " + S.cmd(f"data get entity {self.boss('lycagon')} angry_at"))

    def test_night_encounter_and_dawn_departure(self):
        self.grant("swordsman"); self.set("slf.level", 60); S.cmd("time set 18000"); S.wait_ticks(2)   # on the ground: Lycagon lands within 24 blocks
        self.assertIn("passed", S.cmd("execute if predicate slf:night"))
        self.assertIn("passed", S.cmd("execute if predicate slf:full_moon_night"))
        mark = S.bot.mark()
        S.as_player('function slf:mob/boss/encounter {id:"lycagon",place:"surface"}'); S.wait_ticks(4)
        self.assertIn("passed", S.cmd("execute if entity @e[tag=slf.boss_lycagon]"))
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.boss_new]"))
        self.assertTrue(any("has appeared" in c for c in S.bot.chat_since(mark)), S.bot.chat_since(mark))
        S.wait_cycle(); S.cmd("kill @e[type=minecraft:item]"); S.cmd("time set 1000"); S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.boss_lycagon]"), "Lycagon stayed after dawn")
        self.assertIn("failed", S.cmd('execute if entity @e[type=minecraft:item,distance=..64]'), "Lycagon dropped loot when it left")
        self.assertTrue(any("vanishes with the dawn" in c for c in S.bot.chat_since(mark)))

    def test_night_boss_spawned_by_day_stays_until_after_a_night(self):
        S.cmd("time set 1000"); S.as_player("function slf:test/mob/boss_lycagon"); S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("passed", S.cmd("execute if entity @e[tag=slf.boss_lycagon]"))

    def test_roll_respects_place_and_level(self):
        """A level 5 player on the surface at night: nothing qualifies, even if every chance came up."""
        S.platform(); self.grant("swordsman"); self.set("slf.level", 5); S.cmd("time set 18000")
        for _ in range(30): S.as_player("function slf:mob/boss/roll")
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.boss]"))
        self.set("slf.level", 99)   # now Bilac (full moon, open sky, 10%) and Lycagon (night, 1.7%) both qualify
        for _ in range(60): S.as_player("function slf:mob/boss/roll")
        self.assertIn("passed", S.cmd("execute if entity @e[tag=slf.boss_bilac]"))   # 60 rolls at 10%: misses 0.2% of the time
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.boss_nightclaw]"))   # caves only
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.boss_wethermon]"))   # Nether only
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.boss_ctarnidd]"))    # deep ocean, in the water only

    def test_siegwurm_always_drops_a_unique_core(self):
        S.platform(); S.as_player("function slf:test/mob/boss_siegwurm"); S.wait_ticks(3); S.cmd(f"gamemode survival {S.player}")
        out = S.as_player("damage @e[tag=slf.boss_siegwurm,limit=1] 100000 minecraft:player_attack by @s"); self.assertIn("Applied", out); S.wait_ticks(10)
        self.assertIn("passed", S.as_player('execute if items entity @e[type=minecraft:item,distance=..32] contents *[minecraft:custom_model_data={strings:["slf.unique_core"]}]'))


class Goblins(Base):
    """Goblin and Redcap Goblin (design doc V9): small zombie bodies with 3D goblin heads, where and when they appear,
    level-based stats and EXP, the forest EXP falloff at level 12, Redcaps calling for help and leaving at dawn."""
    KINDS = {"goblin": ("Goblin", 3, 10, 8, 1, 3825419), "red_hat_goblin": ("Redcap Goblin", 14, 22, 10, 2, 11546150)}  # name, min/max level, base hp, base atk, cap colour

    def test_stats_look_and_level(self):
        for gid, (name, lo, hi, hp, atk, cap) in self.KINDS.items():
            with self.subTest(gid):
                S.cmd("kill @e[tag=slf.mob]"); S.as_player(f"function slf:test/mob/{gid}"); S.wait_ticks(3)
                sel = f"@e[tag=slf.{gid},limit=1]"
                m = re.search(rf'"{name} Lv\.(\d+)"', S.cmd(f"data get entity {sel} CustomName")); self.assertTrue(m, gid)
                lv = int(m.group(1)); self.assertTrue(lo <= lv <= hi, lv)
                self.assertIn(f"is {hp + lv}.0", S.cmd(f"attribute {sel} minecraft:max_health base get"))
                self.assertIn(f"is {atk + lv // 3}.0", S.cmd(f"attribute {sel} minecraft:attack_damage base get"))
                self.assertIn("is 0.6", S.cmd(f"attribute {sel} minecraft:scale base get"))
                self.assertIn(f'"slf:{gid}_head"', S.cmd(f"data get entity {sel} equipment.head"))   # the 3D head model
                self.assertIn(f"slf:{gid}_drops", S.cmd(f"data get entity {sel} DeathLootTable"))

    def test_kill_gives_level_exp_not_zombie_exp(self):
        self.grant("swordsman"); self.set("slf.exp", 0); S.cmd("scoreboard players set #spawn_lv slf.mob_level 15")
        S.as_player("function slf:test/mob/red_hat_goblin"); S.wait_ticks(3); S.cmd(f"gamemode survival {S.player}")
        out = S.as_player("damage @e[tag=slf.red_hat_goblin,limit=1] 1000 minecraft:player_attack by @s"); self.assertIn("Applied", out); S.wait_ticks(6)
        self.assertEqual(S.score("slf.exp"), 17)   # level 15 + every kill's 2; not also a common (zombie) kill

    def test_goblins_do_not_burn_by_day(self):
        S.platform(); S.cmd("time set 6000"); S.as_player("function slf:test/mob/goblin"); S.wait_cycle(); S.wait_cycle()
        self.assertIn("passed", S.cmd("execute if entity @e[tag=slf.goblin]"))
        self.assertIn("Fire: 0s", S.cmd("data get entity @e[tag=slf.goblin,limit=1]").replace("Fire: -1s", "Fire: 0s"))

    def test_forest_zombies_become_goblins_and_others_do_not(self):
        S.platform(); S.cmd("time set 18000")
        S.as_player("fillbiome ~-8 190 ~-8 ~8 210 ~8 minecraft:forest")
        for i in range(20): S.as_player(f'summon minecraft:zombie ~{i % 5 - 2} ~ ~{i // 5 + 2} {{Tags:["slf.test"],IsBaby:0b}}')
        S.as_player('summon minecraft:zombie ~ ~ ~-3 {Tags:["slf.test","named"],CustomName:"Bob",IsBaby:0b}')
        S.wait_cycle(); S.wait_ticks(5)
        goblins = S.cmd("execute if entity @e[tag=slf.test,tag=slf.goblin]"); red = S.cmd("execute if entity @e[tag=slf.test,tag=slf.red_hat_goblin]")
        self.assertIn("passed", goblins)   # 20 zombies at 40% each: none at all is ~0.004%
        self.assertIn("failed", red, "Redcaps appeared in a forest")
        self.assertIn("passed", S.cmd("execute if entity @e[type=minecraft:zombie,tag=slf.test,tag=!slf.mob]"))
        self.assertIn("failed", S.cmd("execute if entity @e[type=minecraft:zombie,tag=slf.test,tag=!slf.seen]"))
        self.assertIn("failed", S.cmd("execute if entity @e[tag=named,tag=slf.mob]"))
        S.cmd("kill @e[tag=slf.test]"); S.cmd("kill @e[tag=slf.mob]"); S.as_player("fillbiome ~-8 190 ~-8 ~8 210 ~8 minecraft:desert")
        for i in range(10): S.as_player(f'summon minecraft:zombie ~{i % 5 - 2} ~ ~{i // 5 + 2} {{Tags:["slf.test"],IsBaby:0b}}')
        S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.test,tag=slf.mob]"), "zombies outside forests became goblins")
        S.cmd("time set 1000")

    def summon_zombies(self, n):
        for i in range(n): S.as_player(f'summon minecraft:zombie ~{i % 5 - 2} ~ ~{i // 5 + 2} {{Tags:["slf.test"],IsBaby:0b}}')

    def test_redcaps_only_in_swamps_at_night(self):
        S.platform(); S.as_player("fillbiome ~-8 190 ~-8 ~8 210 ~8 minecraft:swamp")
        S.cmd("time set 6000"); self.summon_zombies(15); S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.test,tag=slf.mob]"), "swamp zombies converted by day")
        S.cmd("kill @e[tag=slf.test]"); S.cmd("time set 18000"); self.summon_zombies(15); S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("passed", S.cmd("execute if entity @e[tag=slf.test,tag=slf.red_hat_goblin]"))   # 15 at 50%: none is 0.003%
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.test,tag=slf.goblin]"), "forest goblins in a swamp")
        S.cmd("kill @e[tag=slf.test]"); S.cmd("time set 1000")

    def test_redcap_calls_for_help_once(self):
        S.platform(); S.cmd("time set 18000"); S.cmd("scoreboard players set #spawn_lv slf.mob_level 20")
        S.as_player("function slf:test/mob/red_hat_goblin"); S.wait_ticks(3); S.cmd(f"gamemode survival {S.player}")
        S.as_player("damage @e[tag=slf.red_hat_goblin,limit=1,sort=nearest] 1 minecraft:player_attack by @s"); S.wait_ticks(4)
        count = int(re.search(r"Count: (\d+)", S.cmd("execute if entity @e[tag=slf.red_hat_goblin]")).group(1))
        self.assertEqual(count, 3)   # the one that was hit, plus the two it called
        S.cmd("execute as @e[tag=slf.red_hat_goblin] run data merge entity @s {HurtTime:0s}")
        S.as_player("damage @e[tag=slf.red_hat_goblin,tag=slf.called,limit=1] 1 minecraft:player_attack by @s"); S.wait_ticks(4)
        self.assertIn("Count: 3", S.cmd("execute if entity @e[tag=slf.red_hat_goblin]"))   # a Redcap only calls once
        S.cmd(f"gamemode creative {S.player}"); S.cmd("time set 1000")

    def test_redcaps_leave_at_dawn_without_loot(self):
        S.platform(); S.cmd("time set 18000"); S.as_player("function slf:test/mob/red_hat_goblin"); S.wait_cycle()
        S.cmd("kill @e[type=minecraft:item]"); S.cmd("time set 1000"); S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.red_hat_goblin]"), "Redcap stayed after dawn")
        self.assertIn("failed", S.cmd("execute if entity @e[type=minecraft:item]"), "Redcap dropped loot when it left")   # items were cleared just before dawn

    def test_forest_exp_falls_off_at_level_12(self):
        self.grant("swordsman")
        for level, expected in ((5, 8 + 2), (12, 8 // 4 + 2)):
            with self.subTest(level=level):
                self.set("slf.level", level); self.set("slf.exp", 0); S.cmd("scoreboard players set #spawn_lv slf.mob_level 8")
                S.as_player("function slf:test/mob/goblin"); S.wait_ticks(3); S.cmd(f"gamemode survival {S.player}")
                S.as_player("damage @e[tag=slf.goblin,limit=1,sort=nearest] 1000 minecraft:player_attack by @s"); S.wait_ticks(6)
                self.assertEqual(S.score("slf.exp"), expected)
        S.cmd(f"gamemode creative {S.player}")

class OrcsAndFrogs(Base):
    """Orc (leads goblins) and Mud Frog (passive, mud-coated, hits back) from design document V9."""

    def health(self, sel):
        return float(re.search(r"([\d.]+)f", S.cmd(f"data get entity {sel} Health")).group(1))

    def test_orc_arrives_with_two_goblins(self):
        S.platform(); S.cmd("scoreboard players set #spawn_lv slf.mob_level 12"); S.as_player("function slf:test/mob/orc"); S.wait_ticks(3)
        orc = "@e[tag=slf.orc,limit=1]"
        self.assertIn("Orc Lv.12", S.cmd(f"data get entity {orc} CustomName"))
        self.assertIn("is 32.0", S.cmd(f"attribute {orc} minecraft:max_health base get"))     # 20 + level
        self.assertIn("is 7.0", S.cmd(f"attribute {orc} minecraft:attack_damage base get"))    # 3 + level/3
        self.assertIn("is 1.25", S.cmd(f"attribute {orc} minecraft:scale base get"))
        self.assertIn('"slf:orc_head"', S.cmd(f"data get entity {orc} equipment.head"))
        self.assertIn("Count: 2", S.cmd("execute at @e[tag=slf.orc,limit=1] if entity @e[tag=slf.goblin,distance=..6]"))   # its scouting party

    def test_mud_frog_shrugs_off_swords_and_hits_back(self):
        S.platform(); S.cmd(f"gamemode survival {S.player}"); S.cmd(f"effect give {S.player} instant_health 1 10"); S.cmd(f"effect clear {S.player} slowness")
        S.cmd("scoreboard players set #spawn_lv slf.mob_level 16"); S.as_player("execute positioned ^ ^ ^2 run function slf:mob/mud_frog/spawn"); S.wait_ticks(3)
        frog = "@e[tag=slf.mud_frog,limit=1]"
        self.assertIn("is 22.0", S.cmd(f"attribute {frog} minecraft:max_health base get"))   # 6 + level
        self.assertIn("is 1.6", S.cmd(f"attribute {frog} minecraft:scale base get"))
        S.cmd(f"item replace entity {S.player} weapon.mainhand with minecraft:iron_sword"); S.wait_ticks(2)
        S.as_player(f"damage {frog} 6 minecraft:player_attack by @s"); S.wait_ticks(4)
        self.assertAlmostEqual(self.health(frog), 22 - 6 + 4, delta=0.01)                     # the mud soaks up most of a sword hit
        self.assertIn("slowness", S.effects())                                                # and it splashed the player
        self.assertLess(float(re.search(r"([\d.]+)f", S.cmd(f"data get entity {S.player} Health")).group(1)), 20)
        S.cmd(f"item replace entity {S.player} weapon.mainhand with minecraft:mace"); S.cmd(f"data merge entity {frog} {{HurtTime:0s}}"); S.wait_ticks(12)
        before = self.health(frog); S.as_player(f"damage {frog} 6 minecraft:player_attack by @s"); S.wait_ticks(4)
        self.assertAlmostEqual(self.health(frog), before - 6, delta=0.01)                    # blunt weapons do full damage
        S.cmd(f"clear {S.player}"); S.cmd(f"gamemode creative {S.player}"); S.cmd(f"effect give {S.player} instant_health 1 10")

    def test_swamp_frogs_become_mud_frogs(self):
        S.platform(); S.as_player("fillbiome ~-8 190 ~-8 ~8 210 ~8 minecraft:swamp")
        for i in range(4): S.as_player(f'summon minecraft:frog ~{i - 2} ~ ~3 {{Tags:["slf.test"]}}')
        S.as_player('summon minecraft:frog ~ ~ ~-3 {Tags:["slf.test","named"],CustomName:"Kermit"}')
        S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("Count: 4", S.cmd("execute if entity @e[tag=slf.test,tag=slf.mud_frog]"))
        self.assertIn("failed", S.cmd("execute if entity @e[tag=named,tag=slf.mud_frog]"))
        S.cmd("kill @e[tag=slf.test]"); S.as_player("fillbiome ~-8 190 ~-8 ~8 210 ~8 minecraft:plains")
        for i in range(4): S.as_player(f'summon minecraft:frog ~{i - 2} ~ ~3 {{Tags:["slf.test"]}}')
        S.wait_cycle(); S.wait_ticks(5)
        self.assertIn("failed", S.cmd("execute if entity @e[tag=slf.test,tag=slf.mud_frog]"), "frogs outside swamps became Mud Frogs")

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
