# SLF.Mine — Shangri-La Frontier in Minecraft

![Minecraft](https://img.shields.io/badge/Minecraft_Java-26.2-brightgreen) ![Data pack](https://img.shields.io/badge/data_pack-format_107-blue) ![Resource pack](https://img.shields.io/badge/resource_pack-format_88-blue)

A data pack and resource pack that turn survival Minecraft into the world of **Shangri-La Frontier**: classes that
evolve, skills you learn by fighting, stats, levels, quests, a currency, and the series' monsters and bosses. It is
all vanilla — no mods — and built from the project's design document (V9).

**What's in it**

- **Classes** that evolve: 8 starting classes and their jobs from the series, with an evolution menu (being
  reworked to the series' class tree)
- **Skills learned through play**: focus one, then earn it by attacking, sprinting, jumping or taking hits
- **9 stats**, levels 1–99, and levels 100–150 after the **Altar of Awakening**
- **Monsters** with levels and their own drops: Goblin, Redcap Goblin, Orc, Mud Frog, Vorpal Bunny
- **Two area bosses** with 3D bodies (the Ravenous Snake, the Mud Digger)
- **The Seven Colossi**: four are in the pack with boss bars (Wethermon, Lycagon, Ctarnidd, Siegwurm); three are
  planned
- **Quests and NPCs** for Firstia and Secondil, Garren's questline, and a quest log
- **Mahni** currency and shops
- **Origins**: the Wanderer's Path, a hard-mode origin with the Dream Penalty; Average Joe; six more origins planned
- **Items**: 62 in the main packs and 29 weapons with 3D held models — see **[ITEMS.md](ITEMS.md)**

---

## Contents

- [Installation](#installation)
- [Getting started](#getting-started)
- [Classes](#classes) · [Skills](#skills) · [Stats and levels](#stats-and-levels) · [Vorpal Soul and Karma](#vorpal-soul-and-karma)
- [Monsters](#monsters) · [Area bosses](#area-bosses) · [The Seven Colossi](#the-seven-colossi)
- [Quests](#quests) · [Mahni and shops](#mahni-and-shops) · [The Diremarsh](#the-diremarsh) · [Origins](#origins)
- [Items and weapons](#items-and-weapons)
- [For server admins](#for-server-admins)
- [For contributors](#for-contributors)
- [Planned](#planned)

---

## Installation

The packs are for **Minecraft Java 26.2** only (they do not load on 1.21.x). Both main packs must be active together.

| Pack | Copy this folder | To |
|---|---|---|
| Resource pack | `resource_pack/` | `.minecraft/resourcepacks/`, then enable it in **Options → Resource Packs** |
| Data pack | `data_pack/` | `<world>/datapacks/`, then run `/reload` |
| 3D weapons (optional) | `weapons/java_out/SLF_Weapons_ResourcePack/` and `SLF_Weapons_Datapack/` | the same two places |

The 3D weapons are a separate pair of packs that load alongside the main ones; see [weapons/README.md](weapons/README.md).
Install them if you want the Vorpal Choppers and the Starter Iron Dagger to show their models.

Worlds using the packs open normally: nothing here uses world generation, so Minecraft does not show its
"experimental settings" warning.

---

## Getting started

```
Join the world
  └─ Choose an origin: Average Joe, or Wanderer (hard mode)
       └─ Choose a class → you get your class and its starting skills
            └─ /trigger slf.menu — everything else is in this menu
                 ├─ [Skills]  focus a skill, then earn it by playing
                 ├─ [Stats]   spend stat points
                 ├─ [Evolve]  evolve your class once you meet the level
                 ├─ [Quests]  your quest log
                 └─ [Status]  class, level, EXP, stats, mana, Mahni
```

`/trigger slf.menu` works **without OP**. A status line above the hotbar shows your level, EXP, mana, focus progress,
unspent points and Mahni; you can switch it off from the menu.

Kill monsters for EXP. Each level gives **5 stat points** (10 above level 99). Talk to NPCs by right-clicking them.

---

## Classes

> **Being reworked.** This is the class tree the pack is moving to, with the official English (anime) names. The
> pack still has its older class list until that rework lands.

Choose one of **8 starting classes**. Your class decides which skills you learn fastest and which jobs open up.
**Knight** is a ninth line that a Fighter, Swordsman or Brawler can join.

| Class | Japanese | Playstyle | Primary focus |
|---|---|---|---|
| Fighter | 戦士 (Senshi) | Any physical weapon, no magic | DMG |
| Swordsman | 剣士 (Kenshi) | Blade techniques; magic with the right build | DMG |
| Brawler | 闘士 (Tōshi) | Fists and heavy weapons, all offence | DMG |
| Mercenary | 傭兵 (Yōhei) | All-weapon freelancer | DMG / DEF |
| Thief | 盗賊 (Tōzoku) | Speed and evasion | EVADE / MOVE |
| Monk | 修行僧 (Monku) | Body as weapon, iron defence | DMG / DEF |
| Priest | 聖職者 (Purīsuto) | Healing and support | DEF |
| Magician | 魔法使い (Majishan) | Magic arts | DEF / DMG |

◆ marks a hidden or specialty job.

```
Fighter ──── Barbarian (蛮兵) ──────── War King (戦王)

Swordsman ─┬─ Sword Master (剣豪) ──── Master Swordsman (剣聖)
           └─ ◆ Magic Swordsman (魔法剣士) ── ◆ Mysterious Swordsman (神秘の剣, Rätzel)

Brawler ──── Destroyer (破壊者) ──────── Berserker (狂拳)

Mercenary ── Veteran (戦巧者) ───────── Warlord

Monk ─────── Monk Soldier (僧兵) ────── Warrior Monk (武僧兵)

Thief ─┬─ Master Thief (大盗賊) ──── Great Stealth (隠密)
       ├─ ◆ Assassin (暗殺者) ──────── ◆ Killing Joker (殺戮の鬼札)
       ├─ ◆ Phantom Thief (怪盗) ───── ◆ Still Joker (華麗なる鬼札)
       └─ ◆ Ninja (忍者) ─┬─ ◆ Star Ninja (星忍) ── ◆ Sacred Star Ninja (星忍聖)
                         └─ ◆ Jonin (上忍) ─────── ◆ Shinobi (忍聖)

Fighter / Swordsman / Brawler
  └── Knight (騎士) ─┬─ Holy Knight (聖騎士) ── Paladin (聖輝士)
                     └─ Dark Knight (暗黒騎士) ── Dark Crusader (黒忌士)

Priest ─┬─ Bishop (僧侶)
        ├─ Cleric (洗礼者)
        ├─ Enchanter (恩寵者)
        └─ Pilgrim (巡礼者) ── ◆ The Saint (大聖者)

Magician ── Sorcerer (魔術師) ── Sage (賢者)
```

Notes from the series:
- **Master Swordsman** (剣聖, *Kensei*) is the job sometimes written "Kansei"; it is also called "Master of the Sword"
- **Berserker** (狂拳) is only partly revealed in the series; the reading "Berse…" points to Berserker. The
  series has no job after **Veteran** yet, so the Mercenary's top job, **Warlord**, is the project's own
- **Magic Swordsman** needs the Swordsman's basics plus extra magical aptitude
- **Holy Knight** comes from raising your faith; **Dark Knight** from raising your slaughter count
- **Bishop** heals, **Cleric** buffs, **Enchanter** enchants, and the **Pilgrim** is a solo job that only grows by
  travelling on foot; the hidden **Saint** follows from it
- **Killing Joker** needs high Karma and ten player kills while red-named; **Ninja** opens through a Thieves' Guild
  trial for a Thief who knows some magic

Evolve from the menu (**[Evolve]**). An evolution appears once your lineage allows it, and unlocks at a level:

| Evolution | Level |
|---|---|
| Advanced jobs: Barbarian, Sword Master, Magic Swordsman, Destroyer, Veteran, Monk Soldier, Master Thief, Assassin, Bishop, Cleric, Enchanter, Pilgrim, Sorcerer | 20 |
| Knight; Phantom Thief, Ninja | 30 |
| Top jobs: War King, Master Swordsman, Mysterious Swordsman, Berserker, Warlord, Warrior Monk, Great Stealth, Holy Knight, Dark Knight, Star Ninja, Jonin, Sage | 50 |
| Paladin, Dark Crusader | 70 |
| Killing Joker, Still Joker, Sacred Star Ninja, Shinobi, The Saint | 80 |

Hidden and specialty jobs (◆) will have extra unlock conditions on top of the level.

Knights choose Holy or Dark after three **Knight Trials**: each elite monster or boss defeated as a Knight counts as one.
You never lose a path you have walked; your class history is kept.

---

## Skills

Skills are **earned through play**. Each has a **focus stat** and a **threshold** of skill progress (SP).

1. Open **[Skills]** in the menu and click a skill: you are now *focusing* it
2. Play: attack, sprint, jump, take damage
3. Every second, what you did is added to your SP
4. At the threshold, the skill is learned

| Focus stat | Driven by | Examples |
|---|---|---|
| DMG | Damage dealt | Power Slash, Megaton Swing, Spin Slash |
| MOVE | Sprint distance | Formula Drift, Skatefoot |
| EVADE | Jumps | Slide Step, Skywalker |
| DEF | Damage taken | Unbreakable, Flash Counter, Ignition |

- **Your class matters:** a skill that fits your class lineage has a much lower threshold
- **Ideal Motion:** while sprinting in the air, SP builds **3×** as fast
- **TEC** lowers every threshold by 1% per point, up to 50%
- **Every skill does something once learned:** a permanent bonus that stacks with stats and gear. The full list is in
  [SKILL_EFFECTS.md](SKILL_EFFECTS.md)
- **Big Tantrum** (大癇癪) draws nearby monsters to you — use it with care in a party
- Skills come from the series. Names follow the anime: the katakana reading when there is one (Retaliate,
  Moment Sight), otherwise the Japanese romanized (Tsujigiri, Hikkyō Un'yō)

---

## Stats and levels

### EXP

| Kill | EXP |
|---|---|
| Any mob | 2 |
| Common monsters (zombie, skeleton, creeper, spider, …) | +8 |
| Elite monsters (enderman, witch, blaze, wither skeleton, …) | +38 |
| Vanilla bosses (Ender Dragon, Wither, Warden, Elder Guardian) | +2,498 |
| SLF monsters | + the monster's level |
| SLF area bosses and bosses | + level, + 300 to 2,400 (see below) |

Forest monsters (Goblin, Orc, Vorpal Bunny) give a quarter of their EXP once you reach level 12. EXP beyond what a
level needs carries over.

| Level | EXP to the next |
|---|---|
| 1 → 10 | 100, 200, 350, 550, 850, 1,300, 2,000, 3,000, 4,500 |
| 10 → 99 | 5,000 each |
| 99 | The level cap: **99 Extend** (below) |

### Stat points

As in the series, stat points come from levels and from meeting Unique Monsters such as the Seven Colossi:

| Source | Points |
|---|---|
| Each level up to 99 | 5 |
| Reaching level 99 | 50 |
| Each level above 99 | 10 |
| Encountering a Unique Monster (UME), once each | 20 |
| Defeating a Unique Monster (UMB) | 200 |

### The nine stats

Spend points from **[Stats]** in the menu. Effects are applied every second.

| Stat | Effect |
|---|---|
| HP | +½ heart of max health per 2 points (up to +20 hearts) |
| MP | Mana pool of 20 + 2 per point; regenerates 1 + MP/10 per second |
| STR | Strength I at 10, II at 20 |
| DEX | Attack speed +0.4 at 5, +0.8 at 10, +1.2 at 20 |
| AGI | Speed I at 5, II at 10, III at 20 |
| TEC | −1% skill threshold per point (up to −50%) |
| VIT | Absorption I at 5, II at 10, III at 20, IV at 30 |
| STM | Saturation at 5, Haste I at 10 |
| LUC | Luck 1/2/3/4 at 10/20/40/60. At 50+, **clench** (食いしばり): damage from your own attacks or recoil can't kill you — you're left at 1 HP |

### 99 Extend and the Altar of Awakening

The first level cap is **99**. At level 99, defeat a monster of **level 100 or higher** and you reach **99 Extend**
(the cap is waiting to be released): EXP is banked instead of levelling you. Use the **Altar of Awakening**
(覚醒の祭壇) to release the cap to **150**, and the banked EXP levels you up all at once.

Each world has one altar. When the first player reaches level 99, the pack raises it on dry ground about 320 blocks
away. Every player at 99 Extend is told its coordinates and gets an **Altar Compass** that points to it;
**[Altar of Awakening]** in the menu repeats the directions.

---

## Vorpal Soul and Karma

Two hidden scores shape the world.

**Vorpal Soul** — the Vorpal Bunnies' ideal: beating stronger opponents with style, under handicaps. In the series it
falls for "boring" fights such as grinding or ganging up in a full party. The pack keeps it simple:
- Rises by 1 when you defeat something at least 20 levels above you
- Falls by 5 when you die

**Karma** — the weight of malice, kept against player killers. The higher it is, the worse. The pack keeps it simple:
- Rises by 25 for killing a player, and by 5 for killing a villager, wandering trader or iron golem
- Decays by 1 a minute
- At 100, a **Bounty Hunter** comes for you. It caps at 200

---

## Monsters

SLF monsters are vanilla creatures given a level, stats, a look and their own drops (a data pack cannot add new
creature types). Each shows its level in its name.

| Monster | Where it appears | Level | Notable drops |
|---|---|---|---|
| **Goblin** | Forests and taiga, above ground: two in five wild zombies | 3–10 | Goblin Hand Axe 25%, Mahni Purse 30% |
| **Orc** | The Rampant Forest between Firstia and Secondil (forests and taiga): one in twenty wild zombies, always leading two goblins | 10–14 | 1–2 Mahni Purses |
| **Vorpal Bunny** | Forests and taiga, rare: one in three wild rabbits, one in twenty wild zombies | 8–30 | **Vorpal Choppers 5%**, Rabbit Neckband 12% |
| **Redcap Goblin** | Swamps (the Diremarsh), **night only**: half of the wild zombies; gone at dawn | 14–22 | Redcap Iron Axe 20%, Red Hood 5%, 1–2 Mahni Purses |
| **Mud Frog** | Swamps: every frog | 14–18 | Mud Frog Skin 50% |

- **Goblin** — small and quick, with a 3D goblin head (big ears, red eyes), a tunic and a stone axe
- **Orc** — big and slow, hits hard; tusked 3D head and a club. Orcs roam the Rampant Forest, each leading two goblins
- **Vorpal Bunny** — an upright grey rabbit with a red scarf (a full 3D body). Fast, armoured and hostile. Its rare
  drop, the **Vorpal Choppers**, are the red twinblades. Beating a high-level one early is the classic way to earn Vorpal Soul
- **Redcap Goblin** — a deep red hood and a forged iron axe. **It calls for backup if it isn't defeated quickly**
- **Mud Frog** — a full 3D teal frog. Passive, but splashes mud back when attacked (2 damage and Slowness).
  **Slash weapons barely hurt it**; blunt, piercing and fire weapons work

---

## Area bosses

Area bosses guard the way between zones. One of each exists at a time, with a boss bar.

### The Ravenous Snake — the Rampant Forest

A giant snake built from 3D models: a dark crocodile-like head with yellow diamond eyes, a wild white mane tied with
red beads, an olive body with a cream belly, and a white-plumed tail.

- Level 15, 150 health, bite 6. Recommended: level 10, a party of three
- Every 5 seconds its tail leaves a pool of **poison** that lasts 30 seconds — it is still on you after the fight
- Appears in forests near players of level 8–25 (2% a minute), or when you accept *The Rampant Forest Guardian*
- Reward: its level in EXP + 300. Drops the **Ravenous Fang** (貪食の牙, always), **Devourer's Scale** (1–2), **Python White Hair**
  (50%), 5–8 Mahni Purses

### The Mud Digger — the Diremarsh

A chimera with a shark's head, fins and tail, a mole's body on long webbed legs, and catfish whiskers.

- Level 25, 400 health, bite 9. A party of 3–4 is strongly recommended
- **Dives and bursts:** 8 seconds above ground, then it dives (it cannot be hurt underground) and 3 seconds later
  bursts out beside its target, ramming everyone within 3 blocks. Alone, you are always the target
- **Phase 2** (below 20% health): it dives underground and sets off a quake that paralyses everyone standing in the
  mud, then bursts up from the mud under a **random player**, ramming them and launching them high into the air
- Appears in swamps near players of level 14–30 (2% a minute), or when you accept *Path to Thirdrema*
- Reward: its level in EXP + 800. Drops **Mud Digger Tooth** (1–3), **Digger Hide** (1–2), 10–15 Mahni Purses

---

## The Seven Colossi

The seven strongest Unique Monsters in the world of Shangri-La Frontier. Four are in the pack; three are planned.

| # | Colossus | In the pack |
|---|---|---|
| 1 | **Wethermon the Tombguard** | Yes |
| 2 | **Lycagon the Nightslayer** | Yes |
| 3 | **Ctarnidd of the Abyss** | Yes |
| 4 | **Siegwurm the Sky Ruler** | Yes |
| 5 | **Goldhuneenay the Inexhaustible** | Planned |
| 6 | **The Orchestra of the Doom Echo** | Planned |
| 7 | **Vysache the Undying** | Planned |

The Colossi in the pack appear near players by chance, rolled once a minute, when the place, the time and the
player's level fit. One of each exists at a time; each shows a boss bar within 64 blocks. Health is 4 × level. Every Colossus is above level 100, so beating one at level 99 reaches 99 Extend.
Killing one gives its level in EXP **+ 2,400** and counts as a Knight Trial. Meeting one gives 20 stat points and
defeating one gives 200 (see [Stat points](#stat-points)).

Their bodies are **stand-ins**: a data pack can only reshape vanilla creatures, so each Colossus borrows the
closest one until it gets a proper model.

| Colossus | Appears | Player level | Level | Stand-in body | Drops (from the series) |
|---|---|---|---|---|---|
| **Ctarnidd of the Abyss** | Swimming in a deep ocean | 40+ | 110 | Giant elder guardian | Tome of Truth: Abyss Edition and Abyssal Warning Bell (everyone who fought); one of Ctarnidd's eight grails each |
| **Lycagon the Nightslayer** | Open sky at night | 50+ | 115 | Giant black wolf, always hunting | Lycagon's Fang |
| **Siegwurm the Sky Ruler** | Open sky above y=150 | 55+ | 120 | Giant ghast | — |
| **Wethermon the Tombguard** | The Nether | 60+ | 125 | Wither skeleton | Tome of Truth: The Tombguard and the Inventoria Key (everyone who fought); the Seiten Skillbook, the Non-Standard Ether Reactor and the Brooch of Faraway Prayer |

Lycagon leaves at dawn without dropping anything. The vanilla bosses still count as boss kills too.

**Ctarnidd's grails** — each invert or nullify something for the one who holds it:

| Grail | Effect |
|---|---|
| Blue | Inverts the avatar's gender (genderless characters are unaffected) |
| Green | Inverts colours: photo-negative sight for everyone nearby |
| Indigo | Swaps the values of two random stats |
| Purple | Inverts damage and healing: taking damage heals, healing hurts |
| Red | Nullifies damage from attacks made within 10 blocks |
| Orange | Nullifies damage from attacks made beyond 10 blocks |
| Yellow | Nullifies physical damage |
| Chartreuse | Nullifies magic damage |

---

## Quests

The series skips Firstia, so its quests, people and town lore are this project's own. Secondil's quests and
Garren's questline are original too.

Talk to an NPC by right-clicking it. A quest offer comes with an **[Accept]** button, and **[Quests]** in the menu
shows your progress. Each player gets their own camp or search site for quests that need one; chat gives its
coordinates.

### Firstia — side quests

| Quest | From | What you do | Reward |
|---|---|---|---|
| A Pioneer's Awakening | Town Elder | Talk to the Local Alchemist, then gather 5 **Wild Herbs** (from cutting grass and ferns) | 50 EXP, 3 Basic Health Potions |
| Clearing the Outskirts | Guard Captain | Defeat 5 Goblins | 100 EXP, Starter Iron Dagger, 20 Mahni |
| The Brute Threat | Guard Captain | Defeat 2 Orcs | 150 EXP, Beginner Leather Chestplate, 40 Mahni |

### Firstia — main quests

| Quest | From | What you do | Reward |
|---|---|---|---|
| The Missing Herd | Distressed Farmer | Beat the goblin raiders at their camp, talk to the Farmer's Daughter to free her, lead the 3 cows home | 120 EXP, Fresh Milk Bundle, 30 Mahni |
| The Serpent's Shadow | Distressed Farmer | Speak with the Guard Captain | 50 EXP |
| The Rampant Forest Guardian | Guard Captain | Defeat the Ravenous Snake | 300 EXP, Devourer's Scale, Python White Hair, 100 Mahni |
| Secondil Supply Delivery | Distressed Farmer | Carry the Sealed Beef Package to Garren in Secondil | 250 EXP, Basic Armor Piece, 50 Mahni |

### Secondil

| Quest | From | What you do | Reward |
|---|---|---|---|
| A Soft Bed at Last | Innkeeper Marrow | Lie in a bed: it registers your respawn point | 75 EXP, Secondil Stew |
| Antidote Run | Lysa | Carry 3 Antidote Bundles to Marrow | 100 EXP, 2 Antidotes, 30 Mahni |
| The Night Watch | Guard Halvor | At night, stand watch near Halvor for 45 seconds. Redcaps appear at the tree line — **do not attack them**, or the watch starts over | 125 EXP, Guard Issue Cloak, 40 Mahni |
| Bar Talk | Old Borric | Hear three stories, then tell the Bartender whether the marsh story is true | 60 EXP, Strong Ale, 20 Mahni |

### Garren's questline

Opens after the beef delivery or The Night Watch.

| Quest | What you do | Reward |
|---|---|---|
| The Iron Pickaxe | Bring back 5 raw iron | 200 EXP, Basic Iron Chestplate, 75 Mahni |
| Splitblade Set | Bring 4 Mud Frog Skins | 250 EXP, Splitblade leather set, 50 Mahni |
| The Missing Miner | Find **Tomic's Journal** at his dig site and bring it to Garren | 300 EXP, Iron Pickaxe (Reinforced), 100 Mahni |
| Red Hoods in the Reeds | Show the journal to Halvor; at night, lead two Secondil Guards against a Redcap camp (two waves) and bring back its banner | 400 EXP, Redcap Iron Axe, 125 Mahni |
| Path to Thirdrema | Defeat the Mud Digger | 500 EXP, Garren's Plated Vambraces, 200 Mahni |

---

## Mahni and shops

**Mahni** is the currency. Monsters drop **Mahni Purses** worth 10 each; a purse turns into Mahni the moment you pick
it up. Quests pay Mahni too.

| Shop | Sells |
|---|---|
| Lysa (florist) | Antidote 15 (cures poison), Basic Health Potion 20 |
| The Bartender | Strong Ale 10 (a minute of Strength), Secondil Stew 5 |

Talk to the shopkeeper and click an item.

---

## The Diremarsh

Swamps and mangrove swamps are the Diremarsh.

- **The walking state:** standing on marsh ground roots one leg in the mud: −40% movement and −40% jump. Rock, logs
  and planks free you, so fight from high ground. This applies in the Mud Digger fight
- **Splitblade leather resists slashes:** it reduces the damage you take from slash attacks

---

## Origins

New players choose an origin before their class. The series has eight origins. The pack has two of them today:
**Average Joe**, the ordinary start in Firstia with its people and quests, and the **Wanderer**. Their NPC effects,
and the other six origins, need NPC affinity (how much each NPC likes you), which the pack doesn't have yet.

| Origin | Japanese | Effect | In the pack |
|---|---|---|---|
| **Wanderer** | 彷徨う者 (Samayō Mono) | Hard mode: start alone in the wilds (see below) | Yes |
| **Guiding Blood** | 尊き血 (Tōtoki Chi) | NPCs start out liking you more, but NPCs with high Karma target you more often | Planned |
| **Private Hero** | 在野の雄 (Zaiya no Yū) | Clearing a quest raises NPC affinity more; the more quests you clear, the further your name spreads among NPCs | Planned |
| **Beast Child** | 獣の子 (Kemono no Ko) | Moves better in natural areas; starts in an exploration area | Planned |
| **Average Joe** | 凡民 (Bonmin) | NPCs are less wary of you, by the same amount at every level. Starts in Firstia | Yes (the effect is planned) |
| **Swordsman** | 剣客 (Kenkaku) | NPCs like you more while you carry a sword or katana; special rules for who can accept some quests | Planned |
| **Optimist** | 楽天家 (Rakutenka) | NPC affinity shifts with your HP and MP percentages and with how you act | Planned |
| **Bluffer** | 一見の実力者 (Ichigen no Jitsuryoku-sha) | NPC affinity changes with the rank of your equipment | Planned |

The **Swordsman** origin is not the Swordsman class.

### The Wanderer's Path

The **Wanderer** is hard mode — the path Sunraku chose — and cannot be undone.

- **Traits:** +2 Luck (better drops) and −10% armour, permanently
- **Start:** a random spot in a forest, alone. Firstia's people turn away strangers from the wilds
- **The Dream Penalty:** die before you sleep at Secondil's inn (*A Soft Bed at Last*) and you wake in Firstia with
  your level, EXP, Mahni, stat points, skill progress and dropped items gone — it was "only a dream". You keep your
  class, skills and traits, and Firstia is open to you from then on
- **First Survivor:** kill the Ravenous Snake while the penalty is on, then sleep at Secondil's inn. Garren then
  welcomes you with **Fellow Survivor** (150 EXP, 75 Mahni, a full meal) and his questline opens without the delivery
- **The Long Way Back:** return to Firstia as a First Survivor and its people greet you differently. The farmer
  leaves **A Brother's Letter** for Garren (250 EXP, 100 Mahni, Fresh-Baked Bread)

---

## Items and weapons

**[ITEMS.md](ITEMS.md)** lists every item with its icon, stats, description, where it comes from (drop
chances, quest rewards, shop prices) and its give command. It is generated from the packs, so it is always current.
It also marks the 24 items that nothing in survival gives yet.

The **3D weapons pack** has 29 weapons with 3D held models and flat inventory icons, including paired weapons and a
shield that raises when blocking. See [weapons/README.md](weapons/README.md).

---

## For server admins

Everything below needs OP.

### Setting up a world

The towns are not built by the pack, so place the people yourself. Each command places the NPC where you stand,
facing you:

```
/function slf:npc/place/<name>
```

| Town | `<name>` |
|---|---|
| Firstia | `elder`, `alchemist`, `guard_captain`, `farmer` |
| Secondil | `marrow`, `lysa`, `halvor`, `borric`, `bartender`, `garren` |

`/function slf:npc/remove` removes NPCs within 8 blocks.

| Command | What it does |
|---|---|
| `/function slf:wanderer/set_firstia_inn` | Marks where Wanderers wake from the dream |
| `/function slf:wanderer/set_forest` | Marks the Rampant Forest's centre; Wanderers start within 64 blocks |
| `/function slf:altar/place` | Builds the Altar of Awakening four blocks south of you (otherwise it rises on its own) |
| `/function slf:altar/remove` | Retires the altar; a new one rises when someone needs it |
| `/function slf:admin/reset_player` | Wipes your own SLF progress |
| `/function slf:setup` | Re-registers the scoreboards (safe at any time) |

### Spawning and giving

```
/function slf:mob/<mob>/spawn          goblin, red_hat_goblin (Redcap), orc, mud_frog, vorpal_bunny
/function slf:mob/boss/<boss>/spawn    ravenous_snake, mud_digger, lycagon, ctarnidd,
                                       siegwurm, wethermon
/function slf:give/<item>              any item (tab completion lists them)
/function slf:weapons/give/<weapon>    a 3D weapon (weapons pack)
```

Set a monster's level first with `/scoreboard players set #spawn_lv slf.mob_level <level>`.

### The test menu

`/function slf:test/menu` opens a clickable menu with every tool:

| Row | What it does |
|---|---|
| Items | Kits of weapons, armour, skill books and materials; the 3D weapons; clear inventory |
| Class | One button per class: resets you, then grants the whole lineage at the level it needs |
| Level | Set your level, jump to 99 (99 Extend), +1,000 EXP, record a boss kill |
| Stats | +10 points, every stat to 20 or 0, fill mana |
| Skills | Learn every skill, finish the one you are focusing, +1 Knight Trial |
| World | Karma 100 or 0, place or remove the altar, an Altar Compass |
| Mobs | Spawn each monster; remove SLF mobs nearby |
| Bosses | Spawn each area boss and boss; set midnight (full moon) or morning |
| NPCs / Secondil | Place each NPC; 5 Wild Herbs; the quest log |
| Origin | The origin choice; become a Wanderer; set Firstia's inn and the forest |
| Me | Status sheet, +100 Mahni, the player menu, reset yourself |

---

## For contributors

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for naming conventions, how to add a skill, class or item, and the
scoreboard reference.

### Layout

| Path | What it holds |
|---|---|
| `data_pack/` | The game logic, all in `data/slf/` (`function/`, `advancement/`, `loot_table/`, `tags/`) |
| `resource_pack/` | Models, textures and names |
| `weapons/` | The 3D weapons packs and the scripts that build them |
| `tools/` | Generators (below) |
| `tests/` | File checks, and `tests/live/` for tests on a real server |

### Generated files

Edit the generator, not its output. A test fails while an output is out of date.

| Generator | Writes |
|---|---|
| `tools/gen_test_commands.py` | Give commands, kits, class setups and the test menu |
| `tools/gen_item_docs.py` | `ITEMS.md` |
| `tools/gen_mob_models.py` | Mob bodies and heads, and the newer item icons |
| `tools/gen_skill_passives.py` | Skill bonuses and `SKILL_EFFECTS.md` |
| `tools/gen_item_textures.py` | The flat item textures (placeholders: hand-made pixel art is very welcome) |
| `weapons/tools/java_build.py` | Everything under `weapons/java_out/` |

### Tests

```
python -m unittest tests/test_datapack.py tests/test_resource_pack.py tests/test_test_suite.py
```

These read files only and take seconds. `tests/live/` starts a real 26.2 server, logs a real player in and plays
through the pack (127 tests, about 8 minutes); see [tests/live/README.md](tests/live/README.md).

---

## Planned

Described in the design or the lore, but not built yet:

- **Thirdrema** and everything beyond it
- **More jobs:** the craft lines (Blacksmith → Master Craftsman, the hidden Ancient Craftsman → Divine Craftsman),
  the hidden Revenger, the Magic Archer, and the hidden **Mastermind** (全能たる叡智, "Omnipotent Wisdom"), which
  follows Sage; open slots in the class tree are kept for hidden and craft jobs
- **The class rework:** the pack moves from its older 34-class list to the tree in [Classes](#classes)
- **The Skill Garden** (combining two skills into a new one, run by Skill Gardeners such as Elke; Firstia's tutorial
  introduces it), skill levels I–X, and skill evolution chains
- **The six other origins** (Guiding Blood, Private Hero, Beast Child, Swordsman, Optimist, Bluffer) and the NPC
  affinity they and Average Joe need
- **Vorpal Soul gates** for heroic skills, and karma affecting how NPCs treat you
- **Arcanum** (神秘): at level 99, Arcanoom, the Monk of Awakening, offers you a card of the Major Arcana — a
  sub-job that raises your stats with a penalty, chosen by how you have played (The Fool: halved skill recast, but
  healing items may fail and debuffs hit twice as hard)
- **Race conversion** in the Altar of Awakening's lower floor (elf, fishfolk, beastfolk, birdfolk, insectfolk,
  dwarf, giant), each with its own stat boost
- **Goldhuneenay the Inexhaustible**, **the Orchestra of the Doom Echo** and **Vysache the Undying**
- The Colossi's drops from the series: the Tomes of Truth, the Inventoria Key, the Non-Standard Ether Reactor, the
  Brooch of Faraway Prayer, the Abyssal Warning Bell and Ctarnidd's grails; and real models in place of the stand-ins
- **The Ravenous Serpent Spear** (貪食の蛇槍), a poison spear made from the Ravenous Snake's materials
- **Shop armour from the series:** the Mercenary's Helm (傭兵の兜), the Snakeskin set (蛇革) and the Hard Chain set,
  and the Stone Shield
- **Crescent Blade** (formerly Bilac's Crescent Blade) sold in a shop in another town
- Survival sources for the 24 items marked in the catalogue
- Balance: every number in the pack is a first pass
