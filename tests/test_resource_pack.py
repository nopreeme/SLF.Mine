"""
SLF.Mine resource pack static checks. No Minecraft needed.

Catches the ways an item silently turns into the purple-and-black missing texture or a plain vanilla item:
  1. An item definition points at a model file that does not exist
  2. A model points at a texture file that does not exist (or at something that is not a resource location)
  3. The data pack hands out a custom_model_data string that no item definition answers to on that base item
  4. Pack metadata uses a declaration 26.2 rejects

Run: python -m unittest tests/test_resource_pack.py
"""
import json, re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RP = ROOT / "resource_pack" / "assets"
DP = ROOT / "data_pack" / "data"
ITEM_DEFS = RP / "minecraft" / "items"
MODELS = RP / "slf" / "models" / "item"
TEXTURES = RP / "slf" / "textures" / "item"
WEAPONS_MODELS = ROOT / "weapons" / "java_out" / "SLF_Weapons_ResourcePack" / "assets" / "slf" / "models" / "item"
MODEL_DIRS = [MODELS, WEAPONS_MODELS]   # both resource packs in this repo


def load(path): return json.loads(path.read_text(encoding="utf-8"))


def model_refs(node, out):
    """Every model id referenced anywhere inside an item definition."""
    if isinstance(node, dict):
        if node.get("type") in ("minecraft:model", "model") and isinstance(node.get("model"), str): out.add(node["model"])
        for v in node.values(): model_refs(v, out)
    elif isinstance(node, list):
        for v in node: model_refs(v, out)
    return out


def cases():
    """{(base item, custom_model_data string)} answered by the item definitions."""
    found = set()
    for f in ITEM_DEFS.glob("*.json"):
        for c in load(f)["model"].get("cases", []):
            for w in (c["when"] if isinstance(c["when"], list) else [c["when"]]): found.add((f.stem, w))
    return found


def datapack_model_strings():
    """{(base item, string): [files]} for every custom_model_data string the data pack puts on an item."""
    found = {}
    def add(base, strings, f):
        for s in strings: found.setdefault((base.replace("minecraft:", ""), s), []).append(f.relative_to(DP).as_posix())
    for f in DP.rglob("*.mcfunction"):
        for m in re.finditer(r"(?:minecraft:)?([a-z_]+)\[[^\n]*?custom_model_data\s*=\s*\{[^}]*?strings\s*:\s*\[([^\]]*)\]", f.read_text(encoding="utf-8")):
            add(m.group(1), re.findall(r'"([^"]+)"', m.group(2)), f)
    def walk(node, f, item=None):
        if isinstance(node, dict):
            if node.get("type") == "minecraft:item" and isinstance(node.get("name"), str): item = node["name"]      # loot table entry
            comps = node.get("components")
            if isinstance(comps, dict) and "minecraft:custom_model_data" in comps:
                base = node.get("id") or item                                                                    # advancement icon / loot function
                if isinstance(base, str): add(base, comps["minecraft:custom_model_data"].get("strings", []), f)
            for v in node.values(): walk(v, f, item)
        elif isinstance(node, list):
            for v in node: walk(v, f, item)
    for f in DP.rglob("*.json"): walk(load(f), f)
    return found


class TestItemDefinitions(unittest.TestCase):
    def test_every_referenced_model_exists(self):
        for f in sorted(ITEM_DEFS.glob("*.json")):
            for ref in sorted(model_refs(load(f), set())):
                if ref.startswith("slf:item/"):
                    self.assertTrue((MODELS / (ref[9:] + ".json")).exists(), f"{f.name}: model {ref} does not exist")

    def test_definitions_keep_a_fallback(self):
        for f in sorted(ITEM_DEFS.glob("*.json")):
            self.assertIn("fallback", load(f)["model"], f"{f.name}: without a fallback the plain vanilla item has no model")

    def test_no_duplicate_cases(self):
        for f in sorted(ITEM_DEFS.glob("*.json")):
            whens = [w for c in load(f)["model"].get("cases", []) for w in (c["when"] if isinstance(c["when"], list) else [c["when"]])]
            self.assertEqual(len(whens), len(set(whens)), f"{f.name}: duplicate case")


