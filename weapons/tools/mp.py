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
MATS = list(RAMPS)
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
