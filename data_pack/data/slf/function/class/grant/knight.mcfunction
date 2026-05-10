# Requires tier 2 of Swordsman line OR Warrior/Barbarian line (via NPC quest)
execute unless entity @s[tag=slf.was_sword_master] unless entity @s[tag=slf.was_magic_swordsman] unless entity @s[tag=slf.was_barbarian] run return fail
scoreboard players set @s slf.class 40
tag @s add slf.was_knight
tag @s add slf.skill.flash_counter
tag @s add slf.skill.paring_protect
tag @s add slf.skill.total_body_takeshi
tellraw @s {"text":"You have become a Knight.","color":"gold","bold":true}
