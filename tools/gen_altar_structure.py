"""Writes data_pack/data/slf/structure/altar.nbt, the Altar of Awakening that world generation places.

    python tools/gen_altar_structure.py

The layout is the same one `altar/build.mcfunction` places by command (5x5 footprint, base layer sunk into the
ground). The template also carries the two entities the pack looks for: a marker tagged slf.altar (players who walk
up to it awaken) and the floating label. No dependencies.
"""
import gzip, os, struct

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data_pack", "data", "slf", "structure", "altar.nbt")
DATA_VERSION = 4903   # Minecraft 26.2 (world_version in the jar's version.json)

# ---- minimal NBT writer: values are tagged explicitly so ints, bytes and doubles are never guessed
class B(int): pass          # byte
class D(float): pass        # double
def _payload(v):
    if isinstance(v, B): return 1, struct.pack(">b", v)
    if isinstance(v, bool): return 1, struct.pack(">b", int(v))
    if isinstance(v, int): return 3, struct.pack(">i", v)
    if isinstance(v, D): return 6, struct.pack(">d", v)
    if isinstance(v, str): b = v.encode("utf-8"); return 8, struct.pack(">H", len(b)) + b
    if isinstance(v, list):
        items = [_payload(x) for x in v]; t = items[0][0] if items else 0
        assert all(i[0] == t for i in items), "mixed list"
        return 9, bytes([t]) + struct.pack(">i", len(items)) + b"".join(i[1] for i in items)
    if isinstance(v, dict):
        out = b""
        for k, x in v.items():
            t, p = _payload(x); kb = k.encode("utf-8"); out += bytes([t]) + struct.pack(">H", len(kb)) + kb + p
        return 10, out + b"\x00"
    raise TypeError(type(v))
def nbt_file(root): return b"\x0a\x00\x00" + _payload(root)[1]

# ---- layout: (x, y, z) -> palette index, y=0 is the base sunk into the ground
PALETTE = [
    {"Name": "minecraft:air"},
    {"Name": "minecraft:polished_blackstone_bricks"},
    {"Name": "minecraft:polished_blackstone_brick_slab", "Properties": {"type": "bottom", "waterlogged": "false"}},
    {"Name": "minecraft:gilded_blackstone"},
    {"Name": "minecraft:crying_obsidian"},
    {"Name": "minecraft:end_rod", "Properties": {"facing": "up"}},
    {"Name": "minecraft:polished_blackstone_wall"},
    {"Name": "minecraft:soul_lantern", "Properties": {"hanging": "false", "waterlogged": "false"}},
]
AIR, BRICK, SLAB, GILDED, CRYING, ROD, WALL, LANTERN = range(8)
SIZE = (5, 5, 5)

def layout():
    cells = {}
    for x in range(5):
        for z in range(5):
            cells[(x, 0, z)] = BRICK
            for y in range(1, 5): cells[(x, y, z)] = AIR          # clear whatever grew here
    for x in range(1, 4):
        for z in range(1, 4): cells[(x, 1, z)] = SLAB
    cells[(2, 1, 2)] = GILDED; cells[(2, 2, 2)] = CRYING; cells[(2, 3, 2)] = ROD
    for x in (0, 4):
        for z in (0, 4): cells[(x, 1, z)] = WALL; cells[(x, 2, z)] = LANTERN
    return cells

def structure():
    blocks = [{"pos": [x, y, z], "state": s} for (x, y, z), s in sorted(layout().items(), key=lambda kv: (kv[0][1], kv[0][2], kv[0][0]))]
    entities = [
        {"pos": [D(2.5), D(1.0), D(2.5)], "blockPos": [2, 1, 2], "nbt": {"id": "minecraft:marker", "Tags": ["slf.altar"]}},
        {"pos": [D(2.5), D(4.4), D(2.5)], "blockPos": [2, 4, 2],
         "nbt": {"id": "minecraft:text_display", "Tags": ["slf.altar_label"], "billboard": "center",
                 "text": {"text": "Altar of Awakening", "color": "light_purple", "bold": B(1)}}},
    ]
    return {"DataVersion": DATA_VERSION, "size": list(SIZE), "palette": PALETTE, "blocks": blocks, "entities": entities}

if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as f: f.write(gzip.compress(nbt_file(structure()), mtime=0))
    print(f"wrote {OUT} ({len(layout())} blocks, 2 entities)")
