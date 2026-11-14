"""
Mob look models for the resource pack: the Goblin / Redcap Goblin head and the goblin's stone axe.

SLF mobs are vanilla creatures (a data pack can't add creature types). A goblin is a small zombie whose head slot holds
an item with item_model slf:goblin_head: the client draws that 3D model over the zombie's head (any item in the head
slot is drawn there, and it also stops the zombie burning by day). The tunic and bandages are dyed leather armour, set
in data_pack/.../mob/goblin/convert.mcfunction.

Writes:
  resource_pack/assets/slf/textures/item/{goblin_head,goblin_axe}.png
  resource_pack/assets/slf/models/item/{goblin_head,red_hat_goblin_head,goblin_axe}.json
  resource_pack/assets/slf/items/{goblin_head,red_hat_goblin_head,goblin_axe}.json

Run: python tools/gen_mob_models.py
"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
RP = ROOT / "resource_pack" / "assets" / "slf"

# ---------------------------------------------------------------- palette (from the anime reference)
SKIN, SKIN_D, SKIN_DD = (110, 115, 80), (88, 93, 62), (66, 70, 46)
WHITE, RED, PUPIL, MOUTH, FANG = (236, 232, 222), (170, 28, 24), (40, 12, 10), (48, 30, 28), (240, 238, 228)
HAT, HAT_D = (168, 36, 30), (120, 24, 20)
WOOD, WOOD_D, STONE, STONE_D, STONE_L, ROPE, ROPE_D = (110, 76, 46), (82, 56, 34), (150, 150, 146), (112, 112, 108), (196, 196, 190), (194, 168, 120), (150, 126, 86)


def head_texture():
    """32x32: four 16x16 tiles. (0,0) face, (16,0) skin, (0,16) ear, (16,16) red hood cloth."""
    im = Image.new("RGBA", (32, 32), SKIN + (255,)); px = im.load()
    def put(x, y, c): px[x, y] = c + (255,)
    # skin tile: mottled
    for x in range(16, 32):
        for y in range(0, 16):
            if (x * 7 + y * 13) % 11 == 0: put(x, y, SKIN_D)
            if (x * 5 + y * 3) % 17 == 0: put(x, y, SKIN_DD)
    # face tile
    for x in range(16):
        for y in range(16):
            if (x * 7 + y * 13) % 13 == 0: put(x, y, SKIN_D)
    for x, y in ((7, 2), (8, 2), (7, 3), (8, 3), (6, 1), (9, 1)): put(x, y, SKIN_DD)       # forehead mark
    for x in range(2, 7): put(x, 4 + (x - 2) // 3, SKIN_DD)                                 # angry brows
    for x in range(9, 14): put(x, 5 - (x - 9) // 3, SKIN_DD)
    for ex in (2, 9):                                                                        # eyes: white, red iris, dark pupil
        for x in range(ex, ex + 5):
            for y in range(6, 9): put(x, y, WHITE)
        for x in range(ex + 1, ex + 4): put(x, 7, RED)
        put(ex + 2, 6, RED); put(ex + 2, 8, RED); put(ex + 2, 7, PUPIL)
        for x in range(ex, ex + 5): put(x, 9, SKIN_D)                                        # lower lid shadow
    put(6, 10, SKIN_DD); put(9, 10, SKIN_DD); put(7, 11, SKIN_D); put(8, 11, SKIN_D)        # snout and nostrils
    for x in range(3, 13): put(x, 12, MOUTH)                                                 # wide grin
    put(2, 11, MOUTH); put(13, 11, MOUTH)
    for x in (4, 11): put(x, 13, FANG)                                                       # fangs
    for x in (6, 9): put(x, 12, FANG)
    for x in range(4, 12): put(x, 14, SKIN_D)                                                # chin
    # ear tile: skin rim, darker inner ear
    for x in range(0, 16):
        for y in range(16, 32):
            if 3 <= x <= 12 and 19 <= y <= 28: put(x, y, SKIN_D)
            if 5 <= x <= 10 and 21 <= y <= 26: put(x, y, SKIN_DD)
    # hat tile: red cloth with folds
    for x in range(16, 32):
        for y in range(16, 32):
            put(x, y, HAT_D if (x + y) % 7 == 0 or y in (20, 27) else HAT)
    return im


def axe_texture():
    """16x16: (0,0)-(7,15) wood, (8,0)-(15,7) stone, (8,8)-(15,15) rope."""
    im = Image.new("RGBA", (16, 16), WOOD + (255,)); px = im.load()
    def put(x, y, c): px[x, y] = c + (255,)
    for x in range(8):
        for y in range(16):
            if x in (0, 7) or (y * 3 + x) % 9 == 0: put(x, y, WOOD_D)
    for x in range(8, 16):
        for y in range(8):
            put(x, y, STONE_L if (x + y) % 5 == 0 else STONE_D if (x * y) % 7 == 3 else STONE)
        for y in range(8, 16):
            put(x, y, ROPE_D if (x + y) % 3 == 0 else ROPE)
    return im


# ---------------------------------------------------------------- models
def faces(uv_all, overrides=None):
    f = {d: {"uv": list(uv_all), "texture": "#0"} for d in ("north", "east", "south", "west", "up", "down")}
    for d, uv in (overrides or {}).items(): f[d] = {"uv": list(uv), "texture": "#0"}
    return f


FACE, SKIN_UV, EAR_UV, HAT_UV = (0, 0, 8, 8), (8, 0, 16, 8), (0, 8, 8, 16), (8, 8, 16, 16)


def ear(side):
    """Long pointed ear, three tapering steps, tilted up 22.5 degrees. side = +1 (east) or -1 (west)."""
    steps = [(6, 5.0), (4, 3.0), (3, 1.5)]   # (length, height) from the head outwards
    out, x = [], 15 if side > 0 else 1
    origin = [15 if side > 0 else 1, 9, 8]
    for length, h in steps:
        x0, x1 = (x, x + length) if side > 0 else (x - length, x)
        y0 = 9.5 - h / 2
        out.append({"from": [x0, y0, 7.5], "to": [x1, y0 + h, 8.5],
                    "rotation": {"angle": 22.5 * side, "axis": "z", "origin": origin},
                    "faces": faces(SKIN_UV, {"north": EAR_UV, "south": EAR_UV})})
        x = x1 if side > 0 else x0
    return out


def head_model(red_hat):
    els = [{"from": [1, 1, 1], "to": [15, 15, 15], "faces": faces(SKIN_UV, {"north": FACE})}] + ear(1) + ear(-1)
    if red_hat:
        # Redcap Goblin (design doc V9): "a deep red hood pulled over its head". The hood covers the top, back and sides of
        # the head, overhangs the brow, drapes over the neck and ends in a drooping point; the ears poke through its sides.
        els += [{"from": [0.5, 14.5, 0.5], "to": [15.5, 16, 15.5], "faces": faces(HAT_UV)},           # crown
                {"from": [0.5, 1, 14.5], "to": [15.5, 16, 15.5], "faces": faces(HAT_UV)},             # back
                {"from": [0.5, 2, 1], "to": [1.5, 16, 15.5], "faces": faces(HAT_UV)},                 # west side
                {"from": [14.5, 2, 1], "to": [15.5, 16, 15.5], "faces": faces(HAT_UV)},               # east side
                {"from": [0.5, 13, 0], "to": [15.5, 16, 1.5], "faces": faces(HAT_UV)},                # brow overhang
                {"from": [1.5, -1.5, 13], "to": [14.5, 1, 15.5], "faces": faces(HAT_UV)},             # drape over the neck
                {"from": [5, 15.5, 12], "to": [11, 17.5, 16], "faces": faces(HAT_UV)},                # hood point...
                {"from": [6.5, 16, 15], "to": [9.5, 17.5, 19.5], "rotation": {"angle": -22.5, "axis": "x", "origin": [8, 16.5, 15]}, "faces": faces(HAT_UV)}]  # ...drooping back
    return {"textures": {"0": "slf:item/goblin_head", "particle": "slf:item/goblin_head"}, "elements": els,
            "display": {"head": {"rotation": [0, 0, 0], "translation": [0, 0, 0], "scale": [1, 1, 1]}}}


def axe_model():
    rot = {"angle": -45, "axis": "z", "origin": [8, 8, 8]}
    W, S, R = (0, 0, 4, 16), (8, 0, 16, 8), (8, 8, 16, 16)
    els = [{"from": [7.5, 0, 7.5], "to": [8.5, 15, 8.5], "rotation": rot, "faces": faces(W)},                 # haft
           {"from": [7.3, 1, 7.3], "to": [8.7, 3, 8.7], "rotation": rot, "faces": faces(R)},                  # grip wrap
           {"from": [3.5, 10, 7], "to": [7.5, 15, 9], "rotation": rot, "faces": faces(S)},                    # stone blade
           {"from": [2.5, 11, 7.25], "to": [3.5, 14, 8.75], "rotation": rot, "faces": faces(S)},              # blade edge
           {"from": [7.2, 10.5, 7.2], "to": [8.8, 13.5, 8.8], "rotation": rot, "faces": faces(R)}]            # lashing
    # display copied from vanilla item/handheld so it is held like any axe
    return {"textures": {"0": "slf:item/goblin_axe", "particle": "slf:item/goblin_axe"}, "elements": els,
            "display": {"thirdperson_righthand": {"rotation": [0, -90, 55], "translation": [0, 4, 0.5], "scale": [0.85, 0.85, 0.85]},
                        "thirdperson_lefthand": {"rotation": [0, 90, -55], "translation": [0, 4, 0.5], "scale": [0.85, 0.85, 0.85]},
                        "firstperson_righthand": {"rotation": [0, -90, 25], "translation": [1.13, 3.2, 1.13], "scale": [0.68, 0.68, 0.68]},
                        "firstperson_lefthand": {"rotation": [0, 90, -25], "translation": [1.13, 3.2, 1.13], "scale": [0.68, 0.68, 0.68]},
                        "gui": {"rotation": [0, 0, 0], "translation": [0, 0, 0], "scale": [1, 1, 1]},
                        "ground": {"rotation": [0, 0, 0], "translation": [0, 2, 0], "scale": [0.5, 0.5, 0.5]}}}


ORC, ORC_D, ORC_DD, TUSK, ORC_EYE = (78, 102, 58), (60, 80, 44), (42, 58, 30), (232, 222, 196), (226, 178, 40)


def orc_texture():
    """32x32 like the goblin's: (0,0) face, (16,0) skin, (0,16) ear, (16,16) tusk ivory."""
    im = Image.new("RGBA", (32, 32), ORC + (255,)); px = im.load()
    def put(x, y, c): px[x, y] = c + (255,)
    for x in range(32):
        for y in range(16):
            if (x * 7 + y * 13) % 11 == 0: put(x, y, ORC_D)
    for x in range(1, 15): put(x, 4, ORC_DD); put(x, 5, ORC_D)                               # one heavy brow
    for ex in (3, 9):                                                                         # small mean yellow eyes
        for x in range(ex, ex + 4): put(x, 6, ORC_DD)
        put(ex + 1, 7, ORC_EYE); put(ex + 2, 7, ORC_EYE); put(ex + 1, 7, (30, 20, 10))
    for x in (6, 9): put(x, 9, ORC_DD)                                                        # flat nose
    put(7, 9, ORC_D); put(8, 9, ORC_D)
    for x in range(3, 13): put(x, 12, ORC_DD); put(x, 13, ORC_D)                              # wide jaw, underbite
    for x in range(0, 16):
        for y in range(16, 32):
            if 3 <= x <= 12 and 19 <= y <= 28: put(x, y, ORC_D)
    for x in range(16, 32):
        for y in range(16, 32): put(x, y, TUSK if (x + y) % 6 else (200, 190, 160))
    return im


