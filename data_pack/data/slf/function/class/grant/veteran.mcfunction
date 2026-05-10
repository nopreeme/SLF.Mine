execute unless entity @s[tag=slf.was_mercenary] run return fail
scoreboard players set @s slf.class 31
tag @s add slf.was_veteran
tag @s add slf.skill.parabelum_routine
tag @s add slf.skill.victim_arts
tag @s add slf.skill.highest_strength
tellraw @s {"text":"You have become a Veteran.","color":"yellow","bold":true}
