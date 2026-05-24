execute if entity @s[tag=slf.skill.megaton_swing] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.megaton_swing] run return fail
execute if score @s slf.focus matches 2 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 2 run return fail
scoreboard players set @s slf.focus 2
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 500
execute if entity @s[tag=slf.was_warrior] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Megaton Swing","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
