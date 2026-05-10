execute unless entity @s[tag=slf.was_fighter] run return fail
scoreboard players set @s slf.class 21
tag @s add slf.was_destroyer
tag @s add slf.skill.meteor_fall
tag @s add slf.skill.zanzui_flying_blade_leg
tag @s add slf.skill.grapple_train
tellraw @s {"text":"You have become a Destroyer.","color":"dark_red","bold":true}
