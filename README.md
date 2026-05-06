# SLF.Mine — Shangri-La Frontier Resource & Data Pack

A Minecraft 1.21.x pack bringing weapons, armor, skills, and quest advancements from the anime **Shangri-La Frontier**.

## Installation

### Resource Pack
1. Copy the `resource_pack/` folder (rename/zip it as desired) into `.minecraft/resourcepacks/`
2. Enable it in **Options → Resource Packs**

### Data Pack
1. Open your world's save folder
2. Copy the `data_pack/` folder into `<world>/datapacks/`
3. Run `/reload` in-game

> Both packs must be active together for full functionality.

---

## Item List

| CMD String | Display Name | Base Item | Category |
|---|---|---|---|
| `slf.wethermon_scythe` | Wethermon Bone Scythe | Netherite Sword | Boss Weapon |
| `slf.wethermon_rib_dagger` | Wethermon Rib Dagger | Iron Sword | Boss Weapon |
| `slf.bilac_crescent_blade` | Bilac Crescent Blade | Netherite Sword | Boss Weapon |
| `slf.bilac_fang_gauntlet` | Bilac Fang Gauntlet | Golden Sword | Boss Weapon |
| `slf.oriana_scepter` | Oriana Scepter | Diamond Sword | Boss Weapon |
| `slf.oriana_void_staff` | Oriana Void Staff | Diamond Sword | Boss Weapon |
| `slf.nightclaw_talon` | Night Claw Talon | Netherite Sword | Boss Weapon |
| `slf.sunraku_blade_r` | Sunraku's Right Blade | Iron Sword | Player Weapon |
| `slf.sunraku_blade_l` | Sunraku's Left Blade | Iron Sword | Player Weapon |
| `slf.sunraku_chaos_rod` | Chaos Rod | Golden Sword | Player Weapon |
| `slf.helmet_tombguard` | Tombguard Helmet | Netherite Helmet | Armor |
| `slf.chestplate_tombguard` | Tombguard Chestplate | Netherite Chestplate | Armor |
| `slf.leggings_tombguard` | Tombguard Leggings | Netherite Leggings | Armor |
| `slf.boots_tombguard` | Tombguard Boots | Netherite Boots | Armor |
| `slf.chestplate_fullmoon` | Full Moon Chestguard | Diamond Chestplate | Armor |
| `slf.skill_slash` | Skill: Slash | Enchanted Book | Skill |
| `slf.skill_thrust` | Skill: Thrust | Enchanted Book | Skill |
| `slf.skill_blade_rush` | Skill: Blade Rush [FUSED] | Enchanted Book | Fused Skill |
| `slf.skill_moonhowl` | Skill: Moon Howl [FUSED] | Enchanted Book | Fused Skill |
| `slf.skill_void_lance` | Skill: Void Lance [FUSED] | Enchanted Book | Fused Skill |
| `slf.unique_core` | Unique Monster Core | Book | Material |

---

## Skill Fusion

Combine skills at the crafting table using a **Nether Star** as the fusion catalyst:

| Fused Skill | Recipe Pattern | Reagent |
|---|---|---|
| **Blade Rush** | Enchanted Book + Nether Star + Enchanted Book | Blaze Powder |
| **Moon Howl** | Enchanted Book + Nether Star + Enchanted Book | Phantom Membrane |
| **Void Lance** | Ender Pearl + Nether Star + Ender Pearl (cross pattern) | — |

---

## Advancements

Open the Advancements screen (`L`) and look for the **Shangri-La Frontier** tab.

Advancement tree:
```
Shangri-La Frontier (root)
├── Rookie Gear — craft Sunraku's right blade
│   └── Dual Fangs — hold both Sunraku blades
├── The Tombguard Awaits — obtain any Tombguard armor piece
│   └── Gravedigger — obtain the Wethermon Bone Scythe
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

## Give Functions (Creative)

```
/function slf:give/wethermon_scythe
/function slf:give/bilac_crescent_blade
/function slf:give/oriana_scepter
/function slf:give/sunraku_blade_r
/function slf:give/sunraku_blade_l
```

## Loot Tables

```
/loot give @s loot slf:wethermon_drops
/loot give @s loot slf:bilac_drops
/loot give @s loot slf:oriana_drops
/loot give @s loot slf:nightclaw_drops
```

---

## Pack Format Compatibility

| MC Version | Resource Pack | Data Pack |
|---|---|---|
| 1.21.0 – 1.21.1 | 34 | 48 |
| 1.21.2 – 1.21.3 | 42 | 57 |
| 1.21.4 | 46 | 61 |

---

## Textures

Current textures are **placeholder solid-color PNGs**. Proper 16×16 pixel art is welcome as contributions — see `resource_pack/assets/slf/textures/item/` for the files to replace.

## Contributing

PR welcome for:
- Proper pixel art textures
- Additional SLF items (Pencilgon gear, Emul weapons)
- Armor layer textures (worn armor on player model)
- Sound effects
