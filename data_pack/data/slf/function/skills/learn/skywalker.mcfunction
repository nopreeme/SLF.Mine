# AirStep lineage: replaces Skatefoot
tag @s remove slf.skill.skatefoot
tag @s add slf.skill.skywalker
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Skywalker","color":"gold"},{"text":" (replaced Skatefoot)","color":"dark_gray"}]
