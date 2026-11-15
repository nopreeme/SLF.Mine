"""MinePiece-style 32x32 sprites: clean 3-5 tone shading, colored outlines, no noise.
Each sprite doubles as the inventory icon and the source for the extruded held model."""
import math
from PIL import Image

S = 32
CLEAR = (0, 0, 0, 0)

def seg_dist(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L2))
    cx, cy = ax + t * dx, ay + t * dy
    return math.hypot(px - cx, py - cy), t, (cx, cy), (dx, dy)

LIGHT_DIR = (-1 / math.sqrt(2), -1 / math.sqrt(2))  # light from the upper left

def thick_path(pts, radii):
    """Return {pixel: s} for pixels inside a variable-width polyline.
    s in [-1, 1] = which side of the line the pixel is on (+1 = lit side)."""
    out = {}
    for y in range(S):
        for x in range(S):
            p = (x + .5, y + .5); best = None
            for i in range(len(pts) - 1):
                d, t, c, (dx, dy) = seg_dist(p, pts[i], pts[i + 1])
                r = radii[i] + (radii[i + 1] - radii[i]) * t
                if d <= r and (best is None or d / r < best[0]):
                    L = math.hypot(dx, dy) or 1
                    n = (-dy / L, dx / L)
                    if n[0] * LIGHT_DIR[0] + n[1] * LIGHT_DIR[1] < 0: n = (-n[0], -n[1])
                    s = ((p[0] - c[0]) * n[0] + (p[1] - c[1]) * n[1]) / r
                    best = (d / r, s)
            if best: out[(x, y)] = best[1]
    return out

