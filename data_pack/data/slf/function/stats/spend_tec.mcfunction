scoreboard players remove @s slf.sp_points 1
scoreboard players add @s slf.stat.tec 1
# TEC reduces focus thresholds: every 10 TEC = 10% reduction (applied as a flat subtraction on focus set)
tellraw @s ["",{"text":"TEC +1 ","color":"light_purple"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.stat.tec"}},{"text":")","color":"dark_gray"},{"text":" — ","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.sp_points"},"color":"gray"},{"text":" points left","color":"gray"}]
