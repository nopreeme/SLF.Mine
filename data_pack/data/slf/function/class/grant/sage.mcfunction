execute unless entity @s[tag=slf.was_mage] run return fail
scoreboard players set @s slf.class 70
tag @s add slf.was_sage
tag @s add slf.skill.instant_vision
tag @s add slf.skill.hegemony_world
tag @s add slf.skill.analyze_legacy
tellraw @s {"text":"You have become a Sage.","color":"blue","bold":true}
