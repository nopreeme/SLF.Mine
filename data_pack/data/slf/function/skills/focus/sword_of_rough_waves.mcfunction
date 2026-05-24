execute if entity @s[tag=slf.skill.sword_of_rough_waves] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.sword_of_rough_waves] run return fail
execute if score @s slf.focus matches 5 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 5 run return fail
scoreboard players set @s slf.focus 5
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 600
execute if entity @s[tag=slf.was_swordsman] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Sword of Rough Waves","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
