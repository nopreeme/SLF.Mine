execute if entity @s[tag=slf.skill.slash_ignition] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.slash_ignition] run return fail
execute unless entity @s[tag=slf.skill.ignition] run tellraw @s {"text":"Requires: Ignition","color":"red"}
execute unless entity @s[tag=slf.skill.ignition] run return fail
execute if score @s slf.focus matches 23 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 23 run return fail
scoreboard players set @s slf.focus 23
scoreboard players set @s slf.focus_stat 1
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 2000
execute if entity @s[tag=slf.was_mercenary] run scoreboard players set @s slf.threshold 300
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Slash Ignition","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
