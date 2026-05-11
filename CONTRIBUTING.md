# Contributing to SLF.Mine

Thank you for helping bring the world of Shangri-La Frontier into Minecraft. This guide covers everything you need to add skills, classes, items, or textures without breaking the existing system.

---

## What We Need Most

| Priority | Contribution | Where |
|---|---|---|
| 🔥 High | 16×16 pixel art textures | `resource_pack/assets/slf/textures/item/` |
| 🔥 High | Quest advancement JSON for class transitions | `data_pack/data/slf/advancement/` |
| ⬆ Medium | New skills (focus + learn + passive) | `data_pack/data/slf/function/skills/` |
| ⬆ Medium | New class nodes (grant + tick dispatch) | `data_pack/data/slf/function/class/grant/` |
| ➡ Normal | New SLF items (model + give function) | `resource_pack/` + `data_pack/` |
| ➡ Normal | Balance feedback (threshold values, exp curve) | GitHub Issues |
| ➡ Normal | Bug reports | GitHub Issues |

---

## Setup

```bash
git clone https://github.com/nopreeme/SLF.Mine.git
cd SLF.Mine
```

1. Copy `data_pack/` into a test world's `datapacks/` folder
2. Copy `resource_pack/` into `.minecraft/resourcepacks/` and enable it
3. Launch the world, run `/reload`
4. Run `/function slf:class/select` to choose a class and start testing

No external tools required — plain JSON and `.mcfunction` files only.

---

## File Structure

```
SLF.Mine/
├── data_pack/
│   └── data/
│       ├── minecraft/tags/function/
│       │   ├── load.json          ← runs slf:setup on world load
│       │   └── tick.json          ← runs slf:skills/tick every game tick
│       └── slf/
│           ├── advancement/       ← quest advancement trees (mostly TODO)
│           ├── function/
│           │   ├── setup.mcfunction          ← creates all scoreboards
│           │   ├── admin/grant.mcfunction    ← OP shortcut to give items
│           │   ├── give/                     ← one file per giveable item
│           │   ├── class/
│           │   │   ├── select.mcfunction     ← starting class menu
│           │   │   ├── alignment_choice.mcfunction
│           │   │   ├── knight_trial_complete.mcfunction
│           │   │   └── grant/               ← one file per class node
│           │   ├── skills/
│           │   │   ├── tick.mcfunction       ← master dispatcher (runs every tick)
│           │   │   ├── sp_tick.mcfunction    ← delta math + SP accumulation
│           │   │   ├── exp_tick.mcfunction   ← EXP + level-up logic
│           │   │   ├── passives.mcfunction   ← passive effects every 20t
│           │   │   ├── menu.mcfunction       ← player-facing skill focus menu
│           │   │   ├── learn_focused.mcfunction ← dispatch ID → learn/
│           │   │   ├── ignition_check.mcfunction
│           │   │   ├── slash_ignition_check.mcfunction
│           │   │   ├── managarm_check.mcfunction
│           │   │   ├── bradion_tick.mcfunction
│           │   │   ├── focus/               ← one file per learnable skill
│           │   │   └── learn/               ← one file per learnable skill
│           │   ├── stats/
│           │   │   ├── menu.mcfunction
│           │   │   ├── level_up.mcfunction
│           │   │   ├── altar.mcfunction
│           │   │   ├── apply.mcfunction
│           │   │   └── spend_*.mcfunction   ← one per stat
│           │   ├── mask/
│           │   │   ├── karma_tick.mcfunction
│           │   │   ├── spawn_bounty_hunter.mcfunction
│           │   │   └── vorpal_kill_check.mcfunction
│           │   └── titles/
│           │       └── passives.mcfunction
│           ├── loot_table/        ← boss drop tables
│           ├── predicate/
│           │   └── ideal_motion.json  ← airborne + sprinting check
│           └── recipe/            ← skill fusion recipes
└── resource_pack/
    └── assets/slf/
        ├── textures/item/         ← PNG textures (replace placeholders here)
        ├── models/item/           ← item model JSON
        └── items/                 ← item_model definitions (1.21.4+)
```

