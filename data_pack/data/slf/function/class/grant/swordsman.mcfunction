execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_swordsman
scoreboard players set @s slf.class 1
tag @s add slf.skill.power_slash
tag @s add slf.skill.sword_of_rough_waves
tag @s add slf.skill.spin_slash
tellraw @s {"text":"You have become a Swordsman.","color":"aqua","bold":true}
