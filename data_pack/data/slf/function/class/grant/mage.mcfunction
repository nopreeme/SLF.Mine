execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_mage
scoreboard players set @s slf.class 6
tag @s add slf.skill.wisdoms_divine_eye
tag @s add slf.skill.chanting_and_memorizing
tag @s add slf.skill.tanda_breathing
tellraw @s {"text":"You have become a Mage.","color":"blue","bold":true}
