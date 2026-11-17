"""
Writes ITEMS.md: every item in the SLF packs - its name, icon, base item, stats, description, where it comes from, and the
command that gives it. Everything is read from the packs themselves (give commands, loot tables, quest and shop functions,
the resource pack's models and the lang file), so re-run it after adding or changing an item:

    python tools/gen_item_docs.py

tests/test_test_suite.py fails while ITEMS.md is out of date.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DP = ROOT / "data_pack" / "data" / "slf"
GIVE = DP / "function" / "give"
RP = ROOT / "resource_pack" / "assets"
WEAPONS_DP = ROOT / "weapons" / "java_out" / "SLF_Weapons_Datapack" / "data" / "slf" / "function" / "weapons" / "give"
WEAPONS_RP = ROOT / "weapons" / "java_out" / "SLF_Weapons_ResourcePack" / "assets"
LANG = json.loads((RP / "slf" / "lang" / "en_us.json").read_text(encoding="utf-8"))
OUT = ROOT / "ITEMS.md"

# ------------------------------------------------------------------ names for the places an item comes from
MOBS = {"vorpal_bunny": "Vorpal Bunny", "goblin": "Goblin", "red_hat_goblin": "Redcap Goblin", "orc": "Orc", "mud_frog": "Mud Frog",
        "ravenous_snake": "the Ravenous Snake (area boss)", "mud_digger": "the Mud Digger (area boss)", "lycagon": "Lycagon the Nightslayer (boss)",
        "wethermon": "Wethermon the Tombguard (boss)", "wezaemon": "Wethermon the Tombguard (boss)", "bilac": "Bilac the Full Moon Fangs (boss)",
        "nightclaw": "Nightclaw (boss)", "oriana": "Oriana the Uncrowned (boss)", "ctarnidd": "Ctarnidd of the Abyss (boss)", "siegwurm": "Siegwurm the Sky Ruler (boss)"}
QUESTS = {"awaken": "A Pioneer's Awakening", "outskirts": "Clearing the Outskirts", "brute": "The Brute Threat", "herd": "The Missing Herd",
          "serpent": "The Serpent's Shadow", "guardian": "The Rampant Forest Guardian", "delivery": "Secondil Supply Delivery", "bed": "A Soft Bed at Last",
          "slept": "A Soft Bed at Last", "antidote": "Antidote Run", "watch": "The Night Watch", "bar": "Bar Talk", "pickaxe": "The Iron Pickaxe",
          "splitblade": "Splitblade Set", "splitblade_check": "Splitblade Set", "pickaxe_check": "The Iron Pickaxe", "miner": "The Missing Miner",
          "reeds": "Red Hoods in the Reeds", "thirdrema": "Path to Thirdrema", "fellow_survivor": "Fellow Survivor (Wanderer)",
          "letter_start": "A Brother's Letter (Wanderer)", "letter_turn_in": "A Brother's Letter (Wanderer)", "site": "The Missing Miner",
          "tick": "Red Hoods in the Reeds", "journal_item": "The Missing Miner", "camp": "The Missing Herd"}
SECTIONS = ["Weapons", "Armour and accessories", "Skill books", "Consumables", "Materials and trophies", "Quest items", "Currency"]


def text_of(snbt_or_json):
    """The display text of an item_name / lore entry, from SNBT or JSON."""
    m = re.search(r'translate"?\s*:\s*"([^"]+)"', snbt_or_json)
    if m: return LANG.get(m.group(1), m.group(1))
    m = re.search(r'text"?\s*:\s*"((?:[^"\\]|\\.)*)"', snbt_or_json)
    return m.group(1).replace("\\'", "'") if m else None


def parse_give(line):
    """{base, key, name, lore, enchantments, attributes, extras} from one '/give @s item[components] n' line."""
    m = re.match(r"give @s (?:minecraft:)?([a-z_]+)(?:\[(.*)\])?(?:\s+\d+)?$", line.strip())
    if not m: return None
    base, comps = m.group(1), m.group(2) or ""
    it = {"base": base, "key": None, "name": None, "lore": [], "enchantments": {}, "attributes": [], "extras": []}
    k = re.search(r'custom_model_data=\{strings:\["([^"]+)"\]\}', comps) or re.search(r'item_model="([^"]+)"', comps)
    if k: it["key"] = k.group(1)
    n = re.search(r'item_name=(\{[^}]*\}|"[^"]*")', comps)
    if n: it["name"] = text_of(n.group(1)) if n.group(1).startswith("{") else n.group(1).strip('"')
    lore = re.search(r"lore=\[(.*?)\](?:,minecraft:|,[a-z_]+=|$)", comps)
    if lore: it["lore"] = [t.replace("\\'", "'") for t in re.findall(r'text:"((?:[^"\\]|\\.)*)"', lore.group(1))]
    for e, lv in re.findall(r'"minecraft:([a-z_]+)":(\d+)', (re.search(r"enchantments=\{([^}]*)\}", comps) or [None, ""])[1] if re.search(r"enchantments=\{", comps) else ""):
        it["enchantments"][e] = int(lv)
    for typ, amt, slot in re.findall(r'type:"minecraft:([a-z_]+)",id:"[^"]+",amount:(-?[\d.]+),operation:"[a-z_]+",slot:"([a-z]+)"', comps):
        it["attributes"].append((typ, float(amt), slot))
    if "potion_contents" in comps:
        p = re.search(r'potion:"minecraft:([a-z_]+)"', comps)
        effects = re.findall(r'id:"minecraft:([a-z_]+)",duration:(\d+)', comps)
        it["extras"].append("potion: " + (p.group(1).replace("_", " ") if p else ", ".join(f"{e.replace('_', ' ')} {int(d) // 20}s" for e, d in effects)))
    if "on_consume_effects" in comps:
        it["extras"].append("when eaten: " + ", ".join(f"{e.replace('_', ' ')} {int(a) + 1}" for e, a in re.findall(r'id:"minecraft:([a-z_]+)",amplifier:(\d+)', comps)))
    if "dyed_color" in comps: it["extras"].append("dyed")
    if "banner_patterns" in comps: it["extras"].append("banner with an unknown sigil")
    if "damage" in re.findall(r"minecraft:([a-z_]+)=", comps) or ",minecraft:damage=" in comps: it["extras"].append("worn out")
    return it


def parse_loot_item(path):
    """An item from a one-entry loot table (used where a give is 'loot give')."""
    d = json.loads(path.read_text(encoding="utf-8"))
    e = d["pools"][0]["entries"][0]; comps = e["functions"][0]["components"]
    return {"base": e["name"].split(":")[1], "key": comps.get("minecraft:item_model"), "name": comps["minecraft:item_name"]["text"] if "minecraft:item_name" in comps else
            comps.get("minecraft:written_book_content", {}).get("title"), "lore": [l["text"] for l in comps.get("minecraft:lore", [])],
            "enchantments": {}, "attributes": [], "extras": ["a readable book"] if "minecraft:written_book_content" in comps else []}


# ------------------------------------------------------------------ icons
def model_texture(models_root, model_id):
    p = models_root / model_id.split(":")[0] / "models" / (model_id.split(":")[1] + ".json")
    if not p.exists(): return None
    tex = json.loads(p.read_text(encoding="utf-8")).get("textures", {})
    t = tex.get("layer0") or tex.get("0") or next(iter(tex.values()), None)
    if not t or t.startswith("#"): return None
    f = models_root / t.split(":")[0] / "textures" / (t.split(":")[1] + ".png")
    return f if f.exists() else None


def gui_model(node):
    """The model the inventory shows: a display_context switch's gui case if there is one."""
    if node.get("type", "").endswith("select") and node.get("property", "").endswith("display_context"):
        for c in node["cases"]:
            if "gui" in (c["when"] if isinstance(c["when"], list) else [c["when"]]): return gui_model(c["model"])
        return gui_model(node["fallback"])
    if node.get("type", "").endswith("model"): return node["model"]
    return None


