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
    ("mercenary_blade", "Mercenary Twinblade", mp.mercenary_blade_cubes, "iron_sword", 6, 2.2, "Mercenary Twinblades"),
    ("vorpal_chopper", "Vorpal Chopper", mp.vorpal_chopper_cubes, "iron_sword", 7, 2.4, "Vorpal Choppers"),
    ("fossil_rod", "Fossil Rod", mp.fossil_rod_cubes, "stick", 3, 1.6, None),
    ("wood_shield", "Wood Shield", mp.wood_shield_cubes, "shield", None, None, None),
    # second batch: the main pack's flat weapons, rebuilt in 3D
    ("vorpal_knife", "Vorpal Knife", mp.vorpal_knife_cubes, "iron_sword", 5, 2.6, None),
    ("rust_saber", "Rust Saber", mp.rust_saber_cubes, "iron_sword", 5, 1.8, None),
    ("lycagon_fang", "Lycagon's Fang", mp.lycagon_fang_cubes, "netherite_sword", 9, 1.8, None),
    ("wethermon_katana", "Wethermon's Blade", mp.wethermon_katana_cubes, "netherite_sword", 10, 1.6, None),
    ("wethermon_rib_dagger", "Wethermon's Rib Dagger", mp.wethermon_rib_dagger_cubes, "netherite_sword", 7, 2.4, None),
    ("wethermon_scythe", "Wethermon's Scythe", mp.wethermon_scythe_cubes, "netherite_sword", 11, 1.0, None),
    ("whalelore_goldsheen", "Whalelore: Goldsheen", mp.whalelore_goldsheen_cubes, "diamond_sword", 8, 1.6, None),
    ("whalelore_netherlight", "Whalelore: Netherlight", mp.whalelore_netherlight_cubes, "diamond_sword", 7, 2.0, None),
    ("gilta_brille", "Gilta Brille", mp.gilta_brille_cubes, "golden_sword", 8, 2.0, None),
    ("bilac_crescent_blade", "Bilac's Crescent Blade", mp.bilac_crescent_blade_cubes, "iron_sword", 8, 1.4, None),
    ("bilac_fang_gauntlet", "Bilac's Fang Gauntlet", mp.bilac_fang_gauntlet_cubes, "iron_sword", 7, 2.0, None),
    ("nightclaw_talon", "Nightclaw Talon", mp.nightclaw_talon_cubes, "iron_sword", 7, 2.2, None),
    ("oriana_scepter", "Oriana's Scepter", mp.oriana_scepter_cubes, "stick", 5, 1.4, None),
    ("oriana_void_staff", "Oriana's Void Staff", mp.oriana_void_staff_cubes, "stick", 6, 1.2, None),
    ("sunraku_blade", "Sunraku's Blade", mp.sunraku_blade_cubes, "iron_sword", 6, 2.4, "Sunraku's Blades"),
    ("sunraku_chaos_rod", "Sunraku's Chaos Rod", mp.sunraku_chaos_rod_cubes, "stick", 5, 1.4, None),
    # third batch: weapons from the source, modelled on the Shangri-La Frontier wiki's art and Evan's manga references
    ("togetsu", "Togetsu: Waxing", mp.togetsu_waxing_cubes, "iron_sword", 8, 2.4, "Togetsu"),
    ("ducusram", "Ducusram", mp.ducusram_cubes, "diamond_sword", 8, 2.6, "Ducusram"),
    ("empire_bee_twinblade", "Empire Bee Twinblade", mp.empire_bee_estoc_cubes, "diamond_sword", 7, 2.6, "Empire Bee Twinblade"),
    ("dullahan_decapitator", "General Dullahan's Decapitator", mp.dullahan_decapitator_cubes, "iron_sword", 11, 1.0, None),
    ("vorpal_sledge", "Vorpal Sledge", mp.vorpal_sledge_cubes, "stick", 10, 0.8, None),
    ("blue_predator", "Blue Predator", mp.blue_predator_cubes, "diamond_sword", 9, 1.6, None),
    ("super_cat_teaser", "Super Cat-Teaser Lv.100", mp.super_cat_teaser_cubes, "iron_sword", 6, 2.0, None),
    ("dis_pater", "Dis Pater", mp.dis_pater_cubes, "shield", None, None, None),
    ("flame_decapitator", "Flame General's Decapitator", mp.flame_decapitator_cubes, "diamond_sword", 12, 1.2, None),
    ("zanbaralia", "Darkhelm Spear Zanbaralia", mp.zanbaralia_cubes, "stick", 9, 1.4, None),
    ("giant_killing_skewer", "Giant-Killing Skewer", mp.giant_killing_skewer_cubes, "stick", 9, 1.2, None),
    ("antinomy", "Antinomy", mp.antinomy_cubes, "netherite_sword", 13, 0.9, None),
    ("slaughter_bringer", "Slaughter Bringer", mp.slaughter_bringer_cubes, "stick", 10, 1.2, None),
    ("caledfwlch", "Holy Spear Caledfwlch", mp.caledfwlch_cubes, "stick", 11, 1.3, None),
]

# Pairs whose off-hand blade is a different weapon from the main-hand one: pair name -> the twin's cube list.
# The twin is built as <name>_twin (model, icon and item definition, no give command of its own).
TWINS = {"togetsu": mp.togetsu_waning_cubes, "empire_bee_twinblade": mp.empire_bee_maingauche_cubes}

