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

### 3D Weapons (optional, separate packs)
Nine weapons with 3D held models live in [`weapons/`](weapons/README.md) as their own resource pack + data pack. They load alongside the main packs; see that README for install and give commands.

---

## Getting Started

```
Join world
  └─ Chat shows the class selection menu
       └─ Choose a class → you receive your class tag and T1 skills
            └─ Open the menu any time → /trigger slf.menu
                 ├─ [Skills]  click a skill to focus it → earn SP by playing → learned when SP ≥ threshold
                 ├─ [Stats]   spend stat points
                 ├─ [Evolve]  class evolution, once you meet the level requirement
                 └─ [Status]  class, level, EXP, stats, mana
```

Everything a player needs is behind `/trigger slf.menu`, which works **without OP**. A status line above the hotbar
shows level, EXP, mana, focus progress and unspent points (toggle it from the menu).

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

Evolve from the menu (`/trigger slf.menu` → **[Evolve]**). An evolution appears once your lineage allows it and unlocks at a level:

| Evolution | Level |
|---|---|
| Tier 2 (Sword Master, Magic Swordsman, Barbarian, Destroyer, Thief, Ninja, Bishop, Monk Soldier, Sage) | 20 |
| Knight (from Sword Master, Magic Swordsman or Barbarian) | 30 |
| Tier 3 (Kansei, Mysterious Sword, War King, Crazy Fist, Assassin, Shinobi, Saint, Spirit Fist, Omnipotent Wisdom) and Veteran | 50 |
| King's Knight, Black Death | 70 |
| Killing Joke, Star Shinobi Sei | 80 |

Knights choose Holy or Dark after three **Knight Trials**; each elite monster defeated as a Knight counts as one.
Level requirements live in one file, `class/evolve_apply.mcfunction`. Quest chains and NPCs are planned to replace
the level gates. History tags (`slf.was_swordsman`, etc.) accumulate permanently — you never lose access to a path you've walked.

