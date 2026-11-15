# SLF Weapons

Nine Shangri-La Frontier weapons as 3D held models with flat inventory icons, for Minecraft Java **26.2** (resource pack format 88, data pack format 107). They ship as their own resource pack + data pack, separate from the main SLF.Mine packs, and can be loaded alongside them.

| Weapon | Base item | Notes |
|---|---|---|
| Wood Staff | stick | |
| Iron Hammer | stick | |
| Iron Sword | iron sword | |
| Iron Dagger | iron sword | single weapon |
| Marsh Daggers | iron sword | pair |
| Mercenary's Blades | iron sword | pair (placeholder name) |
| Vorpal Choppers | iron sword | pair (placeholder name) |
| Fossil Rod | stick | |
| Wood Shield | shield | raises when blocking |

Still to make: Stone Staff, Iron Spear.

## Install

- `java_out/SLF_Weapons_ResourcePack/` → `.minecraft/resourcepacks/`
- `java_out/SLF_Weapons_Datapack/` → `<world>/datapacks/`

Then in game (needs cheats/OP):

```
/function slf:weapons/give_all
/function slf:weapons/give/<name>
```

`<name>` is one of `wood_staff`, `iron_hammer`, `iron_sword`, `iron_dagger`, `marsh_dagger`, `mercenary_blade`, `vorpal_chopper`, `fossil_rod`, `wood_shield`.

## How it works

- **No CustomModelData.** Each weapon is a vanilla base item with the `item_model` component pointing at `assets/slf/items/<name>.json`. That definition switches on `display_context`: the inventory (`gui`) shows a flat pixel icon, everything else shows the 3D model.
- **Pairs are one item.** While a paired weapon is in the main hand and the off hand is empty, `slf:weapons/pairs/tick` puts a display-only twin in the off hand. The twin is removed when you switch away, and dropped twins are deleted.
- **Shield.** `wood_shield` switches to a second model while in use (`minecraft:using_item`), the same way the vanilla shield does.
- The data pack adds its own `data/minecraft/tags/function/tick.json`. Function tags merge across packs, so it coexists with the main data pack. If these files are ever merged *into* the main data pack, combine the two `tick.json` files rather than overwriting one.

## Rebuilding

Everything under `java_out/` is generated. Do not edit it by hand; edit the scripts and rebuild.

```
cd weapons/tools
python java_build.py
```

Needs Python 3 with `numpy` and `Pillow`. The build deletes and recreates `java_out/` (the `.zip` files it also writes are git-ignored).

| File | Purpose |
|---|---|
| `tools/mp.py` | Model definitions (cube lists per weapon), texture atlas palettes and patterns, icon renderer. Edit weapons here. |
| `tools/java_build.py` | Builds the resource pack and data pack. Hand poses, blade facing and the shield's blocking pose are computed here. |
| `tools/java_preview.py` | Renders the built models through the game's first-person hand camera, so hand poses can be tuned without reloading the game. `python java_preview.py out.png iron_sword iron_hammer` |
| `tools/sprites.py` | Older 2D sprite code; `mp.py` still imports it. |

Icons are rendered from the models, and a few edge pixels can differ between operating systems (float rounding). That is cosmetic; avoid committing icon-only churn.

### Settings worth knowing in `java_build.py`

- `EDGE_DOWN` — weapons that are turned over so the model's +x side (the sharp edge) faces down in the hand. Default is +x up.
- `FP_TILT`, `FP_YAW`, `FP_SHIFT_X` — first-person hold, relative to vanilla's handheld pose. Kept close to vanilla on purpose: bottom right of the screen, leaning outward. Pure vanilla values push long 3D models off the screen edge; much larger values make weapons lean in toward the crosshair.
- Left-hand poses are written explicitly for every weapon. Without them the game reuses the right-hand pose with part of the rotation negated, which turns an off-hand blade over. The shield is the exception: it is symmetric left-to-right rather than front-to-back, so it keeps the game's fallback.
- `SHIELD_VANILLA` — vanilla 26.2 shield poses (copied from the client jar). The blocking pose applies vanilla's normal-to-blocking motion on top of our normal hold, so retuning the normal hold moves the blocking pose with it.

## Style

MinePiece-like: chunky angled blocks, big flat-colour texels, banded handles, bold two-tone palettes, diamond-shaped accents. Thin parts, angled curve segments and stepped shapes are intentional. Colour ramps are hue-shifted, there is no random speckle noise, and outlines are tinted per weapon rather than black.

## Status

Tested in game on 26.2 (third person, first person, paired weapons in both hands, shield blocking). Third-person hand positions are calculated from vanilla's sword pose at about 1.3× size and have not needed tuning so far.
