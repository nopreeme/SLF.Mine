execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_thief
scoreboard players set @s slf.class 3
tag @s add slf.skill.stealth_assault
tag @s add slf.skill.slide_step
tag @s add slf.skill.quick_spin
tellraw @s {"text":"You have become a Thief.","color":"dark_green","bold":true}
