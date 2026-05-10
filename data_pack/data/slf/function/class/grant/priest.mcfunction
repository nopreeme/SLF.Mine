execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_priest
scoreboard players set @s slf.class 4
tag @s add slf.skill.breath_of_anti_harm
tag @s add slf.skill.phalanx
tag @s add slf.skill.protect_charge
tellraw @s {"text":"You have become a Priest.","color":"white","bold":true}
