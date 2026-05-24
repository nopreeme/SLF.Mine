execute if entity @s[tag=slf.skill.flash_counter] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.flash_counter] run return fail
execute if score @s slf.focus matches 11 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 11 run return fail
scoreboard players set @s slf.focus 11
scoreboard players set @s slf.focus_stat 4
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 8000
execute if entity @s[tag=slf.was_knight] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Flash Counter","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
