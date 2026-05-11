# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minecraft 1.21.x data pack + resource pack themed around the anime *Shangri-La Frontier*. Implements a full RPG layer: classes, skill learning via motion-trace, stat allocation, leveling, and a karma/mask system — all in vanilla `.mcfunction`.

**Target MC version:** 1.21.4 (data pack format 61, resource pack format 46). See README for older version formats.

## Development Workflow

There is no build step. Edit files directly, then reload in-game:

```
/reload
```

To test a specific function manually (must be OP):
```
/function slf:<path>
```

Install:
- `data_pack/` → `<world>/datapacks/`
- `resource_pack/` → `.minecraft/resourcepacks/`

## Architecture

### Entry Points

- **Load:** `data/minecraft/tags/functions/load.json` → `slf:setup` — registers all scoreboard objectives on world load.
- **Tick:** `data/minecraft/tags/functions/tick.json` → `slf:skills/tick` — runs every game tick (20/s).

> **1.21.8 path note:** Function *tags* use plural `data/minecraft/tags/functions/`, but function *files* use singular `data/<namespace>/function/`. Renaming function files to `functions/` breaks all function loading silently.

### 20-Tick Cycle

`slf:skills/tick` dispatches most logic. At the bottom it runs a `#timer` counter; every 20 ticks (1 second) it calls:

| Function | Purpose |
|---|---|
| `slf:skills/sp_tick` | Motion-trace delta accumulation + skill learn threshold check |
| `slf:skills/exp_tick` | EXP → level-up processing |
| `slf:skills/passives` | Refresh passive potion effects (3-tick duration so they expire if lost) |
| `slf:mask/karma_tick` | Karma decay + bounty hunter spawn |
| `slf:stats/apply` | Translate stat scores into potion effects |

### Scoreboard Namespace

All objectives use the `slf.*` prefix. Key objectives:

| Objective | Type | Purpose |
|---|---|---|
| `slf.class` | dummy | Numeric class ID |
| `slf.choose_class` | trigger | Clickable class/alignment selection |
| `slf.focus_choose` | trigger | Clickable skill focus selection |
| `slf.focus` | dummy | Currently focused skill ID (0 = none) |
| `slf.focus_stat` | dummy | Which raw stat drives SP (1=dmg, 2=move, 3=evade, 4=def) |
| `slf.sp` | dummy | Accumulated skill progress points |
| `slf.threshold` | dummy | SP needed to learn the focused skill |
| `slf.stat.str/dex/vit/agi/int/tec/lck/stm` | dummy | Spent stat points |
| `slf.level` / `slf.exp` | dummy | Progression |
| `slf.sp_points` | dummy | Unspent stat points from leveling |
| `slf.karma` | dummy | Mask/PvP karma (0–200, decays over time) |
| `slf.knight_trials` | dummy | Knight quest progress (0–3) |
| `slf.timer` | dummy | 20-tick cycle counter |
| `slf.tmp` | dummy | Scratch/temp variable |
| `slf.dmg_prev` / `slf.move_prev` / `slf.evade_prev` / `slf.def_prev` | dummy | Motion-trace snapshots (previous-tick raw stat values for delta math) |
| `slf.standby` | dummy | 1 = player is at level 99 cap, buffering EXP |
| `slf.exp_extend` | dummy | EXP accumulated past the level 99 cap |
| `slf.boss_gate` | dummy | Boss defeat flag required to unlock Awakening |
| `slf.awakened` | dummy | 1 = level ceiling raised to 150 |
| `slf.vorpal_soul` | dummy | Vorpal kill count |
| `slf.karma_timer` | dummy | Tracks seconds since last karma event |
| `slf.bt_kills` | dummy | Bounty target kill count |

### Tag Conventions

- `slf.class_chosen` — set after any class grant; gates stat-spend and focus triggers.
- `slf.was_<class>` — permanent lineage tags (e.g. `slf.was_swordsman`, `slf.was_knight`). Used as prerequisites for advanced classes.
- `slf.skill.<name>` — player has learned the skill (e.g. `slf.skill.power_slash`).
- `slf.alignment_offered` — prevents the Holy/Dark Knight choice from appearing twice.
- `slf.tantrum_active` — runtime tag for Big/Grand Tantrum activation.

### Class System

Classes have numeric IDs stored in `slf.class`. Tiers:
- **T1 (1–6):** Swordsman, Warrior, Thief, Priest, Monk, Mage
- **T2 (10–19):** Sword Master, Magic Swordsman, Barbarian, Destroyer, Veteran, Bandit, Ninja, Bishop, Monk Soldier, Sage
- **T2 alt (20–39):** Fighter, Mercenary and their trees
- **T3 (40+):** Knight (40), Holy Knight (41), Dark Knight (42), King's Knight (43), Black Death (44), and rarer classes

Grant functions guard prerequisites differently by tier:
- **T1:** `if entity @s[tag=slf.class_chosen] run return fail` — prevents re-classing once any class is chosen
- **T2+:** `unless entity @s[tag=slf.was_*] run return fail` — enforces lineage prerequisite

Admin class grants: `execute as <player> run function slf:class/grant/<name>`

