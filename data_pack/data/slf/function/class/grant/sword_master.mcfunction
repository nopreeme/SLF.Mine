execute unless entity @s[tag=slf.was_swordsman] run return fail
scoreboard players set @s slf.class 10
tag @s add slf.was_sword_master
tag @s add slf.skill.lash_slash
tag @s add slf.skill.lion_fall
tag @s add slf.skill.shakudanzan
tellraw @s {"text":"You have become a Sword Master.","color":"aqua","bold":true}
