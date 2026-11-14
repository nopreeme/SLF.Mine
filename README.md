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
| **Goblin** | Two in five wild zombies in forests and taiga above y=55 (not in caves) | 3–10 | Health 8 + level, attack 1 + level/3, small (0.6 size), quick; 3D goblin head with big ears and red eyes, brown tunic, bandaged feet, stone axe | **Goblin Hand Axe** 25%; 0–2 leather; a Mahni Purse 30%; emerald 5% |
| **Redcap Goblin** | **Night only**, half of the wild zombies in swamps and mangrove swamps (the Diremarsh); leave at dawn | 14–22 | Health 10 + level, attack 2 + level/3, faster, forged iron axe, deep red hood. **Calls two more Redcaps when hit** (at most five nearby) | **Redcap Iron Axe** 20%, **Red Hood** 5%, 1–2 Mahni Purses, 0–2 leather |
| **Orc** | One in twenty forest zombies; always arrives leading two goblins | 10–14 | Health 20 + level, attack 3 + level/3, big (1.25 size), slow, 3D orc head with tusks, club | 1–3 leather, iron nuggets, 1–2 Mahni Purses |
| **Mud Frog** | Every frog in a swamp or mangrove swamp (the Diremarsh) | 14–18 | Health 6 + level, 1.6 size. Passive; hits back with a mud splash (2 damage, Slowness) when attacked. **Swords barely hurt it** (it heals 4 per sword hit); blunt, piercing and fire weapons do full damage | **Mud Frog Skin** 50% (for the Splitblade set), slime balls |

Forest monsters (Goblin, Orc, Vorpal Bunny) give a quarter of their EXP once you reach level 12: time to cross the bridge (design doc V9).

Admins: `/function slf:mob/vorpal_bunny/spawn`, `slf:mob/goblin/spawn`, `slf:mob/red_hat_goblin/spawn` (the Redcap Goblin), `slf:mob/orc/spawn`, `slf:mob/mud_frog/spawn`, `slf:give/goblin_hand_axe` (set `#spawn_lv slf.mob_level` first to pick the level).

### Area boss: the Ravenous Snake

The Rampant Forest's area boss (design doc V9): a giant snake with tan-green scales, a white belly, yellow diamond eyes, white hair
tied with red beads, and a tail lock that opens like a flower. It is built from 3D models (a head and a chain of body segments that
slither after it) around an invisible hitbox.

- Level 15, 150 health, bite 6. Recommended: level 10, a party of three
- Every 5 seconds its tail leaves a pool of **poison** (30 seconds, so it is still on you after the fight)
- Appears in forests near players level 8–25 (2% a minute), one at a time, with a boss bar
- Killing it: its level in EXP + **300**. It does not count as a boss for the Altar of Awakening
- Drops **Devourer's Scale** (1–2) and **Python White Hair** (50%)

Admins: `/function slf:mob/boss/ravenous_snake/spawn`, `slf:give/devourers_scale`, `slf:give/python_white_hair`.

### Area boss: the Mud Digger, "Solo Killer"

The Diremarsh's area boss (design doc V9): a chimera with a shark's head, fins and tail, a mole's body on long webbed legs and
catfish whiskers, dark green with light splotches and cold blue eyes. One 3D model around an invisible hitbox.