class TestModels(unittest.TestCase):
    def test_every_texture_exists(self):
        for f in sorted(MODELS.glob("*.json")):
            for key, tex in load(f).get("textures", {}).items():
                if tex.startswith("#"): continue
                self.assertRegex(tex, r"^[a-z0-9_.-]+:[a-z0-9_./-]+$", f"{f.name}: texture '{tex}' is not a namespaced resource location")
                if tex.startswith("slf:item/"):
                    self.assertTrue((TEXTURES / (tex[9:] + ".png")).exists(), f"{f.name}: texture {tex} does not exist")

    def test_every_face_uses_a_defined_texture_variable(self):
        """A face that names an undefined variable (Blockbench writes "#missing" for untextured faces) falls back to
        the missing texture, which lives in the block atlas. In 26.2 a cuboid model that mixes atlases fails to bake,
        and that takes down the whole item definition it belongs to — every iron sword, not just the one model."""
        for models in MODEL_DIRS:
            for f in sorted(models.glob("*.json")):
                d = load(f); defined = {"#" + k for k in d.get("textures", {})}
                if "parent" in d and "elements" not in d: continue
                used = {face.get("texture") for e in d.get("elements", []) for face in e.get("faces", {}).values()}
                self.assertEqual(sorted(used - defined), [], f"{f.name}: faces use texture variables the model does not define")

    def test_cuboid_models_use_one_atlas(self):
        """Same client rule from the other side: textures/item/ and textures/block/ are different atlases in 26.2."""
        for models in MODEL_DIRS:
            for f in sorted(models.glob("*.json")):
                d = load(f)
                if "elements" not in d: continue
                kinds = {t.split(":", 1)[-1].split("/", 1)[0] for t in d.get("textures", {}).values() if not t.startswith("#")}
                self.assertEqual(len(kinds), 1, f"{f.name}: textures come from more than one atlas folder: {sorted(kinds)}")

    def test_every_model_is_reachable(self):
        """A model nothing points at can never be seen in game. Known leftovers are listed explicitly."""
        leftovers = {"chestplate_tombguard", "helmet_tombguard", "leggings_tombguard"}   # older duplicates of chest_/helm_/legs_tombguard
        used = set()
        for f in ITEM_DEFS.glob("*.json"): used |= {r[9:] for r in model_refs(load(f), set()) if r.startswith("slf:item/")}
        unreachable = {f.stem for f in MODELS.glob("*.json")} - used - leftovers
        self.assertEqual(unreachable, set())

    def test_parents_are_namespaced_or_vanilla_shorthand(self):
        for f in sorted(MODELS.glob("*.json")):
            parent = load(f).get("parent")
            if parent: self.assertRegex(parent, r"^(minecraft:)?(item|block|builtin)/[a-z0-9_/]+$", f.name)


class TestDatapackLinks(unittest.TestCase):
    def test_every_handed_out_model_string_has_a_case(self):
        answered = cases(); missing = []
        for (base, string), files in sorted(datapack_model_strings().items()):
            if (base, string) not in answered: missing.append(f"{base}[{string}] used in {files[0]}")
        self.assertEqual(missing, [], "the data pack gives items the resource pack has no model for")

    def test_datapack_scan_finds_items(self):
        self.assertGreater(len(datapack_model_strings()), 20, "scanner found too few items; its patterns are probably out of date")


class TestPackMetadata(unittest.TestCase):
    def test_both_packs_use_min_max_format(self):
        for pack, fmt in (("resource_pack", 88), ("data_pack", 107)):
            meta = load(ROOT / pack / "pack.mcmeta")["pack"]
            self.assertEqual((meta.get("min_format"), meta.get("max_format")), (fmt, fmt), pack)
            self.assertNotIn("pack_format", meta, f"{pack}: 26.2 rejects pack_format together with formats above 81")
            self.assertNotIn("supported_formats", meta, pack)


if __name__ == "__main__":
    unittest.main(verbosity=2)
