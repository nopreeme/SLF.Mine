execute if entity @s[tag=slf.skill.rechette_step] run return fail
execute if entity @s[scores={slf.focus=26}] run return fail
scoreboard players set @s slf.focus 26
scoreboard players set @s slf.focus_stat 3
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_ninja]  run scoreboard players set @s slf.threshold 300
execute if entity @s[tag=slf.was_thief]  run scoreboard players set @s slf.threshold 400
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Rechette Step","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
