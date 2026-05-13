execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_fighter
scoreboard players set @s slf.class 20
tag @s add slf.skill.dual_impact
tag @s add slf.skill.crash_upper
tag @s add slf.skill.knuckle_rush
give @s minecraft:leather_helmet
give @s minecraft:leather_chestplate
give @s minecraft:leather_leggings
give @s minecraft:leather_boots
tellraw @s {"text":"You have become a Fighter.","color":"dark_red","bold":true}
function slf:class/select_cleanup
