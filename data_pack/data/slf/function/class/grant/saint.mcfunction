execute unless entity @s[tag=slf.was_bishop] run return fail
scoreboard players set @s slf.class 19
tag @s add slf.skill.embrace_of_devil
tag @s add slf.skill.causal_accumulation
tag @s add slf.skill.unbreakable
tellraw @s {"text":"You have become a Saint.","color":"white","bold":true}
