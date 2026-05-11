# SLF.Mine — Test Guide

Run all commands as OP in creative mode. After each `/reload`, the pack must print:
`[SLF] Shangri-La Frontier pack loaded.`

**Reset between tests:**
```
/function slf:admin/reset_player
```

---

## KNOWN BUG — Thief / Bandit mismatch

Your class tree has **Bandit as T1** and **Thief as T2 from Bandit**.
The code has the opposite: **Thief is T1**, **Bandit requires `was_thief`**.
Veteran also requires `was_thief` in code, but the tree shows it from Mercenary.

These need to be fixed before the Thief/Bandit/Veteran paths are correct.

---

## 1. PACK LOAD

```
/reload
/scoreboard objectives list
```
Expected: list includes `slf.class`, `slf.level`, `slf.exp`, `slf.sp_points`, `slf.focus`, `slf.karma`, etc.

---

## 2. T1 CLASS SELECTION (test each independently — reset between)

### Swordsman
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Swordsman]** in chat.
Expected: "You have become a Swordsman." — tags `slf.class_chosen`, `slf.was_swordsman`, `slf.skill.power_slash`, `slf.skill.sword_of_rough_waves`, `slf.skill.spin_slash`
```
/scoreboard players get @s slf.class
```
Expected: `1`

### Warrior
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Warrior]**. Expected: class `2`, skills `megaton_swing`, `rigid_strength`, `front_position`.

### Fighter
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Fighter]**. Expected: class `20`, skills `dual_impact`, `crash_upper`, `knuckle_rush`.

### Mercenary
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Mercenary]**. Expected: class `30`, skills `manbufu`, `duelism`, `overheat`, `ignition`.

### Thief (NOTE: Bandit is listed T1 in tree but code has Thief as T1 — see known bug above)
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Thief]**. Expected: class `3`, skills `stealth_assault`, `slide_step`, `quick_spin`.

### Priest
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Priest]**. Expected: class `4`, skills `breath_of_anti_harm`, `phalanx`, `protect_charge`.

### Monk
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Monk]**. Expected: class `5`, skills `tasram_fist`, `skull_shaker`, `tanda_breathing`.

### Mage
```
/function slf:admin/reset_player
/function slf:class/select
```
Click **[Mage]**. Expected: class `6`, skills `wisdoms_divine_eye`, `chanting_and_memorizing`, `tanda_breathing`.

### Block double-selection
```
/function slf:class/select
```
Click any class again. Expected: silent fail (no second class granted, `class_chosen` gate blocks it).
```
/scoreboard players get @s slf.class
```
Expected: still `6` (unchanged from Mage).

---

## 3. T2 CLASS EVOLUTION

Use `execute as @s` to grant while already having the prerequisite from the T1 test above, or set up manually.

### Sword Master (requires was_swordsman)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/execute as @s run function slf:class/grant/sword_master
```
Expected: "You have become a Sword Master." — class `10`, skills `lash_slash`, `lion_fall`, `shakudanzan`, tag `slf.was_sword_master`.

### Magic Swordsman (requires was_swordsman)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/execute as @s run function slf:class/grant/magic_swordsman
```
Expected: class `11`, skills `slash_ignition`, `sword_dance`, `manbufu`, tag `slf.was_magic_swordsman`.

### Barbarian (requires was_warrior OR was_fighter)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/warrior
/execute as @s run function slf:class/grant/barbarian
```
Expected: class `14`, skills `gigaton_swing`, `fortress_breaker`, `gobus_courage`.
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/fighter
/execute as @s run function slf:class/grant/barbarian
```
Expected: same — confirm either prerequisite works.

### Destroyer (requires was_fighter)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/fighter
/execute as @s run function slf:class/grant/destroyer
```
Expected: class `21`, skills `meteor_fall`, `zanzui_flying_blade_leg`, `grapple_train`.

### Bandit (requires was_thief — see known bug)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/thief
/execute as @s run function slf:class/grant/bandit
```
Expected: class `50`, skills `dirty_sword`, `assassin_pierce`, `big_tantrum`, tag `slf.was_bandit`.

