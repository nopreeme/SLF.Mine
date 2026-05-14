You are performing an automated documentation drift audit on this repository.

Your job is to:
1. Read CLAUDE.md and identify every factual claim
2. Verify each claim against the actual codebase
3. Edit CLAUDE.md directly to fix any inaccuracies
4. Write a drift-changelog.md file summarising what changed and why

---

## Step 1: Gather ground truth

Read these files to establish what is actually true in the codebase:

- CLAUDE.md (the doc to audit)
- data_pack/data/slf/function/setup.mcfunction (all scoreboard objectives)
- data_pack/data/slf/function/skills/tick.mcfunction (class dispatch, focus dispatch, 20t cycle)
- data_pack/data/slf/function/skills/learn_focused.mcfunction (focus ID → learn file mapping)
- data_pack/data/slf/function/stats/apply.mcfunction (stat → effect thresholds)
- List all files in: data_pack/data/slf/function/class/grant/ (class grant files)
- List all files in: data_pack/data/slf/function/skills/focus/ (skill focus files)
- List all files in: data_pack/data/slf/function/skills/learn/ (skill learn files)
- List all files in: data_pack/data/minecraft/tags/ (confirm tag directory name: function/ or functions/)
- For each grant file that seems misclassified in the docs, read it to confirm its prerequisite tag

---

## Step 2: Check every factual claim category

**A. Entry point paths**
Verify the exact paths used for function tags (load.json, tick.json). Check whether the tag directory is singular `function/` or plural `functions/`. CLAUDE.md must match actual directory structure.

**B. Scoreboard objectives table**
Compare every row against setup.mcfunction:
- Any objective in the table but not in setup → mark stale
- Any objective in setup but missing from the table → add it if significant
- Wrong Type column values

**C. Class tier table**
For each class listed, read its grant file to confirm:
- Class ID (scoreboard players set @s slf.class N)
- Which tier it belongs to (T1 guard vs T2+ was_* guard)
- Which prerequisite tag it requires (was_X)
- That it exists under the right tree heading

Pay special attention to classes with IDs that don't match their tier range (e.g. ID 16 in a T3 shadow tree).

**D. 20-tick cycle table**
Confirm each function file exists at the stated path.

**E. Stat → Effect Mapping table**
Compare each row against stats/apply.mcfunction thresholds line by line.

**F. Tooling section**
Check that all directories/scripts mentioned exist. Note any new tooling added since the docs were written (tests/, give helpers, etc.).

**G. Path notes and architecture descriptions**
Verify any explicit paths, directory names, or architectural claims.

---

## Step 3: Edit CLAUDE.md

For each inaccuracy found:
- Edit CLAUDE.md directly to correct it
- Keep the same style and section structure
- Do NOT add commentary about what you changed inside CLAUDE.md — just fix the facts

---

## Step 4: Write drift-changelog.md

Create drift-changelog.md in the repo root with this structure:

```markdown
# CLAUDE.md Drift Report — <date>

## Summary
<N> inaccuracies corrected.

## Changes

### <Section Name>
- **Was:** <original claim>
- **Now:** <corrected claim>
- **Why:** <what in the codebase contradicts the old claim>

[repeat for each change]

## No-change findings
<List of things checked that were already correct>
```

---

## Important constraints

- Only edit CLAUDE.md and create drift-changelog.md. Do not modify any .mcfunction, .json, or other source files.
- If a claim in CLAUDE.md is ambiguous but not clearly wrong, leave it alone.
- If something is missing from CLAUDE.md that would genuinely help a developer, add it.
- Keep corrections minimal and factual — do not rewrite sections, just fix the specific inaccurate claims.