# The main SLF.Mine resource pack has its own (flat) assets/slf/models/item/<name>.json for some of these weapons.
# With both packs loaded one file would replace the other, so those weapons get a prefixed model file here.
MAIN_MODELS = os.path.join(os.path.dirname(OUT), "..", "resource_pack", "assets", "slf", "models", "item")
def model_id(name): return f"weapon_{name}" if os.path.exists(os.path.join(MAIN_MODELS, f"{name}.json")) else name

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
EDGE_DOWN = {"marsh_dagger", "rust_saber", "lycagon_fang", "wethermon_katana", "wethermon_rib_dagger",
             "wethermon_scythe", "bilac_crescent_blade", "nightclaw_talon", "vorpal_knife", "sunraku_blade",
             "whalelore_goldsheen", "whalelore_netherlight", "gilta_brille", "togetsu", "togetsu_twin", "blue_predator",
             "super_cat_teaser", "antinomy", "slaughter_bringer", "ducusram"}

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

# Vanilla 26.2 shield hand poses (models/item/shield.json -> shield_blocking.json): (rotation, translation) pairs.
# Vanilla's scale is 1 in third person and 1.25 in first person.
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

# Our round board is 19 across; vanilla's plate is 12 x 22. In third person the shield is shrunk about the handle, so
# the grip stays in the fist. In first person no arm is drawn and vanilla shows only the top of its tall plate, so
# there the board is shrunk about a point above it, which puts its top edge where the vanilla plate's top edge is.
SHIELD_SIZE = {"third": 0.7, "first": 0.8}
SHIELD_R, VANILLA_TOP = 9.5, 11.0
SHIELD_PIVOT = {"third": np.array([0.0, 0, -2]),   # centre of the vanilla shield's handle, in model pixels
                "first": np.array([0.0, (VANILLA_TOP - SHIELD_SIZE["first"] * SHIELD_R) / (1 - SHIELD_SIZE["first"]), 1.5])}

def shield_pose(rot, t, s_v, left, view):
    """Vanilla's shield pose, with the model shrunk by SHIELD_SIZE about SHIELD_PIVOT."""
    Ra, Ta = applied(rot, t, left); s = s_v * SHIELD_SIZE[view]
    T = Ta + (s_v - s) * (Ra @ (SHIELD_PIVOT[view] - C))
    if left: T = [-T[0], T[1], T[2]]
    return {"rotation": list(rot), "translation": [r4(v) for v in T], "scale": [r4(s)] * 3}

def shield_model(cubes):
    """The shield is laid out where the vanilla shield is (board centred on x = y = 0 just in front of z = 0, handle
    behind it), so vanilla's own resting and blocking poses apply unchanged. Returns (model, blocking display)."""
    els = []
    for q in cubes:
        el = element(q, 24); f, t = el["from"], el["to"]
        f[0], t[0] = r4(f[0] - 8), r4(t[0] - 8)
        f[2], t[2] = r4(-(t[2] - 8) + 0.5), r4(-(f[2] - 8) + 0.5)             # board faces +z, like vanilla's
        el["faces"]["north"], el["faces"]["south"] = el["faces"]["south"], el["faces"]["north"]
        if "rotation" in el: el["rotation"]["origin"] = [r4(el["rotation"]["origin"][0] - 8), el["rotation"]["origin"][1], 2]
        els.append(el)
    rest, block = {}, {}
    for ctx, ((rn, tn), (rb, tb)) in SHIELD_VANILLA.items():
        view = ctx[:5]; s_v = 1.25 if view == "first" else 1; left = ctx.endswith("lefthand")
        rest[ctx], block[ctx] = shield_pose(rn, tn, s_v, left, view), shield_pose(rb, tb, s_v, left, view)
    bc = np.array([0.0, 0, 3])
    rest.update({"ground": centered([0, 0, 0], 0.5, bc, 2), "fixed": centered([0, 180, 0], 0.8, bc), "head": centered([0, 0, 0], 1, bc, 14)})
    return ({"credit": "SLF.Mine weapons", "texture_size": [mp.ATLAS_W, mp.ATLAS_H],
             "textures": {"0": "slf:item/weapons_atlas", "particle": "slf:item/weapons_atlas"},
             "elements": els, "display": rest}, block)

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
    for name, display, fn, base, dmg, spd, pair in WEAPONS + [(n + "_twin", None, f, "stick", None, None, None) for n, f in TWINS.items()]:
        weapon = base != "shield"
        cubes = fn()
        if weapon: m = model(cubes, flip=name in EDGE_DOWN, fp_tilt=FP_TILT, fp_yaw=FP_YAW, fp_shift_x=FP_SHIFT_X)
        else: m, blocking = shield_model(cubes)
        mid = model_id(name)
        wj(f"{RP}/assets/slf/models/item/{mid}.json", m)
        icons[name] = mp.icon_from(cubes); icons[name].save(f"{RP}/assets/slf/textures/item/{name}_icon.png")
        wj(f"{RP}/assets/slf/models/item/{name}_icon.json", {"parent": "minecraft:item/generated", "textures": {"layer0": f"slf:item/{name}_icon"}})
        held = {"type": "minecraft:model", "model": f"slf:item/{mid}"}
        if base == "shield":   # raise it while blocking, like the vanilla shield
            wj(f"{RP}/assets/slf/models/item/{mid}_blocking.json", {"parent": f"slf:item/{mid}", "display": blocking})
            held = {"type": "minecraft:condition", "property": "minecraft:using_item",
                    "on_true": {"type": "minecraft:model", "model": f"slf:item/{mid}_blocking"}, "on_false": held}
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
            twin = components(name + "_twin" if name in TWINS else name, pair, "stick", None, None, f'twin:"{name}",is_twin:1b')
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
