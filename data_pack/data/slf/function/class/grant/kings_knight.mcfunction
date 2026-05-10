execute unless entity @s[tag=slf.was_holy_knight] run return fail
scoreboard players set @s slf.class 43
tag @s add slf.skill.causal_accumulation
tag @s add slf.skill.unbreakable
tag @s add slf.skill.fatal_gain
tellraw @s {"text":"You have become a King's Knight.","color":"gold","bold":true}
