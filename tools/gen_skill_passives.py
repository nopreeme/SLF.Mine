"""Writes the passive bonus every skill grants, from the one table below.

    python tools/gen_skill_passives.py

Outputs
  data_pack/data/slf/function/skills/attributes.mcfunction   attribute modifiers, re-checked once per second
  data_pack/data/slf/function/skills/mana_bonus.mcfunction   mana pool / regeneration bonuses (called by stats/apply_derived)
  SKILL_EFFECTS.md                                           the same table for players and contributors

Skills that already had hand-written behaviour (Ignition, Skywalker, Big Tantrum, ...) live in skills/passives.mcfunction
and are listed under HANDWRITTEN only so the document is complete.

Each modifier has the id slf:skill/<skill>/<attribute>. Changing a value here does not update players who already hold
the modifier (the game refuses to add an id twice); rename the skill's entry or remove the tag and re-add it to refresh.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FN = os.path.join(REPO, "data_pack", "data", "slf", "function", "skills")

V, B, T = "add_value", "add_multiplied_base", "add_multiplied_total"
# skill: [(attribute, amount, operation), ...]   — or ("mana_max", n) / ("mana_regen", n)
SKILLS = {
    # ---- Swordsman line
    "power_slash":               [("attack_damage", 1, V)],
    "sword_of_rough_waves":      [("sweeping_damage_ratio", 0.25, V)],
    "spin_slash":                [("attack_speed", 0.2, V)],
    "lash_slash":                [("attack_damage", 1.5, V)],
    "lion_fall":                 [("safe_fall_distance", 4, V), ("fall_damage_multiplier", -0.25, V)],
    "shakudanzan":               [("entity_interaction_range", 0.5, V)],
    "hekaton_slash":             [("attack_speed", 0.5, V)],
    "spectrum_slash":            [("sweeping_damage_ratio", 0.5, V)],
    "sword_dance":               [("movement_speed", 0.1, B)],
    "manbufu":                   [("mana_regen", 1)],
    "sword_dance_reincarnation": [("attack_speed", 0.4, V), ("movement_speed", 0.1, B)],
    "sword_god_danba":           [("attack_damage", 3, V)],
    "asura_kagura":              [("armor", 2, V), ("attack_damage", 1, V)],
    # ---- Warrior line
    "megaton_swing":             [("attack_damage", 1, V), ("attack_knockback", 0.5, V)],
    "rigid_strength":            [("knockback_resistance", 0.2, V)],
    "front_position":            [("armor", 2, V)],
    "gigaton_swing":             [("attack_damage", 2, V), ("attack_knockback", 1, V)],
    "fortress_breaker":          [("block_break_speed", 0.25, B), ("mining_efficiency", 5, V)],
    "gobus_courage":             [("max_health", 4, V)],
    "break_attack":              [("attack_damage", 2, V)],
    "tsujizanri":                [("attack_speed", 0.3, V), ("sweeping_damage_ratio", 0.25, V)],
    # ---- Fighter line
    "dual_impact":               [("attack_speed", 0.3, V)],
    "crash_upper":               [("attack_knockback", 0.5, V)],
    "knuckle_rush":              [("attack_damage", 1, V)],
    "meteor_fall":               [("safe_fall_distance", 6, V), ("attack_damage", 1, V)],
    "zanzui_flying_blade_leg":   [("jump_strength", 0.1, V), ("movement_speed", 0.05, B)],
    "grapple_train":             [("entity_interaction_range", 0.5, V), ("knockback_resistance", 0.1, V)],
    "strong_puncher":            [("attack_damage", 2, V)],
    "one_inch_impact":           [("attack_knockback", 1.5, V)],
    "hundred_sounding":          [("attack_speed", 0.6, V)],
    # ---- Mercenary line
    "duelism":                   [("armor", 1, V), ("attack_damage", 0.5, V)],
    "overheat":                  [("attack_speed", 0.2, V), ("burning_time", -0.5, T)],
    # ---- Bandit / Thief / Assassin / Killing Joke
    "dirty_sword":               [("attack_damage", 1, V)],
    "assassin_pierce":           [("attack_damage", 0.5, V), ("sneaking_speed", 0.2, V)],
    "stealth_assault":           [("sneaking_speed", 0.3, V)],
    "quick_spin":                [("attack_speed", 0.25, V)],
    "desperate_sting":           [("attack_damage", 2, V)],
    "masakuru_byte":             [("attack_speed", 0.3, V)],
    "hate_trumple":              [("movement_speed", 0.1, B), ("step_height", 0.4, V)],
    "limit_break_rees":          [("movement_speed", 0.2, B), ("attack_speed", 0.3, V)],
    "ablaze_advanced_ale":       [("attack_damage", 2, V), ("burning_time", -1, T)],
    "serial_killer":             [("attack_damage", 2.5, V)],
    # ---- Ninja / Shinobi
    "after_all_unyo":            [("safe_fall_distance", 8, V), ("fall_damage_multiplier", -0.5, V)],
    "burnout":                   [("movement_speed", 0.15, B)],
    # ---- Priest / Bishop / Saint
    "breath_of_anti_harm":       [("max_health", 2, V)],
    "phalanx":                   [("armor", 2, V)],
    "protect_charge":            [("knockback_resistance", 0.2, V)],
    "guardian_heart":            [("max_health", 4, V)],
    "protect_smash":             [("armor_toughness", 2, V)],
    "shield_bashing":            [("attack_knockback", 1, V)],
    "embrace_of_devil":          [("armor", 3, V)],
    "causal_accumulation":       [("luck", 1, V), ("mana_max", 20)],
    "unbreakable":               [("knockback_resistance", 0.5, V), ("armor_toughness", 2, V)],
    # ---- Monk / Monk Soldier / Spirit Fist
    "tasram_fist":               [("attack_damage", 1.5, V)],
    "skull_shaker":              [("attack_knockback", 0.5, V)],
    "tanda_breathing":           [("oxygen_bonus", 2, V), ("mana_regen", 1)],
    "infight":                   [("attack_speed", 0.3, V)],
    "meditation":                [("mana_regen", 2)],
    "hand_of_fortune":           [("luck", 2, V)],
    "kings_silver_arm":          [("armor", 3, V), ("attack_damage", 1, V)],
    # ---- Mage / Sage
    "chanting_and_memorizing":   [("mana_max", 20)],
    "instant_vision":            [("entity_interaction_range", 1, V), ("block_interaction_range", 1, V)],
    "hegemony_world":            [("mana_max", 40)],
    "analyze_legacy":            [("luck", 2, V)],
    "blaze_shot":                [("attack_damage", 0.5, V), ("burning_time", -0.5, T)],
    # ---- Knight line
    "flash_counter":             [("attack_speed", 0.3, V)],
    "paring_protect":            [("armor", 2, V)],
    "total_body_takeshi":        [("knockback_resistance", 0.3, V), ("max_health", 2, V)],
    "fatal_gain":                [("attack_damage", 1.5, V)],
    "iggist_requiem":            [("attack_damage", 3, V)],
    # ---- Boss skill
    "reflexus":                  [("movement_speed", 0.1, B), ("attack_speed", 0.2, V)],
}
HANDWRITTEN = {
    "wisdoms_divine_eye": "Night Vision", "skywalker": "Jump Boost I and Slow Falling", "skatefoot": "Speed I", "formula_drift": "Speed II",
    "slide_step": "Speed I", "gravity_zero": "Slow Falling", "acrobat": "Resistance I while airborne",
    "managarm_pride": "Strength I–III, stronger the lower your health", "ignition": "Strength I and Speed I for a minute after taking damage",
    "slash_ignition": "Strength II and Speed II for a minute after taking damage", "holy_shield": "Resistance I", "iron_skin": "Resistance II",
    "rechette_step": "Speed I and Jump Boost I", "big_tantrum": "Activated from the menu: glowing, kills count toward Grand Tantrum (drains mana)",
    "grand_tantrum": "Activated from the menu: glowing and Strength I (drains mana)", "inexhaustible_beasts": "Strength I", "terraton_corapsa": "Strength I",
    "bradion": "Haste I–II while sprinting",
}
NAMES = {"armor": "armour", "armor_toughness": "armour toughness", "attack_damage": "attack damage", "attack_knockback": "attack knockback",
         "attack_speed": "attack speed", "block_break_speed": "block breaking speed", "block_interaction_range": "block reach",
         "burning_time": "time spent on fire", "entity_interaction_range": "attack reach", "fall_damage_multiplier": "fall damage",
         "jump_strength": "jump strength", "knockback_resistance": "knockback resistance", "luck": "luck", "max_health": "max health",
         "mining_efficiency": "mining efficiency", "movement_speed": "movement speed", "oxygen_bonus": "oxygen", "safe_fall_distance": "safe fall distance (blocks)",
         "sneaking_speed": "sneaking speed", "step_height": "step height", "sweeping_damage_ratio": "sweep damage"}

def num(x): return str(int(x)) if float(x).is_integer() else repr(float(x))
def title(k): return " ".join(w.capitalize() for w in k.split("_"))
def describe(e):
    if e[0] == "mana_max": return f"+{e[1]} max mana"
    if e[0] == "mana_regen": return f"+{e[1]} mana per second"
    attr, amount, op = e; sign = "+" if amount > 0 else "−"; a = abs(amount)
    if op == V:
        if attr in ("knockback_resistance", "sweeping_damage_ratio", "fall_damage_multiplier"): return f"{sign}{round(a * 100)}% {NAMES[attr]}"
        if attr == "max_health": return f"{sign}{num(a / 2)} heart{'s' if a != 2 else ''} of max health"
        return f"{sign}{num(a)} {NAMES[attr]}"
    return f"{sign}{round(a * 100)}% {NAMES[attr]}"

def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f: f.write(text.rstrip("\n") + "\n")

if __name__ == "__main__":
    assert not set(SKILLS) & set(HANDWRITTEN)
    attr = ["# GENERATED by tools/gen_skill_passives.py — edit the table there, not this file.",
            "# Runs every 20t. Each skill tag keeps its attribute modifiers on the player; losing the tag removes them.",
            "# 'modifier add' on a modifier that is already there (and 'remove' on one that is not) fails quietly, which is intended."]
    mana = ["# GENERATED by tools/gen_skill_passives.py — edit the table there, not this file.",
            "# Called by stats/apply_derived as the player. #m slf.tmp = mana pool size, #r slf.tmp = mana gained per second."]
    for skill, effects in SKILLS.items():
        attr.append(f"# {title(skill)}: " + ", ".join(describe(e) for e in effects))
        for e in effects:
            if e[0] == "mana_max": mana.append(f"execute if entity @s[tag=slf.skill.{skill}] run scoreboard players add #m slf.tmp {e[1]}")
            elif e[0] == "mana_regen": mana.append(f"execute if entity @s[tag=slf.skill.{skill}] run scoreboard players add #r slf.tmp {e[1]}")
            else:
                a, amount, op = e; mid = f"slf:skill/{skill}/{a}"
                attr.append(f"execute as @a[tag=slf.skill.{skill}] run attribute @s minecraft:{a} modifier add {mid} {num(amount)} {op}")
                attr.append(f"execute as @a[tag=!slf.skill.{skill}] run attribute @s minecraft:{a} modifier remove {mid}")
        if all(e[0].startswith("mana") for e in effects): attr.pop()
    write(os.path.join(FN, "attributes.mcfunction"), "\n".join(attr))
    write(os.path.join(FN, "mana_bonus.mcfunction"), "\n".join(mana))
    rows = {**{k: ", ".join(describe(e) for e in v) for k, v in SKILLS.items()}, **HANDWRITTEN}
    doc = ["# Skill effects", "",
           "What each skill does once you have it. Generated by `tools/gen_skill_passives.py`; edit the table there.", "",
           "Bonuses are permanent while you hold the skill and stack with each other, with stat bonuses and with gear.", "",
           "| Skill | Effect |", "|---|---|"]
    doc += [f"| {title(k)} | {rows[k]} |" for k in sorted(rows)]
    write(os.path.join(REPO, "SKILL_EFFECTS.md"), "\n".join(doc))
    print(f"{len(SKILLS)} generated + {len(HANDWRITTEN)} hand-written = {len(rows)} skills")
