scoreboard players remove @s slf.sp_points 1
scoreboard players add @s slf.stat.dex 1
tellraw @s ["",{"text":"DEX +1 ","color":"yellow"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.stat.dex"}},{"text":")","color":"dark_gray"},{"text":" — ","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.sp_points"},"color":"gray"},{"text":" points left","color":"gray"}]
