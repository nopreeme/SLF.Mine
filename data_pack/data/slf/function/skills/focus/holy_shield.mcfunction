execute if entity @s[tag=slf.skill.holy_shield] run return fail
execute if entity @s[scores={slf.focus=8}] run return fail
scoreboard players set @s slf.focus 8
scoreboard players set @s slf.focus_stat 4
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 1000
execute if entity @s[tag=slf.was_priest] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Holy Shield","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
