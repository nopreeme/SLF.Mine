# Runs every 20t — EXP processing, level-up, Standby gate
# EXP is added externally by mob death functions and advancements

# Standby: players at level 99 buffer future EXP into exp_extend
execute as @a if score @s slf.level >= 99 if score @s slf.standby = 0 run scoreboard players set @s slf.standby 1
execute as @a if score @s slf.standby = 1 if score @s slf.exp >= 1 run scoreboard players operation @s slf.exp_extend += @s slf.exp
execute as @a if score @s slf.standby = 1 if score @s slf.exp >= 1 run scoreboard players set @s slf.exp 0

# Level thresholds (×1.5 curve, checked highest first so only one fires per tick)
# L1->2: 100, L2->3: 200, L3->4: 350, L4->5: 550, L5->6: 850
# L6->7: 1300, L7->8: 2000, L8->9: 3000, L9->10: 4500, L10+: 4500*1.5^(n-10) approx
# Practical cap: levels 10-99 use a flat 5000 per level for simplicity
execute as @a if score @s slf.standby = 0 if score @s slf.level = 1  if score @s slf.exp >= 100  run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 2  if score @s slf.exp >= 200  run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 3  if score @s slf.exp >= 350  run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 4  if score @s slf.exp >= 550  run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 5  if score @s slf.exp >= 850  run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 6  if score @s slf.exp >= 1300 run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 7  if score @s slf.exp >= 2000 run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 8  if score @s slf.exp >= 3000 run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level = 9  if score @s slf.exp >= 4500 run function slf:stats/level_up
execute as @a if score @s slf.standby = 0 if score @s slf.level matches 10..98 if score @s slf.exp >= 5000 run function slf:stats/level_up
