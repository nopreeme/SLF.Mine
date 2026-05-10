tag @s add slf.skill.ignition
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill learned: ","color":"green"},{"text":"Ignition","color":"gold"}]
