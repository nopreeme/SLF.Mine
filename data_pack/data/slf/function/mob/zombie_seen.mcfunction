# Runs once per wild zombie near a player (mob/tick). In forests and taiga above y=55 (not in caves), one in two
# becomes a goblin, and one goblin in five is a Red Hat Goblin. Named, baby, AI-less and other zombies stay zombies.
tag @s add slf.seen
execute if data entity @s CustomName run return 0
execute if data entity @s {IsBaby:1b} run return 0
execute if data entity @s {NoAI:1b} run return 0
execute unless biome ~ ~ ~ #minecraft:is_forest unless biome ~ ~ ~ #minecraft:is_taiga run return 0
execute unless entity @s[y=55,dy=400] run return 0
execute store result score #roll slf.tmp run random value 1..10
execute if score #roll slf.tmp matches 1 run return run function slf:mob/red_hat_goblin/convert
execute if score #roll slf.tmp matches 2..5 run function slf:mob/goblin/convert
