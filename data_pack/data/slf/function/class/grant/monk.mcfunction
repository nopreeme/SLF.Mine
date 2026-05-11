execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_monk
scoreboard players set @s slf.class 5
tag @s add slf.skill.tasram_fist
tag @s add slf.skill.skull_shaker
tag @s add slf.skill.tanda_breathing
tellraw @s {"text":"You have become a Monk.","color":"dark_purple","bold":true}
function slf:class/select_cleanup
