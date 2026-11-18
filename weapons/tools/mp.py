"""MinePiece-style models: chunky angled cuboids, big flat texels, banded handles, per-face tones."""
import math
from PIL import Image
import sprites

TILE_W, TILE_H, ATLAS_W, ATLAS_H = 16, 32, 256, 256
def sn(a): return a   # 26.2 allows any element angle, so no snapping
def c(r, g, b): return (r, g, b, 255)

RAMPS = {  # [shadow, dark, base, highlight]
    "wood":   [c(62, 36, 44), c(108, 66, 48), c(152, 104, 62), c(198, 156, 96)],
    "knot":   [c(46, 28, 38), c(70, 42, 40), c(102, 64, 46), c(134, 92, 58)],
    "wrap":   [c(112, 92, 96), c(166, 142, 122), c(216, 198, 160), c(244, 234, 196)],
    "steel":  [c(50, 54, 96), c(86, 100, 142), c(122, 140, 176), c(176, 196, 216)],
    "cap":    [c(26, 24, 54), c(42, 44, 82), c(60, 70, 108), c(90, 106, 138)],
    "face":   [c(118, 134, 176), c(158, 176, 208), c(198, 212, 232), c(236, 242, 248)],
    "handle": [c(30, 20, 46), c(52, 38, 72), c(78, 60, 98), c(108, 90, 122)],
}
def flat(col, hi=None): return [col, col, col, hi or col]
RAMPS.update({
    "iron":    [c(28, 26, 46), c(48, 50, 72), c(70, 78, 100), c(104, 116, 134)],
    "ridge":   flat(c(116, 126, 148)),
    "silver":  [c(96, 104, 140), c(154, 166, 192), c(206, 216, 228), c(246, 248, 250)],
    "marsh":   [c(16, 66, 58), c(36, 124, 72), c(86, 180, 92), c(204, 238, 180)],
    "medge":   flat(c(226, 242, 206)),
    "mdark":   flat(c(18, 54, 52)),
    "olive":   [c(36, 44, 40), c(64, 78, 48), c(100, 114, 64), c(160, 166, 100)],
    "mgrip":   [c(14, 18, 24), c(26, 36, 34), c(40, 56, 44), c(60, 78, 58)],
    "redwrap": [c(58, 16, 32), c(98, 30, 34), c(142, 50, 38), c(180, 82, 54)],
    "gem":     flat(c(214, 40, 48), c(255, 130, 130)),
    "bone":    [c(140, 134, 140), c(188, 182, 172), c(228, 224, 208), c(250, 248, 236)],
    "cloth":   [c(26, 26, 38), c(46, 48, 58), c(68, 72, 82), c(94, 100, 106)],
    "plank":   [c(36, 30, 36), c(62, 54, 54), c(90, 80, 70), c(120, 108, 92)],
    "rim":     flat(c(30, 26, 32)),
})
RAMPS.update({   # second batch of weapons; append only, the atlas position of a material is its index here
    "rust":     [c(58, 28, 34), c(112, 56, 40), c(168, 92, 52), c(214, 150, 88)],
    "night":    [c(14, 16, 40), c(30, 40, 84), c(52, 68, 124), c(104, 132, 186)],
    "lilac":    [c(70, 60, 104), c(120, 110, 156), c(170, 160, 198), c(222, 214, 236)],
    "gold":     [c(96, 52, 28), c(170, 108, 36), c(232, 178, 60), c(255, 232, 140)],
    "tsuka":    [c(30, 20, 46), c(60, 40, 90), c(92, 66, 130), c(232, 190, 90)],
    "sheen":    [c(150, 110, 60), c(214, 176, 96), c(246, 226, 150), c(255, 250, 214)],
    "teal":     [c(16, 50, 62), c(30, 96, 104), c(56, 144, 146), c(130, 208, 196)],
    "aqua":     flat(c(80, 214, 236), c(200, 250, 255)),
    "rose":     [c(74, 22, 56), c(130, 40, 76), c(186, 70, 100), c(236, 140, 150)],
    "ember":    flat(c(244, 120, 30), c(255, 214, 120)),
    "crystal":  [c(70, 110, 150), c(130, 190, 214), c(190, 236, 240), c(244, 255, 255)],
    "lavender": [c(74, 54, 110), c(128, 100, 164), c(180, 150, 206), c(226, 206, 240)],
    "orchid":   [c(70, 18, 90), c(128, 36, 140), c(190, 70, 190), c(244, 160, 236)],
    "void":     [c(10, 8, 22), c(22, 16, 44), c(38, 28, 68), c(70, 54, 110)],
    "azure":    [c(18, 26, 70), c(34, 58, 128), c(58, 96, 178), c(120, 170, 226)],
    "emerald":  [c(10, 70, 48), c(24, 130, 70), c(60, 196, 96), c(170, 246, 170)],
    "amber":    [c(150, 70, 10), c(226, 130, 16), c(250, 186, 40), c(255, 236, 130)],
    "crimson":  [c(70, 10, 24), c(130, 20, 34), c(190, 36, 44), c(236, 96, 84)],
})
RAMPS.update({   # source-accurate batch; append only
    "ducus":    [c(14, 30, 110), c(24, 60, 170), c(36, 90, 214), c(200, 230, 255)],
    "moss":     [c(40, 56, 20), c(84, 108, 30), c(132, 156, 44), c(196, 210, 96)],
    "abyss":    [c(30, 14, 60), c(56, 28, 100), c(82, 44, 138), c(150, 110, 200)],
})
MATS = list(RAMPS)
assert len(MATS) * 3 <= (ATLAS_W // TILE_W) * (ATLAS_H // TILE_H), "atlas is full"
SHADES = {"lit": 1.1, "mid": 0.94, "dark": 0.74}
FACE_SHADE = {"up": "lit", "west": "lit", "north": "mid", "south": "mid", "east": "dark", "down": "dark"}

def pattern(m, x, y):
    if m in ("wood", "handle"):
        return 0 if y % 5 == 4 else 2           # dark ring bands across the shaft
    if m == "knot": return 2 if (x + y) % 2 == 0 else 1
    if m == "wrap": return 2 if y % 2 == 0 else 1
    if m == "steel":
        if y % 6 == 0: return 3
        if y % 6 == 5: return 1
        return 2
    if m == "iron": return 2
    if m == "silver": return 2
    if m == "marsh": return 3 if ((x + y) % 6 == 0 or (x - y) % 9 == 4) else 2   # crossing vein lines
    if m == "olive": return 3 if ((x // 2) + (y // 2)) % 3 == 0 else 2
    if m in ("mgrip", "cloth"): return 2 if y % 2 == 0 else 1
    if m == "redwrap": return 0 if y % 3 == 2 else 2
    if m == "gem": return 3 if (x, y) == (0, 0) else 2
    if m == "bone": return 1 if y % 6 == 5 else 2
    if m == "plank": return 0 if x % 4 == 3 else (2 if (x // 4) % 2 == 0 else 1)
    if m == "cap": return 3 if y % 8 == 0 else 2
    if m == "rust": return 0 if (x + 2 * y) % 9 == 0 else (3 if (x - y) % 7 == 3 else 2)      # pitted streaks
    if m == "night": return 1 if (x + y) % 7 == 0 else 2
    if m in ("lilac", "sheen", "rose"): return 3 if y % 9 == 0 else 2
    if m == "gold": return 3 if (x + y) % 6 == 0 else 2
    if m == "tsuka": return (2, 3, 2, 0)[y % 4]                                               # gold bands on the wrap
    if m in ("teal", "azure"): return 1 if y % 4 == 3 else 2
    if m in ("aqua", "ember"): return 3 if (x, y) == (0, 0) else 2
    if m in ("crystal", "emerald", "orchid"): return 3 if (x + y) % 5 == 0 else (1 if (x - y) % 5 == 2 else 2)   # facets
    if m == "lavender": return 1 if (x + y) % 8 == 0 else 2
    if m == "void": return 0 if y % 5 == 4 else 2
    if m == "amber": return 1 if (x * 2 + y) % 7 in (0, 1) else (3 if (x - y) % 6 == 0 else 2)   # mottled resin
    if m == "crimson": return 3 if (x + y) % 11 == 0 else 2
    if m == "ducus": return 3 if ((x * 3 + y) % 7 == 0 or (x - 2 * y) % 9 == 0) else 2            # pale cracks through deep blue
    if m == "moss": return 1 if y % 7 == 6 else 2
    if m == "abyss": return 0 if (x * 2 + y) % 7 in (0, 1) else (3 if (x - y) % 9 == 0 else (1 if (x + y) % 3 == 0 else 2))   # mottled
    return 2

def tile_origin(m, shade):
    i = MATS.index(m) * 3 + list(SHADES).index(shade)
    return (i % 16) * TILE_W, (i // 16) * TILE_H

def texture():
    im = Image.new("RGBA", (ATLAS_W, ATLAS_H), (0, 0, 0, 0))
    for m in MATS:
        for sh, k in SHADES.items():
            ox, oy = tile_origin(m, sh)
            for x in range(TILE_W):
                for y in range(TILE_H):
                    r, g, b, a = RAMPS[m][pattern(m, x, y)]
                    im.putpixel((ox + x, oy + y), (min(255, int(r * k)), min(255, int(g * k)), min(255, int(b * k)), 255))
    return im

def cube(x0, y0, z0, w, h, d, m, rot=None, pivot=None, uo=0):
    uv = {}
    for f, (fw, fh) in {"north": (w, h), "south": (w, h), "east": (d, h), "west": (d, h), "up": (w, d), "down": (w, d)}.items():
        ox, oy = tile_origin(m, FACE_SHADE[f])
        uv[f] = {"uv": [ox + (uo if f in ("north", "south") else 0), oy], "uv_size": [min(fw, TILE_W), min(fh, TILE_H)]}
    out = {"origin": [round(x0, 3), round(y0, 3), round(z0, 3)], "size": [w, h, d], "uv": uv, "_m": m, "_uo": uo}
    if rot:
        rot = [0, 0, sn(rot[2])]
        out["rotation"] = rot; out["pivot"] = [round(v, 3) for v in pivot]
    return out

def chain(start, segs, m):
    """Segments leaning in the x/y plane. segs = [(length, angle_from_vertical, thickness)]. Returns cubes, joints."""
    x, y = start; cubes = []; joints = [(x, y)]
    for L, a, t in segs:
        a = sn(a)
        cubes.append(cube(x - t / 2, y - 0.4, -t / 2, t, L + 0.4, t, m, [0, 0, a], [x, y, 0]))
        x += L * math.sin(math.radians(a)); y += L * math.cos(math.radians(a))
        joints.append((x, y))
    return cubes, joints

# ---------------- Wood Staff ----------------
def staff_cubes():
    cubes, j = chain((0, 10), [(4, 0, 1.5), (7, -5, 2), (7, 5, 2), (6, 13, 2), (6, -15, 2), (5, 8, 2),
                               (4, 38, 2), (4, 78, 2), (3.5, 122, 1.75), (3, 165, 1.5), (1.5, 200, 1)], "wood")
    # knots at the bends
    for (kx, ky), s in ((j[4], 3), (j[6], 3.25), (j[2], 2.75)):
        cubes.append(cube(kx - s / 2, ky - s / 2, -s / 2, s, s, s, "knot", [0, 0, 45], [kx, ky, 0]))
    # twig
    tw, _ = chain(j[5], [(4, -52, 1), (3, -18, 1)], "wood"); cubes += tw
    # cloth grip around the hand (y = 24)
    for gy in (21.5, 23.5, 25.5):
        gx = j[2][0] + (gy - j[2][1]) * math.tan(math.radians(5))
        cubes.append(cube(gx - 1.3, gy, -1.3, 2.6, 1.2, 2.6, "wrap", [0, 0, 5], [gx, gy, 0]))
    return cubes

# ---------------- Iron Hammer ----------------
def hammer_cubes():
    C = []
    C.append(cube(-1.25, 12.2, -1.25, 2.5, 2.5, 2.5, "face", [0, 0, 45], [0, 13.45, 0]))   # diamond pommel
    C.append(cube(-1.5, 14.5, -1.5, 3, 2, 3, "cap"))
    C.append(cube(-1, 16.5, -1, 2, 22, 2, "handle"))
    for gy in (19, 21.5, 24, 26.5):
        C.append(cube(-1.3, gy, -1.3, 2.6, 1.4, 2.6, "wrap"))
    C.append(cube(-1.75, 37.5, -1.75, 3.5, 2.5, 3.5, "cap"))                               # collar
    C.append(cube(-5, 40, -3, 10, 6, 6, "steel"))                                          # head core
    C.append(cube(-1.5, 45.5, -3.25, 3, 1, 6.5, "cap"))                                    # top strap
    for sx in (-1, 1):
        x0 = 5 if sx > 0 else -7.5
        C.append(cube(x0, 39.25, -3.75, 2.5, 7.5, 7.5, "cap"))                             # end caps
        C.append(cube(7.5 if sx > 0 else -8.25, 40, -3, 0.75, 6, 6, "face"))               # striking faces
    for z0 in (-3.6, 2.85):                                                                # diamond bosses front/back
        C.append(cube(-1.75, 41.25, z0, 3.5, 3.5, 0.75, "cap", [0, 0, 45], [0, 43, 0]))
        C.append(cube(-0.9, 42.1, z0 - 0.2 if z0 < 0 else z0 + 0.2, 1.8, 1.8, 0.75, "face", [0, 0, 45], [0, 43, 0]))
    return C

# ---------------- icons recolored to match ----------------
def _sync_palette():
    sprites.W_RAMP = RAMPS["wood"]; sprites.W_KNOT = RAMPS["knot"][1]; sprites.W_OUT = c(44, 24, 22)
    sprites.M_RAMP = RAMPS["steel"]; sprites.CAP_RAMP = RAMPS["cap"]; sprites.H_RAMP = RAMPS["handle"]
    sprites.M_OUT = c(20, 20, 40); sprites.GRIP_L = RAMPS["wrap"][2]; sprites.GRIP_D = RAMPS["wrap"][1]
def staff_icon(): _sync_palette(); return sprites.staff_sprite()
def hammer_icon(): _sync_palette(); return sprites.hammer_sprite()


# ======================= more weapons =======================
def P(x0, y0, w, h, t, m, rot=None, piv=None, uo=0):
    """Plate centered on z."""
    return cube(x0, y0, -t / 2, w, h, t, m, rot, piv, uo)

def diamond(cx, cy, s, t, m):
    return P(cx - s / 2, cy - s / 2, s, s, t, m, [0, 0, 45], [cx, cy, 0])

def chain2(start, segs, th, m, strips=()):
    """Flat segments (length, angle, width) leaning in the x/y plane; strips = (side, width, material, thickness)."""
    x, y = start; cubes = []; joints = [(x, y)]
    for L, a, w in segs:
        a = sn(a)
        cubes.append(P(x - w / 2, y - 0.4, w, L + 0.4, th, m, [0, 0, a], [x, y, 0]))
        for side, sw, sm, st in strips:
            sx = x + w / 2 - 0.1 if side > 0 else (x - w / 2 - sw + 0.1 if side < 0 else x - sw / 2)
            cubes.append(P(sx, y - 0.4, sw, L + 0.4, st, sm, [0, 0, a], [x, y, 0]))
        x += L * math.sin(math.radians(a)); y += L * math.cos(math.radians(a))
        joints.append((x, y))
    return cubes, joints

def iron_dagger_cubes():
    return [diamond(0, 19.2, 2, 2, "cap"), P(-0.75, 20, 1.5, 6.5, 1.5, "handle"), P(-3.5, 26.5, 7, 1, 2, "cap"),
            P(-4, 26.25, 1, 1.5, 2.4, "iron"), P(3, 26.25, 1, 1.5, 2.4, "iron"),
            P(-1.25, 27.5, 2.5, 11, 1, "iron"), P(-0.4, 27.5, 0.8, 10.5, 1.4, "ridge"), diamond(0, 38.5, 1.77, 1, "iron")]

def iron_sword_cubes():
    return [diamond(0, 17.6, 2.6, 2.6, "cap"), P(-0.9, 19, 1.8, 8, 1.8, "handle"), P(-5, 27, 10, 1.25, 2, "cap"),
            P(-5.75, 26.6, 1.25, 2, 2.4, "iron"), P(4.5, 26.6, 1.25, 2, 2.4, "iron"), diamond(0, 27.6, 3, 2.6, "iron"),
            diamond(0, 27.6, 1.4, 3, "ridge"),
            P(-1.75, 28.25, 3.5, 21, 1, "iron"), P(-0.5, 29, 1, 19.5, 1.4, "ridge"), diamond(0, 49.25, 2.47, 1, "iron")]

def mercenary_blade_cubes():
    # Mercenary Twinblade, after the anime (ep. 1): a broad short sword, the same on both sides of the centre line,
    # with a thin dark fuller, a plain grey block guard, a black wrapped grip and a grey pommel cap
    C = [P(-1.25, 18.5, 2.5, 1.5, 2.5, "steel"), P(-1, 20, 2, 7, 2, "cloth"),
         P(-4, 27, 8, 1.75, 2.5, "steel"), P(-0.25, 28.75, 0.5, 15.5, 1.15, "cap")]
    for y0, w, h in ((28.75, 4.5, 4.25), (33, 5, 7), (40, 4.5, 3), (43, 3.5, 2.25), (45.25, 2.5, 2), (47.25, 1.5, 1.75), (49, 0.7, 1.25)):
        C.append(P(-w / 2, y0, w, h, 1, "silver"))
        if w > 1:
            for sx in (-1, 1): C.append(P(w / 2 - 0.65 if sx > 0 else -w / 2 - 0.1, y0, 0.75, h, 0.6, "face"))
    return C

def marsh_dagger_cubes():
    # Marsh Dagger, after the anime: a green blade veined with pale cracks that swells, steps in at a notch on the
    # back, then sweeps to the point in one S-curve; a pale bevel on the edge (+x); an angular olive guard with
    # paler plates; a dark wrapped grip and round pommel
    C = [P(-1.3, 17.5, 2.6, 2.2, 2.6, "rim"), P(-0.9, 19.5, 1.8, 7.5, 1.8, "mgrip"),
         P(-2.4, 27, 5.6, 3.3, 2.75, "olive"), P(-1.5, 30, 3, 1, 2.2, "olive"),
         P(-1.9, 27.5, 1.5, 2.2, 2.95, "wrap"), P(1.3, 28.3, 1.5, 1.6, 2.95, "wrap"),
         P(1.75, 28, 1.75, 4.5, 1.75, "olive", [0, 0, 68], [2.5, 28.6, 0])]
    path = [(5, 12, 3.8), (4.5, 0, 4), (4.5, -16, 3.4), (4.5, -18, 3.6), (4, -4, 2.7), (3, 12, 1.5)]
    blade, j = chain2((0, 30.8), path, 1, "marsh", strips=((1, 0.8, "medge", 0.6), (-1, 0.6, "mdark", 1.2))); C += blade
    x, y = j[2]; C.append(P(x - 2.4, y - 0.4, 1.4, 3, 1, "marsh", [0, 0, -52], [x - 1.7, y, 0]))      # the step on the back
    return C

def vorpal_chopper_cubes():
    C = [P(-1.4, 18.5, 2.8, 1.5, 2.8, "cap"), diamond(0, 17.6, 1.6, 1.6, "gem"),
         P(-1, 20, 2, 7.5, 2, "redwrap"), P(-1.3, 27.5, 2.6, 1.5, 2.6, "steel"),
         P(-6, 28.2, 2.5, 4, 1, "silver", [0, 0, -40], [-4, 29.4, 0])]
    tail, _ = chain2((0, 16.8), [(2, 160, 1), (2, 215, 0.8)], 0.8, "silver"); C += tail
    path = [(4.5, -10, 7.5), (4.5, 6, 8.5), (4.5, 22, 7.5), (4, 38, 6), (3.5, 54, 4), (3, 68, 2)]
    blade, _ = chain2((0.5, 29), path, 1, "silver", strips=((1, 0.8, "face", 0.6),)); C += blade
    line, _ = chain2((0.5, 29), [(L, a, 0.6) for L, a, w in path[:4]], 1.3, "cap"); C += line
    return C

def fossil_rod_cubes():
    C, j = chain((0, 10), [(2.5, 0, 2.6), (9, -4, 1.6), (9, 5, 1.8), (8, -5, 1.6), (6, 6, 1.8)], "bone")
    thin, _ = chain((1.5, 13), [(8, 3, 1.1), (7, -3, 1.1)], "bone"); C += thin
    kx, ky = j[3]; C.append(cube(kx - 1.3, ky - 1.3, -1.3, 2.6, 2.6, 2.6, "bone", [0, 0, 45], [kx, ky, 0]))
    x, y = j[5]
    C += [cube(x - 2.5, y - 0.5, -1.5, 5, 4.5, 3, "bone", [0, 0, -18], [x, y, 0]),
          cube(x + 1.5, y + 0.5, -1, 3.2, 2, 2, "bone", [0, 0, 20], [x + 1.5, y + 1.5, 0]),
          cube(x - 3.6, y + 3, -0.75, 1.5, 3.2, 1.5, "bone", [0, 0, -40], [x - 2.8, y + 3, 0]),
          cube(x + 0.6, y + 3.6, -0.75, 1.5, 2.6, 1.5, "bone", [0, 0, 28], [x + 1.3, y + 3.6, 0])]
    for gy, gx in ((13.5, 0.6), (22.6, 0), (24.6, 0), (36, 0.2), (43, 0.2)):
        C.append(cube(gx - 1.6, gy, -1.5, 3.2, 1.3, 3, "cloth"))
    for gy, gx, a in ((13.5, 1.6, -28), (36, 1.4, -22), (43, -1.6, 24), (43, 1.6, -35)):
        C.append(P(gx - 0.5, gy - 3.6, 1, 4, 0.4, "cloth", [0, 0, a], [gx, gy + 0.4, 0]))
    return C

def wood_shield_cubes():
    C = []
    for R, m, z0, d in ((9.5, "rim", -3.1, 1.2), (8.5, "plank", -3.5, 2)):
        for k in range(-int(R + .5), int(R + .5)):
            v = R * R - (k + .5) ** 2
            if v <= 0: continue
            half = round(math.sqrt(v) * 2) / 2
            if half < 1: continue
            C.append(cube(-half, 24 + k, z0, 2 * half, 1, d, m, uo=(8 - half) if half <= 8 else 0))
    C.append(cube(-1, 21, -1.5, 2, 6, 7, "rim"))   # handle, as deep as the vanilla shield's so the fist sits behind the board
    return C

# ======================= second batch =======================
def mirror(cubes):
    """Left-handed copy: flip the model across x."""
    out = []
    for q in cubes:
        q = dict(q); (x0, y0, z0), (w, _, _) = q["origin"], q["size"]
        q["origin"] = [round(-(x0 + w), 3), y0, z0]
        if q.get("rotation"):
            q["rotation"] = [0, 0, -q["rotation"][2]]; q["pivot"] = [-q["pivot"][0]] + list(q["pivot"][1:])
        out.append(q)
    return out

def bands(ys, s, m, h=1.2, x=0):
    return [cube(x - s / 2, y, -s / 2, s, h, s, m) for y in ys]

def rust_saber_cubes():
    C = [P(-1.3, 18.3, 2.6, 1.7, 2.6, "knot"), P(-0.9, 20, 1.8, 7, 1.8, "wood"), P(-2.4, 27, 5.6, 1.4, 2.4, "rust")]
    bow, _ = chain((2.8, 27.6), [(3.4, 166, 0.9), (3.2, 190, 0.9), (2.6, 236, 0.9)], "rust"); C += bow    # knuckle bow
    blade, _ = chain2((0, 28.4), [(6, 0, 3.4), (6, -5, 3.4), (5, -11, 3.1), (4, -18, 2.5), (3, -27, 1.5)], 1, "rust",
                      strips=((-1, 0.7, "knot", 1.3), (1, 0.6, "wrap", 0.6))); C += blade
    return C

def wethermon_katana_cubes():
    # after the manga cover: a long nodachi, black grip crossed with rose cord, dark ring guard
    C = [P(-1.1, 13.4, 2.2, 1.2, 2.2, "cap"), P(-0.9, 14.6, 1.8, 12, 1.8, "cloth"),
         P(-2.5, 26.6, 5, 0.9, 4.4, "cap"), P(-1.7, 26.4, 3.4, 1.3, 5, "cap"), P(-1, 27.6, 2, 1.2, 1.4, "steel")]
    C += bands((16, 18.4, 20.8, 23.2), 2.1, "rose", 0.7)
    blade, _ = chain2((0, 28.8), [(7, 0, 2.3), (7, -3, 2.3), (6, -6, 2.2), (5, -9, 2), (3.4, -13, 1.6), (2, -22, 0.9)], 0.9, "silver",
                      strips=((1, 0.6, "face", 0.5), (-1, 0.5, "cap", 1.1))); C += blade
    return C

def _straight_sword(blade_m, line_m, guard_m, grip_m, gem_m, L, w=3.2):
    C = [diamond(0, 17.6, 2.4, 2.4, gem_m), P(-1.2, 18.6, 2.4, 1.2, 2.4, guard_m), P(-0.9, 19.8, 1.8, 7.2, 1.8, grip_m),
         P(-4.6, 27, 9.2, 1.3, 2.2, guard_m),
         P(-6.2, 27.2, 2.4, 1.3, 2, guard_m, [0, 0, 32], [-4.4, 27.6, 0]), P(3.8, 27.2, 2.4, 1.3, 2, guard_m, [0, 0, -32], [4.4, 27.6, 0]),
         diamond(0, 27.8, 2.8, 2.8, guard_m), diamond(0, 27.8, 1.5, 3.2, gem_m),
         P(-w / 2, 28.4, w, L, 1, blade_m), P(-0.45, 29.2, 0.9, L - 1.6, 1.4, line_m),
         diamond(0, 28.4 + L, w / math.sqrt(2), 1, blade_m)]
    return C

def _ball(y): return cube(-1.3, y - 1.3, -1.3, 2.6, 2.6, 2.6, "cap", [0, 0, 45], [0, y, 0])

def whalelore_goldsheen_cubes():
    # after manga chapter 227: long wrapped grip with a ball pommel, no guard, one broad curved single-edged blade
    C = [_ball(16.4), P(-0.9, 17.6, 1.8, 10, 1.8, "wrap"), P(-1.6, 27.6, 3.2, 1.2, 2.4, "cap")]
    base, j = chain2((0.3, 28.8), [(4, 7, 4.2), (4, 2, 5)], 1.2, "gold", strips=((-1, 0.7, "cap", 1.5),)); C += base   # rippled root
    blade, k = chain2(j[2], [(5, -3, 5.4), (5, -8, 5), (4.5, -13, 4.2), (4, -18, 3), (3, -24, 1.6)], 1, "sheen",
                      strips=((1, 0.9, "face", 0.6), (-1, 0.7, "gold", 1.3))); C += blade
    x, y = k[1]
    C += [P(x - 3.4, y - 0.6, 1.6, 2.6, 1.6, "cap"),                                     # block on the spine and its ribbon
          P(x - 6.8, y + 0.2, 3.6, 0.7, 0.4, "wrap", [0, 0, 24], [x - 3.4, y + 0.5, 0]),
          P(x - 6.2, y - 1.4, 3, 0.7, 0.4, "wrap", [0, 0, -30], [x - 3.4, y + 0.3, 0])]
    return C

def whalelore_netherlight_cubes():
    # after manga chapter 227: the short one, a crescent blade with crystals growing at its root
    C = [_ball(16.4), P(-0.9, 17.6, 1.8, 8.6, 1.8, "wrap"), P(-1.3, 26.2, 2.6, 2.4, 2.4, "rim"),
         P(-3.6, 28.2, 1.3, 3.4, 1.3, "crystal", [0, 0, -42], [-1.4, 28.6, 0]),
         P(-2.9, 26.6, 1, 2.4, 1, "crystal", [0, 0, -70], [-1.3, 27.4, 0])]
    blade, _ = chain2((0.4, 28.6), [(4, -22, 3), (4, -6, 4), (4, 10, 4.2), (3.5, 26, 3.4), (3, 42, 2.2), (2.4, 56, 1.1)], 1, "night",
                      strips=((1, 0.8, "face", 0.6), (-1, 0.5, "cap", 1.3))); C += blade
    return C

def _gauntlet(body_m, trim_m):
    return [cube(-2.7, 18.6, -2.5, 5.4, 2.8, 5, trim_m),                        # cuff
            cube(-3.2, 21.4, -2.8, 6.4, 5.6, 5.6, body_m),                      # back of the hand
            cube(3.2, 22.4, -1.1, 1.4, 3.2, 2.2, trim_m),                       # thumb
            cube(-3.5, 27, -3, 7, 1.5, 6, trim_m)]                              # knuckle plate

def gilta_brille_cubes():
    # after the anime (episode 34): a long dark machine housing with red slits and a vent pipe, the Golden
    # Scorpion's amber stinger out of the front and a long crystal down each side. This is the right-hand one.
    C = [cube(-3, 19, -2.6, 6, 13, 5.2, "iron"),                                         # housing
         cube(-3.5, 24.5, -3, 7, 4.5, 6, "cap"), cube(-3.4, 32, -3, 6.8, 1.8, 6, "cap"), # armour band and front collar
         cube(-2.3, 16.6, -2, 4.6, 2.4, 4, "cap"), P(-0.9, 13.4, 1.8, 3.2, 1.4, "amber"), diamond(0, 13.4, 1.27, 1.4, "amber"),
         cube(-5.4, 15.6, -1, 2, 9.4, 2, "silver"), cube(-5.6, 14.8, -1.2, 2.4, 1, 2.4, "cap"),   # vent pipe
         cube(3, 25.4, -1.4, 0.9, 2.8, 2.8, "face")]
    for y in (20.4, 21.8, 30):
        C.append(cube(-0.9, y, -2.75, 1.8, 0.5, 5.5, "gem"))                             # red slits
    sting, _ = chain2((0, 33.6), [(5, -6, 4.6), (5, 4, 4.4), (4.5, 16, 3.6), (4, 30, 2.6), (3, 44, 1.4)], 1.6, "amber",
                      strips=((1, 0.7, "sheen", 0.9),)); C += sting
    for x, y0, L, a in ((5.2, 21, 14, 8), (-7.6, 22, 12, -8)):                           # side crystals
        C += [cube(x - 0.9, y0, -0.9, 1.8, L, 1.8, "crystal", [0, 0, a], [x, y0, 0])]
        for d in (0, L):                                                               # pointed ends
            tx, ty = x + d * math.sin(math.radians(a)), y0 + d * math.cos(math.radians(a))
            C.append(cube(tx - 0.64, ty - 0.64, -0.9, 1.27, 1.27, 1.8, "crystal", [0, 0, 45], [tx, ty, 0]))
    return C

def crescent_blade_cubes():
    C = [diamond(0, 17.4, 2, 2, "gold"), P(-0.9, 18.2, 1.8, 9.2, 1.8, "wood"), P(-1.4, 27.4, 2.8, 1.4, 2.6, "gold")]
    C += bands((20.5, 23, 25.5), 2.3, "gold", 0.9)
    moon, _ = chain2((-0.4, 28.6), [(4.2, -62, 2), (4.2, -34, 3), (4.2, -6, 3.7), (4.2, 22, 4), (4.2, 50, 4), (4.2, 78, 3.6),
                                    (4, 106, 2.9), (3.6, 134, 1.8)], 1, "lavender",
                     strips=((-1, 0.8, "face", 0.6), (1, 0.6, "handle", 1.3))); C += moon
    return C

# ======================= source-accurate batch (wiki art and Evan's manga references) =======================
def _togetsu(body, edge, line, pommel):
    # Togetsu, after the anime: a broad crescent chopper on a dark red wrapped grip. The cutting edge (+x) is the
    # outside of the curve; a horn juts back from the heel of the blade.
    C = pommel + [P(-0.95, 19.5, 1.9, 7.6, 1.9, "redwrap"), P(-1.4, 27, 2.8, 1.6, 2.6, "silver")]
    path = [(4.5, 14, 6.4), (4.5, 2, 7.4), (4.5, -11, 7), (4, -24, 5.6), (3.5, -37, 3.9), (3, -50, 2.1)]
    blade, _ = chain2((1.2, 28.4), path, 1, body, strips=((1, 0.9, edge, 0.6),)); C += blade
    seam, _ = chain2((0.2, 28.4), [(L, a, 0.5) for L, a, w in path[:4]], 1.25, line); C += seam
    C.append(P(-5.6, 27.6, 2.4, 4.6, 1, body, [0, 0, 38], [-3.2, 28.6, 0]))                    # horn at the heel
    return C

def togetsu_waxing_cubes():   # the white right-hand blade
    return _togetsu("face", "silver", "cap", [diamond(0, 18.4, 1.7, 1.7, "gem"), P(-1.1, 18.9, 2.2, 0.8, 2.2, "cap")])

def togetsu_waning_cubes():   # the dark left-hand blade: hex nut, red bead and a white fang on the pommel
    return _togetsu("iron", "silver", "cap", [P(-1.3, 18.3, 2.6, 1.4, 2.6, "steel"), diamond(0, 17.5, 1.5, 1.5, "gem"),
                                               P(-0.4, 14.6, 0.9, 2.8, 0.9, "bone", [0, 0, -24], [0, 17, 0])])

def ducusram_cubes():
    # Ducusram, after the anime: the Marsh Dagger grown into a broad swept blade, deep blue shot with pale cracks.
    # The pale edge (+x) is the outside of the curve; two horns hook back off the inside; a sculpted teal guard,
    # dark wrapped grip and round pommel
    C = [P(-1.3, 17.2, 2.6, 2.2, 2.6, "mgrip"), P(-0.9, 19.4, 1.8, 7.4, 1.8, "mgrip"),
         P(-2.4, 26.6, 6.2, 3.4, 2.8, "teal"), P(-1.6, 30, 3.4, 1, 2.2, "teal"),
         P(2.2, 27.4, 1.9, 4.6, 1.9, "teal", [0, 0, 64], [3, 28.2, 0]), P(-0.2, 27.4, 0.5, 2.4, 2.95, "crystal")]
    path = [(5.5, 10, 4.4), (5.5, -6, 5), (5, -22, 4.6), (4.5, -36, 3.6), (4, -48, 2.4), (3, -58, 1.2)]
    blade, j = chain2((0.4, 30.6), path, 1, "ducus", strips=((1, 1, "face", 0.6),)); C += blade
    for k, a, L, w in ((1, 228, 5.4, 1.9), (3, 246, 3.6, 1.5)):                                   # horns off the inside
        x, y = j[k]; x -= path[k][2] / 2 - 0.6
        C.append(P(x - w / 2, y, w, L, 0.9, "ducus", [0, 0, a], [x, y, 0]))
        C.append(P(x - w / 2 - 0.25, y, 0.6, L, 0.6, "face", [0, 0, a], [x, y, 0]))
    C.append(P(2.4, 30.4, 1.4, 3, 0.9, "ducus", [0, 0, 62], [3, 31, 0]))                           # notch horn by the guard
    return C

def empire_bee_estoc_cubes():
    # Empire Bee Twinblade, right hand, after the anime: a long violet estoc. From the pommel up: a rose spike,
    # gold ring, black grip, gold ring, a pale carved bulb, a black neck wound with gold, then the blade; an
    # angular black bow runs from the neck out and back to the pommel
    C = [diamond(0, 15.2, 1.4, 1.4, "rose"), P(-1.1, 15.9, 2.2, 0.8, 2.2, "gold"), P(-0.85, 16.7, 1.7, 9.4, 1.7, "void"),
         P(-1.15, 26.1, 2.3, 0.7, 2.3, "gold"), P(-1.5, 26.8, 3, 3, 2.8, "sheen"), P(-0.85, 29.8, 1.7, 4, 1.7, "void")]
    for k, gy in enumerate((30.1, 31.3, 32.5)):                                                  # the gold winding
        C.append(P(-1.1, gy, 2.2, 0.7, 2.1, "gold", [0, 0, 24], [0, gy + 0.35, 0]))
    bow, _ = chain((1.1, 32.4), [(8.4, 148, 0.9), (9.2, 205, 0.9)], "void"); C += bow
    for y0, w, h in ((33.6, 1.5, 7), (40.6, 1.3, 6.4), (47, 1.05, 5), (52, 0.75, 3)):
        C.append(P(-w / 2, y0, w, h, 0.9, "orchid"))
    C.append(P(-0.2, 33.6, 0.4, 19.6, 1.15, "lavender"))
    return C

def empire_bee_maingauche_cubes():
    # Empire Bee Twinblade, left hand, after the anime: a steel parrying dagger. Gold block at the blade, flared gold
    # quillons, and a violet shell guard edged and scrolled in gold that bows from the quillon to the pommel
    C = [diamond(0, 17.6, 1.4, 1.4, "rose"), P(-0.85, 18.4, 1.7, 8.6, 1.7, "void"),
         P(-1.3, 27, 2.6, 1.8, 2.4, "gold"), P(-4.6, 27.2, 9.2, 0.9, 1.6, "gold"),
         P(-5.2, 26.6, 1, 2, 1.3, "gold", [0, 0, -20], [-4.6, 27.6, 0]), P(4.2, 26.6, 1, 2, 1.3, "gold", [0, 0, 20], [4.6, 27.6, 0]),
         P(-1.1, 28.8, 2.2, 11, 0.9, "silver"), P(-0.3, 28.8, 0.6, 10.4, 1.2, "ridge"),
         P(-0.75, 39.8, 1.5, 2, 0.9, "silver"), diamond(0, 42, 1.06, 0.9, "silver")]
    shell, _ = chain2((3.6, 27), [(3.4, 172, 2.6), (3.4, 190, 2.6), (2.6, 214, 2.2)], 3, "orchid",
                      strips=((-1, 0.5, "gold", 3.2), (1, 0.5, "gold", 3.2))); C += shell
    scroll, _ = chain2((3.6, 26.6), [(3, 178, 0.5), (3, 196, 0.5)], 3.3, "gold"); C += scroll
    return C

def dullahan_decapitator_cubes():
    # General Dullahan's Decapitator, after the anime: a two-handed executioner's sword. Long black grip, dark
    # cross guard with squared ends, a broad pale blade narrowing evenly to the point
    C = [P(-1.3, 10.6, 2.6, 1.8, 2.6, "cap"), P(-0.9, 12.4, 1.8, 14.6, 1.8, "cloth"),
         P(-6.5, 27, 13, 1.6, 2.2, "cap"), P(-7.3, 26.4, 1.6, 2.8, 2.8, "cap"), P(5.7, 26.4, 1.6, 2.8, 2.8, "cap"),
         P(-1.4, 28.6, 2.8, 1.2, 1.6, "iron"), P(-0.5, 29.8, 1, 13, 1.4, "cap")]
    for y0, w, h in ((29.8, 6.4, 5), (34.8, 5.8, 5), (39.8, 5, 5), (44.8, 4, 4), (48.8, 3, 3), (51.8, 2, 2.4), (54.2, 1, 1.8)):
        C.append(P(-w / 2, y0, w, h, 1, "silver"))
        for sx in (-1, 1): C.append(P(w / 2 - 0.7 if sx > 0 else -w / 2 - 0.1, y0, 0.8, h, 0.6, "face"))
    return C

def vorpal_sledge_cubes():
    # Vorpal Sledge, after the manga: a long banded shaft with a spiked butt, and a blocky dark red head bound with
    # gold rings, a spike on top
    C = [cube(-0.5, 9.4, -0.5, 1, 2.4, 1, "rim", [0, 0, 45], [0, 10.6, 0]), cube(-1.3, 11.6, -1.3, 2.6, 1.6, 2.6, "gold"),
         cube(-0.95, 13.2, -0.95, 1.9, 26, 1.9, "void")]
    for gy in (17, 19.6, 22.2, 24.8, 27.4):
        C.append(cube(-1.25, gy, -1.25, 2.5, 1.3, 2.5, "redwrap"))
    C += [cube(-1.7, 38.4, -1.7, 3.4, 1.8, 3.4, "gold"), cube(-5, 40.2, -3, 10, 6.4, 6, "crimson")]
    for x0 in (-3.9, -1.4, 1.1):                                                        # three gold rings round the head
        C.append(cube(x0, 39.9, -3.3, 1.4, 7, 6.6, "gold"))
    for sx in (-1, 1):
        C.append(cube(5 if sx > 0 else -7.4, 39.5, -3.7, 2.4, 7.8, 7.4, "rim"))
        C.append(cube(7.4 if sx > 0 else -8.1, 40.4, -2.8, 0.7, 6, 5.6, "gold"))
    C += [cube(-1.3, 46.6, -1.3, 2.6, 1, 2.6, "rim"), cube(-0.9, 47, -0.9, 1.8, 1.8, 1.8, "rim", [0, 0, 45], [0, 47.9, 0])]
    return C

def blue_predator_cubes():
    # Blue Predator, after the manga: a long wavy single-edged blade, the flat filled with a dark swirling grain,
    # three fangs hanging off the back near the tip, on a knobbly bone hilt
    C = [P(-1.5, 16.6, 3, 2.4, 2.8, "bone"), P(-1.05, 19, 2.1, 7.6, 2.1, "bone"),
         P(-2.6, 26.6, 5.2, 2.2, 2.8, "bone"), diamond(0, 27.7, 1.6, 3, "void"),
         P(-4.4, 26.4, 2.2, 1.1, 1.2, "bone", [0, 0, -30], [-2.6, 27.4, 0]), P(2.2, 26.4, 2.2, 1.1, 1.2, "bone", [0, 0, 30], [2.6, 27.4, 0])]
    C += bands((20.2, 22.4, 24.6), 2.5, "bone", 0.9)
    path = [(5, -6, 3.6), (5, 6, 4), (5, 14, 4.4), (5, 4, 4.6), (4.5, -10, 4.2), (4, -22, 3.2), (3, -34, 1.9)]
    blade, j = chain2((0, 28.6), path, 1, "silver", strips=((1, 0.8, "face", 0.6),)); C += blade
    grain, _ = chain2((-0.3, 28.6), [(L, a, w * 0.55) for L, a, w in path[:6]], 1.2, "night"); C += grain
    for k, L in ((4, 2.6), (5, 2.3), (6, 1.9)):                                                # fangs on the back edge
        x, y = j[k]
        C.append(P(x - 2.6, y - 2.2, 0.9, L, 0.8, "bone", [0, 0, 62], [x - 1.6, y - 1, 0]))
    return C

def super_cat_teaser_cubes():
    # Super Cat-Teaser Lv.100, after the colour art: a long olive-green comb of a sword, a row of pale spines
    # down the whole edge, bolted plates along the back, a dark red wrapped grip with a hooked brown pommel
    C = [P(-1, 17.4, 2.6, 1.6, 2, "knot", [0, 0, 30], [0, 18.4, 0]), P(-0.95, 19, 1.9, 8, 1.9, "redwrap"),
         P(-1.9, 27, 3.8, 3.4, 2.4, "moss"), diamond(0, 28.7, 1.3, 2.7, "void")]
    path = [(6, 4, 3.4), (6, -2, 3.4), (6, -8, 3.2), (5, -3, 3), (3, 24, 3)]
    blade, j = chain2((0, 30.2), path, 1.3, "moss", strips=((-1, 0.7, "olive", 1.6),)); C += blade
    for k in (1, 3):                                                                         # bolts on the back plates
        x, y = j[k]; C.append(diamond(x - 1.2, y, 0.9, 1.9, "sheen"))
    y = 30.8
    while y < 53:                                                                            # the spines
        seg = min(range(len(path)), key=lambda k: abs((j[k][1] + j[k + 1][1]) / 2 - y))
        (x0, y0), (x1, y1) = j[seg], j[seg + 1]; t = max(0.0, min(1.0, (y - y0) / (y1 - y0)))
        x = x0 + (x1 - x0) * t + 1.5; L = 3.4 if int(y * 10) % 3 else 2.4
        C.append(P(x, y, L, 0.5, 0.5, "bone", [0, 0, -8 + (int(y * 7) % 5) * 4], [x, y, 0]))
        y += 1.15
    return C

def dis_pater_cubes():
    # Dis Pater, after the manga: a round shield in rings - a dark rune band on the rim, a pale ring split into four
    # by spokes, and three crystals set round a dark boss. Laid out like wood_shield (board in front of z, handle behind)
    C = []
    for R, m, z0, d in ((9.5, "void", -3.1, 1.2), (8.4, "lilac", -3.5, 2), (4.2, "steel", -3.9, 2.2), (1.6, "void", -4.2, 2.4)):
        for k in range(-int(R + .5), int(R + .5)):
            v = R * R - (k + .5) ** 2
            if v <= 0: continue
            half = round(math.sqrt(v) * 2) / 2
            if half < 1: continue
            C.append(cube(-half, 24 + k, z0, 2 * half, 1, d, m))
    for a in (0, 90):                                                                        # spokes
        C.append(cube(-8.4, 23.75, -3.7, 16.8, 0.5, 0.4, "void", [0, 0, a + 45], [0, 24, 0]))
    for a in (90, 210, 330):                                                                 # crystals
        C.append(cube(-0.7, 25.2, -4.7, 1.4, 3.4, 1.2, "crystal", [0, 0, a], [0, 24, 0]))
    C.append(cube(-1, 21, -1.5, 2, 6, 7, "rim"))
    return C

def flame_decapitator_cubes():
    # Flame General's Decapitator, after the anime: a long narrow longsword. Black cross-wrapped grip, a mottled dark
    # bar under a slim silver guard with drooping tips, a plain steel blade
    C = [P(-1.2, 10.4, 2.4, 1.6, 2.4, "silver"), P(-0.9, 12, 1.8, 12.6, 1.8, "cloth"), P(-3, 24.6, 6, 1.5, 2.2, "night"),
         P(-4.6, 27, 9.2, 1, 1.8, "silver"), P(-5.4, 25.9, 1.1, 1.6, 1.4, "silver"), P(4.3, 25.9, 1.1, 1.6, 1.4, "silver"),
         P(-0.3, 28, 0.6, 24, 1.3, "ridge")]
    for y0, w, h in ((28, 2.6, 10), (38, 2.3, 8), (46, 1.9, 6), (52, 1.3, 2.6), (54.6, 0.7, 1.4)):
        C.append(P(-w / 2, y0, w, h, 0.9, "silver"))
    return C

def zanbaralia_cubes():
    # Darkhelm Spear Zanbaralia, after the anime: an all-black spear. Violet binding below a black-and-white collar,
    # and a head of flat black blades - a long centre one flanked by two more
    C = [cube(-0.75, 10.2, -0.75, 1.5, 32.4, 1.5, "void"), cube(-1.1, 42, -1.1, 2.2, 2.2, 2.2, "face"),
         cube(-1.3, 42.7, -1.3, 2.6, 0.8, 2.6, "rim")]
    for gy in (33, 34.8, 36.6, 38.4, 40.2):
        C.append(cube(-0.95, gy, -0.95, 1.9, 1.1, 1.9, "lavender"))
    C += [P(-0.9, 44.2, 1.8, 8.6, 0.9, "rim"), P(-0.55, 52.8, 1.1, 2, 0.9, "rim"), diamond(0, 55, 0.78, 0.9, "rim")]
    for sx in (-1, 1):
        C.append(P(sx * 1.9 - 0.6, 44, 1.2, 8.4, 0.8, "void", [0, 0, sx * 14], [sx * 1.4, 44.2, 0]))
        C.append(P(sx * 2.6 - 0.5, 43.2, 1, 3.2, 0.8, "void", [0, 0, sx * 132], [sx * 1.6, 44.6, 0]))
    return C

def giant_killing_skewer_cubes():
    # Giant-Killing Skewer, after the manga: a spear with a broad leaf blade and two long wings sweeping back down
    # the shaft
    C = [cube(-1.1, 10.2, -1.1, 2.2, 1.6, 2.2, "steel"), cube(-0.75, 11.2, -0.75, 1.5, 29, 1.5, "cloth"),
         cube(-1.2, 39.4, -1.2, 2.4, 1.6, 2.4, "steel"), P(-0.35, 41, 0.7, 12, 1.3, "night")]
    for y0, w, h in ((41, 2.4, 1.6), (42.6, 4, 2.6), (45.2, 4.8, 3.4), (48.6, 3.8, 2.8), (51.4, 2.6, 2.2), (53.6, 1.5, 1.6), (55.2, 0.7, 0.8)):
        C.append(P(-w / 2, y0, w, h, 1, "silver"))
        if w > 2:
            for sx in (-1, 1): C.append(P(w / 2 - 0.65 if sx > 0 else -w / 2 - 0.1, y0, 0.75, h, 0.6, "face"))
    for sx in (-1, 1):
        wing, _ = chain2((sx * 1.3, 42.4), [(5.5, sx * 150, 2.4), (5, sx * 166, 1.7), (3.5, sx * 176, 0.9)], 0.9, "silver",
                         strips=((sx, 0.6, "face", 0.6),)); C += wing
    return C

def antinomy_cubes():
    # Antinomy, after the colour art: a huge slab of a greatsword in mottled deep purple, single-edged, with a dark
    # thorned guard and a pale eye set in it
    C = [P(-1.2, 10.4, 2.4, 1.8, 2.4, "void"), P(-0.95, 12.2, 1.9, 14, 1.9, "abyss"), P(-3.4, 26, 6.8, 2.8, 2.8, "void"),
         diamond(0, 27.4, 1.4, 3, "face"),
         P(-5.4, 26.4, 2.6, 1.2, 1.4, "void", [0, 0, -32], [-3.4, 27.2, 0]), P(2.8, 26.4, 2.6, 1.2, 1.4, "void", [0, 0, 32], [3.4, 27.2, 0])]
    C += bands((14.4, 17.4, 20.4, 23.4), 2.3, "void", 0.7)
    path = [(5.5, -4, 7.4), (5.5, 2, 8), (5, 6, 8), (5, 3, 7.2), (4, -14, 5.2), (3, -34, 2.8)]
    blade, _ = chain2((0.6, 28.4), path, 1.2, "abyss", strips=((1, 0.9, "lavender", 0.7), (-1, 0.7, "void", 1.5))); C += blade
    return C

def slaughter_bringer_cubes():
    # Slaughter Bringer, after the anime: a polearm with a ragged black blade veined in pink, torn spikes down both
    # sides, on a banded shaft
    C = [cube(-0.75, 10.2, -0.75, 1.5, 29, 1.5, "void"), cube(-1.2, 37.6, -1.2, 2.4, 1.4, 2.4, "rose")]
    for gy in (13, 17, 21, 25, 29, 33):
        C.append(cube(-0.95, gy, -0.95, 1.9, 1.4, 1.9, "teal"))
    path = [(5, 8, 5.6), (5, -3, 6.6), (4.5, -14, 5.4), (3.5, -27, 3.2)]
    blade, j = chain2((0, 38.6), path, 1, "void", strips=((1, 0.6, "rose", 0.6),)); C += blade
    vein, _ = chain2((0, 38.6), [(L, a, 0.6) for L, a, w in path], 1.25, "rose"); C += vein
    for k, (off, a, L) in enumerate(((1.2, 70, 3.2), (3.4, 62, 3.6), (1.6, -72, 3), (4, -64, 3.4), (2.4, 58, 3), (2.2, -60, 2.6), (1.6, 50, 2.2))):
        x, y = j[min(k // 2, 3)]; y += off
        C.append(P(x - 0.6, y, 1.2, L, 0.8, "void", [0, 0, a], [x, y, 0]))
    return C

def caledfwlch_cubes():
    # Holy Spear Caledfwlch, after the anime: an all-gold spear whose head is an open diamond frame over a pair of
    # swept side blades
    C = [cube(-0.5, 10.2, -0.5, 1, 1.6, 1, "amber"), cube(-0.7, 11.2, -0.7, 1.4, 30, 1.4, "gold"),
         cube(-1.2, 41, -1.2, 2.4, 1.6, 2.4, "amber")]
    for sx in (-1, 1):
        C.append(P(-0.6, 42.4, 1.2, 5.6, 0.9, "gold", [0, 0, sx * 58], [0, 42.8, 0]))        # side blades
        C.append(P(-0.55, 43.2, 1.1, 6, 0.9, "gold", [0, 0, sx * 31], [0, 43.4, 0]))         # lower bars of the frame
        C.append(P(sx * 3.05 - 0.55, 48.3, 1.1, 6, 0.9, "gold", [0, 0, -sx * 31], [sx * 3.05, 48.5, 0]))   # upper bars
    C += [P(-0.5, 53.2, 1, 2.2, 0.9, "amber"), diamond(0, 55.4, 0.7, 0.9, "amber")]
    return C

# ---------------- icons drawn from the models ----------------
def icon_from(cubes, flip=False):
    S = 32; th = math.radians(45); tex = texture().load()
    def to_icon(x, y):   # model -> icon frame (y up)
        if flip: x = -x
        return (x * math.cos(th) + y * math.sin(th), -x * math.sin(th) + y * math.cos(th))
    pts = []
    for q in cubes:
        (x0, y0, _), (w, h, _) = q["origin"], q["size"]; a = math.radians((q.get("rotation") or [0, 0, 0])[2])
        px, py = (q.get("pivot") or [0, 0, 0])[:2]
        for cx, cy in ((x0, y0), (x0 + w, y0), (x0, y0 + h), (x0 + w, y0 + h)):
            dx, dy = cx - px, cy - py
            pts.append(to_icon(px + dx * math.cos(a) + dy * math.sin(a), py - dx * math.sin(a) + dy * math.cos(a)))
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    sc = max(max(xs) - min(xs), max(ys) - min(ys)) / 29.0; cx0, cy0 = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); filled = set()
    for py_ in range(S):
        for px_ in range(S):
            iu, iv = cx0 + (px_ + .5 - 16) * sc, cy0 - (py_ + .5 - 16) * sc
            mx, my = iu * math.cos(th) - iv * math.sin(th), iu * math.sin(th) + iv * math.cos(th)
            if flip: mx = -mx
            best = None
            for q in cubes:
                (x0, y0, z0), (w, h, d) = q["origin"], q["size"]; a = math.radians((q.get("rotation") or [0, 0, 0])[2])
                pvx, pvy = (q.get("pivot") or [0, 0, 0])[:2]
                dx, dy = mx - pvx, my - pvy
                lx, ly = pvx + dx * math.cos(a) - dy * math.sin(a), pvy + dx * math.sin(a) + dy * math.cos(a)
                if x0 <= lx < x0 + w and y0 <= ly < y0 + h:
                    key = d
                    if best is None or key > best[0]:
                        ox, oy = tile_origin(q["_m"], "mid")
                        best = (key, tex[int(ox + q["_uo"] + min(lx - x0, TILE_W - 1)), int(oy + min(y0 + h - ly, TILE_H - 1))])
            if best: im.putpixel((px_, py_), best[1]); filled.add((px_, py_))
    for y in range(S):
        for x in range(S):
            if (x, y) in filled: continue
            nb = [im.getpixel((x + dx, y + dy)) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) in filled]
            if nb:
                r, g, b = [sum(p[i] for p in nb) / len(nb) for i in range(3)]
                im.putpixel((x, y), (int(r * 0.28), int(g * 0.26), int(b * 0.36 + 8), 255))
    return im