def icon_for(item, rp_root=RP):
    key = item["key"]
    if not key: return None
    if key.startswith("slf:"):                                                    # item_model
        d = rp_root / "slf" / "items" / (key[4:] + ".json")
        if d.exists(): return model_texture(rp_root, gui_model(json.loads(d.read_text(encoding="utf-8"))["model"]))
        return None
    defs = rp_root / "minecraft" / "items" / (item["base"] + ".json")             # custom_model_data string
    if not defs.exists(): return None
    for c in json.loads(defs.read_text(encoding="utf-8"))["model"].get("cases", []):
        if key in (c["when"] if isinstance(c["when"], list) else [c["when"]]):
            return model_texture(rp_root, gui_model(c["model"]))
    return None


# ------------------------------------------------------------------ where an item comes from
def chance_in(loot, key):
    """The drop chance (and player-kill rule) of the pool holding this item, as text."""
    for pool in loot.get("pools", []):
        if key in json.dumps(pool):
            parts = []
            entry = next((e for e in pool.get("entries", []) if key in json.dumps(e)), {})
            for cond in pool.get("conditions", []) + entry.get("conditions", []):
                if cond["condition"].endswith("random_chance"): parts.append(f"{cond['chance'] * 100:g}%")
                if cond["condition"].endswith("killed_by_player"): parts.append("player kills")
            r = pool.get("rolls")
            if isinstance(r, dict): parts.insert(0, f"{r['min']}-{r['max']}")
            return ", ".join(parts) or "always"
    return ""


