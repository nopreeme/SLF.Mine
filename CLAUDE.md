# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minecraft 1.21.x data pack + resource pack themed around the anime *Shangri-La Frontier*. Implements a full RPG layer: classes, skill learning via motion-trace, stat allocation, leveling, and a karma/mask system — all in vanilla `.mcfunction`.

**Target MC version:** 1.21.4+ (data pack format 61, resource pack format 46, supported through 1.21.8+). See README for older version formats.

## Minecraft Datapack/Resourcepack Conventions

- When modifying item models, preserve existing `texture_size`, `display` settings, and texture references unless explicitly asked to change them.
- Only modify the specific file/version mentioned (e.g., if the user says "fix v1", do **not** touch v2).
- For hotbar icons vs 3D models: use `display_context` switching rather than replacing the working 3D model.
- GUI model files use pixel art PNGs, not 3D texture atlases.

## Verification Before Changes

- When the user reports a bug, diagnose by reading the actual file before assuming a fix; do not guess at values (e.g., display coordinates).
- Do not assume sync/cache issues are the cause — the user manages their own file sync.
- Before claiming a fix works, verify the specific symptom the user reported is gone.

## Working Style

### Scope Discipline

- Make the minimum change needed; do not refactor or "improve" adjacent code unless asked.
- If a working file is involved tangentially, leave it alone.
- Confirm chart/spec details by quoting the source before acting on them.

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

- **Load:** `data/minecraft/tags/function/load.json` → `slf:setup` — registers all scoreboard objectives on world load.
- **Tick:** `data/minecraft/tags/function/tick.json` → `slf:skills/tick` — runs every game tick (20/s).

> **Path note:** Both function *tags* and function *files* use the **singular** `function/` directory (`data/minecraft/tags/function/`, `data/slf/function/`). The plural `functions/` breaks all loading silently.

### 20-Tick Cycle

`slf:skills/tick` dispatches most logic. At the bottom it runs a `#timer` counter; every 20 ticks (1 second) it calls:

| Function | Purpose |
|---|---|
| `slf:skills/sp_tick` | Motion-trace delta accumulation + skill learn threshold check |
| `slf:skills/exp_tick` | EXP → level-up processing |
| `slf:skills/passives` | Refresh passive potion effects (3-tick duration so they expire if lost) |
| `slf:mask/karma_tick` | Karma decay + bounty hunter spawn |
| `slf:stats/apply` | Translate stat scores into potion effects |
| `slf:stats/lck_check` | LCK save proc check (per player with LCK ≥ 1) |
| `slf:class/select_expire` | Expire timed class selection GUIs |

### Scoreboard Namespace

All objectives use the `slf.*` prefix. Key objectives:

