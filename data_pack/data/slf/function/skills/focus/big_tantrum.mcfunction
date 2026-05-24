execute if entity @s[tag=slf.skill.big_tantrum] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.big_tantrum] run return fail
execute if score @s slf.focus matches 25 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 25 run return fail
scoreboard players set @s slf.focus 25
scoreboard players set @s slf.focus_stat 4
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 3000
execute if entity @s[tag=slf.was_bandit] run scoreboard players set @s slf.threshold 300
execute if entity @s[tag=slf.was_thief] run scoreboard players set @s slf.threshold 500
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Big Tantrum","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
