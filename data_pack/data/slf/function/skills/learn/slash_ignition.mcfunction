# Ignition lineage: replaces Ignition
tag @s remove slf.skill.ignition
tag @s add slf.skill.slash_ignition
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Slash Ignition","color":"gold"},{"text":" (replaced Ignition)","color":"dark_gray"}]
