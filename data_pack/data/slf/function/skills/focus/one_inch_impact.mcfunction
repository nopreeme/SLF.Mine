execute if entity @s[tag=slf.skill.one_inch_impact] run return fail
execute if entity @s[scores={slf.focus=16}] run return fail
scoreboard players set @s slf.focus 16
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_fighter] run scoreboard players set @s slf.threshold 400
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"One Inch Impact","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
