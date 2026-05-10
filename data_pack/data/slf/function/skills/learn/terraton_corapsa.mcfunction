# Heavy lineage: replaces Gigaton Swing
tag @s remove slf.skill.gigaton_swing
tag @s add slf.skill.terraton_corapsa
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Terraton Corapsa","color":"gold"},{"text":" (replaced Gigaton Swing)","color":"dark_gray"}]
