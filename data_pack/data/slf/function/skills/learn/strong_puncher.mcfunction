# Knuckle lineage: replaces Knuckle Rush
tag @s remove slf.skill.knuckle_rush
tag @s add slf.skill.strong_puncher
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Strong Puncher","color":"gold"},{"text":" (replaced Knuckle Rush)","color":"dark_gray"}]
