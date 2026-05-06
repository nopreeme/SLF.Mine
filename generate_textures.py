#!/usr/bin/env python3
"""
SLF.Mine — Placeholder Texture Generator

Runs from the repo root and writes solid-colour 16x16 PNG placeholders
for all item textures plus the required GUI sprites.

Usage:
    python3 generate_textures.py

After running, load the resource_pack in Minecraft to verify colours,
then replace files in resource_pack/assets/slf/textures/ with proper art.
"""

import os
import struct
import zlib


def _chunk(tag: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(tag + data) & 0xFFFF_FFFF
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)


def make_png(width: int, height: int, r: int, g: int, b: int) -> bytes:
    """Return bytes of a solid-colour RGB PNG."""
    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = _chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    raw = b"".join(b"\x00" + bytes([r, g, b] * width) for _ in range(height))
    idat = _chunk(b"IDAT", zlib.compress(raw, 9))
    iend = _chunk(b"IEND", b"")
    return sig + ihdr + idat + iend


def write(path: str, data: bytes) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    print(f"  wrote {path}  ({len(data)} bytes)")


RP = "resource_pack"
ITEM_DIR = f"{RP}/assets/slf/textures/item"
GUI_DIR  = f"{RP}/assets/minecraft/textures/gui/sprites"

# ── Item textures (16x16) ────────────────────────────────────────────────────
ITEM_TEXTURES = {
    # Boss weapons
    "wethermon_scythe":       (0x3A, 0x00, 0x50),  # dark purple
    "wethermon_rib_dagger":   (0xE8, 0xE0, 0xD0),  # off-white bone
    "bilac_crescent_blade":   (0x1A, 0x30, 0x50),  # steel blue
    "bilac_fang_gauntlet":    (0x70, 0x70, 0x70),  # grey-silver
    "oriana_scepter":         (0xC8, 0xA0, 0x00),  # gold
    "oriana_void_staff":      (0x1A, 0x00, 0x40),  # deep indigo
    "nightclaw_talon":        (0x08, 0x08, 0x08),  # midnight black
    # Sunraku weapons
    "sunraku_blade_r":        (0xC0, 0xC0, 0xC0),  # silver
    "sunraku_blade_l":        (0xC0, 0xC0, 0xC0),  # silver (mirrored)
    "sunraku_chaos_rod":      (0x00, 0x80, 0x80),  # teal
    # Tombguard armour
    "armor_tombguard_helmet": (0x5A, 0x4A, 0x3A),  # dark bone
    "armor_tombguard_chest":  (0x5A, 0x4A, 0x3A),
    "armor_tombguard_legs":   (0x5A, 0x4A, 0x3A),
    "armor_tombguard_boots":  (0x5A, 0x4A, 0x3A),
    # Full Moon armour
    "armor_fullmoon_chest":   (0x30, 0x60, 0xA0),  # silver-blue
    # Skill books
    "skill_book_slash":       (0xC0, 0x00, 0x00),  # red
    "skill_book_thrust":      (0xC0, 0x60, 0x00),  # orange
    "skill_book_blade_rush":  (0xFF, 0xD7, 0x00),  # bright gold (fused)
    "skill_book_moonhowl":    (0x80, 0xE0, 0xFF),  # cyan-white (fused)
    "skill_book_void_lance":  (0x60, 0x00, 0xA0),  # deep purple (fused)
    # Material
    "unique_core":            (0xFF, 0x80, 0xFF),  # magenta/rainbow hint
}

# ── GUI sprites ──────────────────────────────────────────────────────────────
# SLF theme: dark navy #0a0f2a backgrounds, gold #c8a000 accents
GUI_SPRITES = {
    # HUD
    f"{GUI_DIR}/hud/hotbar.png":              (182, 22,  0x0A, 0x0F, 0x2A),
    f"{GUI_DIR}/hud/hotbar_selection.png":    (24,  23,  0xC8, 0xA0, 0x00),
    f"{GUI_DIR}/hud/crosshair.png":           (15,  15,  0xC8, 0xA0, 0x00),
    f"{GUI_DIR}/hud/heart/full.png":          (9,   9,   0xCC, 0x00, 0x00),
    f"{GUI_DIR}/hud/heart/half.png":          (9,   9,   0x88, 0x00, 0x00),
    f"{GUI_DIR}/hud/heart/container.png":     (9,   9,   0x0A, 0x0F, 0x2A),
    f"{GUI_DIR}/hud/food/full.png":           (9,   9,   0x00, 0x44, 0xCC),
    f"{GUI_DIR}/hud/food/half.png":           (9,   9,   0x00, 0x22, 0x88),
    # Widgets
    f"{GUI_DIR}/widget/button.png":           (200, 20,  0x0A, 0x0F, 0x2A),
    f"{GUI_DIR}/widget/button_disabled.png":  (200, 20,  0x20, 0x20, 0x30),
    f"{GUI_DIR}/widget/button_highlighted.png": (200, 20, 0xC8, 0xA0, 0x00),
}


def main() -> None:
    print("\n=== SLF.Mine Texture Generator ===")
    print(f"Working directory: {os.getcwd()}\n")

    print("[1/3] Item textures (16x16)")
    for name, (r, g, b) in ITEM_TEXTURES.items():
        write(f"{ITEM_DIR}/{name}.png", make_png(16, 16, r, g, b))

    print("\n[2/3] GUI sprites")
    for path, (w, h, r, g, b) in GUI_SPRITES.items():
        write(path, make_png(w, h, r, g, b))

    print("\n[3/3] Pack icon (64x64 gold)")
    write(f"{RP}/pack.png", make_png(64, 64, 0xC8, 0xA0, 0x00))

    total = len(ITEM_TEXTURES) + len(GUI_SPRITES) + 1
    print(f"\n✓ Done! {total} files written.")
    print("Load resource_pack in Minecraft to verify.")
    print("Replace files in resource_pack/assets/slf/textures/item/ with proper art.")


if __name__ == "__main__":
    main()