def orc_head_model():
    """Bigger, squarer head than a goblin's, short ears, two tusks jutting up from the jaw."""
    TUSK_UV = (8, 8, 16, 16)
    els = [{"from": [0.5, 0.5, 0.5], "to": [15.5, 15, 15.5], "faces": faces(SKIN_UV, {"north": FACE})},
           {"from": [3, 0, -0.5], "to": [13, 4, 1], "faces": faces(SKIN_UV)},                                     # jutting jaw
           {"from": [3.5, 3, -1.5], "to": [5, 7, 0], "faces": faces(TUSK_UV)},                                    # tusks
           {"from": [11, 3, -1.5], "to": [12.5, 7, 0], "faces": faces(TUSK_UV)}]
    for side in (1, -1):
        x0, x1 = (15.5, 19.5) if side > 0 else (-3.5, 0.5)
        els.append({"from": [x0, 8, 7.5], "to": [x1, 12, 8.5], "rotation": {"angle": 22.5 * side, "axis": "z", "origin": [15.5 if side > 0 else 0.5, 10, 8]},
                    "faces": faces(SKIN_UV, {"north": EAR_UV, "south": EAR_UV})})
    return {"textures": {"0": "slf:item/orc_head", "particle": "slf:item/orc_head"}, "elements": els,
            "display": {"head": {"rotation": [0, 0, 0], "translation": [0, 0, 0], "scale": [1, 1, 1]}}}


