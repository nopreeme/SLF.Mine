execute if entity @s[tag=slf.skill.knuckle_rush] run return fail
execute if score @s slf.focus = 3 run return fail
scoreboard players set @s slf.focus 3
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 500
execute if entity @s[tag=slf.was_fighter] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Knuckle Rush","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
