execute if entity @s[tag=slf.skill.slide_step] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.slide_step] run return fail
execute if score @s slf.focus matches 7 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 7 run return fail
scoreboard players set @s slf.focus 7
scoreboard players set @s slf.focus_stat 3
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 500
execute if entity @s[tag=slf.was_thief] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Slide Step","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
