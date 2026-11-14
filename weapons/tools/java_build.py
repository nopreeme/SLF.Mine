"""Java Edition 26.2 resource pack (format 88) + datapack (format 107) for the SLF weapons."""
import json, math, os, shutil, zipfile
import numpy as np
from PIL import Image
import mp

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "java_out")
RP, DP = f"{OUT}/SLF_Weapons_ResourcePack", f"{OUT}/SLF_Weapons_Datapack"

# name, display, cubes, base item, damage, attack speed, pair display name (or None)
WEAPONS = [
    ("wood_staff", "Wood Staff", mp.staff_cubes, "stick", 4, 1.4, None),
    ("iron_hammer", "Iron Hammer", mp.hammer_cubes, "stick", 8, 0.8, None),
    ("iron_sword", "Iron Sword", mp.iron_sword_cubes, "iron_sword", 6, 1.6, None),
    ("iron_dagger", "Iron Dagger", mp.iron_dagger_cubes, "iron_sword", 4, 2.4, None),
    ("marsh_dagger", "Marsh Dagger", mp.marsh_dagger_cubes, "iron_sword", 5, 2.6, "Marsh Daggers"),
    ("mercenary_blade", "Mercenary's Blade", mp.mercenary_blade_cubes, "iron_sword", 6, 2.2, "Mercenary's Blades"),
    ("vorpal_chopper", "Vorpal Chopper", mp.vorpal_chopper_cubes, "iron_sword", 7, 2.4, "Vorpal Choppers"),
    ("fossil_rod", "Fossil Rod", mp.fossil_rod_cubes, "stick", 3, 1.6, None),
    ("wood_shield", "Wood Shield", mp.wood_shield_cubes, "shield", None, None, None),
]

def r4(v): return round(float(v), 4)

def corners(q):
    (x0, y0, _), (w, h, _) = q["origin"], q["size"]; a = math.radians((q.get("rotation") or [0, 0, 0])[2])
    px, py = (q.get("pivot") or [0, 0, 0])[:2]
    for cx, cy in ((x0, y0), (x0 + w, y0), (x0, y0 + h), (x0 + w, y0 + h)):
        dx, dy = cx - px, cy - py
        yield px + dx * math.cos(a) + dy * math.sin(a), py - dx * math.sin(a) + dy * math.cos(a)

def element(q, oy):
    (x0, y0, z0), (w, h, d) = q["origin"], q["size"]
    a = (q.get("rotation") or [0, 0, 0])[2]; px, py = (q.get("pivot") or [0, 0, 0])[:2]
    k = int(math.floor(a / 90 + 0.5)); r = a - 90 * k; km = k % 4
    pts = [(x0 - px, y0 - py), (x0 + w - px, y0 + h - py)]
    for _ in range(km): pts = [(dy, -dx) for dx, dy in pts]          # quarter turns baked into the box
    nx0, nx1 = sorted((pts[0][0] + px, pts[1][0] + px)); ny0, ny1 = sorted((pts[0][1] + py, pts[1][1] + py))
    el = {"from": [r4(nx0 + 8), r4(ny0 - oy), r4(z0 + 8)], "to": [r4(nx1 + 8), r4(ny1 - oy), r4(z0 + d + 8)]}
    if abs(r) > 1e-6:
        el["rotation"] = {"angle": -r, "axis": "z", "origin": [r4(px + 8), r4(py - oy), 8]}
    odd = km % 2 == 1
    def face(name, fw, fh, rot, uo=0):
        ox, oy_ = mp.tile_origin(q["_m"], mp.FACE_SHADE[name])
        fw, fh = min(fw, mp.TILE_W), min(fh, mp.TILE_H)
        f = {"uv": [r4((ox + uo) / 16), r4(oy_ / 16), r4((ox + uo + fw) / 16), r4((oy_ + fh) / 16)], "texture": "#0"}
        if rot: f["rotation"] = rot
        return f
    uo = q.get("_uo", 0)
    if not odd:
        el["faces"] = {"north": face("north", w, h, 0, uo), "south": face("south", w, h, 0, uo),
                       "east": face("east", d, h, 0), "west": face("west", d, h, 0),
                       "up": face("up", w, d, 0), "down": face("down", w, d, 0)}
    else:
        el["faces"] = {"north": face("north", w, h, 90, uo), "south": face("south", w, h, 90, uo),
                       "up": face("up", d, h, 90), "down": face("down", d, h, 90),
                       "east": face("east", d, w, 0), "west": face("west", d, w, 0)}
    return el

