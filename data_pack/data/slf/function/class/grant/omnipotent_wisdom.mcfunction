execute unless entity @s[tag=slf.was_sage] run return fail
scoreboard players set @s slf.class 71
tag @s add slf.skill.chronostaxia
tag @s add slf.skill.star_yukai_wire
tag @s add slf.skill.iggist_requiem
tellraw @s {"text":"You have reached Omnipotent Wisdom.","color":"blue","bold":true}
