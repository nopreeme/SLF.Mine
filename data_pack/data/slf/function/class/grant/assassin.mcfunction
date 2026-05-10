execute unless entity @s[tag=slf.was_bandit] run return fail
scoreboard players set @s slf.class 16
tag @s add slf.was_assassin
tag @s add slf.skill.desperate_sting
tag @s add slf.skill.masakuru_byte
tag @s add slf.skill.hate_trumple
tellraw @s {"text":"You have become an Assassin.","color":"dark_green","bold":true}
