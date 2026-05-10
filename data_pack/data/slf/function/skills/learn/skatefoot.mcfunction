# AirStep lineage: replaces Formula Drift
tag @s remove slf.skill.formula_drift
tag @s add slf.skill.skatefoot
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Skatefoot","color":"gold"},{"text":" (replaced Formula Drift)","color":"dark_gray"}]
