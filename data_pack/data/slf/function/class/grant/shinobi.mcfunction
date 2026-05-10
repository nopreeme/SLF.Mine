execute unless entity @s[tag=slf.was_ninja] run return fail
scoreboard players set @s slf.class 52
tag @s add slf.was_shinobi
tag @s add slf.skill.skywalker
tag @s add slf.skill.after_all_unyo
tag @s add slf.skill.burnout
tellraw @s {"text":"You have become a Shinobi.","color":"dark_green","bold":true}
