# CLAUDE.md Drift Report — 2026-05-14

## Summary

4 inaccuracies corrected. This is the first drift report produced by the automated workflow.

---

## Changes

### Entry Points — path note contradiction

- **Was:** `data/minecraft/tags/functions/load.json` and `data/minecraft/tags/functions/tick.json` (plural `functions/`)
- **Now:** `data/minecraft/tags/function/load.json` and `data/minecraft/tags/function/tick.json` (singular `function/`)
- **Why:** `ls data_pack/data/minecraft/tags/` shows the directory is named `function` (singular). The entry-points bullet used the plural form while the path-note callout below it (correctly) used the singular form, creating a direct contradiction.

### Class Tier Table — Assassin/Killing Joke misclassified, branching undocumented

- **Was:** Assassin (16) and Killing Joke (17) listed under "T2 — Blade/Brawler (10–22)" alongside Sword Master, Barbarian, Bishop, etc.
- **Now:** Both moved to Shadow tree with correct tier labels (Assassin = T3 from Thief; Killing Joke = T4 from Assassin). Full table rewritten to show prerequisite sources per tier.
- **Why:** `assassin.mcfunction` line 1: `execute unless entity @s[tag=slf.was_thief] run return fail` — Assassin requires `was_thief`, not `was_swordsman` or any Blade class. Killing Joke requires `was_assassin`. Neither class belongs in the Blade/Brawler grouping. The rewrite of Bandit→T1 and Thief/Ninja→T2 (from the class tree rework commit) also meant the shadow branching point (Bandit → Thief OR Ninja) was never documented.

### Class Tier Table — Tier depth labels were misleading

- **Was:** "T2" and "T3" labels implied exactly two/three prerequisites deep, but grouped classes of different actual depths together (e.g. Kansei requires Sword Master which requires Swordsman, so it's 3 deep but was labelled T2).
- **Now:** Table rewritten to show T2/T3/T4 labels aligned with actual prerequisite depth and includes the `from <X>` source for each class.
- **Why:** All grant files confirmed via prerequisite chain reading. The old table was grouping by ID range rather than lineage depth, making it impossible to derive the class tree from the documentation alone.

### Tooling — tests/ and armor helper undocumented

- **Was:** Tooling section listed only `build.sh` and `discord_bot/`.
- **Now:** Added `tests/test_datapack.py` (33-test static analysis suite) and `give/armor_leather_full.mcfunction` (shared armor helper called by T1 grant files).
- **Why:** Both were added in recent commits but the Tooling section was not updated.

---

## No-change findings (checked and confirmed correct)

- All scoreboard objectives in the table match setup.mcfunction registrations — no stale or missing entries
- Stat → Effect Mapping thresholds (AGI, STM, VIT, STR, DEX, LCK) match stats/apply.mcfunction
- 20-tick cycle table — all 7 functions exist at stated paths with accurate descriptions
- Tag Conventions section — all tags accurate
- Skill Learning Flow — sp_tick ideal_motion 3× bonus description accurate
- T1 guard pattern description accurate
- T2+ guard pattern description accurate
- Knight trials alignment flow accurate
- Mask/Karma system description accurate
