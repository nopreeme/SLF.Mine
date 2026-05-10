# Runs at player position; don't spawn if one is already nearby
execute if entity @e[type=minecraft:pillager,tag=slf.bounty_hunter,distance=..30] run return fail
summon minecraft:pillager ~ ~ ~ {Tags:["slf.bounty_hunter"],Health:40.0,Attributes:[{Name:"minecraft:generic.max_health",Base:40.0},{Name:"minecraft:generic.movement_speed",Base:0.38}]}
effect give @e[type=minecraft:pillager,tag=slf.bounty_hunter,distance=..5,limit=1] minecraft:strength 600 1 true
tellraw @s {"text":"A Bounty Hunter has found you.","color":"dark_red","bold":true}