# ---------------------------------------------------------------- the Ravenous Snake (design doc V9, Rampant Forest area boss)
# "Tan-green hardened scales, a light white belly, diamond-shaped crystal-frame yellow eyes, a white flow of hair tied with
# red beads on both sides of its face, and a long lock on its tail which opens like a flower to release a purple ooze."
SN, SN_D, SN_L, BELLY, BELLY_D = (150, 150, 92), (112, 116, 66), (178, 176, 116), (232, 228, 210), (204, 198, 176)
HAIR, HAIR_D, BEAD, POISON, POISON_D, EYE, EYE_D, MOUTH_C = (244, 242, 236), (214, 210, 200), (190, 30, 30), (150, 60, 180), (100, 30, 130), (242, 214, 40), (40, 30, 10), (70, 30, 30)
# texture tiles (uv units; the texture is 32x32, so 1 uv unit = 2 px)
SC_UV, BE_UV, HA_UV, PO_UV, EY_UV, BD_UV, MO_UV = (0, 0, 8, 8), (8, 0, 16, 8), (0, 8, 8, 16), (8, 8, 12, 12), (12, 8, 16, 12), (8, 12, 12, 16), (12, 12, 16, 16)


def snake_texture():
    im = Image.new("RGBA", (32, 32), SN + (255,)); px = im.load()
    def put(x, y, c): px[x, y] = c + (255,)
    for x in range(16):                                                       # scales: offset diamond rows
        for y in range(16):
            put(x, y, SN_D if (x + 2 * (y // 2 % 2)) % 4 == 0 or y % 2 == 0 and x % 4 == 2 else SN_L if (x + y) % 7 == 0 else SN)
    for x in range(16, 32):                                                   # belly plates
        for y in range(16): put(x, y, BELLY_D if y % 4 == 0 else BELLY)
    for x in range(16):                                                       # hair: white strands
        for y in range(16, 32): put(x, y, HAIR_D if x % 3 == 0 else HAIR)
    for x in range(16, 24):
        for y in range(16, 24): put(x, y, POISON_D if (x + y) % 3 == 0 else POISON)
    for x in range(24, 32):                                                   # eye: yellow diamond, dark slit
        for y in range(16, 24): put(x, y, EYE if abs(x - 27.5) + abs(y - 19.5) <= 4 else SN_D)
    for y in range(17, 23): put(27, y, EYE_D); put(28, y, EYE_D)
    for x in range(16, 24):
        for y in range(24, 32): put(x, y, BEAD)
    for x in range(24, 32):
        for y in range(24, 32): put(x, y, MOUTH_C)
    return im


def snake_faces(top=SC_UV, bottom=BE_UV):
    f = faces(top); f["down"] = {"uv": list(bottom), "texture": "#0"}; return f


def snake_head_model():
    """Snout along +z. (An item display shows a model turned 180 degrees, so body.mcfunction turns each part back.)
    Long head, snout, yellow diamond eyes, white hair tied with red beads."""
    els = [{"from": [3, 2, 1], "to": [13, 9, 13], "faces": snake_faces()},                       # skull
           {"from": [4, 2, 13], "to": [12, 7, 18], "faces": snake_faces()},                      # snout
           {"from": [4.5, 1.5, 13], "to": [11.5, 2.5, 17.5], "faces": faces(MO_UV)},            # jaw line
           {"from": [2.5, 6, 9], "to": [3, 8.5, 12], "faces": faces(EY_UV)},                     # eyes
           {"from": [13, 6, 9], "to": [13.5, 8.5, 12], "faces": faces(EY_UV)}]
    for side in (-1, 1):                                                                         # hair flowing back
        x0, x1 = (0.5, 3) if side < 0 else (13, 15.5)
        els += [{"from": [x0, 3, -3], "to": [x1, 8, 8], "faces": faces(HA_UV)},
                {"from": [x0 - 0.3, 4.5, -2.5], "to": [x1 + 0.3, 6.5, -1], "faces": faces(BD_UV)},       # red beads tying the hair
                {"from": [x0 - 0.3, 4.5, 3], "to": [x1 + 0.3, 6.5, 4.5], "faces": faces(BD_UV)}]
    return {"textures": {"0": "slf:item/ravenous_snake", "particle": "slf:item/ravenous_snake"}, "elements": els}


def snake_body_model():
    return {"textures": {"0": "slf:item/ravenous_snake", "particle": "slf:item/ravenous_snake"},
            "elements": [{"from": [3, 2, 2], "to": [13, 10, 14], "faces": snake_faces()},
                         {"from": [7, 10, 4], "to": [9, 11, 12], "faces": faces(SC_UV)}]}            # dorsal ridge


def snake_tail_model():
    """Tapering tail ending in the lock that opens like a flower (purple), pointing along -z."""
    return {"textures": {"0": "slf:item/ravenous_snake", "particle": "slf:item/ravenous_snake"},
            "elements": [{"from": [4, 3, 4], "to": [12, 9, 16], "faces": snake_faces()},
                         {"from": [5.5, 4, -2], "to": [10.5, 8, 4], "faces": snake_faces()},
                         {"from": [6.5, 4.5, -6], "to": [9.5, 7.5, -2], "faces": faces(HA_UV)},
                         {"from": [3.5, 3, -8], "to": [12.5, 9.5, -6], "faces": faces(PO_UV)},      # the flower, open
                         {"from": [5, 1.5, -8.5], "to": [11, 11, -7.5], "faces": faces(PO_UV)}]}


def item_icon(name, draw):
    im = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); draw(im.load()); im.save(RP / "textures" / "item" / f"{name}.png")
    return {"parent": "minecraft:item/generated", "textures": {"layer0": f"slf:item/{name}"}}


def draw_scale(px):
    for x in range(3, 13):
        for y in range(3, 13):
            px[x, y] = (SN_D if x in (3, 12) or y in (3, 12) else SN_L if x + y < 12 else SN) + (255,)


def draw_hair(px):
    for y in range(1, 15):
        for x in range(6 + (y > 8), 10 - (y > 11)):
            px[x + (y // 5) - 1, y] = (HAIR_D if (x + y) % 3 == 0 else HAIR) + (255,)
    for x in range(6, 10):
        for y in (5, 6): px[x, y] = BEAD + (255,)


# ---------------------------------------------------------------- the Mud Digger (design doc V9, Diremarsh area boss)
# "A large chimera with the head, tail, and dorsal fins of a great white shark, the body and limbs of a mole with abnormally
# long legs and webbed feet, and a catfish's whiskers. Dark green with splotches of light green; clear cold blue eyes."
MD, MD_D, MD_L, MD_BELLY, MD_EYE, MD_TOOTH, MD_WHISK = (46, 78, 46), (32, 56, 32), (104, 150, 80), (150, 170, 130), (120, 200, 240), (236, 236, 228), (24, 30, 24)
MD_SKIN, MD_BELLY_UV, MD_EYE_UV, MD_TEETH_UV, MD_WHISK_UV = (0, 0, 8, 8), (8, 0, 16, 8), (0, 8, 4, 12), (8, 8, 12, 12), (12, 8, 16, 12)


def digger_texture():
    im = Image.new("RGBA", (32, 32), MD + (255,)); px = im.load()
    def put(x, y, c): px[x, y] = c + (255,)
    for x in range(16):
        for y in range(16):
            if (x * 5 + y * 3) % 13 < 3 or (x - 9) ** 2 + (y - 5) ** 2 < 5: put(x, y, MD_L)          # light green splotches
            elif (x + y * 7) % 11 == 0: put(x, y, MD_D)
    for x in range(16, 32):
        for y in range(16): put(x, y, MD_BELLY)
    for x in range(8):
        for y in range(16, 24): put(x, y, MD_EYE if 2 <= x <= 5 and 18 <= y <= 21 else MD_D)
    for x in range(16, 24):
        for y in range(16, 24): put(x, y, MD_TOOTH if (x + (y > 19)) % 2 else (90, 30, 30))
    for x in range(24, 32):
        for y in range(16, 24): put(x, y, MD_WHISK)
    return im


def digger_model():
    """Snout along +z (turned 180 degrees by the item display, like the snake). About 16 x 15 x 30 units before scaling."""
    S, B = MD_SKIN, MD_BELLY_UV
    def box(f, t, uv=S, rot=None, down=None):
        e = {"from": f, "to": t, "faces": faces(uv)}
        if down: e["faces"]["down"] = {"uv": list(down), "texture": "#0"}
        if rot: e["rotation"] = rot
        return e
    els = [box([3, 6, 1], [13, 12, 13], down=B),                                      # mole body
           box([3.5, 6.5, 13], [12.5, 12, 20], down=B),                               # shark head
           box([5, 6.5, 20], [11, 10.5, 24], down=B),                                 # snout
           box([5.2, 6, 19.5], [10.8, 7, 23.5], MD_TEETH_UV),                         # jaw full of teeth
           box([3.2, 9.5, 16.5], [3.5, 11, 18.5], MD_EYE_UV), box([12.5, 9.5, 16.5], [12.8, 11, 18.5], MD_EYE_UV),   # cold blue eyes
           box([4.5, 7.5, 22], [5, 8, 29], MD_WHISK_UV), box([11, 7.5, 22], [11.5, 8, 29], MD_WHISK_UV),             # catfish whiskers
           box([7.5, 12, 4], [8.5, 17, 10], rot={"angle": -22.5, "axis": "x", "origin": [8, 12, 7]}),               # dorsal fin
           box([6, 7, -5], [10, 11, 1]),                                               # tail
           box([7.5, 5, -10], [8.5, 15, -4], rot={"angle": 22.5, "axis": "x", "origin": [8, 10, -5]})]              # shark tail fin
    for lx in (3, 11):                                                                # long mole legs on webbed feet
        for lz in (2.5, 9.5):
            els += [box([lx, 0.5, lz], [lx + 2, 6.5, lz + 2]), box([lx - 0.75, 0, lz - 1.25], [lx + 2.75, 0.5, lz + 3], MD_BELLY_UV)]
    return {"textures": {"0": "slf:item/mud_digger", "particle": "slf:item/mud_digger"}, "elements": els}


def draw_tooth(px):
    for y in range(2, 14):
        w_ = max(1, (14 - y) // 3)
        for x in range(8 - w_, 8 + w_): px[x, y] = (MD_TOOTH if x > 6 else (200, 200, 190)) + (255,)


def draw_hide(px):
    for x in range(2, 14):
        for y in range(3, 13):
            px[x, y] = (MD_L if (x * 5 + y * 3) % 13 < 3 else MD_D if x in (2, 13) or y in (3, 12) else MD) + (255,)


def draw_trophy(px):
    for x in range(4, 12):
        for y in range(2, 8): px[x, y] = ((236, 196, 60) if (x + y) % 5 else (255, 230, 120)) + (255,)      # gold cup
    for y in range(8, 11): px[7, y] = px[8, y] = (200, 160, 40, 255)
    for x in range(5, 11): px[x, 11] = px[x, 12] = (120, 90, 30, 255)
    for x, y in ((6, 4), (7, 3), (8, 3), (9, 4), (7, 5), (8, 5)): px[x, y] = MD_TOOTH + (255,)                  # a tooth set in it


def draw_purse(px):
    """Mahni Purse: a tied brown pouch with a gold coin peeking out."""
    for y in range(5, 15):
        half = 3 + min(y - 5, 14 - y, 2)
        for x in range(8 - half, 8 + half): px[x, y] = ((122, 82, 46) if (x + y) % 5 else (98, 64, 34)) + (255,)
    for x in range(6, 10): px[x, 5] = (70, 46, 24, 255)                       # drawstring
    for x in range(7, 11):
        for y in range(1, 5):
            if (x - 8.5) ** 2 + (y - 2.5) ** 2 <= 3: px[x, y] = ((240, 200, 70) if x < 10 else (200, 160, 40)) + (255,)


def main():
    (RP / "textures" / "item").mkdir(parents=True, exist_ok=True)
    head_texture().save(RP / "textures" / "item" / "goblin_head.png")
    axe_texture().save(RP / "textures" / "item" / "goblin_axe.png")
    orc_texture().save(RP / "textures" / "item" / "orc_head.png")
    snake_texture().save(RP / "textures" / "item" / "ravenous_snake.png")
    digger_texture().save(RP / "textures" / "item" / "mud_digger.png")
    models = {"goblin_head": head_model(False), "red_hat_goblin_head": head_model(True), "goblin_axe": axe_model(), "orc_head": orc_head_model(),
              "ravenous_snake_head": snake_head_model(), "ravenous_snake_body": snake_body_model(), "ravenous_snake_tail": snake_tail_model(),
              "devourers_scale": item_icon("devourers_scale", draw_scale), "python_white_hair": item_icon("python_white_hair", draw_hair),
              "mud_digger": digger_model(), "mud_digger_tooth": item_icon("mud_digger_tooth", draw_tooth), "digger_hide": item_icon("digger_hide", draw_hide),
              "solo_killers_trophy": item_icon("solo_killers_trophy", draw_trophy), "mahni_purse": item_icon("mahni_purse", draw_purse)}
    (RP / "items").mkdir(parents=True, exist_ok=True)
    for name, m in models.items():
        (RP / "models" / "item" / f"{name}.json").write_text(json.dumps(m, indent=1) + "\n", encoding="utf-8", newline="\n")
        (RP / "items" / f"{name}.json").write_text(json.dumps({"model": {"type": "minecraft:model", "model": f"slf:item/{name}"}}, indent=1) + "\n",
                                                   encoding="utf-8", newline="\n")
    print("wrote", ", ".join(models))


if __name__ == "__main__":
    main()
