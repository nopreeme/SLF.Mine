execute unless entity @s[tag=slf.was_priest] run return fail
scoreboard players set @s slf.class 18
tag @s add slf.was_bishop
tag @s add slf.skill.guardian_heart
tag @s add slf.skill.protect_smash
tag @s add slf.skill.shield_bashing
tellraw @s {"text":"You have become a Bishop.","color":"white","bold":true}
