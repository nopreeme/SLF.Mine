execute unless entity @s[tag=slf.was_thief] run return fail
scoreboard players set @s slf.class 51
tag @s add slf.was_ninja
tag @s add slf.skill.formula_drift
tag @s add slf.skill.skatefoot
tag @s add slf.skill.rechette_step
tellraw @s {"text":"You have become a Ninja.","color":"dark_green","bold":true}
