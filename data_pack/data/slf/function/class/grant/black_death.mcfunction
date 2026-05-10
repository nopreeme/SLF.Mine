execute unless entity @s[tag=slf.was_dark_knight] run return fail
scoreboard players set @s slf.class 44
tag @s add slf.skill.iggist_requiem
tag @s add slf.skill.fatal_gain
tag @s add slf.skill.serial_killer
tellraw @s {"text":"You have become Black Death.","color":"dark_gray","bold":true}
