# SLF.Mine — Shangri-La Frontier Pack

![Minecraft](https://img.shields.io/badge/Minecraft-1.21.x-brightgreen) ![Pack Format](https://img.shields.io/badge/data_pack-format_61-blue) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

A Minecraft 1.21.x data pack + resource pack bringing the world of **Shangri-La Frontier** into survival. Includes anime-faithful weapons, armor, and a full RPG system: 8 starting classes, a tiered skill-focus engine, 9 spendable stats, custom leveling, and hidden mask data that shapes the world around you.

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
Swordsman ─┬─ Sword Master ───── Kansei
           └─ Magic Swordsman ── Mysterious Sword

Warrior ──────────────────────┐
                              ├─ Barbarian ── War King
Fighter ─┬────────────────────┘
         └─ Destroyer ── Crazy Fist

[Swordsman OR Warrior lineage — NPC quest]
          └── Knight ─┬─ Holy Knight ── King's Knight
                      └─ Dark Knight ── Black Death

Mercenary ── Veteran

Bandit ───┬─ Thief ── Assassin ── Killing Joke
          └─ Ninja ── Shinobi ─── Star Shinobi Sei

Priest ──── Bishop ── Saint

Monk ─────── Monk Soldier ── Spirit Fist

Mage ─────── Sage ── Omnipotent Wisdom
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
| DMG (1) | Damage dealt | Power Slash, Ignition, Loop Slash |
| MOVE (2) | Sprint distance | Formula Drift, Skate Foot, Drift Step |
| EVADE (3) | Jumps | Slide Step, Skywalker, Best Steps |
| DEF (4) | Damage taken | Unbreakable, Drain, Flash Counter |

### Ideal Motion bonus

While **airborne and sprinting**, your SP accumulation is **3× normal** for that cycle. Aggressive, mobile combat is rewarded across all skill types.

### Skill tiers

| Tier | Who can learn | Class role |
|---|---|---|
| T1 | Anyone | Aligned class gets ~5× lower threshold |
| T2 | Anyone, but slow | Aligned class gets ~10× lower threshold |
| T3 | Only after class evolution | Evolution unlocks the skill in your menu |
| T4 | Achievement-gated | Class irrelevant; gates are level, kills, Vorpal Soul |
| T5 | Pruning | Combine two skills at the Skill Garden — originals are lost |

### Skill processes

Every skill belongs to one of four growth paths:

- **Strengthened** — Skills with Roman numeral notation (I–X) grow stronger as you use them. Level X is max.
- **Evolution** — Skills without a level notation evolve into a new skill through mastery. Some offer a choice of evolution path.
- **Pruning** — Two skills can be combined at the Skill Garden to forge a new one. Both originals are permanently lost. Higher-level inputs produce a stronger result — max your skills before pruning for the best outcome.
- **Connected** — *(to be revealed)*

### Skill evolution chains

```
Spin Slash → Rush Slash → Boundless Slash → Boundless Massacre

Screw Pierce → Spiral Edge → Drill Pierce → Glowing Pierce

Tap Step → Slide Step → Slide Move → Skate Foot → Drift Step

Best Steps → Moon Jumper → Skywalker → Flit Float → Hermes Boot → Dione's Help

Formula Drift → Limit Over Axel → Limit Break Less

Slash Ignition → Firefly
```

### Strengthened skills

The following skills level from I to X through continued use:

Accel, Power Slash, Loop Slash, Diastep, Drain, Fighting Spirit, Unbreakable, High Runner, Infight, Hand of Fortune, Assassin Pierce, Offroad, Overheat, Ignition

---

## Stats & Leveling

Earn EXP from mob kills. Level-ups grant **stat points** to spend via `/function slf:stats/menu`.

### 9 spendable stats

| Stat | Full Name | Lore | Minecraft Effect |
|---|---|---|---|
| HP | Physical Strength / Health | Your total health. Reaching 0 turns your avatar into a mass of polygons. | Max health *(planned)* |
| MP | Magic Power | Total mana you can exercise. Higher MP boosts magic performance and makes magic skills easier to acquire. | Mana pool *(planned)* |
| STR | Muscle Strength | Required to wield weapons effectively. Higher STR lets you handle heavier weapons with ease. | Strength I (10+), Strength II (20+) |
| DEX | Dexterity | Governs fine and precise weapon handling and inventory operations. | Attack speed +0.4 (5+), +0.8 (10+), +1.2 (20+) |
| AGI | Agility | Determines your avatar's base movement speed. | Speed I (5+), Speed II (10+), Speed III (20+) |
| TEC | Technique | Governs your ability to handle complex or unknown weapons at first sight. Assists player skill — trajectory control, projectile and magic manipulation. | Reduces skill focus thresholds |
| VIT | Endurance | Physical defense against trauma. Low VIT will cause your body to break down regardless of armor. | Absorption I (5+), II (10+), III (20+), IV (30+) |
| STM | Stamina | Decreases as you move or fight. Too low and your avatar becomes sluggish. Also affects lung capacity. | Saturation I (5+), Haste I (10+) |
| LCK | Luck | Affects random numbers and makes critical hit angles more forgiving. At LCK ≥ 50, activates **Bite** — survive a fatal blow at exactly 1 HP. | Luck attribute 1/2/3/4 (10/20/40/60+); Bite proc active |

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

*The spirit of knowing fear and still confronting it. Mask data measuring the integrity of the soul — an indomitable resolve untainted by despair.*

- **Rises** when you defeat enemies far beyond your current level
- **Falls** (−5) on your death — despair leaves a mark
- High Vorpal Soul is recognized by the **Vorpal Bunny** and certain elite monsters — they only appear before those whose soul is strong enough
- **Gates** T4 Heroic skills at `vorpal_soul ≥ 50`

### Karma

*Mask data that accumulates by succumbing to the temptation of malice.*

- **Rises** from any kill, but especially PK and slaughter driven by greed (farming for loot and items)
- **Decays** naturally over time; decreases through NPC quests and charitable acts
- At `karma ≥ 100` a **Bounty Hunter** (prize money hunter) will seek you out
- Caps at 200
- High karma affects your **trust value** with NPCs and factions *(planned)*

---

## Hidden Bosses

Seven unique boss monsters are hidden throughout the world. Defeating them is the highest challenge in the game.

| # | Boss | Drops |
|---|---|---|
| 1 | Lycagon the Nightslayer | |
| 2 | Wethermon the Tombguard | |
| 3 | Ctarnidd of the Abyss | |
| 4 | Siegwurm the Sky Ruler | |
| 5 | Goldhuneenay the Inexhaustible | |
| 6 | Orchestra of the Doom Echo | |
| 7 | *(unknown)* | |

---

## Items

### Weapons

| Name | Category | Notes |
|---|---|---|
| Mercenary Twinblades | Starting Weapon | Sunraku's initial dual swords; granted to Mercenary class |
| Goblin Hand Axe | Drop Weapon | Drops from goblins |
| Vorpal Chopper | Rare Drop | Rare drop from Vorpal Bunny; critical damage bonus |
| Togetsu Waning | Ascended Weapon | Ascended from Vorpal Choppers by Vysache |
| Togetsu Waxing | Ascended Weapon | Ascended from Vorpal Choppers by Vysache |
| Whalelore Moonblade "Goldsheen" | Ascended Weapon | Ascended from Togetsu by Vysache; requires Golden Scorpion stinger |
| Whalelore Moonblade "Netherlight" | Ascended Weapon | Ascended from Togetsu by Vysache; requires Atlanticus Lepnorca scale |

### Headgear

| Name | Notes |
|---|---|
| Staring Bird Mask | |
| Battlehorn Helm "4A" | |
| Lichman King Salmon's Headpiece | |
| Lacedaemon Helm | |

### Belts

| Name | Notes |
|---|---|
| Splitblade Belt | |
| Lifestide Sash | |
| Excavated Grindsash "Veteran" | |
| Lacedaemon Girdle | |

### Armor Sets

| Name | Notes |
|---|---|
| Splitblade Leather Equipment Set | |
| Non-Standard Specialized Armor "Adebane" | |
| Suit of the Protector | |
| Non-Standard Specialized Armor "Shoro" | |

### Accessories

| Name | Notes |
|---|---|
| Vorpal Soul Collar | |

---

## Skill Garden (Pruning)

Combine two skills at the **Skill Garden** to forge a new one. Both input skills are permanently destroyed. The level of your input skills at the time of pruning affects the base strength of the result — higher is better.

| Input A | Input B | Result |
|---|---|---|
| Oppression Kick | Loop Slash | Infight I |
| Strong Puncher | Crossing Slash | Hand of Fortune I |
| Accel | Fighting Spirit | Climax Boost I |
| Armor Piercer | Cutwater | Assassin Pierce I |
| Deerstep | Unbreakable | Offroad I |
| Starving Impulse | Naked Sense | Hunger Wolf |


---


## Admin / Creative Commands

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
| 1.21.4+ (target: 1.21.8+) | 46 | 61 |

Both packs declare a `supported_formats` wildcard range — they load on all 1.21.x versions.

---

## Textures

Current textures are **placeholder solid-colour PNGs**. Proper 16×16 pixel art is the single highest-impact contribution you can make. Files to replace are in `resource_pack/assets/slf/textures/item/`.

## Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for a full contributor guide — naming conventions, step-by-step instructions for adding skills, classes, and items, a scoreboard reference, and a PR checklist.
