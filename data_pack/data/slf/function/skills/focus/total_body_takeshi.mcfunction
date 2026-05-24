execute if entity @s[tag=slf.skill.total_body_takeshi] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.total_body_takeshi] run return fail
execute if score @s slf.focus matches 12 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 12 run return fail
scoreboard players set @s slf.focus 12
scoreboard players set @s slf.focus_stat 4
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 8000
execute if entity @s[tag=slf.was_knight] run scoreboard players set @s slf.threshold 100
execute if entity @s[tag=slf.was_warrior] run scoreboard players set @s slf.threshold 200
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Total Body Takeshi","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
