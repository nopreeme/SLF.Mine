execute if entity @s[tag=slf.skill.power_slash] run return fail
execute if entity @s[scores={slf.focus=1}] run return fail
scoreboard players set @s slf.focus 1
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 500
execute if entity @s[tag=slf.was_swordsman] run scoreboard players set @s slf.threshold 100
execute if entity @s[tag=slf.was_warrior]   run scoreboard players set @s slf.threshold 120
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Power Slash","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