def Rx(a): a = math.radians(a); c, s = math.cos(a), math.sin(a); return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
def Ry(a): a = math.radians(a); c, s = math.cos(a), math.sin(a); return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
def Rz(a): a = math.radians(a); c, s = math.cos(a), math.sin(a); return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
def R(rot): return Rx(rot[0]) @ Ry(rot[1]) @ Rz(rot[2])
C = np.array([8.0, 8, 8]); GRIP = np.array([3.0, 3, 8])   # where a vanilla handheld sprite sits in the fist

def hand(T, s, rot, f, h, tilt=0, yaw=0):
    """Re-express vanilla 'handheld' for an upright model whose grip is at h (instead of a diagonal sprite).
    tilt leans the weapon away from the camera, yaw turns it about its own length; the grip point stays where vanilla has it."""
    T = np.array(T, float); rot2 = [rot[0], rot[1] + yaw, rot[2] - 45 + tilt]; s2 = s * f
    T2 = T + s * (R(rot) @ (GRIP - C)) - s2 * (R(rot2) @ (h - C))
    return {"rotation": rot2, "translation": [r4(v) for v in T2], "scale": [r4(s2)] * 3}

def centered(rot, s, bc, lift=0):
    T = -s * (R(rot) @ (bc - C)) + np.array([0, lift, 0])
    return {"rotation": rot, "translation": [r4(v) for v in T], "scale": [s] * 3}

# Weapons whose +x side (the sharp edge) should face down in the hand; by default +x faces up.
EDGE_DOWN = {"mercenary_blade", "marsh_dagger"}

def other_side(t):
    """Same hold turned half a turn about the weapon's length (the grip stays in the fist)."""
    r = t["rotation"]; y = r[1] + 180
    return dict(t, rotation=[r[0], y - 360 if y > 180 else y, -r[2]])

# First-person hold for weapons (not the shield), relative to vanilla's handheld pose. Vanilla leans the item 20
# degrees toward the camera; with long 3D models the top then balloons and leaves the screen. FP_TILT leans it back
# by that many degrees (20 = upright), FP_YAW turns the flat of a blade toward the player, FP_SHIFT_X nudges it
# sideways (pixels, negative = toward the middle). Tuned with java_preview.py against in-game screenshots.
# 35/35/-1.5 was tried and read as leaning and angled too far in; Evan wants it close to vanilla's look.
FP_TILT, FP_YAW, FP_SHIFT_X = 12, 10, 0

def model(cubes, size=0.75, flip=False, both_hands=True, fp_size=None, fp_tilt=0, fp_yaw=0, fp_shift_x=0):
    """size / fp_size: third / first person scale relative to a vanilla handheld item's own scale (fp_size defaults to size).
    fp_tilt / fp_yaw / fp_shift_x: first-person adjustments relative to vanilla's handheld pose (see FP_TILT)."""
    pts = [p for q in cubes for p in corners(q)]
    ymin, ymax = min(p[1] for p in pts), max(p[1] for p in pts); xmin, xmax = min(p[0] for p in pts), max(p[0] for p in pts)
    oy = max(20, math.ceil(ymax - 31.5))
    assert ymin - oy >= -16 and xmin + 8 >= -16 and xmax + 8 <= 32, (ymin, ymax, xmin, xmax)
    h = np.array([8.0, 24 - oy, 8]); bc = np.array([8 + (xmin + xmax) / 2, (ymin + ymax) / 2 - oy, 8])
    big = max(xmax - xmin, ymax - ymin)
    tp, fp = hand([0, 4, 0.5], 0.85, [0, -90, 55], size, h), hand([1.13 + fp_shift_x, 3.2, 1.13], 0.68, [0, -90, 25], fp_size or size, h, fp_tilt, fp_yaw)
    if flip: tp, fp = other_side(tp), other_side(fp)
    display = {"thirdperson_righthand": tp, "firstperson_righthand": fp}
    if both_hands:
        # Without left-hand entries the game reuses the right-hand ones with y/z rotation negated, which turns a
        # blade over (edge up in one hand, down in the other). Pre-negating cancels that, so the left hand is a
        # true mirror image. Only valid for models symmetric front-to-back (z), i.e. everything but the shield.
        display["thirdperson_lefthand"], display["firstperson_lefthand"] = other_side(tp), other_side(fp)
    display.update({"ground": centered([0, 0, 0], r4(min(0.5, 14 / big)), bc, 2),
                    "fixed": centered([0, 180, -45], r4(min(0.9, 20 / big)), bc),
                    "head": centered([0, 0, 0], 1, bc, 14)})
    return {"credit": "SLF.Mine weapons", "texture_size": [mp.ATLAS_W, mp.ATLAS_H],
            "textures": {"0": "slf:item/weapons_atlas", "particle": "slf:item/weapons_atlas"},
            "elements": [element(q, oy) for q in cubes],
            "display": display}