### Ninja (requires was_thief)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/thief
/execute as @s run function slf:class/grant/ninja
```
Expected: class `51`, skills `formula_drift`, `skatefoot`, `rechette_step`, tag `slf.was_ninja`.

### Veteran (requires was_thief — see known bug, tree shows from Mercenary)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/thief
/execute as @s run function slf:class/grant/veteran
```
Expected: class `31`, title `slf.title.apex_veteran`, apex message + sound.

### Bishop (requires was_priest)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/priest
/execute as @s run function slf:class/grant/bishop
```
Expected: class `18`, skills `guardian_heart`, `protect_smash`, `shield_bashing`.

### Monk Soldier (requires was_monk)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/monk
/execute as @s run function slf:class/grant/monk_soldier
```
Expected: class `60`, skills `infight`, `grapple_train`, `meditation`.

### Sage (requires was_mage)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/mage
/execute as @s run function slf:class/grant/sage
```
Expected: class `70`, skills `instant_vision`, `hegemony_world`, `analyze_legacy`.

---

## 4. T3 CLASS EVOLUTION

### Kansei (requires was_sword_master)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/execute as @s run function slf:class/grant/sword_master
/execute as @s run function slf:class/grant/kansei
```
Expected: class `12`, skills `inexhaustible_beasts`, `hekaton_slash`, `spectrum_slash`.

### Mysterious Sword (requires was_magic_swordsman)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/execute as @s run function slf:class/grant/magic_swordsman
/execute as @s run function slf:class/grant/mysterious_sword
```
Expected: class `13`, skills `sword_dance_reincarnation`, `sword_god_danba`, `asura_kagura`.

### War King (requires was_barbarian)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/warrior
/execute as @s run function slf:class/grant/barbarian
/execute as @s run function slf:class/grant/war_king
```
Expected: class `15`, skills `terraton_corapsa`, `break_attack`, `tsujizanri`.

### Crazy Fist (requires was_destroyer) — APEX
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/fighter
/execute as @s run function slf:class/grant/destroyer
/execute as @s run function slf:class/grant/crazy_fist
```
Expected: class `22`, apex message + challenge_complete sound, title `slf.title.apex_crazy_fist`. Confirm `knuckle_rush` tag is removed, `strong_puncher` is added.

### Assassin (requires was_bandit)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/thief
/execute as @s run function slf:class/grant/bandit
/execute as @s run function slf:class/grant/assassin
```
Expected: class `16`, skills `desperate_sting`, `masakuru_byte`, `hate_trumple`.

### Killing Joke (requires was_assassin)
```
/execute as @s run function slf:class/grant/killing_joke
```
(Continue from Assassin above.) Expected: class `17`, skills `limit_break_rees`, `ablaze_advanced_ale`, `serial_killer`.

### Shinobi (requires was_ninja)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/thief
/execute as @s run function slf:class/grant/ninja
/execute as @s run function slf:class/grant/shinobi
```
Expected: class `52`, skills `skywalker`, `after_all_unyo`, `burnout`.

### Star Shinobi Sei (requires was_shinobi) — APEX
```
/execute as @s run function slf:class/grant/star_shinobi_sei
```
Expected: class `16`, apex message + sound, title `slf.title.apex_star_shinobi`.

### Saint (requires was_bishop)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/priest
/execute as @s run function slf:class/grant/bishop
/execute as @s run function slf:class/grant/saint
```
Expected: class `19`, skills `embrace_of_devil`, `causal_accumulation`, `unbreakable`.

### Spirit Fist (requires was_monk_soldier)
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/monk
/execute as @s run function slf:class/grant/monk_soldier
/execute as @s run function slf:class/grant/spirit_fist
```
Expected: class `61`, skills `hand_of_fortune`, `kings_silver_arm`, `hundred_sounding`.

### Omnipotent Wisdom (requires was_sage) — APEX
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/mage
/execute as @s run function slf:class/grant/sage
/execute as @s run function slf:class/grant/omnipotent_wisdom
```
Expected: class `62`, apex message + sound, title `slf.title.apex_omni_wisdom`.

---

## 5. PREREQUISITE BLOCKING (negative tests)

These should all silently fail with no class change.

```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/sword_master
```
Expected: no message, class stays `0`.

```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/execute as @s run function slf:class/grant/kansei
```
Expected: no message (needs sword_master first), class stays `1`.

