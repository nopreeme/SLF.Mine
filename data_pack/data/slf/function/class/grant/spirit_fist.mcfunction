execute unless entity @s[tag=slf.was_monk_soldier] run return fail
scoreboard players set @s slf.class 61
tag @s add slf.skill.hand_of_fortune
tag @s add slf.skill.kings_silver_arm
tag @s add slf.skill.hundred_sounding
tellraw @s {"text":"You have become Spirit Fist.","color":"dark_purple","bold":true}
