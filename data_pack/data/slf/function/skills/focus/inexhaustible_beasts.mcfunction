execute if entity @s[tag=slf.skill.inexhaustible_beasts] run return fail
execute unless entity @s[tag=slf.skill.lash_slash] run tellraw @s {"text":"Requires: Lash Slash","color":"red"}
execute unless entity @s[tag=slf.skill.lash_slash] run return fail
execute if score @s slf.focus = 30 run return fail
scoreboard players set @s slf.focus 30
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 8000
execute if entity @s[tag=slf.was_swordsman] run scoreboard players set @s slf.threshold 1000
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Inexhaustible Beasts","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
