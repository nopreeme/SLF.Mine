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


def main():
    (RP / "textures" / "item").mkdir(parents=True, exist_ok=True)
    head_texture().save(RP / "textures" / "item" / "goblin_head.png")
    axe_texture().save(RP / "textures" / "item" / "goblin_axe.png")
    orc_texture().save(RP / "textures" / "item" / "orc_head.png")
    models = {"goblin_head": head_model(False), "red_hat_goblin_head": head_model(True), "goblin_axe": axe_model(), "orc_head": orc_head_model()}
    (RP / "items").mkdir(parents=True, exist_ok=True)
    for name, m in models.items():
        (RP / "models" / "item" / f"{name}.json").write_text(json.dumps(m, indent=1) + "\n", encoding="utf-8", newline="\n")
        (RP / "items" / f"{name}.json").write_text(json.dumps({"model": {"type": "minecraft:model", "model": f"slf:item/{name}"}}, indent=1) + "\n",
                                                   encoding="utf-8", newline="\n")
    print("wrote", ", ".join(models))


if __name__ == "__main__":
    main()
