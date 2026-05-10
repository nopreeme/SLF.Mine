execute if entity @s[tag=slf.skill.formula_drift] run return fail
execute unless entity @s[tag=slf.skill.slide_step] run tellraw @s {"text":"Requires: Slide Step","color":"red"}
execute unless entity @s[tag=slf.skill.slide_step] run return fail
execute if entity @s[scores={slf.focus=24}] run return fail
scoreboard players set @s slf.focus 24
scoreboard players set @s slf.focus_stat 2
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_thief] run scoreboard players set @s slf.threshold 300
execute if entity @s[tag=slf.was_ninja]  run scoreboard players set @s slf.threshold 250
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Formula Drift","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
