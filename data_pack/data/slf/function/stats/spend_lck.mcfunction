scoreboard players remove @s slf.sp_points 1
scoreboard players add @s slf.stat.lck 1
playsound minecraft:entity.experience_orb.pickup player @s
tellraw @s ["",{"text":"LCK +1 ","color":"gold"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.stat.lck"}},{"text":")","color":"dark_gray"},{"text":" — ","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.sp_points"},"color":"gray"},{"text":" points left","color":"gray"}]
