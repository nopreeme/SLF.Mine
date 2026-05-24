execute if entity @s[tag=slf.skill.gigaton_swing] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.gigaton_swing] run return fail
execute unless entity @s[tag=slf.skill.megaton_swing] run tellraw @s {"text":"Requires: Megaton Swing","color":"red"}
execute unless entity @s[tag=slf.skill.megaton_swing] run return fail
execute if score @s slf.focus matches 21 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 21 run return fail
scoreboard players set @s slf.focus 21
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_warrior] run scoreboard players set @s slf.threshold 300
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Gigaton Swing","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
