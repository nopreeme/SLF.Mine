execute if entity @s[tag=slf.skill.one_inch_impact] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.one_inch_impact] run return fail
execute if score @s slf.focus matches 16 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 16 run return fail
scoreboard players set @s slf.focus 16
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_fighter] run scoreboard players set @s slf.threshold 400
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"One Inch Impact","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