FOUND = {"tomic_journal": "Found at Tomic's dig site (The Missing Miner)", "sigil_banner": "Left at the Redcap camp (Red Hoods in the Reeds)"}


def sources(item):
    key, out = item["key"], []
    if not key and item["name"]:                                             # a plain vanilla item: find it by its name
        key = None; names = (f'text:"{item["name"]}"', f'"text": "{item["name"]}"', f'"{item["name"]}"')
    else:
        names = None
    if not key and not names: return out
    for f in sorted(DP.rglob("*")):
        if not f.is_file() or "give" in f.parts or "test" in f.parts: continue
        text = f.read_text(encoding="utf-8", errors="replace")
        if key and key not in text: continue
        if names and not any(n in text for n in names): continue
        rel = f.relative_to(DP).as_posix(); stem = f.stem
        if rel.startswith("loot_table/"):
            if rel.startswith("loot_table/quest/"): out.append(FOUND.get(stem, "Quest item")); continue
            mob = MOBS.get(stem.replace("_drops", "").replace("boss/", ""), stem.replace("_drops", "").replace("_", " "))
            out.append(f"Drop: {mob} ({chance_in(json.loads(text), key or names[1])})")
        elif rel.startswith("function/shop/item/"):
            price = re.search(r"remove @s slf.mahni (\d+)", text)
            npc = "Lysa (florist)" if stem in ("1", "2") else "the Bartender"
            out.append(f"Shop: {npc}, {price.group(1) if price else '?'} Mahni")
        elif rel.startswith(("function/quest/", "function/wanderer/")) and stem not in ("log",):
            q = QUESTS.get(stem) or QUESTS.get(f.parent.name) or stem.replace("_", " ")
            if "start" in f.parts: out.append(f"Given when you accept {q}")
            else: out.append(f"Quest reward: {q}")
        elif rel.startswith("function/mob/"): out.append(f"Carried by {MOBS.get(f.parent.name, f.parent.name.replace('_', ' '))}")
        elif rel.startswith("advancement/"):
            title = LANG.get(f"advancements.slf.{stem}.title")
            if title: out.append(f"Advancement: {title}")
        elif rel.startswith("function/skills/learn/"): out.append("Teaches its skill when picked up")
        elif rel.startswith("function/quest/garren/"): out.append(f"Used in {QUESTS.get(stem, stem)}")
    if item["key"] in ("slf.mud_frog_skin",): out.append("Used in Splitblade Set (Garren)")
    seen = []
    return [s for s in out if not (s in seen or seen.append(s))]


# ------------------------------------------------------------------ categories and stats
def section(item, srcs):
    b, k = item["base"], item["key"] or ""
    if k == "slf:mahni_purse": return "Currency"
    if b == "enchanted_book" or "skill" in k: return "Skill books"
    if any(b.endswith(s) for s in ("_sword", "_axe", "_pickaxe", "mace", "trident", "bow")) or "dagger" in k: return "Weapons"
    if any(b.endswith(s) for s in ("_helmet", "_chestplate", "_leggings", "_boots")) or "vambraces" in k: return "Armour and accessories"
    if b in ("potion", "honey_bottle", "mushroom_stew", "bread", "milk_bucket"): return "Consumables"
    if any(s.startswith(("Given when", "Quest reward")) for s in srcs) and not any(s.startswith(("Drop", "Shop")) for s in srcs): return "Quest items"
    if b in ("black_banner", "written_book") or k in ("slf:beef_package", "slf:sealed_letter", "slf:antidote_bundle", "slf:tomic_journal"): return "Quest items"
    return "Materials and trophies"


