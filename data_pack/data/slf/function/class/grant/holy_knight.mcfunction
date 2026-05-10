execute unless entity @s[tag=slf.was_knight] run return fail
scoreboard players set @s slf.class 41
tag @s add slf.was_holy_knight
tag @s remove slf.alignment_offered
tellraw @s {"text":"You have become a Holy Knight.","color":"yellow","bold":true}
