# Runs every 20t — skill progress accumulation via motion trace

# Step 1: compute raw deltas (delta = raw - prev)
scoreboard players operation @a slf.dmg_delta = @a slf.raw.dmg
scoreboard players operation @a slf.dmg_delta -= @a slf.dmg_prev
scoreboard players operation @a slf.move_delta = @a slf.raw.move
scoreboard players operation @a slf.move_delta -= @a slf.move_prev
scoreboard players operation @a slf.evade_delta = @a slf.raw.evade
scoreboard players operation @a slf.evade_delta -= @a slf.evade_prev
scoreboard players operation @a slf.def_delta = @a slf.raw.def
scoreboard players operation @a slf.def_delta -= @a slf.def_prev

# Step 2: update prev snapshots (always — handles stat resets and respawns safely)
scoreboard players operation @a slf.dmg_prev = @a slf.raw.dmg
scoreboard players operation @a slf.move_prev = @a slf.raw.move
scoreboard players operation @a slf.evade_prev = @a slf.raw.evade
scoreboard players operation @a slf.def_prev = @a slf.raw.def

# Step 3: accumulate sp by focus_stat (1.. filter discards negative deltas silently)
execute as @a[scores={slf.focus_stat=1,slf.focus=1..},scores={slf.dmg_delta=1..}]   run scoreboard players operation @s slf.sp += @s slf.dmg_delta
execute as @a[scores={slf.focus_stat=2,slf.focus=1..},scores={slf.move_delta=1..}]  run scoreboard players operation @s slf.sp += @s slf.move_delta
execute as @a[scores={slf.focus_stat=3,slf.focus=1..},scores={slf.evade_delta=1..}] run scoreboard players operation @s slf.sp += @s slf.evade_delta
execute as @a[scores={slf.focus_stat=4,slf.focus=1..},scores={slf.def_delta=1..}]   run scoreboard players operation @s slf.sp += @s slf.def_delta

# Step 4: Ideal Motion bonus — 3x total (base already added in step 3, add 2x more)
# Applies to all focus_stat types; each line guards its own delta with 1.. to block negatives
execute as @a[scores={slf.focus_stat=1,slf.focus=1..},scores={slf.dmg_delta=1..},predicate=slf:ideal_motion]   run scoreboard players operation @s slf.sp += @s slf.dmg_delta
execute as @a[scores={slf.focus_stat=1,slf.focus=1..},scores={slf.dmg_delta=1..},predicate=slf:ideal_motion]   run scoreboard players operation @s slf.sp += @s slf.dmg_delta
execute as @a[scores={slf.focus_stat=2,slf.focus=1..},scores={slf.move_delta=1..},predicate=slf:ideal_motion]  run scoreboard players operation @s slf.sp += @s slf.move_delta
execute as @a[scores={slf.focus_stat=2,slf.focus=1..},scores={slf.move_delta=1..},predicate=slf:ideal_motion]  run scoreboard players operation @s slf.sp += @s slf.move_delta
execute as @a[scores={slf.focus_stat=3,slf.focus=1..},scores={slf.evade_delta=1..},predicate=slf:ideal_motion] run scoreboard players operation @s slf.sp += @s slf.evade_delta
execute as @a[scores={slf.focus_stat=3,slf.focus=1..},scores={slf.evade_delta=1..},predicate=slf:ideal_motion] run scoreboard players operation @s slf.sp += @s slf.evade_delta
execute as @a[scores={slf.focus_stat=4,slf.focus=1..},scores={slf.def_delta=1..},predicate=slf:ideal_motion]   run scoreboard players operation @s slf.sp += @s slf.def_delta
execute as @a[scores={slf.focus_stat=4,slf.focus=1..},scores={slf.def_delta=1..},predicate=slf:ideal_motion]   run scoreboard players operation @s slf.sp += @s slf.def_delta

# Step 5: threshold check — dispatch to learn if sp reached goal
execute as @a[scores={slf.focus=1..}] if score @s slf.sp >= @s slf.threshold run function slf:skills/learn_focused
