execute unless entity @s[tag=slf.was_sword_master] run return fail
scoreboard players set @s slf.class 12
tag @s add slf.skill.inexhaustible_beasts
tag @s add slf.skill.hekaton_slash
tag @s add slf.skill.spectrum_slash
tellraw @s {"text":"You have reached Kansei.","color":"aqua","bold":true}
