execute unless entity @s[tag=slf.was_swordsman] run return fail
scoreboard players set @s slf.class 11
tag @s add slf.was_magic_swordsman
tag @s add slf.skill.slash_ignition
tag @s add slf.skill.sword_dance
tag @s add slf.skill.manbufu
tellraw @s {"text":"You have become a Magic Swordsman.","color":"aqua","bold":true}
