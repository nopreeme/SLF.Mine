# Requires Warrior OR Fighter history
execute unless entity @s[tag=slf.was_warrior] unless entity @s[tag=slf.was_fighter] run return fail
scoreboard players set @s slf.class 14
tag @s add slf.was_barbarian
tag @s add slf.skill.gigaton_swing
tag @s add slf.skill.fortress_breaker
tag @s add slf.skill.gobus_courage
tellraw @s {"text":"You have become a Barbarian.","color":"red","bold":true}
