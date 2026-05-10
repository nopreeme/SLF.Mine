scoreboard players remove @s slf.sp_points 1
scoreboard players add @s slf.stat.agi 1
tellraw @s ["",{"text":"AGI +1 ","color":"aqua"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.stat.agi"}},{"text":")","color":"dark_gray"},{"text":" — ","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.sp_points"},"color":"gray"},{"text":" points left","color":"gray"}]
