execute if entity @s[tag=slf.skill.skywalker] run tellraw @s {"text":"You already know this skill!","color":"red"}
execute if entity @s[tag=slf.skill.skywalker] run return fail
execute unless entity @s[tag=slf.skill.skatefoot] run tellraw @s {"text":"Requires: Skatefoot","color":"red"}
execute unless entity @s[tag=slf.skill.skatefoot] run return fail
execute if score @s slf.focus matches 33 run tellraw @s {"text":"Already focusing this skill.","color":"yellow"}
execute if score @s slf.focus matches 33 run return fail
scoreboard players set @s slf.focus 33
scoreboard players set @s slf.focus_stat 3
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 5000
execute if entity @s[tag=slf.was_shinobi] run scoreboard players set @s slf.threshold 500
execute if entity @s[tag=slf.was_ninja] run scoreboard players set @s slf.threshold 700
tellraw @s ["",{"text":"Focusing: ","color":"gray"},{"text":"Skywalker","color":"gold"},{"text":" [0/","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.threshold"}},{"text":"]","color":"dark_gray"}]
