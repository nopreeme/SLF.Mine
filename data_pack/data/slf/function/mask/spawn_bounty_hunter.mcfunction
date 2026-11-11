# Runs at player position; don't spawn if one is already nearby
execute if entity @e[type=minecraft:pillager,tag=slf.bounty_hunter,distance=..30] run return fail
summon minecraft:pillager ~ ~ ~ {Tags:["slf.bounty_hunter"],Health:40.0f,attributes:[{id:"minecraft:max_health",base:40.0},{id:"minecraft:movement_speed",base:0.38}]}
effect give @e[type=minecraft:pillager,tag=slf.bounty_hunter,distance=..5,limit=1] minecraft:strength 600 1 true
tellraw @s {"text":"A Bounty Hunter has found you.","color":"dark_red","bold":true}
