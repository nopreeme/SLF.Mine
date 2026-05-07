#!/usr/bin/env python3
"""Generate 16x16 placeholder PNG textures for SLF.Mine.
Run from the repo root: python3 generate_textures.py
"""
import struct, zlib, os

def _chunk(tag, data):
    crc = zlib.crc32(tag + data) & 0xffffffff
    return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', crc)

def make_png(w, h, rgb):
    r, g, b = rgb
    ihdr = _chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
    raw = b''.join(b'\x00' + bytes([r, g, b] * w) for _ in range(h))
    idat = _chunk(b'IDAT', zlib.compress(raw))
    iend = _chunk(b'IEND', b'')
    return b'\x89PNG\r\n\x1a\n' + ihdr + idat + iend

def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(data)

BASE = 'resource_pack/assets/slf/textures/item'

ITEMS = {
    # Weapons
    'vorpal_knife':             (0xe0, 0xd8, 0xc0),
    'togetsu_waxing':           (0xf0, 0xf0, 0xf0),
    'togetsu_waning':           (0x10, 0x10, 0x10),
    'whalelore_goldsheen':      (0xff, 0xd7, 0x00),
    'whalelore_netherlight':    (0x30, 0x30, 0x40),
    'gilta_brille':             (0x90, 0x60, 0xc0),
    'wezaemon_katana':          (0x40, 0x48, 0x50),
    'lycagon_fang':             (0x0a, 0x08, 0x10),
    'rust_saber':               (0x8b, 0x3a, 0x2a),
    'seiten_skillbook':         (0x00, 0x80, 0xff),
    # Armor
    'helm_battlehorn':          (0x48, 0x40, 0x40),
    'helm_tombguard':           (0x38, 0x38, 0x40),
    'chest_tombguard':          (0x38, 0x38, 0x40),
    'legs_tombguard':           (0x38, 0x38, 0x40),
    'boots_tombguard':          (0x38, 0x38, 0x40),
    'chest_splitblade':         (0x4a, 0x60, 0x30),
    'helm_lacedaemon':          (0x60, 0xc0, 0xe0),
    'belt_lacedaemon':          (0x60, 0xc0, 0xe0),
    # Skills
    'skill_slash':              (0xc0, 0x00, 0x00),
    'skill_evasion':            (0x00, 0xcc, 0x44),
    'skill_meteor':             (0xff, 0x66, 0x00),
    'skill_night_rush':         (0x00, 0x66, 0x88),
    'skill_void_collapse':      (0x44, 0x00, 0x88),
    # Materials
    'quad_beetle_shell':        (0x18, 0x18, 0x18),
    'gleaming_crystal_stinger': (0xc8, 0x90, 0x00),
    'mud_frog_skin':            (0x50, 0x60, 0x30),
    'unique_core':              (0xff, 0x80, 0xff),
    'seiten_memory':            (0x00, 0xe8, 0xc8),
}

for name, rgb in ITEMS.items():
    write(f'{BASE}/{name}.png', make_png(16, 16, rgb))
    print(f'  {name}.png')

print(f'\nDone - {len(ITEMS)} textures written to {BASE}/')
