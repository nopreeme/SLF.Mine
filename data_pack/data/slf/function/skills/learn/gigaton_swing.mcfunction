# Heavy lineage: replaces Megaton Swing
tag @s remove slf.skill.megaton_swing
tag @s add slf.skill.gigaton_swing
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Gigaton Swing","color":"gold"},{"text":" (replaced Megaton Swing)","color":"dark_gray"}]
