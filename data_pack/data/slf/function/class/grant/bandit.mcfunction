execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_bandit
scoreboard players set @s slf.class 3
scoreboard players set @s slf.level 1
tag @s add slf.skill.dirty_sword
tag @s add slf.skill.assassin_pierce
tag @s add slf.skill.big_tantrum
give @s minecraft:stone_sword
function slf:give/armor_leather_full
give @s minecraft:bow
give @s minecraft:arrow 16
tellraw @s {"text":"You have become a Bandit.","color":"dark_green","bold":true}
function slf:class/select_cleanup
