# SLF.Mine — Shangri-La Frontier Pack

![Minecraft](https://img.shields.io/badge/Minecraft-1.21.x-brightgreen) ![Pack Format](https://img.shields.io/badge/data_pack-format_61-blue) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

A Minecraft 1.21.x data pack + resource pack bringing the world of **Shangri-La Frontier** into survival. Includes anime-faithful weapons, armor, and a full RPG system: 8 starting classes, a tiered skill-focus engine, 8 spendable stats, custom leveling, and hidden mask data that shapes the world around you.

> Both packs must be active together for full functionality.

---

## Installation

### Resource Pack
1. Copy the `resource_pack/` folder into `.minecraft/resourcepacks/` (zip or folder, both work)
2. Enable it in **Options → Resource Packs**

### Data Pack
1. Open your world's save folder
2. Copy the `data_pack/` folder into `<world>/datapacks/`
3. Run `/reload` in-game

---

## Getting Started

```
Join world
  └─ Chat shows class selection UI  (/function slf:class/select to reopen)
       └─ Choose a class → you receive your class tag and T1 skills
            └─ Open skill menu → /function slf:skills/menu
                 └─ Click a skill to focus it → earn SP by playing
                      └─ Skill learned when SP ≥ threshold
                           └─ Spend stat points → /function slf:stats/menu
```

Kill mobs to earn EXP and level up. Each level grants **5 stat points** (bonus at milestones). Reaching level 99 enters **Standby** — defeat a worthy boss and visit the **Altar of Awakening** to unlock levels 100–150.

---

## Class System

Choose one of **8 starting classes** on your first join. Your class determines which skills you learn fastest and which evolution paths you can unlock.

| Class | Playstyle | Primary stat |
|---|---|---|
| Swordsman | Blade techniques, fast combos | DMG |
| Warrior | Raw power, wide swings | DMG |
| Fighter | Bare-fist brawler | DMG |
| Mercenary | All-weapon freelancer, combat ignition | DMG / DEF |
| Bandit | Speed and evasion | EVADE / MOVE |
| Priest | Shield arts, stamina | DEF |
| Monk | Body as weapon, iron defense | DMG / DEF |
| Mage | Magic arts, chanting | DEF / DMG |

### Evolution Tree (overview)

```
Swordsman      Warrior        Fighter    Mercenary   Thief       Priest    Monk        Mage
  ↓      ↓      ↓      ↓        ↓            ↓       ↓    ↓      ↓          ↓           ↓
Sword  Magic   │    Barbarian──┘          Destroyer  Vet  Ban   Ninja    Bishop   Monk    Sage
Master Sword   │      ↓                      ↓            ↓      ↓         ↓      Soldier   ↓
  ↓      ↓   War King                   Crazy Fist  Assassin Shinobi    Saint  Spirit  Omnipotent
Kansei  Myst   │                                       ↓       ↓                Fist    Wisdom
        Sword  │                                   Kill   Star Shin
               └──Knight (NPC quest — Swordsman OR Warrior path)
                    ↓            ↓
               Holy Knight   Dark Knight
                    ↓              ↓
               King's Knight   Black Death
```

Class evolution is gated by **quest chains and NPC interactions**, not time. History tags (`slf.was_swordsman`, etc.) accumulate permanently — you never lose access to a path you've walked.

See [CONTRIBUTING.md](CONTRIBUTING.md#class-id-table) for the full class ID table.

---

## Skill Focus System

Skills are **earned through play**, not handed out on class grant. Every skill has a **focus stat** (DMG / MOVE / EVADE / DEF) and a **threshold** of skill-progress (SP) you must accumulate.

### How it works

1. Open the skill menu: `/function slf:skills/menu`
2. Click a skill — you are now *focusing* it
3. Play normally: attack, sprint, jump, take damage
4. Every second (20 ticks), the pack reads how much of that action you did and adds SP
5. When your SP reaches the threshold, the skill is learned automatically

### Focus stat categories

| `focus_stat` | Driven by | Example skills |
|---|---|---|
| DMG (1) | Damage dealt | Power Slash, Megaton Swing, Lash Slash |
| MOVE (2) | Sprint distance | Formula Drift, Skatefoot |
| EVADE (3) | Jumps | Slide Step, Rechette Step, Skywalker |
| DEF (4) | Damage taken | Iron Skin, Holy Shield, Flash Counter |

### Ideal Motion bonus

While **airborne and sprinting**, your SP accumulation is **3× normal** for that cycle. Aggressive, mobile combat is rewarded across all skill types.

### Skill tiers

| Tier | Who can learn | Class role |
|---|---|---|
| T1 | Anyone | Aligned class gets ~5× lower threshold |
| T2 | Anyone, but slow | Aligned class gets ~10× lower threshold |
| T3 | Only after class evolution | Evolution unlocks the skill in your menu |
| T4 | Achievement-gated | Class irrelevant; gates are level, kills, Vorpal Soul |
| T5 | Synthesis | Combine two owned skill tags at the synthesis station |

### Skill lineages

Within a lineage, learning a higher skill **replaces** its predecessor:

```
Slash:   Power Slash → Lash Slash → Inexhaustible Beasts
Heavy:   Megaton Swing → Gigaton Swing → Terraton Corapsa
Knuckle: Knuckle Rush → Strong Puncher
Ignition: Ignition → Slash Ignition
AirStep: Slide Step → Formula Drift → Skatefoot → Skywalker
```

Skills from **different lineages stack permanently** and are never removed.

---

## Stats & Leveling

Earn EXP from mob kills. Level-ups grant **stat points** to spend via `/function slf:stats/menu`.

### 8 spendable stats

| Stat | Effect |
|---|---|
| STR | Strength effect — melee damage |
| DEX | Dexterity — attack speed and crit (future) |
| VIT | Vitality — increases max HP (via Absorption) |
| AGI | Agility — movement Speed effect |
| INT | Intelligence — magic power multiplier (future mana) |
| TEC | Technique — reduces skill focus thresholds |
| LCK | Luck — drop rates and crit chance (future) |
| STM | Stamina — Haste + Saturation |

Stats are applied automatically every second via Minecraft status effects.

### Level curve

| Level range | EXP to next level |
|---|---|
| 1 → 2 | 100 |
| 2 → 3 | 200 |
| 3 → 4 | 350 |
| 4 → 5 | 550 |
| 5 → 6 | 850 |
| 6 → 7 | 1,300 |
| 7 → 8 | 2,000 |
| 8 → 9 | 3,000 |
| 9 → 10 | 4,500 |
| 10 – 98 | 5,000 per level |
| 99 | **Standby gate** |

Every 10 levels grants **2 bonus stat points** on top of the standard 5 per level.

### Standby & Awakening

At level 99 you enter **Standby** — EXP no longer advances your level but is banked. Defeat a qualifying high-tier boss (sets `slf.boss_gate = 1`), then run `/function slf:stats/altar` at the **Altar of Awakening** structure to convert banked EXP into levels 100–150.

---

## Mask Data

Two hidden scoreboards shape the world without being shown in any UI.

### Vorpal Soul

- **Rises** when you kill a mob whose level is 20+ above yours
- **Falls** (−5) on your death
- **Gates** T4 Heroic skills at `vorpal_soul ≥ 50`

### Karma

- **Rises** (+2) when you kill passive mobs or NPCs
- **Decays** (−1 every 60 seconds) naturally
- At `karma ≥ 100` a **Bounty Hunter** spawns near you
- Caps at 200 — bounty hunters keep coming

---

## Boss Drop Skills

Some skills are earned from boss encounters rather than the focus system. Any class can obtain these.

| Boss | Drop |
|---|---|
| Wezaemon | Seitan skill book — *Clear Sky* (fast aerial slash) |
| Siegwurm | *Critical Speed - Bradion* (sprint-based Haste buildup) |
| Ctarnidd | *Reflexus* (briefly copy last enemy attack pattern) |
| Lycagon | Title: **** (first 10 players) + materials |
| Vorpal Bunny *(rare enemy)* | *Acrobat* (Resistance I while airborne) |

---

## Items

| Display Name | Base Item | Category |
|---|---|---|
| Wethermon Bone Scythe | Netherite Sword | Boss Weapon |
| Wethermon Rib Dagger | Iron Sword | Boss Weapon |
| Bilac Crescent Blade | Netherite Sword | Boss Weapon |
| Bilac Fang Gauntlet | Golden Sword | Boss Weapon |
| Oriana Scepter | Diamond Sword | Boss Weapon |
| Oriana Void Staff | Diamond Sword | Boss Weapon |
| Night Claw Talon | Netherite Sword | Boss Weapon |
| Sunraku's Right Blade | Iron Sword | Player Weapon |
| Sunraku's Left Blade | Iron Sword | Player Weapon |
| Chaos Rod | Golden Sword | Player Weapon |
| Tombguard Helmet | Netherite Helmet | Armor |
| Tombguard Chestplate | Netherite Chestplate | Armor |
| Tombguard Leggings | Netherite Leggings | Armor |
| Tombguard Boots | Netherite Boots | Armor |
| Full Moon Chestguard | Diamond Chestplate | Armor |
| Skill: Slash | Enchanted Book | Skill Book |
| Skill: Thrust | Enchanted Book | Skill Book |
| Skill: Blade Rush \[FUSED\] | Enchanted Book | Fused Skill |
| Skill: Moon Howl \[FUSED\] | Enchanted Book | Fused Skill |
| Skill: Void Lance \[FUSED\] | Enchanted Book | Fused Skill |
| Unique Monster Core | Book | Material |

---

## Skill Fusion

Combine skills at the **Skill Garden** using a **<item>** as the fusion catalyst:

| Fused Skill | Pattern | Reagent |
|---|---|---|


---

## Advancements

Open the Advancements screen (`L`) and look for the **Shangri-La Frontier** tab.

```
Shangri-La Frontier (root)
├── Rookie Gear — craft Sunraku's right blade
│   └── Dual Fangs — hold both Sunraku blades
├── The Tombguard Awaits — obtain any Tombguard armor piece
│   └── Gravedigger — obtain the Wethermon Katana
│       └── Bone Knight — wear the full Tombguard set
├── Moonlit Challenge — obtain the Full Moon Chestguard
│   └── Wolf Bane — obtain the Bilac Crescent Blade
├── Uncrowned Crown — craft Oriana's Scepter
│   └── Elven Mastery — obtain the Oriana Void Staff
└── First Technique — craft Skill: Slash or Thrust
    └── Skill Fusion — create any fused skill
        └── Unique Hunter — own all 3 Unique Monster weapons
            └── Grand Capture — obtain the Night Claw Talon
```

---

## Admin / Creative Commands

### Give items

```
/function slf:give/wethermon_scythe
/function slf:give/bilac_crescent_blade
/function slf:give/oriana_scepter
/function slf:give/sunraku_blade_r
/function slf:give/sunraku_blade_l
/function slf:give/rust_saber
/function slf:give/lycagon_fang
/function slf:give/vorpal_knife
/function slf:give/wezaemon_katana
```

### Loot tables

```
/loot give @s loot slf:wethermon_drops
/loot give @s loot slf:bilac_drops
/loot give @s loot slf:oriana_drops
/loot give @s loot slf:nightclaw_drops
```

### Class & progression

```
/function slf:class/select          — open the class selection menu
/function slf:skills/menu           — open the skill focus menu
/function slf:stats/menu            — open the stat point allocation menu
/function slf:stats/altar           — attempt Altar of Awakening (requires boss gate)
/function slf:setup                 — re-register all scoreboards (safe to run anytime)
```

---

## Pack Format Compatibility

| MC Version | Resource Pack | Data Pack |
|---|---|---|
| 1.21.0 – 1.21.1 | 34 | 48 |
| 1.21.2 – 1.21.3 | 42 | 57 |
| 1.21.4 | 46 | 61 |

The data pack declares `supported_formats: [48, 999]` so it loads on all 1.21.x versions.

---

## Textures

Current textures are **placeholder solid-colour PNGs**. Proper 16×16 pixel art is the single highest-impact contribution you can make. Files to replace are in `resource_pack/assets/slf/textures/item/`.

## Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for a full contributor guide — naming conventions, step-by-step instructions for adding skills, classes, and items, a scoreboard reference, and a PR checklist.
