execute unless entity @s[tag=slf.was_knight] run return fail
scoreboard players set @s slf.class 42
tag @s add slf.was_dark_knight
tag @s remove slf.alignment_offered
tellraw @s {"text":"You have become a Dark Knight.","color":"dark_gray","bold":true}
