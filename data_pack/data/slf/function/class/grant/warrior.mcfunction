execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_warrior
scoreboard players set @s slf.class 2
tag @s add slf.skill.megaton_swing
tag @s add slf.skill.rigid_strength
tag @s add slf.skill.front_position
give @s minecraft:stone_axe
give @s minecraft:chainmail_chestplate
give @s minecraft:leather_leggings
give @s minecraft:leather_boots
tellraw @s {"text":"You have become a Warrior.","color":"red","bold":true}
function slf:class/select_cleanup
