tag @s add slf.skill.flash_counter
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill learned: ","color":"green"},{"text":"Flash Counter","color":"gold"}]