# Vanilla 26.2 shield hand poses (models/item/shield.json -> shield_blocking.json): (rotation, translation) pairs
SHIELD_VANILLA = {
    "thirdperson_righthand": (([0, 90, 0], [10, 6, -4]), ([45, 155, 0], [-3.49, 11, -2])),
    "thirdperson_lefthand": (([0, 90, 0], [10, 6, 12]), ([45, 155, 0], [11.51, 7, 2.5])),
    "firstperson_righthand": (([0, 180, 5], [-10, 1.75, -10]), ([0, 180, -5], [-15, 3.25, -11])),
    "firstperson_lefthand": (([0, 180, 5], [10, 0, -10]), ([0, 180, -5], [5, 5, -11])),
}

def applied(rot, t, left):
    """What the game actually applies: the left hand negates x translation and y/z rotation."""
    if left: return R([rot[0], -rot[1], -rot[2]]), np.array([-t[0], t[1], t[2]], float)
    return R(rot), np.array(t, float)

def euler_xyz(M):
    """Inverse of R(): angles (x, y, z) with M = Rx @ Ry @ Rz."""
    b = math.asin(max(-1.0, min(1.0, M[0, 2])))
    if abs(M[0, 2]) > 0.99999:   # gimbal lock: fold z into x
        a, cz = math.atan2(M[2, 1], M[1, 1]), 0.0
    else:
        a, cz = math.atan2(-M[1, 2], M[2, 2]), math.atan2(-M[0, 1], M[0, 0])
    out = [math.degrees(a), math.degrees(b), math.degrees(cz)]
    assert np.allclose(R(out), M, atol=1e-6), out
    return out

def blocking_display(disp):
    """Hand poses for blocking: move our normal pose by the same rigid motion vanilla's shield makes when raised."""
    out = {}
    for ctx, ((rn, tn), (rb, tb)) in SHIELD_VANILLA.items():
        left = ctx.endswith("lefthand")
        own = disp.get(ctx) or disp[ctx.replace("lefthand", "righthand")]   # missing left-hand entries fall back to right
        Rn, Tn = applied(rn, tn, left); Rb, Tb = applied(rb, tb, left); Ro, To = applied(own["rotation"], own["translation"], left)
        D = Rb @ Rn.T
        r, t = euler_xyz(D @ Ro), Tb + D @ (To - Tn)
        if left: r, t = [r[0], -r[1], -r[2]], [-t[0], t[1], t[2]]
        out[ctx] = {"rotation": [r4(v) for v in r], "translation": [r4(v) for v in t], "scale": own["scale"]}
    return out

