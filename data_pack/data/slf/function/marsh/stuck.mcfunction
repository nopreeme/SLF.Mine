# One leg in the mud: -40% movement, -40% jump. (Adding a modifier the player already has just fails quietly.)
execute unless entity @s[tag=slf.in_marsh] run title @s actionbar {"text":"The marsh grips your legs - find solid ground","color":"dark_green"}
tag @s add slf.in_marsh
attribute @s minecraft:movement_speed modifier add slf:marsh_walk -0.4 add_multiplied_total
attribute @s minecraft:jump_strength modifier add slf:marsh_jump -0.4 add_multiplied_total