def stats(item):
    parts = []
    for typ, amt, slot in item["attributes"]:
        if typ == "attack_damage": parts.append(f"damage {amt + 1:g}")
        elif typ == "attack_speed": parts.append(f"speed {amt + 4:g}")
        else: parts.append(f"{'+' if amt >= 0 else ''}{amt * 100:g}% {typ.replace('_', ' ')}" if abs(amt) < 1 else f"+{amt:g} {typ.replace('_', ' ')}" + (f" ({slot})" if slot not in ("mainhand", "any") else ""))
    parts += [f"{e.replace('_', ' ').title()} {lv}" for e, lv in item["enchantments"].items()]
    return ", ".join(parts + item["extras"])


def row(item, srcs, command, rp_root=RP):
    icon = icon_for(item, rp_root)
    img = f'<img src="{icon.relative_to(ROOT).as_posix()}" width="32" alt="">' if icon else ""
    name = item["name"] or item["key"] or item["base"]
    desc = " / ".join(item["lore"])
    where = "<br>".join(srcs) if srcs else "*Not obtainable in survival yet* (give command only)"
    return f"| {img} | **{name}** | {item['base'].replace('_', ' ')} | {stats(item) or '-'} | {desc or '-'} | {where} | `{command}` |"


def main():
    groups = {s: [] for s in SECTIONS}
    count = 0
    for f in sorted(GIVE.glob("*.mcfunction")):
        lines = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
        if len(lines) != 1: continue                                       # helpers that give several items
        line = lines[0]
        if line.startswith("loot give"):
            item = parse_loot_item(DP / "loot_table" / (line.split("slf:")[1].strip() + ".json"))
        else:
            item = parse_give(line)
        if not item: continue
        srcs = sources(item)
        groups[section(item, srcs)].append((item["name"] or f.stem, row(item, srcs, f"/function slf:give/{f.stem}")))
        count += 1
    weapons = []
    for f in sorted(WEAPONS_DP.glob("*.mcfunction")):
        item = parse_give(f.read_text(encoding="utf-8").strip().splitlines()[-1])
        if not item: continue
        srcs = sources(item) + ["The 3D weapons pack (`weapons/`)"]
        weapons.append((item["name"] or f.stem, row(item, srcs, f"/function slf:weapons/give/{f.stem}", WEAPONS_RP)))
    unobtainable = sum(r.count("Not obtainable in survival yet") for s in SECTIONS for _, r in groups[s]) + sum(r.count("Not obtainable in survival yet") for _, r in weapons)
    header = "| | Item | Base | Stats | Description | Where it comes from | Give command |\n|---|---|---|---|---|---|---|"
    out = ["# SLF items", "",
           f"Every item in the SLF packs: {count} in the main packs and {len(weapons)} in the 3D weapons pack. Generated by",
           "`tools/gen_item_docs.py` from the packs themselves - don't edit this file by hand; re-run the tool after changing an item.", "",
           "*Give commands* need OP. `/function slf:test/menu` has kits with most of them. *Stats* show weapon damage and attack speed",
           "the way the game's tooltip does, plus enchantments and other modifiers. Items without a custom icon use the vanilla",
           "item's look.", "",
           f"**{unobtainable} items are not obtainable in survival yet**: they exist in the packs but no monster, quest or shop gives",
           "them. They're marked in the tables below.", ""]
    for s in SECTIONS:
        if not groups[s]: continue
        out += [f"## {s} ({len(groups[s])})", "", header] + [r for _, r in sorted(groups[s], key=lambda x: x[0].lower())] + [""]
    out += [f"## 3D weapons pack ({len(weapons)})", "", "These need the separate weapons data and resource packs.", "", header] + [r for _, r in weapons] + [""]
    OUT.write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"ITEMS.md: {count} items + {len(weapons)} weapons")


if __name__ == "__main__":
    main()
