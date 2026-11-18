# Pack fixes: bringing the packs in line with the README

The README was reviewed line by line against the source material (the Japanese and English SLF wikis). This
checklist is everything the data pack, resource pack and weapons pack still need to match it. Work through it in
order, one tested commit per step, then delete this file.

Naming rule: official English (anime) names. For skills and items, the katakana reading when the source gives one,
otherwise the Japanese romanized. The project keeps **Wethermon** (the wiki's "Wezaemon").

## 1. Remove the fake bosses and invented items

- [x] Bosses: Nightclaw, Oriana the Uncrowned, Bilac the Full Moon Fangs — `function/mob/boss/{nightclaw,oriana,bilac}/`,
      spawn rolls, loot tables, advancements, test-menu buttons
- [x] Weapons: Nightclaw Talon, Oriana's Scepter, Oriana's Void Staff, Wethermon's Scythe, Wethermon's Rib Dagger,
      Lycagon's Fang, Vorpal Knife, Bilac's Fang Gauntlet, Sunraku's Blades (L/R), Sunraku's Chaos Rod (no source)
- [x] Wethermon's Blade: only Wethermon wields it — not obtainable by players
- [x] Bilac's Crescent Blade → **Crescent Blade**, unlinked from any boss (later: sold in a shop in another town)
- [x] Armour: the Tombguard set (4 pieces), the Fullmoon Chestplate
- [x] Items: Solo Killer's Trophy (and `mob/boss/mud_digger/solo.mcfunction`), Unique Monster Core
- [x] Skill books dropped by the Colossi: Reflexus, Gravity Zero, Managarm Pride, and the Acrobat book. The skills
      themselves stay (they are real)

## 2. Monster and Colossus drops and levels

- [x] Vorpal Bunny: Vorpal Choppers 5% (now 4%), **Rabbit Neckband** (兎の首巻布, new item) 12% (the knife and Acrobat
      book are already gone)
- [x] Ravenous Snake: add the guaranteed **Ravenous Fang** (貪食の牙); keep Devourer's Scale (喰蛇の鱗) and Python
      White Hair (喰蛇の白髪)
- [x] Solo Killer's Trophy removed (step 1)
- [x] Mud Digger phase 2: the burst targets a **random** player (it already did, with `@r`)
- [x] Colossi levels: Ctarnidd 110, Lycagon 115, Siegwurm 120, Wethermon 125
- [x] Colossus drops per the README (Tome of Truth, Inventoria Key, Seiten Skillbook, …) — the ones not yet built
      stay in Planned

## 3. Levels and stats

- [x] Standby → **99 Extend**: at 99, killing a **level 100+ monster** (not "any boss") banks EXP
- [x] Stat points: 5 a level, +50 on reaching 99, 10 a level after 99 (remove the +2 every tenth level);
      +20 the first time you meet each Colossus (UME), +200 for defeating one (UMB)
- [x] LCK → **LUC**; clench at 50+ (a data pack can't tell self-inflicted damage apart, so at 50+ the existing LUC save
      always triggers instead of being a LUC% chance)

## 4. Origins and the Diremarsh

- [x] Origin Citizen → **Average Joe** (`wanderer/become_citizen`, `origin_menu`, `origin`, `dream`, setup, test menu)
- [x] Splitblade (`marsh/slashed.mcfunction`): reduce slash damage taken instead of healing (a new `slf:splitblade` armour
      enchantment: 12% less damage from swords and axes per piece); the set stays 4 pieces
      (Mask, Vest, Pants, Boots — the boots stand in for the source's belt)

## 5. Skills (`tools/gen_skill_passives.py`, `skills/learn|focus/*`, lang)

Display names only: the skill ids (tags like `slf.skill.manbufu`) stay, so players keep the skills they have.

- [x] Renames:
      After All Unyo → Hikkyō Un'yō · Causal Accumulation → Retaliate · Chanting And Memorizing → Chant Memorization ·
      Desperate Sting → Fatal Sting · Embrace Of Devil → Embrace of the Karmic Demon · Gobus Courage → Gōbu Funtan ·
      Grapple Train → Grapple Drain · Hate Trumple → Hate Trample · Hegemony World → Hadan Seikai ·
      Hundred Sounding → Hundred Beat · Iggist Requiem → Exist Requiem · Inexhaustible Beasts → Jūō Mujin ·
      Instant Vision → Moment Sight · Kings Silver Arm → Nuada Airgetlám · Lash Slash → Rush Slash ·
      Limit Break Rees → Limit Break Race · Lion Fall → Shishi-otoshi · Manbufu → Banbu Futō ·
      Masakuru Byte → Massacre Bite · Paring Protect → Parrying Protect · Rechette Step → Ricochet Step ·
      Rigid Strength → Gōriki Jūku · Sword God Danba → Kenshin Danpa · Sword Of Rough Waves → Aranami no Tachi ·
      Tanda Breathing → Tanden Breathing · Terraton Corapsa → Teraton Collapsar ·
      Total Body Takeshi → Full Body Parrying · Tsujizanri → Tsujigiri · Wisdoms Divine Eye → Odin's Surpr-Eyes ·
      Zanzui Flying Blade Leg → Gettoment Blaster · Breath Of Anti Harm → Breath of Resistance
- [x] Made-up skills replaced with real ones (same effect): Blaze Shot → Bloodburn Burst, Bradion → Accel,
      Break Attack → Power Straight, Holy Shield → Spirit of Guardian, Iron Skin → Futō Fukutsu,
      Shield Bashing → Raging Shield
- [x] Remove Grand Tantrum; Big Tantrum (大癇癪) draws nearby monsters instead of the mana toggle

## 6. Weapons

- [x] One entry per weapon in ITEMS.md (a weapon in both packs is listed once, with both give commands); Whalelore is now
      one paired weapon in the 3D pack, like Togetsu; Empire Bee Twinblade → Empire Bee Twin
- [x] Official names: Togetsu 兎月 [Waxing 上弦 / Waning 下弦] → evolves into **Whalelore** 勇魚兎月 [Gold Sheen 金照 /
      Nether Light 冥輝; joined: Pale Sheen 蒼耀月] (fix "Goldsheen/Netherlight"); Marsh Daggers 湖沼の短剣 → evolves into
      Ducusram 傑剣への憧刃; Vorpal Choppers 致命の包丁; Vorpal Sledge 致命の大鎚; Blue Predator 海喰の剣;
      General Dullahan's Decapitator 喪失骸将の斬首剣 (reforged: Flame General's Decapitator); Empire Bee Twinblade 帝蜂双剣;
      Holy Spear Caledfwlch; Dis Pater 冥王の鏡盾; Zanbaralia 黒兇槍ザンバラリア; Giant-Killing Skewer 巨人殺し・串刺し;
      Fossil Rod 化石のロッド; Super Cat-Teaser Lv.100; Antinomy 神魔の大剣; Slaughter Bringer 殺戮者の魔剣;
      Gilta Brille 煌蠍の籠手
- [x] Rust Saber stays, marked as the project's own

## 7. The class rework

- [ ] Move from the old 34-class list to the tree in the README's Classes section (8 starting classes + Knight,
      Warlord as the Mercenary's top job, hidden/specialty jobs, unlock levels 20 / 30 / 50 / 70 / 80)
- [ ] Old → new: Warrior → Fighter, Fighter → Brawler, Bandit → Thief (Bandit becomes Master Thief), Mage → Magician,
      Kansei → Master Swordsman, Crazy Fist → Berserker, Killing Joke → Killing Joker, Star Shinobi Sei → Sacred Star
      Ninja; removed: Black Death, King's Knight, Spirit Fist, Saint (from Bishop), Omnipotent Wisdom (planned)

## 8. ITEMS.md

- [x] `tools/gen_item_docs.py`: mark the project's own items with `*` and add a legend line (Rust Saber, Garren's
      Plated Vambraces, Mud Digger Tooth, Digger Hide, Age of Divinity Memory, the consumables and quest items)
- [ ] Regenerate everything (`gen_test_commands.py`, `gen_skill_passives.py`, `gen_item_docs.py`) and run the tests
- [ ] Update the README's admin and contributor sections for the changed commands; delete this file
