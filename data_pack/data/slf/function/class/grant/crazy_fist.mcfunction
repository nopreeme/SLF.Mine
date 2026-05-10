execute unless entity @s[tag=slf.was_destroyer] run return fail
scoreboard players set @s slf.class 22
tag @s add slf.skill.strong_puncher
tag @s add slf.skill.one_inch_impact
tag @s add slf.skill.hundred_sounding
tellraw @s {"text":"You have become Crazy Fist.","color":"dark_red","bold":true}
