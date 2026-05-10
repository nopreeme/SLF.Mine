# Slash lineage: replaces Lash Slash
tag @s remove slf.skill.lash_slash
tag @s add slf.skill.inexhaustible_beasts
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Inexhaustible Beasts","color":"gold"},{"text":" (replaced Lash Slash)","color":"dark_gray"}]
