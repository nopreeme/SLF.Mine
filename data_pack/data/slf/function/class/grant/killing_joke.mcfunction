execute unless entity @s[tag=slf.was_assassin] run return fail
scoreboard players set @s slf.class 17
tag @s add slf.skill.limit_break_rees
tag @s add slf.skill.ablaze_advanced_ale
tag @s add slf.skill.serial_killer
tellraw @s {"text":"You have become Killing Joke.","color":"dark_green","bold":true}