---

## Naming Conventions

### Scoreboard objectives

```
slf.<name>           — top-level (slf.class, slf.level, slf.exp …)
slf.<group>.<name>   — grouped  (slf.stat.str, slf.raw.dmg …)
```

Never use vanilla objective names or non-`slf` prefixes.

### Entity tags on players

| Pattern | Purpose | Example |
|---|---|---|
| `slf.skill.<name>` | Learned skill | `slf.skill.lash_slash` |
| `slf.was_<class>` | Class history (permanent) | `slf.was_swordsman` |
| `slf.title.<name>` | Earned title | `slf.title.tombguard_destroyer` |
| `slf.avail.<name>` | T3 skill unlocked by class | `slf.avail.skywalker` |
| `slf.class_chosen` | Player has selected a class | — |
| `slf.tantrum_active` | Big Tantrum currently active | — |

### Function paths

```
slf:<dir>/<name>     — matches folder structure under function/
```

### Focus IDs

| Range | Tier |
|---|---|
| 1 – 19 | T1 (universal) |
| 20 – 29 | T2 (class-accelerated) |
| 30 – 39 | T3 (class-gated) |

Leave gaps within each range so related skills can be grouped.

---

## How to Add a Skill

This example adds a hypothetical T2 skill **Iron Fist** (Fighter-aligned, DEF-type, focus ID 23).

### 1. Create the focus file

`data_pack/data/slf/function/skills/focus/iron_fist.mcfunction`

```mcfunction
# Guard: already learned or already focusing
execute if entity @s[tag=slf.skill.iron_fist] run return fail
execute if entity @s[scores={slf.focus=23}] run return fail

# Require prerequisite if this is a lineage evolution
# execute unless entity @s[tag=slf.skill.knuckle_rush] run return fail

scoreboard players set @s slf.focus 23
scoreboard players set @s slf.focus_stat 4      # 4 = DEF
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000    # T2 base
execute if entity @s[tag=slf.was_fighter] run scoreboard players set @s slf.threshold 300
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Iron Fist","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
```

**Focus stat values:** `1` = DMG, `2` = MOVE, `3` = EVADE, `4` = DEF

### 2. Create the learn file

`data_pack/data/slf/function/skills/learn/iron_fist.mcfunction`

```mcfunction
# If this is a lineage replacement, remove the predecessor:
# tag @s remove slf.skill.knuckle_rush

tag @s add slf.skill.iron_fist
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill learned: ","color":"green"},{"text":"Iron Fist","color":"gold"}]
```

### 3. Register in `learn_focused.mcfunction`

Add one line in `data_pack/data/slf/function/skills/learn_focused.mcfunction`:

```mcfunction
execute if score @s slf.focus matches 23 run function slf:skills/learn/iron_fist
```

### 4. Register in `skills/tick.mcfunction` (focus_choose dispatch)

Add one line in the focus_choose dispatch block:

```mcfunction
execute as @a[scores={slf.focus_choose=23}] run function slf:skills/focus/iron_fist
```

### 5. Add to the menu

Add a `{"text":"[Iron Fist]", ...}` entry in `data_pack/data/slf/function/skills/menu.mcfunction`, in the T2 row, with:

```json
"clickEvent": {"action": "run_command", "value": "/trigger slf.focus_choose set 23"},
"hoverEvent": {"action": "show_text", "value": "DEF • Requires Knuckle Rush • Fighter affinity"}
```

### 6. Add a passive effect (if the skill has one)

In `data_pack/data/slf/function/skills/passives.mcfunction`, add:

```mcfunction
# Iron Fist — Resistance I
effect give @a[tag=slf.skill.iron_fist] minecraft:resistance 3 0 true
```

---

## How to Add a Class

This example adds **Blade Dancer** (ID 14, evolves from Sword Master).

### 1. Assign a class ID