def outline(px, filled, color):
    for y in range(S):
        for x in range(S):
            if (x, y) in filled: continue
            if any((x + dx, y + dy) in filled for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                px[x, y] = color

def tone(s, ramp):
    """ramp = [shadow, mid, light, highlight]"""
    if s > .5: return ramp[3]
    if s > .05: return ramp[2]
    if s > -.5: return ramp[1]
    return ramp[0]

# ---------------- Wood Staff ----------------
W_OUT = (40, 27, 25, 255)
W_RAMP = [(78, 54, 45, 255), (106, 77, 61, 255), (138, 104, 81, 255), (170, 135, 104, 255)]
W_KNOT = (62, 43, 37, 255)

STAFF_PATH = [(3, 29), (5, 26.5), (8, 24.5), (10, 21), (13, 19.5), (14.5, 16.5), (17, 14.5),
              (18.5, 11.5), (21, 9.5), (22.5, 7), (24.5, 5), (26.5, 3.8), (28.5, 4.2), (29.3, 6), (28.4, 8.3)]
STAFF_R = [0.9, 1.15, 1.3, 1.35, 1.3, 1.75, 1.3, 1.3, 1.35, 1.8, 1.3, 1.15, 1.05, 0.95, 0.75]
STAFF_TWIG = [(21.3, 9.2), (19.4, 6.4), (19.6, 3.6)]
STAFF_TWIG_R = [0.95, 0.8, 0.6]
STAFF_GRIP_PX = (9, 22.5)   # where the hand goes

def staff_sprite(depth=False):
    im = Image.new("RGBA", (S, S), CLEAR); px = im.load(); D = {}
    twig = thick_path(STAFF_TWIG, STAFF_TWIG_R)
    shape = dict(twig)
    shape.update(thick_path(STAFF_PATH, STAFF_R))
    for (x, y), s in shape.items():
        px[x, y] = tone(s, W_RAMP)
        D[(x, y)] = 2 if (x, y) in twig and (x, y) not in thick_path(STAFF_PATH, STAFF_R) else (4 if abs(s) < .5 else 2)
    # knot rings and bark marks on the shaded side
    for (x, y) in [(14, 16), (15, 17), (22, 7), (23, 6), (11, 21), (18, 12), (7, 25)]:
        if (x, y) in shape: px[x, y] = W_KNOT; D[(x, y)] = 5
    for (x, y) in [(14, 15), (15, 16), (13, 16), (22, 6), (21, 7), (23, 7)]:  # knot bulges
        if (x, y) in shape: D[(x, y)] = 5
    outline(px, shape, W_OUT)
    return (im, D) if depth else im

# ---------------- Iron Hammer (Gray Ore) ----------------
M_OUT = (36, 36, 52, 255)
M_RAMP = [(86, 90, 114, 255), (128, 134, 160, 255), (170, 176, 200, 255), (220, 224, 238, 255)]
CAP_RAMP = [(62, 64, 84, 255), (92, 96, 120, 255), (118, 123, 148, 255), (150, 156, 180, 255)]
H_RAMP = [(46, 40, 54, 255), (66, 58, 76, 255), (88, 78, 100, 255), (112, 100, 124, 255)]
GRIP_L, GRIP_D = (216, 208, 188, 255), (150, 140, 124, 255)

HANDLE = [(3, 28.5), (19.5, 12)]
HAMMER_GRIP_PX = (7.5, 24)

def hammer_sprite(depth=False):
    im = Image.new("RGBA", (S, S), CLEAR); px = im.load(); D = {}
    filled = set()
    u = (1 / math.sqrt(2), -1 / math.sqrt(2))   # along handle, toward head
    w = (1 / math.sqrt(2), 1 / math.sqrt(2))    # across handle = head's long axis
    hc = (20.9, 10.9)
    # handle
    hp = thick_path(HANDLE, [1.05, 1.05])
    for (x, y), s in hp.items():
        a = ((x + .5 - 3) * u[0] + (y + .5 - 28.5) * u[1])
        if 1.5 < a < 9:  # wrapped grip with diagonal bands like the anime's markings
            band = int(a * 1.4) % 2 == 0
            px[x, y] = (GRIP_L if s > -.6 else GRIP_D) if band else GRIP_D
            D[(x, y)] = 4 if band else 3
        else:
            px[x, y] = tone(s, H_RAMP); D[(x, y)] = 3
        filled.add((x, y))
    # pommel
    for y in range(S):
        for x in range(S):
            if math.hypot(x + .5 - 3.2, y + .5 - 28.3) <= 1.7:
                px[x, y] = CAP_RAMP[1] if (x + y) % 2 else CAP_RAMP[2]; filled.add((x, y)); D[(x, y)] = 4
    # head
    for y in range(S):
        for x in range(S):
            dx, dy = x + .5 - hc[0], y + .5 - hc[1]
            a = dx * u[0] + dy * u[1]      # thickness direction (+ = top)
            b = dx * w[0] + dy * w[1]      # length direction
            cap = abs(b) > 6.2
            half_t = 5.0 if cap else 4.2
            if abs(b) <= 9.0 and abs(a) <= half_t:
                if cap:
                    ramp = CAP_RAMP; s = a / half_t
                    if abs(b) > 8.2: s += .6       # bright striking face
                else:
                    ramp = M_RAMP; s = a / half_t * 1.1
                c = tone(s, ramp)
                if not cap and abs(abs(b) - 6.2) < .8: c = CAP_RAMP[0]   # seam line
                if not cap and a > half_t - 1.1 and b < 2: c = M_RAMP[3]  # bevel glint
                px[x, y] = c; filled.add((x, y))
                d = 10 if cap else 8                       # chunky head, caps stick out further
                if abs(a) > half_t - 1.2: d -= 2           # beveled top/bottom edge
                if cap and abs(b) > 8.2: d -= 1            # striking face lip
                if not cap and abs(abs(b) - 6.2) < .8: d = 7  # recessed seam
                D[(x, y)] = d
    outline(px, filled, M_OUT)
    return (im, D) if depth else im

if __name__ == "__main__":
    out = Image.new("RGBA", (S * 16 + 20, S * 8), (139, 110, 80, 255))
    out.alpha_composite(staff_sprite().resize((S * 8, S * 8), Image.NEAREST), (0, 0))
    out.alpha_composite(hammer_sprite().resize((S * 8, S * 8), Image.NEAREST), (S * 8 + 20, 0))
    out.save("sprites_preview.png")