def wj(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f: json.dump(obj, f, indent=1)
def wt(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f: f.write(text)

def components(name, display, base, dmg, spd, extra):
    c = [f'minecraft:item_model="slf:{name}"', f'minecraft:item_name="{display}"']
    if base == "stick": c.append("minecraft:max_stack_size=1")
    if dmg is not None:
        c.append('minecraft:attribute_modifiers=[{type:"minecraft:attack_damage",id:"minecraft:base_attack_damage",amount:%s,operation:"add_value",slot:"mainhand"},'
                 '{type:"minecraft:attack_speed",id:"minecraft:base_attack_speed",amount:%s,operation:"add_value",slot:"mainhand"}]' % (dmg - 1, round(spd - 4, 2)))
    c.append("minecraft:custom_data={slf:{%s}}" % extra)
    return f"minecraft:{base}[{','.join(c)}]"

def build():
    shutil.rmtree(OUT, ignore_errors=True)
    # ---------- resource pack ----------
    wj(f"{RP}/pack.mcmeta", {"pack": {"description": "SLF.Mine weapons (3D in hand, flat icons)", "min_format": 88, "max_format": 88}})
    os.makedirs(f"{RP}/assets/slf/textures/item", exist_ok=True)
    mp.texture().save(f"{RP}/assets/slf/textures/item/weapons_atlas.png")
    icons = {}
    for name, display, fn, base, dmg, spd, pair in WEAPONS:
        weapon = base != "shield"
        cubes = fn(); m = model(cubes, flip=name in EDGE_DOWN, both_hands=weapon,
                                fp_tilt=FP_TILT if weapon else 0, fp_yaw=FP_YAW if weapon else 0, fp_shift_x=FP_SHIFT_X if weapon else 0)
        wj(f"{RP}/assets/slf/models/item/{name}.json", m)
        icons[name] = mp.icon_from(cubes); icons[name].save(f"{RP}/assets/slf/textures/item/{name}_icon.png")
        wj(f"{RP}/assets/slf/models/item/{name}_icon.json", {"parent": "minecraft:item/generated", "textures": {"layer0": f"slf:item/{name}_icon"}})
        held = {"type": "minecraft:model", "model": f"slf:item/{name}"}
        if base == "shield":   # raise it while blocking, like the vanilla shield
            wj(f"{RP}/assets/slf/models/item/{name}_blocking.json", {"parent": f"slf:item/{name}", "display": blocking_display(m["display"])})
            held = {"type": "minecraft:condition", "property": "minecraft:using_item",
                    "on_true": {"type": "minecraft:model", "model": f"slf:item/{name}_blocking"}, "on_false": held}
        wj(f"{RP}/assets/slf/items/{name}.json", {"model": {"type": "minecraft:select", "property": "minecraft:display_context",
            "cases": [{"when": "gui", "model": {"type": "minecraft:model", "model": f"slf:item/{name}_icon"}}],
            "fallback": held}})
    pi = Image.new("RGBA", (128, 128), (24, 44, 84, 255))
    pi.alpha_composite(icons["marsh_dagger"].resize((96, 96), Image.NEAREST), (0, 32))
    pi.alpha_composite(icons["iron_hammer"].resize((96, 96), Image.NEAREST), (32, 0))
    pi.save(f"{RP}/pack.png")
    # ---------- datapack ----------
    wj(f"{DP}/pack.mcmeta", {"pack": {"description": "SLF.Mine weapons: give functions + paired weapons", "min_format": 107, "max_format": 107}})
    pi.save(f"{DP}/pack.png")
    F = f"{DP}/data/slf/function/weapons"; allf = []; check = ["# Runs as each player, every tick. Keeps the off-hand twin of a paired weapon in sync."]
    for name, display, fn, base, dmg, spd, pair in WEAPONS:
        if pair:
            item = components(name, pair, base, dmg, spd, f'weapon:"{name}",pair:"{name}"')
            twin = components(name, pair, "stick", None, None, f'twin:"{name}",is_twin:1b')
            sel = '*[minecraft:custom_data~{slf:{pair:"%s"}}]' % name
            check += [f"# {pair}",
                      'execute unless items entity @s weapon.mainhand %s run clear @s *[minecraft:custom_data~{slf:{twin:"%s"}}]' % (sel, name),
                      f"execute if items entity @s weapon.mainhand {sel} unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with {twin}"]
        else:
            item = components(name, display, base, dmg, spd, f'weapon:"{name}"')
        wt(f"{F}/give/{name}.mcfunction", f"give @s {item}\n"); allf.append(f"function slf:weapons/give/{name}")
    wt(f"{F}/give_all.mcfunction", "\n".join(allf) + "\n")
    wt(f"{F}/pairs/check.mcfunction", "\n".join(check) + "\n")
    wt(f"{F}/pairs/tick.mcfunction", "execute as @a run function slf:weapons/pairs/check\n"
       "# twins are display-only: remove any that get dropped\n"
       "execute as @e[type=minecraft:item] if items entity @s contents *[minecraft:custom_data~{slf:{is_twin:1b}}] run kill @s\n")
    wj(f"{DP}/data/minecraft/tags/function/tick.json", {"values": ["slf:weapons/pairs/tick"]})
    for root in (RP, DP):
        with zipfile.ZipFile(root + ".zip", "w", zipfile.ZIP_DEFLATED) as zf:
            for dp_, _, fs in os.walk(root):
                for fn_ in fs:
                    full = os.path.join(dp_, fn_); zf.write(full, os.path.relpath(full, root))

if __name__ == "__main__":
    build()
    # checks
    import glob
    for f in glob.glob(OUT + "/**/*.json", recursive=True) + glob.glob(OUT + "/**/*.mcmeta", recursive=True): json.load(open(f))
    for f in glob.glob(RP + "/assets/slf/models/item/*.json"):
        m = json.load(open(f))
        for e in m.get("elements", []):
            assert all(-16 <= v <= 32 for v in e["from"] + e["to"]), (f, e["from"], e["to"])
            if "rotation" in e: assert -45 <= e["rotation"]["angle"] <= 45, (f, e["rotation"])
            for fc in e["faces"].values(): assert all(0 <= v <= 16 for v in fc["uv"]), (f, fc)
    m = json.load(open(RP + "/assets/slf/models/item/iron_sword.json"))
    print(len(m["elements"]), json.dumps(m["display"]["thirdperson_righthand"]), json.dumps(m["display"]["firstperson_righthand"]))
    print(open(DP + "/data/slf/function/weapons/give/marsh_dagger.mcfunction").read())
    print(open(DP + "/data/slf/function/weapons/pairs/check.mcfunction").read()[:900])
    print("ok")
