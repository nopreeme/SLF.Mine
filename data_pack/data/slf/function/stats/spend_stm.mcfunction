scoreboard players remove @s slf.sp_points 1
scoreboard players add @s slf.stat.stm 1
tellraw @s ["",{"text":"STM +1 ","color":"white"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.stat.stm"}},{"text":")","color":"dark_gray"},{"text":" — ","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.sp_points"},"color":"gray"},{"text":" points left","color":"gray"}]
