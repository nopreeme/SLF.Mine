execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_priest
scoreboard players set @s slf.class 4
scoreboard players set @s slf.level 1
tag @s add slf.skill.breath_of_anti_harm
tag @s add slf.skill.phalanx
tag @s add slf.skill.protect_charge
give @s minecraft:wooden_sword
give @s minecraft:shield
give @s minecraft:leather_chestplate
give @s minecraft:bread 8
tellraw @s {"text":"You have become a Priest.","color":"white","bold":true}
function slf:class/select_cleanup
