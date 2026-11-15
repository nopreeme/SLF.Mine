# Runs as the new Wanderer, at the drop centre: a random spot within 200 blocks (64 if an admin set the forest), tried
# up to 12 times until it lands in a forest or taiga.
scoreboard players add @s slf.wtry 1
execute if data storage slf:world forest run spreadplayers ~ ~ 0 64 false @s
execute unless data storage slf:world forest run spreadplayers ~ ~ 0 200 false @s
execute at @s if biome ~ ~ ~ #minecraft:is_forest run return 1
execute at @s if biome ~ ~ ~ #minecraft:is_taiga run return 1
execute if score @s slf.wtry matches ..11 run function slf:wanderer/drop
