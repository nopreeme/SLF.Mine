scoreboard players remove @s slf.sp_points 1
scoreboard players add @s slf.stat.vit 1
playsound minecraft:entity.experience_orb.pickup player @s
tellraw @s ["",{"text":"VIT +1 ","color":"green"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.stat.vit"}},{"text":")","color":"dark_gray"},{"text":" — ","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.sp_points"},"color":"gray"},{"text":" points left","color":"gray"}]
