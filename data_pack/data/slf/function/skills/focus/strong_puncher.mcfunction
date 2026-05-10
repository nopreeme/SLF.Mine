execute if entity @s[tag=slf.skill.strong_puncher] run return fail
execute unless entity @s[tag=slf.skill.knuckle_rush] run tellraw @s {"text":"Requires: Knuckle Rush","color":"red"}
execute unless entity @s[tag=slf.skill.knuckle_rush] run return fail
execute if entity @s[scores={slf.focus=22}] run return fail
scoreboard players set @s slf.focus 22
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_fighter] run scoreboard players set @s slf.threshold 300
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Strong Puncher","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
