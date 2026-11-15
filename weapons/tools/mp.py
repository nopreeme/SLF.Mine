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
    C = [P(-1.25, 18.5, 2.5, 1.5, 2.5, "steel"), P(-1, 20, 2, 7, 2, "handle"),
         P(-2.75, 27, 7, 1.75, 2.5, "steel", [0, 0, -8], [0, 27.8, 0]),
         P(-2, 28.75, 4, 14, 1, "silver"), P(2, 28.75, 1, 14, 0.6, "face"), P(-1.25, 29.5, 0.75, 12.5, 1.3, "cap")]
    for y0, w, h in ((42.75, 4.25, 2.5), (45.25, 3.25, 2), (47.25, 2.25, 1.75), (49, 1.25, 1.5)):   # clip point
        C.append(P(-2, y0, w, h, 1, "silver")); C.append(P(-2 + w, y0, 0.75, h, 0.6, "face"))
    return C

def marsh_dagger_cubes():
    C = [P(-1.3, 17.5, 2.6, 2.2, 2.6, "rim"), P(-0.9, 19.5, 1.8, 7.5, 1.8, "mgrip"),
         P(-2.5, 27, 5, 3.5, 2.75, "olive"), P(-1.5, 30, 3, 1, 2.2, "olive"),
         P(1.75, 28, 1.75, 4.5, 1.75, "olive", [0, 0, 68], [2.5, 28.6, 0])]
    blade, _ = chain2((0, 30.8), [(5, 18, 3.5), (5, -24, 3.5), (5, 22, 3.2), (4.5, -20, 2.6), (3.5, 12, 1.8), (2.5, -5, 1)],
                      1, "marsh", strips=((1, 0.8, "medge", 0.6), (-1, 0.6, "mdark", 1.2)))
    return C + blade

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
    C.append(cube(-1, 22.5, -1.5, 2, 3, 1.5, "rim"))   # hand strap
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

def vorpal_knife_cubes():
    # after the anime's Vorpal Chopper: a long narrow crimson blade, no guard, dark wrapped grip
    C = [P(-1.1, 17.4, 2.2, 1.3, 2.2, "rim"), P(-0.9, 18.7, 1.8, 8.6, 1.8, "knot"), P(-1.2, 27.3, 2.4, 0.9, 2.2, "rim")]
    blade, _ = chain2((0, 28.2), [(5, 3, 2.6), (5, -1, 3.2), (5, -4, 3), (4, -7, 2.2), (3, -12, 1.2)], 1, "crimson",
                      strips=((1, 0.7, "rose", 0.6), (-1, 0.6, "knot", 1.2))); C += blade
    C.append(P(-2.7, 40, 1.3, 2.4, 1, "crimson", [0, 0, -32], [-1.5, 40, 0]))            # step on the spine
    return C

def rust_saber_cubes():
    C = [P(-1.3, 18.3, 2.6, 1.7, 2.6, "knot"), P(-0.9, 20, 1.8, 7, 1.8, "wood"), P(-2.4, 27, 5.6, 1.4, 2.4, "rust")]
    bow, _ = chain((2.8, 27.6), [(3.4, 166, 0.9), (3.2, 190, 0.9), (2.6, 236, 0.9)], "rust"); C += bow    # knuckle bow
    blade, _ = chain2((0, 28.4), [(6, 0, 3.4), (6, -5, 3.4), (5, -11, 3.1), (4, -18, 2.5), (3, -27, 1.5)], 1, "rust",
                      strips=((-1, 0.7, "knot", 1.3), (1, 0.6, "wrap", 0.6))); C += blade
    return C

def lycagon_fang_cubes():
    C = [diamond(0, 18.2, 2, 2, "aqua"), P(-1.2, 19, 2.4, 1.2, 2.4, "silver"), P(-0.9, 20.2, 1.8, 6.8, 1.8, "cloth"),
         P(-3, 27, 6, 1.4, 2.4, "silver"),
         P(-4.4, 26.6, 2.4, 1.2, 2, "silver", [0, 0, -28], [-3, 27.6, 0]), P(2, 26.6, 2.4, 1.2, 2, "silver", [0, 0, 28], [3, 27.6, 0])]
    blade, _ = chain2((0, 28.4), [(5, -8, 4.4), (5, -2, 4.6), (4.5, 8, 4.2), (4, 19, 3.4), (3.5, 31, 2.3), (2.6, 44, 1.2)], 1, "night",
                      strips=((1, 0.9, "face", 0.6), (-1, 0.6, "cap", 1.3))); C += blade
    return C

