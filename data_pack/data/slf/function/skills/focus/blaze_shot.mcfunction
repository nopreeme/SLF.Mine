execute if entity @s[tag=slf.skill.blaze_shot] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.blaze_shot] run return fail
execute if score @s slf.focus matches 13 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 13 run return fail
scoreboard players set @s slf.focus 13
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 500
execute if entity @s[tag=slf.was_mage] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Blaze Shot","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
