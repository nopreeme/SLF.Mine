execute unless entity @s[tag=slf.was_monk] run return fail
scoreboard players set @s slf.class 60
tag @s add slf.was_monk_soldier
tag @s add slf.skill.infight
tag @s add slf.skill.grapple_train
tag @s add slf.skill.meditation
tellraw @s {"text":"You have become a Monk Soldier.","color":"dark_purple","bold":true}