- Level 25, 400 health, bite 9. A party of 3–4 is strongly recommended
- **Dives and bursts:** 8 seconds up, then it dives underground (it can't be hurt there) and 3 seconds later bursts out beside its
  target, ramming everyone within 3 blocks (6 damage) and throwing them. Fought solo, it always goes for that one player
- **Phase 2** (below 20% health): every dive starts with a quake that paralyses anyone standing in mud or water for 3 seconds (stand
  on solid ground to stay mobile), and every burst comes up right beneath a player and launches them high enough for the fall to kill
- Appears in swamps near players level 14–30 (2% a minute), one at a time, with a boss bar
- Killing it: its level in EXP + **800**. Not an Altar boss. Drops **Mud Digger Tooth** (1–3) and **Digger Hide** (1–2); killing it with
  nobody else within 32 blocks also gives the **Solo Killer's Trophy** and the title tag `slf.title.solo_killer`

Admins: `/function slf:mob/boss/mud_digger/spawn`, `slf:give/mud_digger_tooth`, `slf:give/digger_hide`, `slf:give/solo_killers_trophy`.

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

## Quests

Firstia's side quests from the design document (V9, section 2). Talk to an NPC by right-clicking it; quest offers come with an
**[Accept]** button, and `/trigger slf.menu set 10` (or **[Quests]** in the main menu) shows your quest log.

| Quest | From | Objective | Reward |
|---|---|---|---|
| A Pioneer's Awakening | Town Elder | Speak with the Local Alchemist, then gather 5 **Wild Herbs** (8% from cutting grass and ferns) | 50 EXP, 3 Basic Health Potions |
| Clearing the Outskirts | Guard Captain | Defeat 5 Goblins | 100 EXP, Starter Iron Dagger, 20 Mahni |
| The Brute Threat | Guard Captain (after Clearing the Outskirts) | Defeat 2 Orcs | 150 EXP, Beginner Leather Chestplate, 40 Mahni |

**Main quests** (Distressed Farmer, then the Guard Captain and Garren), one after another:

| Quest | From | Objective | Reward |
|---|---|---|---|
| The Missing Herd | Distressed Farmer | Accepting it sets up *your own* raiders' camp 40 blocks away (coordinates in chat): beat the 3 goblin raiders, talk to the Farmer's Daughter to rescue her, then lead the 3 cows back to the farmer (wheat or a lead) | 120 EXP, Fresh Milk Bundle, 30 Mahni |
| The Serpent's Shadow | Distressed Farmer | Speak with the Guard Captain about the bridge | 50 EXP |
| The Rampant Forest Guardian | Guard Captain | Defeat the Ravenous Snake (summoned 50 blocks away when you accept, unless one is already about) | 300 EXP, Devourer's Scale, Python White Hair, 100 Mahni |
| Secondil Supply Delivery + Brother's Beef | Distressed Farmer, ends at Garren | Carry the Sealed Beef Package to Garren in Secondil | 250 EXP, Basic Armor Piece, 50 Mahni; Garren becomes your armorer |

**Secondil** (section 4): Innkeeper Marrow, Lysa the florist, Guard Halvor, Old Borric and the Bartender.

| Quest | From | Objective | Reward |
|---|---|---|---|
| A Soft Bed at Last | Innkeeper Marrow | Rent a room (first night free) and lie in a bed: that registers your respawn point | 75 EXP, Secondil respawn, Secondil Stew |
| Antidote Run | Lysa | Carry 3 Antidote Bundles to Marrow | 100 EXP, 2 Antidotes, 30 Mahni |
| The Night Watch | Guard Halvor | At night, stand watch within 24 blocks of Halvor for 45 seconds; two Redcaps appear at the tree line 30 blocks west. **Don't engage**: hitting one starts the watch over | 125 EXP, Guard Issue Cloak, 40 Mahni, unlocks Garren's first quest |
| Bar Talk | Old Borric | Hear three of his stories, then tell the Bartender whether the marsh humming is true (it is) | 60 EXP, Strong Ale, 20 Mahni |

**Garren's questline** (unlocked by delivering his brother's beef, or by The Night Watch):

| Quest | Objective | Reward |
|---|---|---|
| The Iron Pickaxe | Take Garren's pickaxe to the Diremarsh and bring back 5 raw iron | 200 EXP, Basic Iron Chestplate, 75 Mahni |
| Splitblade Set | Bring 4 Mud Frog Skins | 250 EXP, Splitblade Leather Set (body, pants, mask), 50 Mahni |
| The Missing Miner | Your own search site 60 blocks out (coordinates in chat): a torn bag, a broken pickaxe and **Tomic's Journal**, a readable book whose last page mentions the humming and the red hoods. Pick up the journal, bring it to Garren | 300 EXP, Iron Pickaxe (Reinforced), 100 Mahni |
| Red Hoods in the Reeds | Show the journal to Halvor; at night he sends you with two Secondil Guards (iron golems) to your own Redcap camp 50 blocks out. Two waves (3, then 4 Redcaps); then take their **Unknown Sigil Banner** to Halvor | 400 EXP, Redcap Iron Axe, 125 Mahni (keep the banner) |
| Path to Thirdrema | Defeat the Mud Digger (summoned 60 blocks out when you accept) | 500 EXP, Garren's Plated Vambraces (off hand: +4 armour, +10% knockback resistance), 200 Mahni |