```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/warrior
/execute as @s run function slf:class/grant/destroyer
```
Expected: no message (destroyer needs fighter, not warrior).

---

## 6. SKILL FOCUS & LEARNING

Set up as Swordsman (has `power_slash` skill already, so focusing it should be blocked):
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/function slf:skills/menu
```
Click **[Power Slash]** — expected: fail message (already learned).

Focus a skill you don't have yet (Spin Slash is granted, so try Megaton Swing):
Click **[Megaton Swing]** — expected: "Focusing: Megaton Swing [0/500]", `slf.focus = 2`, `slf.focus_stat = 1`, `slf.threshold = 500`.
```
/scoreboard players get @s slf.focus
/scoreboard players get @s slf.threshold
```

Force-trigger threshold to test instant learn:
```
/scoreboard players set @s slf.sp 500
```
Wait 1 second (next 20t cycle). Expected: "Skill learned: Megaton Swing", `slf.focus` resets to `0`, tag `slf.skill.megaton_swing` added.
```
/tag @s list
```

---

## 7. STAT SPENDING

```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/scoreboard players set @s slf.sp_points 10
/function slf:stats/menu
```
Click **[+AGI]** — expected: `slf.stat.agi = 1`, `slf.sp_points = 9`.
Click **[+STR]** — expected: `slf.stat.str = 1`, `slf.sp_points = 8`.

Verify stat menu blocked before choosing class:
```
/function slf:admin/reset_player
/function slf:stats/menu
```
Expected: silent fail (no class chosen).

Test effects applying (spend 5 AGI, wait 1 second for apply cycle):
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/scoreboard players set @s slf.sp_points 10
/scoreboard players set @s slf.stat.agi 5
```
Wait 1 second. Expected: Speed I effect visible.
```
/scoreboard players set @s slf.stat.agi 10
```
Wait 1 second. Expected: Speed II.

---

## 8. EXP & LEVELING

```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/scoreboard players set @s slf.level 1
/scoreboard players set @s slf.exp 100
```
Wait 1 second. Expected: "Level Up! Now level 2. +3 stat points.", `slf.sp_points = 3`.

Test standby gate at level 99:
```
/scoreboard players set @s slf.level 99
/scoreboard players set @s slf.exp 5000
```
Wait 1 second. Expected: level stays `99`, exp drains into `slf.exp_extend`, `slf.standby = 1`.
```
/scoreboard players get @s slf.exp_extend
```

Test milestone bonus (level 10):
```
/scoreboard players set @s slf.level 9
/scoreboard players set @s slf.sp_points 0
/scoreboard players set @s slf.exp 5000
```
Wait 1 second. Expected: level `10`, `slf.sp_points = 5` (3 base + 2 milestone bonus).

---

## 9. KARMA & MASK

```
/function slf:admin/reset_player
/scoreboard players set @s slf.karma 50
```
Wait 60 seconds (karma decay cycle). Expected: `slf.karma` drops by 1.

Test bounty hunter spawn at 100 karma:
```
/scoreboard players set @s slf.karma 100
```
Wait 1 second. Expected: "A Bounty Hunter has found you." — pillager spawns nearby with Strength II.

Test karma cap:
```
/scoreboard players set @s slf.karma 210
```
Wait 1 second. Expected: capped to `200`.
```
/scoreboard players get @s slf.karma
```

---

## 10. PASSIVE EFFECTS

Verify passives fire every second. Set up a skill and watch the effect:
```
/function slf:admin/reset_player
/execute as @s run function slf:class/grant/swordsman
/tag @s add slf.skill.holy_shield
```
Wait 1 second. Expected: Resistance I applied (3t duration, constantly refreshed).

```
/tag @s add slf.skill.iron_skin
```
Wait 1 second. Expected: Resistance II (overrides Resistance I from holy_shield — stacking check).

```
/tag @s add slf.skill.slide_step
```
Expected: Speed I.

---

## 11. TITLES

```
/function slf:admin/reset_player
/tag @s add slf.title.apex_veteran
```
Wait 1 second. Expected: Resistance I passive applied from `titles/passives`.

```
/tag @s add slf.title.apex_crazy_fist
```
Expected: Strength I passive.
