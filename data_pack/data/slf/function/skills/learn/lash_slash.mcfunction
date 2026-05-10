# Slash lineage: replaces Power Slash
tag @s remove slf.skill.power_slash
tag @s add slf.skill.lash_slash
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Lash Slash","color":"gold"},{"text":" (replaced Power Slash)","color":"dark_gray"}]
