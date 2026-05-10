# AirStep lineage: replaces Slide Step
tag @s remove slf.skill.slide_step
tag @s add slf.skill.formula_drift
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Formula Drift","color":"gold"},{"text":" (replaced Slide Step)","color":"dark_gray"}]
