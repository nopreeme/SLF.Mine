execute if entity @s[tag=slf.skill.paring_protect] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.paring_protect] run return fail
execute if score @s slf.focus matches 10 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 10 run return fail
scoreboard players set @s slf.focus 10
scoreboard players set @s slf.focus_stat 4
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 8000
execute if entity @s[tag=slf.was_knight] run scoreboard players set @s slf.threshold 100
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Paring Protect","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
