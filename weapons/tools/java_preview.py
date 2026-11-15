"""First-person preview of the built Java item models.

Reproduces the game's hand camera at rest (ItemInHandRenderer: arm offset (0.56, -0.52, -0.72), then the model's
firstperson_righthand display transform, then the -0.5 block recentre; fixed 70 degree vertical FOV), so hand
positions can be tuned without reloading the game.

    python java_preview.py out.png iron_sword iron_hammer ...        # render models from java_out
    python java_preview.py out.png iron_sword --against shot.png     # put a game screenshot next to the render
"""
import json, math, os, sys
import numpy as np
from PIL import Image, ImageDraw
import java_build as jb

ARM = np.array([0.56, -0.52, -0.72])
NORMALS = {"north": (0, 0, -1), "south": (0, 0, 1), "east": (1, 0, 0), "west": (-1, 0, 0), "up": (0, 1, 0), "down": (0, -1, 0)}

def quads(e):
    (x0, y0, z0), (x1, y1, z1) = e["from"], e["to"]
    return {"north": [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], "south": [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],
            "west": [(x0, y0, z0), (x0, y0, z1), (x0, y1, z1), (x0, y1, z0)], "east": [(x1, y0, z0), (x1, y0, z1), (x1, y1, z1), (x1, y1, z0)],
            "down": [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], "up": [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)]}

def render(model, atlas, size=(960, 540), display=None, bg=(120, 170, 235)):
    W, H = size; f = (H / 2) / math.tan(math.radians(35)); tex = atlas.load()
    d = display or model["display"]["firstperson_righthand"]
    Rd, T, s = jb.R(d["rotation"]), np.array(d["translation"], float) / 16, d["scale"][0]
    light = np.array([0.35, 0.8, 0.5]); light /= np.linalg.norm(light)
    items = []
    for e in model["elements"]:
        rot = e.get("rotation"); Re = jb.Rz(rot["angle"]) if rot else np.eye(3); o = np.array(rot["origin"], float) if rot else np.zeros(3)
        for name, q in quads(e).items():
            face = e["faces"].get(name)
            if not face: continue
            pts = [ARM + T + s * (Rd @ ((o + Re @ (np.array(p, float) - o)) / 16 - 0.5)) for p in q]
            if any(p[2] > -0.05 for p in pts): continue
            u0, v0, u1, v1 = face["uv"]; col = tex[min(255, int((u0 + u1) * 8)), min(255, int((v0 + v1) * 8))]
            shade = 0.75 + 0.25 * max(0.0, float((Rd @ Re @ np.array(NORMALS[name], float)) @ light))
            items.append((min(p[2] for p in pts), [(W / 2 + f * p[0] / -p[2], H / 2 - f * p[1] / -p[2]) for p in pts], tuple(int(c * shade) for c in col[:3])))
    im = Image.new("RGB", size, bg); dr = ImageDraw.Draw(im)
    for _, poly, col in sorted(items, key=lambda t: t[0]): dr.polygon(poly, fill=col)
    dr.line([(W / 2 - 8, H / 2), (W / 2 + 8, H / 2)], fill="white", width=2); dr.line([(W / 2, H / 2 - 8), (W / 2, H / 2 + 8)], fill="white", width=2)
    return im

if __name__ == "__main__":
    args = sys.argv[1:]; out = args.pop(0); against = None
    if "--against" in args: i = args.index("--against"); against = args[i + 1]; del args[i:i + 2]
    atlas = Image.open(f"{jb.RP}/assets/slf/textures/item/weapons_atlas.png").convert("RGBA")
    tiles = []
    for n in args:
        im = render(json.load(open(f"{jb.RP}/assets/slf/models/item/{n}.json")), atlas); ImageDraw.Draw(im).text((8, 6), n, fill="white"); tiles.append(im)
    if against: tiles.append(Image.open(against).convert("RGB").resize((960, 540), Image.LANCZOS))
    cols = 2 if len(tiles) > 1 else 1; rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (960 * cols, 540 * rows), (20, 20, 20))
    for k, t in enumerate(tiles): sheet.paste(t, ((k % cols) * 960, (k // cols) * 540))
    sheet.save(out); print(out)
