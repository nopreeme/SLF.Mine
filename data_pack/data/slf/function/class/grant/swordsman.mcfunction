execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_swordsman
scoreboard players set @s slf.class 1
tag @s add slf.skill.power_slash
tag @s add slf.skill.sword_of_rough_waves
tag @s add slf.skill.spin_slash
give @s minecraft:iron_sword
give @s minecraft:leather_helmet
give @s minecraft:leather_chestplate
give @s minecraft:leather_leggings
give @s minecraft:leather_boots
tellraw @s {"text":"You have become a Swordsman.","color":"aqua","bold":true}
function slf:class/select_cleanup