| Objective | Type | Purpose |
|---|---|---|
| `slf.class` | dummy | Numeric class ID |
| `slf.choose_class` | trigger | Clickable class/alignment selection |
| `slf.focus_choose` | trigger | Clickable skill focus selection |
| `slf.stat_str/dex/vit/agi/tec/lck/stm` | trigger | Stat-spend click triggers (from `slf:stats/menu`) |
| `slf.focus` | dummy | Currently focused skill ID (0 = none) |
| `slf.focus_stat` | dummy | Which raw stat drives SP (1=dmg, 2=move, 3=evade, 4=def) |
| `slf.sp` | dummy | Accumulated skill progress points |
| `slf.threshold` | dummy | SP needed to learn the focused skill |
| `slf.stat.str/dex/vit/agi/tec/lck/stm` | dummy | Spent stat point scores (dot-separated, 7 stats) |
| `slf.level` / `slf.exp` | dummy | Progression |
| `slf.sp_points` | dummy | Unspent stat points from leveling |
| `slf.boss_kills` | dummy | Generic boss kill counter |
| `slf.karma` | dummy | Mask/PvP karma (0–200, decays over time) |
| `slf.karma_timer` | dummy | Tracks seconds since last karma event |
| `slf.bt_kills` | dummy | Bounty target kill count |
| `slf.vorpal_soul` | dummy | Vorpal kill count |
| `slf.knight_quest` | dummy | Knight quest active flag (1 = active) |
| `slf.knight_trials` | dummy | Knight trial completion count (0–3) |
| `slf.raw.dmg/move/evade/def` | stat criterion | Vanilla tracking objectives used as motion-trace inputs |
| `slf.dmg_prev/move_prev/evade_prev/def_prev` | dummy | Previous-tick snapshots for delta math |
| `slf.dmg_delta/move_delta/evade_delta/def_delta` | dummy | Per-tick raw delta values |
| `slf.ign.prev` | dummy | Previous-tick snapshot for Ignition detection (separate from def_prev) |
| `slf.standby` | dummy | 1 = player is at level 99 cap, buffering EXP |
| `slf.exp_extend` | dummy | EXP accumulated past the level 99 cap |
| `slf.boss_gate` | dummy | Boss defeat flag required to unlock Awakening |
| `slf.awakened` | dummy | 1 = level ceiling raised to 150 |
| `slf.mob_level` | dummy | Level set on mob entities at spawn |
| `slf.lck_save_cd` | dummy | LCK save proc cooldown counter |
| `slf.hp` | dummy | Player HP tracking |
| `slf.timer` | dummy | 20-tick cycle counter |
| `slf.tmp` | dummy | Scratch/temp variable |

### Tag Conventions

- `slf.class_chosen` — set after any class grant; gates stat-spend and focus triggers.
- `slf.was_<class>` — permanent lineage tags (e.g. `slf.was_swordsman`, `slf.was_knight`). Used as prerequisites for advanced classes.
- `slf.skill.<name>` — player has learned the skill (e.g. `slf.skill.power_slash`).
- `slf.alignment_offered` — prevents the Holy/Dark Knight choice from appearing twice.
- `slf.tantrum_active` — runtime tag for Big/Grand Tantrum activation.

### Class System

Classes have numeric IDs stored in `slf.class`. Tiers:
- **T1 (starting classes):** Swordsman (1), Warrior (2), Bandit (3), Priest (4), Monk (5), Mage (6), Fighter (20), Mercenary (30)
- **T2 — Blade:** Sword Master (10, from Swordsman), Magic Swordsman (11, from Swordsman)
- **T2 — Brawler:** Barbarian (14, from Warrior or Fighter), Destroyer (21, from Fighter)
- **T2 — Support/Magic:** Bishop (18, from Priest), Monk Soldier (60, from Monk), Sage (70, from Mage)
- **T2 — Shadow:** Thief (50, from Bandit), Ninja (51, from Bandit)
- **T2 — Merc:** Veteran (31, from Mercenary)
- **T3 — Blade:** Kansei (12, from Sword Master), Mysterious Sword (13, from Magic Swordsman), War King (15, from Barbarian), Crazy Fist (22, from Destroyer)
- **T3 — Support/Magic:** Saint (19, from Bishop), Spirit Fist (61, from Monk Soldier), Omnipotent Wisdom (62, from Sage)
- **T3 — Shadow:** Assassin (16, from Thief), Shinobi (52, from Ninja)
- **T3 — Knight tree (40–44):** Knight (40), Holy Knight (41), Dark Knight (42), King's Knight (43), Black Death (44)
- **T4 — Shadow:** Killing Joke (17, from Assassin), Star Shinobi Sei (53, from Shinobi)

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
| DEX 5/10/20 | Attack Speed +0.4/+0.8/+1.2 (attribute modifier `slf:dex_speed`) |
| LCK 10/20/40/60 | Luck attribute 1/2/3/4 |

TEC has no current effect mapping (reserved).

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
- `tests/test_datapack.py` — static analysis test suite (33 tests). Run with `python3 -m unittest tests/test_datapack.py`. Catches ID collisions, broken prerequisite chains, missing dispatch entries, and menu syntax regressions without a live server.
- `give/armor_leather_full.mcfunction` — shared helper that gives all four leather armor pieces. Called by T1 classes that grant a full leather starter set.

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
