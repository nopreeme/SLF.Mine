# Runs once per wild rabbit near a player (mob/tick), at the rabbit. In forests and taiga (the Rampant Forest), one
# in three becomes a Vorpal Bunny. Named rabbits (a player's pet), babies and rabbits elsewhere stay rabbits.
tag @s add slf.seen
execute if data entity @s CustomName run return 0
execute unless data entity @s {Age:0} run return 0
execute unless biome ~ ~ ~ #minecraft:is_forest unless biome ~ ~ ~ #minecraft:is_taiga run return 0
execute store result score #roll slf.tmp run random value 1..3
execute if score #roll slf.tmp matches 1 run function slf:mob/vorpal_bunny/convert
