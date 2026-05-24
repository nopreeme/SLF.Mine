execute if entity @s[tag=slf.skill.lash_slash] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.lash_slash] run return fail
execute unless entity @s[tag=slf.skill.power_slash] run tellraw @s {"text":"Requires: Power Slash","color":"red"}
execute unless entity @s[tag=slf.skill.power_slash] run return fail
execute if score @s slf.focus matches 20 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 20 run return fail
scoreboard players set @s slf.focus 20
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_swordsman] run scoreboard players set @s slf.threshold 300
execute if entity @s[tag=slf.was_warrior] run scoreboard players set @s slf.threshold 350
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Lash Slash","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