def wethermon_katana_cubes():
    # after the manga cover: a long nodachi, black grip crossed with rose cord, dark ring guard
    C = [P(-1.1, 13.4, 2.2, 1.2, 2.2, "cap"), P(-0.9, 14.6, 1.8, 12, 1.8, "cloth"),
         P(-2.5, 26.6, 5, 0.9, 4.4, "cap"), P(-1.7, 26.4, 3.4, 1.3, 5, "cap"), P(-1, 27.6, 2, 1.2, 1.4, "steel")]
    C += bands((16, 18.4, 20.8, 23.2), 2.1, "rose", 0.7)
    blade, _ = chain2((0, 28.8), [(7, 0, 2.3), (7, -3, 2.3), (6, -6, 2.2), (5, -9, 2), (3.4, -13, 1.6), (2, -22, 0.9)], 0.9, "silver",
                      strips=((1, 0.6, "face", 0.5), (-1, 0.5, "cap", 1.1))); C += blade
    return C

def wethermon_rib_dagger_cubes():
    C = [diamond(0, 18.3, 1.8, 1.8, "orchid"), P(-1.1, 19, 2.2, 1.2, 2.2, "cap"), P(-0.9, 20.2, 1.8, 6.8, 1.8, "handle"),
         P(-2.3, 27, 4.6, 1.3, 2.4, "cap")]
    rib, j = chain2((0, 28.3), [(4, -10, 2.4), (4, 0, 2.4), (4, 11, 2.2), (3.5, 22, 1.8), (3, 34, 1.2)], 1.4, "bone",
                    strips=((1, 0.6, "face", 0.7),)); C += rib
    for kx, ky in j[1:4]: C.append(diamond(kx - 0.9, ky, 1.3, 1.8, "bone"))      # knuckles along the back of the rib
    return C

def wethermon_scythe_cubes():
    C, j = chain((0, 11), [(14, 0, 1.5), (14, -2, 1.5), (12, 2, 1.5)], "bone")
    C += bands((21.4, 23.4, 25.4), 2.2, "handle") + [diamond(0, 10.6, 2, 2, "orchid")]
    x, y = j[3]
    C += [cube(x - 1.4, y - 3.4, -1.4, 2.8, 2.6, 2.8, "cap"), diamond(x - 0.4, y - 0.4, 3, 2, "cap")]
    blade, _ = chain2((x - 1.2, y - 0.8), [(5, 66, 4.6), (5, 84, 4.3), (4.5, 103, 3.5), (4, 122, 2.5), (3.2, 140, 1.3)], 1, "lilac",
                      strips=((1, 0.8, "face", 0.6), (-1, 0.6, "cap", 1.3))); C += blade
    spur, _ = chain2((x - 0.6, y - 0.6), [(3.4, -72, 1.7), (2, -56, 0.9)], 1, "lilac"); C += spur
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

def bilac_fang_gauntlet_cubes():
    C = _gauntlet("lavender", "gold")
    for x, h in ((-2.6, 3), (-0.9, 4.6), (0.8, 4.6), (2.5, 3)):                 # fangs over the knuckles
        C += [P(x - 0.6, 28.5, 1.2, h, 1.4, "bone"), diamond(x, 28.5 + h, 0.85, 1.4, "bone")]
    C.append(diamond(0, 24.2, 2.6, 6, "handle"))
    return C

def bilac_crescent_blade_cubes():
    C = [diamond(0, 17.4, 2, 2, "gold"), P(-0.9, 18.2, 1.8, 9.2, 1.8, "wood"), P(-1.4, 27.4, 2.8, 1.4, 2.6, "gold")]
    C += bands((20.5, 23, 25.5), 2.3, "gold", 0.9)
    moon, _ = chain2((-0.4, 28.6), [(4.2, -62, 2), (4.2, -34, 3), (4.2, -6, 3.7), (4.2, 22, 4), (4.2, 50, 4), (4.2, 78, 3.6),
                                    (4, 106, 2.9), (3.6, 134, 1.8)], 1, "lavender",
                     strips=((-1, 0.8, "face", 0.6), (1, 0.6, "handle", 1.3))); C += moon
    return C