See [CONTRIBUTING.md](CONTRIBUTING.md#class-id-table) for the full class ID table.

---

## Skill Focus System

Every skill does something once you hold it: a permanent bonus that stacks with your stats and gear. The full list is in [SKILL_EFFECTS.md](SKILL_EFFECTS.md).

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

Earn EXP from mob kills. Level-ups grant **stat points** to spend from the menu (`/trigger slf.menu` → **[Stats]**).

| Kill | EXP |
|---|---|
| Any mob | 2 |
| Common monsters (zombie, skeleton, creeper, spider, …) | 10 |
| Elite monsters (enderman, witch, blaze, wither skeleton, …) | 40 |
| Bosses (Ender Dragon, Wither, Warden, Elder Guardian) | 2,500 |

The lists are entity tags in `data/slf/tags/entity_type/`. EXP beyond what a level needs carries over.

### 9 spendable stats

| Stat | Full Name | Lore | Minecraft Effect |
|---|---|---|---|
| HP | Physical Strength / Health | Your total health. Reaching 0 turns your avatar into a mass of polygons. | +½ heart of max health per 2 points (up to +20 hearts) |
| MP | Magic Power | Total mana you can exercise. Higher MP boosts magic performance and makes magic skills easier to acquire. | Mana pool of 20 + 2 per point, regenerating 1 + MP/10 per second. Spent by Big / Grand Tantrum |
| STR | Muscle Strength | Required to wield weapons effectively. Higher STR lets you handle heavier weapons with ease. | Strength I (10+), Strength II (20+) |
| DEX | Dexterity | Governs fine and precise weapon handling and inventory operations. | Attack speed +0.4 (5+), +0.8 (10+), +1.2 (20+) |
| AGI | Agility | Determines your avatar's base movement speed. | Speed I (5+), Speed II (10+), Speed III (20+) |
| TEC | Technique | Governs your ability to handle complex or unknown weapons at first sight. Assists player skill — trajectory control, projectile and magic manipulation. | −1% skill focus threshold per point (up to −50%) |
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

At level 99 you enter **Standby** — EXP no longer advances your level but is banked. Defeat a qualifying high-tier boss (sets `slf.boss_gate = 1`), then walk up to the **Altar of Awakening** to convert banked EXP into levels 100–150. Killing any boss on the list above sets the gate.

Each world has one Altar of Awakening. When the first player reaches level 99, the pack raises it on dry ground about 320 blocks away in a random direction (480 if nothing within 320 is dry ground: water, lava and forest canopy are skipped), with a foundation so it never overhangs a slope. Every player in Standby is told its coordinates and gets an **Altar Compass** that points to it; **[Altar of Awakening]** in the menu repeats the directions.

To choose the spot yourself, an admin can build it with `/function slf:altar/place` (four blocks south of where they stand) at any time, before or after one has risen; `/function slf:altar/remove` retires it, and the next player who needs an altar gets a new one raised. The altar is built by functions, not world generation, so worlds using the pack open without Minecraft's "experimental settings" warning.

---

## Mask Data

Two hidden scoreboards shape the world without being shown in any UI.

### Vorpal Soul

*The spirit of knowing fear and still confronting it. Mask data measuring the integrity of the soul — an indomitable resolve untainted by despair.*

- **Rises** when you defeat enemies far beyond your current level
- **Falls** (−5) on your death — despair leaves a mark
- **Gates** T4 Heroic skills at `vorpal_soul ≥ 50`

### Karma

*Mask data that accumulates by succumbing to the temptation of malice.*

- **Rises** from any kill, but especially PK and slaughter driven by greed (farming for loot and items)
- **Decays** naturally over time; decreases through NPC quests and charitable acts
- At `karma ≥ 100` a **Bounty Hunter** (prize money hunter) will seek you out
- Caps at 200
- High karma affects your **trust value** with NPCs and factions *(planned)*

---

## Monsters

SLF monsters are vanilla creatures the pack gives a level, stats, a name and its own drops (a data pack can't add new
creature types). Every SLF monster shows its level in its name. Killing one gives EXP equal to its level (plus the 2
every kill gives) and a **Vorpal Soul** if it was at least 20 levels above you.

| Monster | Where | Level | Stats | Drops |
|---|---|---|---|---|
| **Vorpal Bunny** | Rare, in forests and taiga (the Rampant Forest): one in three wild rabbits there, and one in twenty forest zombies is replaced by one | 8–30 | Health 6 + level, attack 2 + level/6, armour 8, faster than a rabbit, hostile (vanilla's Killer Bunny) | 2–4 bones; Vorpal Knife 5%; **Vorpal Choppers 4%** (the weapons pack's item: install it to see the model); Acrobat skill book 3% (player kills only) |
| **Goblin** | Two in five wild zombies in forests and taiga above y=55 (not in caves) | 3–10 | Health 8 + level, attack 1 + level/3, small (0.6 size), quick; 3D goblin head with big ears and red eyes, brown tunic, bandaged feet, stone axe | **Goblin Hand Axe** 25%; 0–2 leather, 0–2 gold nuggets; emerald 5% |
| **Redcap Goblin** | **Night only**, half of the wild zombies in swamps and mangrove swamps (the Diremarsh); leave at dawn | 14–22 | Health 10 + level, attack 2 + level/3, faster, forged iron axe, deep red hood. **Calls two more Redcaps when hit** (at most five nearby) | **Redcap Iron Axe** 20%, **Red Hood** 5%, 1–4 gold nuggets (stand-in for Mahni), 0–2 leather |

Forest monsters (Goblin, Vorpal Bunny) give a quarter of their EXP once you reach level 12: time to cross the bridge (design doc V9).

Admins: `/function slf:mob/vorpal_bunny/spawn`, `slf:mob/goblin/spawn`, `slf:mob/red_hat_goblin/spawn` (the Redcap Goblin), `slf:give/goblin_hand_axe` (set `#spawn_lv slf.mob_level` first to pick the level).

### Bosses

Bosses appear near players by chance, rolled once a minute per player in survival, when the place, time and the
player's level fit. Only one of each exists at a time. A boss shows a boss bar to everyone within 64 blocks.
Killing one gives its level in EXP plus **2400**, counts as a boss kill for the Altar of Awakening, and is a Knight Trial.
Health is 4 × level, attack 4 + level/10.

| Boss | Appears | Player level | Level | Body | Drops |
|---|---|---|---|---|---|
| **Nightclaw** | Overworld caves below y=0 (2.5% a minute) | 10+ | 40 | Spider, ×2.5 size | Nightclaw Talon |
| **Bilac the Full Moon Fangs** | Under the open sky on a full-moon night (10%) | 30+ | 60 | Phantom, ×3 size | Bilac's Crescent Blade, phantom membrane, iron |
| **Oriana the Uncrowned** | The End (5%) | 45+ | 75 | Evoker, ×1.3 size | Oriana's Void Staff, ender pearls, diamonds |
| **Lycagon the Nightslayer** | Under the open sky at night (1.7%) | 50+ | 90 | Black wolf, ×3 size, always hunting | Lycagon's Fang, bones, obsidian; Managarm Pride book 25% |
| **Ctarnidd of the Abyss** | Swimming in a deep ocean (5%) | 40+ | 85 | Elder guardian, ×2 size | Reflexus book 30%, prismarine crystals, nautilus shells |
| **Siegwurm the Sky Ruler** | Under the open sky above y=150 (4%) | 55+ | 95 | Ghast, ×1.5 size | Unique Monster Core, Gravity Zero book 30%, ghast tears, phantom membrane |
| **Wethermon the Tombguard** | The Nether (3.3%) | 60+ | 100 | Wither skeleton in netherite with its scythe, ×1.6 size | Wethermon's Scythe, the Seiten Skillbook, bones, scrap; a Tombguard armour piece 50% |

Night bosses (Bilac, Lycagon) leave at dawn without dropping anything. The vanilla bosses (Ender Dragon, Wither,
Warden, Elder Guardian) still count as boss kills too.

Admins: `/function slf:mob/boss/<id>/spawn` (`nightclaw`, `bilac`, `oriana`, `lycagon`, `ctarnidd`, `siegwurm`, `wethermon`), or the
Bosses row of the test menu.

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

### Test menu

`/function slf:test/menu` opens a clickable menu with every test tool (operators only, since it runs `/function`):

| Row | What it does |
|---|---|
| Items | One kit per group: weapons (22), armor (16), skill books (15), materials & tomes (5), plus the 3D weapons pack and clear inventory |
| Class | One button per class (34): resets you, then grants the whole lineage up to that class at the level it needs |
| Level | Set level 1/10/20/30/50/70/80, jump to 99 (Standby, the altar rises), +1000 EXP, record a boss kill |
| Stats | +10 stat points, every stat to 20 or 0, fill mana |
| Skills | Learn every skill, finish the skill you are focusing on, +1 Knight trial |
| World | Karma 100 (bounty hunter) or 0, place / remove the altar, an altar compass |
| Mobs | A Vorpal Bunny (random level, or level 30), a Goblin, a Redcap Goblin, remove SLF mobs nearby |
| Bosses | Each of the seven bosses, six blocks ahead; midnight (full moon) or morning |
| Me | Status sheet, the player menu, reset yourself |

Every item can also be given on its own: `/function slf:give/<item>` (tab completion lists them), e.g. `/function slf:give/bilac_crescent_blade`. A few skill books (Acrobat, Gravity Zero, Managarm Pride, Reflexus) teach their skill and are used up the first time you pick them up; that is how they work in play.

`tools/gen_test_commands.py` writes the give commands, kits, class setups and menu; run it after adding an item or a class (a test fails until you do).

### Commands

```
/function slf:class/select          — open the class selection menu
/function slf:skills/menu           — open the skill focus menu
/function slf:stats/menu            — open the stat point allocation menu
/function slf:stats/altar           — attempt Altar of Awakening (requires boss gate)
/function slf:setup                 — re-register all scoreboards (safe to run anytime)
/function slf:altar/place           — build the Altar of Awakening four blocks south of you
/function slf:altar/remove          — retire the altar (a new one rises when someone needs it)
/function slf:admin/reset_player    — wipe your own SLF state (for testing)
```

---

## Pack Format Compatibility

| MC Version | Resource Pack | Data Pack |
|---|---|---|
| 26.2 | 88 | 107 |

Both packs declare `min_format`/`max_format` for 26.2 only. 26.2 rejects the old `pack_format` + `supported_formats` declaration, and these packs no longer load on 1.21.x.

---

## Textures

Every item has a 16×16 texture. The flat ones are drawn by `tools/gen_item_textures.py` from pixel templates and per-item palettes, so they are consistent placeholders rather than final art. Hand-made pixel art is still the single highest-impact contribution you can make: replace a PNG in `resource_pack/assets/slf/textures/item/` and remove its line from the generator.

## Tests

```
python -m unittest tests/test_datapack.py tests/test_resource_pack.py tests/test_test_suite.py
```

Both read files only. `tests/live/` runs the pack on a real server with a real player; see [tests/live/README.md](tests/live/README.md).

## Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for a full contributor guide — naming conventions, step-by-step instructions for adding skills, classes, and items, a scoreboard reference, and a PR checklist.