**Class selection GUI:** `class/select.mcfunction` renders a clickable tellraw menu grouped by art type (Blade, Brawler, Shadow, Support, Magic). `class/select_fill.mcfunction` populates a chest GUI with custom-model-data items for each class. `select_cleanup.mcfunction` and `select_expire.mcfunction` handle post-selection teardown.

**Knight trials → alignment flow:**
1. Granting Knight sets `slf.knight_quest=1`
2. Completing each trial increments `slf.knight_trials` (max 3)
3. When `slf.knight_trials=3`, the next tick calls `class/alignment_choice`
4. `alignment_choice` enables the `slf.choose_class` trigger; `slf.alignment_offered` prevents repeat offers
5. Player chooses Holy Knight (41) or Dark Knight (42); further T3 evolutions branch from there

### Skill Learning Flow

1. Player runs `/function slf:class/select` → clickable menu → `/trigger slf.choose_class set <N>` → `slf:skills/tick` dispatches to the appropriate `class/grant/` function.
2. Player runs `/function slf:skills/menu` → clickable skill focus menu → `/trigger slf.focus_choose set <N>` → `slf:skills/tick` dispatches to `skills/focus/<name>`.
3. `focus/<name>.mcfunction` sets `slf.focus` (ID), `slf.focus_stat` (1–4), and `slf.threshold`. Class lineage tags reduce the threshold (e.g. swordsman pays 100 SP for Power Slash vs the default 500).
4. `sp_tick` computes per-second deltas from vanilla stat objectives (`damage_dealt`, `sprint_one_cm`, `jump`, `damage_taken`) and adds to `slf.sp`. Delta = current − prev snapshot; negative deltas are discarded via `scores={*_delta=1..}`. Snapshots update every 20t regardless of current focus. The `slf:ideal_motion` predicate triggers when the player is sprinting while airborne; `sp_tick` adds the delta two extra times (3× total).
5. When `slf.sp >= slf.threshold`, `sp_tick` calls `learn_focused` → dispatches to `skills/learn/<name>`, which adds the `slf.skill.*` tag and resets focus/sp.
6. Passive effects for learned skills are applied every 20t in `skills/passives.mcfunction`.

### Stat → Effect Mapping (`stats/apply`)

| Stat | Effect |
|---|---|
| AGI 5/10/20 | Speed I/II/III |
| STM 5+ | Saturation I |
| STM 10+ | Haste I |
| VIT 5/10/20/30 | Absorption I/II/III/IV |
| STR 10/20 | Strength I/II |

INT, DEX, TEC, LCK have no current effect mapping (reserved).

### Level 99 Standby / Awakening

At level 99, `slf.standby` is set to 1 — EXP no longer triggers level-ups and overflows into `slf.exp_extend` instead. To break the cap:
1. Defeat the designated boss (`slf.boss_gate` = 1)
2. Visit the Altar of Awakening → `slf.awakened` is set to 1

Once awakened, normal EXP tick behavior resumes with a ceiling of 150.

### Titles System

`data/slf/function/titles/` is a subsystem parallel to skills. `titles/passives.mcfunction` is called at the end of `skills/passives.mcfunction` every 20t and applies passive effects tied to title tags (pattern mirrors `slf.skill.*` tags).

### Mask / Karma System

`slf.karma` rises via PvP kills and vorpal-bunny mechanics (`mask/vorpal_kill_check.mcfunction`). `karma_tick` decays it by 1 every 60 cycles (60 seconds). At 100+ karma a bounty hunter mob is spawned. Hard cap: 200.

### Resource Pack

Item models live in `resource_pack/assets/slf/models/item/`. Each model file references a texture at `slf:item/<name>`. The base Minecraft item models in `assets/minecraft/items/` use `custom_model_data` predicates to select the SLF variants.

Textures go in `resource_pack/assets/slf/textures/item/` as 16×16 PNGs, named to match the model file (e.g. `power_slash.png`).

### Tooling

- `build.sh` — zips `data_pack/` and `resource_pack/` into versioned `.zip` releases for distribution.
- `discord_bot/` — Discord.js bot (`index.js`, `notify.js`, `deploy-commands.js`) that posts commit/branch update embeds. Not required for gameplay development.

### Adding a New Skill

1. Add a `skills/focus/<name>.mcfunction` — set `slf.focus` to a new unique ID, `slf.focus_stat`, `slf.threshold`, and print a tellraw.
2. Add a `skills/learn/<name>.mcfunction` — add the `slf.skill.<name>` tag, reset focus/sp, print learned message.
3. Wire both into the dispatch tables in `skills/tick` (focus_choose trigger) and `skills/learn_focused`.
4. If it has a passive effect, add it to `skills/passives.mcfunction`.
5. If it's class-locked, add `execute unless entity @s[tag=slf.was_<class>] run return fail` at the top of the focus file.

### Adding a New Class

1. Create `class/grant/<name>.mcfunction` — enforce prerequisites with `unless entity @s[tag=slf.was_*] run return fail`, set `slf.class`, add `slf.was_<name>` and any starting skill tags.
2. Add a trigger line in `skills/tick` under `# --- Class selection ---`.
3. Add a clickable entry to `class/select.mcfunction`.
4. Document the class ID in this file.
