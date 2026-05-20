execute if entity @s[tag=slf.skill.skatefoot] run return fail
execute unless entity @s[tag=slf.skill.formula_drift] run tellraw @s {"text":"Requires: Formula Drift","color":"red"}
execute unless entity @s[tag=slf.skill.formula_drift] run return fail
execute if score @s slf.focus = 32 run return fail
scoreboard players set @s slf.focus 32
scoreboard players set @s slf.focus_stat 2
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 5000
execute if entity @s[tag=slf.was_ninja]  run scoreboard players set @s slf.threshold 500
execute if entity @s[tag=slf.was_thief]  run scoreboard players set @s slf.threshold 700
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Skatefoot","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