See the [Class ID Table](#class-id-table) below. Pick the next unused ID in the appropriate range.

### 2. Create the grant file

`data_pack/data/slf/function/class/grant/blade_dancer.mcfunction`

```mcfunction
# Prerequisite guard
execute unless entity @s[tag=slf.was_sword_master] run return fail

scoreboard players set @s slf.class 14
tag @s add slf.was_blade_dancer

# Grant T3 skill availability tags unlocked by this class
tag @s add slf.avail.phantom_step

tellraw @s {"text":"You have become a Blade Dancer.","color":"aqua","bold":true}
```

For **dead-end classes** (no further evolution), add:

```mcfunction
tag @s add slf.title.apex_blade_dancer
tellraw @s {"text":"You have reached the pinnacle of this path. No further evolution exists — your mastery is complete.","color":"gold"}
playsound minecraft:ui.toast.challenge_complete master @s
```

### 3. Wire the trigger (if class choosable from tick)

Class grants triggered by `slf.choose_class` need a dispatch line in `skills/tick.mcfunction`. If the class is granted by a quest advancement reward instead, point the reward function directly at the grant function — no tick change needed.

---

## How to Add an Item

### 1. Create the texture

Add `resource_pack/assets/slf/textures/item/<name>.png` — 16×16 pixels, RGBA PNG.

### 2. Create the model

`resource_pack/assets/slf/models/item/<name>.json`

```json
{
  "parent": "minecraft:item/handheld",
  "textures": {
    "layer0": "slf:item/<name>"
  }
}
```

### 3. Create the item_model definition (1.21.4+)

`resource_pack/assets/slf/items/<name>.json`

```json
{
  "model": {
    "type": "minecraft:model",
    "model": "slf:item/<name>"
  }
}
```

### 4. Create the give function

`data_pack/data/slf/function/give/<name>.mcfunction`

```mcfunction
give @s minecraft:iron_sword[item_model="slf:<name>",custom_name='{"text":"My Item","italic":false}',lore=["{\"text\":\"Flavour text\",\"italic\":true,\"color\":\"gray\"}"],attribute_modifiers=[{type:"minecraft:generic.attack_damage",amount:8.0,operation:"add_value",slot:"mainhand",id:"slf:my_item"}]]
```

### 5. Add a loot table entry (if it drops from a mob)

Create or edit `data_pack/data/slf/loot_table/<boss>_drops.json` and add an entry for the new item.

---

## Scoreboard Reference

| Objective | Type | Description |
|---|---|---|
| `slf.class` | dummy | Integer class ID of the player |
| `slf.choose_class` | trigger | Player trigger for class/alignment selection |
| `slf.focus_choose` | trigger | Player trigger for skill focus selection |
| `slf.level` | dummy | Custom level (1–150) |
| `slf.exp` | dummy | Current EXP toward next level |
| `slf.sp_points` | dummy | Unspent stat points |
| `slf.boss_kills` | dummy | Boss kill counter (also used for first-10 title tracking) |
| `slf.stat.str` | dummy | Strength stat |
| `slf.stat.dex` | dummy | Dexterity stat |
| `slf.stat.vit` | dummy | Vitality stat |
| `slf.stat.agi` | dummy | Agility stat |
| `slf.stat.int` | dummy | Intelligence stat |
| `slf.stat.tec` | dummy | Technique stat |
| `slf.stat.lck` | dummy | Luck stat |
| `slf.stat.stm` | dummy | Stamina stat |
| `slf.stat_str` | trigger | Player spend trigger for STR |
| `slf.stat_dex` | trigger | Player spend trigger for DEX |
| `slf.stat_vit` | trigger | Player spend trigger for VIT |
| `slf.stat_agi` | trigger | Player spend trigger for AGI |
| `slf.stat_int` | trigger | Player spend trigger for INT |
| `slf.stat_tec` | trigger | Player spend trigger for TEC |
| `slf.stat_lck` | trigger | Player spend trigger for LCK |
| `slf.stat_stm` | trigger | Player spend trigger for STM |
| `slf.raw.dmg` | criterion | Vanilla: `damage_dealt` (read-only, auto-tracked) |
| `slf.raw.move` | criterion | Vanilla: `sprint_one_cm` (read-only) |
| `slf.raw.evade` | criterion | Vanilla: `jump` (read-only) |
| `slf.raw.def` | criterion | Vanilla: `damage_taken` (read-only) |
| `slf.dmg_prev` | dummy | Snapshot of `slf.raw.dmg` from previous 20t cycle |
| `slf.dmg_delta` | dummy | `raw.dmg - dmg_prev` this cycle |
| `slf.move_prev` | dummy | Snapshot of `slf.raw.move` |
| `slf.move_delta` | dummy | `raw.move - move_prev` this cycle |
| `slf.evade_prev` | dummy | Snapshot of `slf.raw.evade` |
| `slf.evade_delta` | dummy | `raw.evade - evade_prev` this cycle |
| `slf.def_prev` | dummy | Snapshot of `slf.raw.def` |
| `slf.def_delta` | dummy | `raw.def - def_prev` this cycle |
| `slf.focus` | dummy | Active focus skill ID (0 = none) |
| `slf.focus_stat` | dummy | Stat category of focused skill (1–4) |
| `slf.sp` | dummy | Accumulated skill progress toward threshold |
| `slf.threshold` | dummy | SP required to learn the focused skill |
| `slf.exp_extend` | dummy | EXP banked after reaching level 99 (Standby) |
| `slf.standby` | dummy | 1 = at level 99, awaiting Awakening |
| `slf.boss_gate` | dummy | 1 = awakening boss defeated; altar can convert exp_extend |
| `slf.awakened` | dummy | 1 = Altar used; levels 100–150 accessible |
| `slf.vorpal_soul` | dummy | Hidden: rises killing high-level mobs, falls on death |
| `slf.karma` | dummy | Hidden: rises killing passives, triggers bounty hunter at 100 |
| `slf.karma_timer` | dummy | Secondary tick counter for karma decay (cycles at 60×20t) |
| `slf.bt_kills` | dummy | Kills made while `slf.tantrum_active` tag is set |
| `slf.knight_quest` | dummy | Knight questline step |
| `slf.knight_trials` | dummy | Knight trials completed (alignment unlocks at 3) |
| `slf.mob_level` | dummy | Level of a mob entity (set at spawn) |
| `slf.ign.prev` | dummy | Ignition-specific prev snapshot (separate from `slf.def_prev`) |
| `slf.hp` | dummy | Temp: player Health read via `data get` |
| `slf.tmp` | dummy | Temp scratch for scoreboard math |
| `slf.timer` | dummy | Tick counter for 20t cycle gate |

---

## Class ID Table

| ID | Class | ID | Class |
|---|---|---|---|
| 1 | Swordsman | 20 | Fighter |
| 2 | Warrior | 21 | Destroyer |
| 3 | Thief | 22 | Crazy Fist |
| 4 | Priest | 30 | Mercenary |
| 5 | Monk | 31 | Veteran |
| 6 | Mage | 40 | Knight |
| 10 | Sword Master | 41 | Holy Knight |
| 11 | Magic Swordsman | 42 | Dark Knight |
| 12 | Kansei | 43 | King's Knight |
| 13 | Mysterious Sword | 44 | Black Death |
| 14 | Barbarian | 50 | Bandit |
| 15 | War King | 51 | Ninja |
| 16 | Assassin | 52 | Shinobi |
| 17 | Killing Joke | 53 | Star Shinobi Sei |
| 18 | Bishop | 60 | Monk Soldier |
| 19 | Saint | 61 | Spirit Fist |
| 70 | Sage | 71 | Omnipotent Wisdom |

---

## PR Checklist

Before opening a pull request:

- [ ] `/reload` completes without errors in the log
- [ ] `/function slf:class/select` shows the class menu and class selection works
- [ ] If you added a skill: focus → accumulate SP → skill learned, passive applies
- [ ] If you added a class: grant fires, class ID is correct, was_* tag is set
- [ ] If you added an item: give function works, item renders with correct model
- [ ] No new objectives or tags outside the `slf.*` namespace
- [ ] No hardcoded player names — use `@s` / `@a` / fake-player names like `#counter`
- [ ] Function files use Unix line endings (LF) and UTF-8 encoding
- [ ] PR description explains what the change does and how to test it
