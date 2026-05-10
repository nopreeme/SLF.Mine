execute unless entity @s[tag=slf.was_magic_swordsman] run return fail
scoreboard players set @s slf.class 13
tag @s add slf.was_mysterious_sword
tag @s add slf.skill.sword_dance_reincarnation
tag @s add slf.skill.sword_god_danba
tag @s add slf.skill.asura_kagura
tellraw @s {"text":"You have become a Mysterious Sword user.","color":"aqua","bold":true}