def nightclaw_talon_cubes():
    C = [diamond(0, 18.2, 2, 2, "orchid"), P(-1, 19, 2, 7.4, 2, "cloth"), P(-2.7, 26.4, 5.4, 2.2, 3.2, "orchid"),
         P(-2.2, 28.4, 4.4, 0.8, 2.4, "cap")]
    claw, _ = chain2((0.2, 29), [(5, -12, 4), (5, 3, 3.8), (4.5, 20, 3.2), (4, 38, 2.4), (3.2, 57, 1.4)], 1.2, "iron",
                     strips=((1, 0.7, "orchid", 0.7),)); C += claw
    spur, _ = chain2((-1.6, 28.8), [(3.6, -34, 1.6), (2.8, -14, 1.2), (2, 8, 0.8)], 1, "iron"); C += spur
    return C

def oriana_scepter_cubes():
    C = [diamond(0, 11.6, 2.2, 2.2, "gold"), cube(-0.9, 12.4, -0.9, 1.8, 29.6, 1.8, "rose")]
    C += bands((20.6, 26.2, 34), 2.4, "gold", 1) + [cube(-1.5, 41, -1.5, 3, 1.2, 3, "gold"), cube(-2.8, 42.2, -1.8, 5.6, 1.8, 3.6, "gold")]
    for x, h in ((-2.2, 2.6), (0, 4), (2.2, 2.6)):                              # crown points
        C += [P(x - 0.6, 44, 1.2, h, 1.4, "gold"), diamond(x, 44 + h, 1.5, 1.4, "gold")]
    C.append(diamond(0, 43.4, 2.4, 4.2, "orchid"))
    return C

def oriana_void_staff_cubes():
    C, j = chain((0, 10), [(12, 0, 1.6), (12, -3, 1.6), (10, 3, 1.6)], "void")
    C += bands((21.4, 23.4, 25.4), 2.3, "handle") + [diamond(0, 9.6, 2, 2, "orchid")]
    x, y = j[3]
    C.append(cube(x - 1.5, y - 1, -1.5, 3, 1.6, 3, "handle"))
    for s in (-1, 1):                                                           # claws holding the orb
        arm, _ = chain((x + s * 0.8, y + 0.4), [(3.6, s * 52, 1.2), (4.2, s * 6, 1.2), (3, s * -38, 1)], "void"); C += arm
    C.append(cube(x - 2.2, y + 3, -2.2, 4.4, 4.4, 4.4, "orchid", [0, 0, 45], [x, y + 5.2, 0]))
    return C

def sunraku_blade_r_cubes():
    C = [diamond(0, 18, 2, 2, "aqua"), P(-1.2, 18.8, 2.4, 1.2, 2.4, "azure"), P(-0.9, 20, 1.8, 7, 1.8, "cloth"),
         P(-3.4, 27, 6.8, 1.3, 2.3, "azure"), P(2.4, 27.3, 1.3, 3.2, 2, "azure", [0, 0, 28], [3, 27.4, 0]),
         diamond(0, 27.7, 2, 2.7, "aqua")]
    blade, _ = chain2((0, 28.3), [(6, 0, 3.2), (5, 3, 3.1), (4, 9, 2.6), (3, 18, 1.6)], 1, "silver",
                      strips=((1, 0.8, "face", 0.6),)); C += blade
    line, _ = chain2((-0.8, 28.3), [(6, 0, 0.7), (5, 3, 0.7), (3, 9, 0.6)], 1.3, "azure"); C += line
    return C

def sunraku_blade_l_cubes(): return mirror(sunraku_blade_r_cubes())

def sunraku_chaos_rod_cubes():
    C, j = chain((0, 10), [(13, 0, 1.6), (12, -3, 1.6), (7, 3, 1.6)], "mgrip")
    C += bands((21.4, 23.4, 25.4), 2.3, "handle") + [diamond(0, 9.6, 2, 2, "emerald")]
    x, y = j[3]
    C += [cube(x - 1.5, y - 1, -1.5, 3, 1.6, 3, "handle"),
          cube(x - 2.4, y + 1.4, -2.4, 4.8, 4.8, 4.8, "emerald", [0, 0, 45], [x, y + 3.8, 0]),
          P(x - 0.8, y + 5.6, 1.6, 4.2, 1.6, "emerald"), diamond(x, y + 9.8, 1.13, 1.6, "emerald"),
          P(x - 4.6, y + 2.4, 1.4, 4.4, 1.4, "emerald", [0, 0, -34], [x - 2.4, y + 3, 0]),
          P(x + 3.2, y + 2.4, 1.4, 3.4, 1.4, "emerald", [0, 0, 34], [x + 2.4, y + 3, 0])]
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
