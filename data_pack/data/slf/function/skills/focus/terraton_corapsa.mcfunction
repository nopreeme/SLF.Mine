execute if entity @s[tag=slf.skill.terraton_corapsa] run return fail
execute unless entity @s[tag=slf.skill.gigaton_swing] run tellraw @s {"text":"Requires: Gigaton Swing","color":"red"}
execute unless entity @s[tag=slf.skill.gigaton_swing] run return fail
execute if entity @s[scores={slf.focus=31}] run return fail
scoreboard players set @s slf.focus 31
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 8000
execute if entity @s[tag=slf.was_warrior] run scoreboard players set @s slf.threshold 1000
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Terraton Corapsa","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