**Shops** (Mahni): Lysa sells Antidotes (15, cures poison) and Basic Health Potions (20); the Bartender sells Strong Ale (10:
Strength for a minute, a little Nausea) and Secondil Stew (5). Talk to them and click an item.

NPCs are villagers that stand still, can't be hurt, never despawn and have no trades. Your world's towns aren't built yet, so an admin
places them: `/function slf:npc/place/elder`, `.../alchemist`, `.../guard_captain`, `.../farmer`, `.../garren`, `.../marrow`, `.../lysa`, `.../halvor`, `.../borric`, `.../bartender` (facing the nearest player), and
`/function slf:npc/remove` removes NPCs within 8 blocks. The Starter Iron Dagger is the weapons pack's Iron Dagger model.

Not built yet: Thirdrema (the design document only names it).

---

## The Diremarsh

- **Walking state**: in a swamp or mangrove swamp, a player standing on marsh ground (anything but rock, logs or planks)
  has one leg stuck in the mud: −40% movement speed and −40% jump. Step onto higher ground - a rock outcrop, a stump, a
  boardwalk - and you're free. It applies in the Mud Digger fight too, so positioning matters
- **Splitblade leather turns a blade**: when something holding a sword or an axe hits you, the full Splitblade set
  (body, pants, mask) gives back 4 health; one or two pieces give back about 1-2

---

## The Wanderer's Path

The hard-mode origin from the design document (V9, section 6). New players choose an origin before their class:
**Citizen** (start with Firstia's people and quests) or **Wanderer** (a warning screen first; there is no going back).

- **Traits**, permanent: +2 Luck (better drops and rolls) and −10% armour (you take more damage from every hit)
- **Start**: a random spot in a forest or taiga, within 64 blocks of the Rampant Forest's centre if an admin set it
  (`/function slf:wanderer/set_forest`), otherwise within 200 blocks of where you joined
- **Firstia is closed**: its Guard Captain, Elder, Alchemist and Farmer turn away strangers from the wilds
- **The Dream Penalty**: die before you complete *A Soft Bed at Last* at Secondil's inn, and you wake at Firstia's inn
  (`/function slf:wanderer/set_firstia_inn`) with your level, EXP, Mahni, stat points, skill progress and everything you
  dropped gone - "only a dream". You keep your class, skills and the Wanderer traits, and Firstia's gates are open from then on
- **First Survivor**: kill the Ravenous Snake while still under the Dream Penalty, then register at Secondil's inn. Garren then
  greets you with **Fellow Survivor** (150 EXP, 75 Mahni, Garren's Full Meal) instead of the beef delivery, and his questline opens
- **The Long Way Back**: Firstia's people greet a First Survivor differently, and the farmer leaves **A Brother's Letter** on
  the table; carry it back to Garren (250 EXP, 100 Mahni, Fresh-Baked Bread, *Trusted of Garren*)

---

## Mahni

Mahni is the currency (design doc V9). Your balance shows on the status sheet and at the end of the status line above the hotbar.
Monsters drop **Mahni Purses** worth 10 Mahni each; a purse turns into Mahni the moment it reaches your inventory.

| Source | Purses |
|---|---|
| Goblin | 1 (30%) |
| Orc, Redcap Goblin | 1–2 |
| Ravenous Snake | 5–8 |
| Mud Digger | 10–15 |

Spend it at the Secondil shops (Lysa, the Bartender); quests pay Mahni too. Admins: `/function slf:give/mahni_purse`,
`/scoreboard players add <player> slf.mahni <n>`.

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

**[ITEMS.md](ITEMS.md)** lists every item: icon, stats, description, where it comes from (drops, quests, shops) and its give
command. It is generated from the packs by `tools/gen_item_docs.py`.

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
| Mobs | A Vorpal Bunny (random level, or level 30), a Goblin, a Redcap Goblin, an Orc with its goblins, a Mud Frog, remove SLF mobs nearby |
| Bosses | The two area bosses and each of the seven bosses, six blocks ahead; midnight (full moon) or morning |
| NPCs | Place the Town Elder, Local Alchemist, Guard Captain, Distressed Farmer or Garren; 5 Wild Herbs; quest log; remove NPCs |
| Secondil | Place Innkeeper Marrow, Lysa, Guard Halvor, Old Borric or the Bartender |
| Origin | The origin choice, become a Wanderer, set Firstia's inn and the Rampant Forest's centre |
| Me | Status sheet, +100 Mahni, the player menu, reset yourself |

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
