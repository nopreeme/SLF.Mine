execute if entity @s[tag=slf.skill.spin_slash] run return fail
execute if entity @s[scores={slf.focus=6}] run return fail
scoreboard players set @s slf.focus 6
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 600
execute if entity @s[tag=slf.was_swordsman] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Spin Slash","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
