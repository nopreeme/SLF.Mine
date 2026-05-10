scoreboard players remove @s slf.sp_points 1
scoreboard players add @s slf.stat.int 1
tellraw @s ["",{"text":"INT +1 ","color":"blue"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.stat.int"}},{"text":")","color":"dark_gray"},{"text":" — ","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.sp_points"},"color":"gray"},{"text":" points left","color":"gray"}]
