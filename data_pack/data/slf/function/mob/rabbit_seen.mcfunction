# Runs once per wild rabbit near a player (mob/tick). One in three becomes a Vorpal Bunny.
# Named rabbits (a player's pet) and babies stay as they are.
tag @s add slf.seen
execute if data entity @s CustomName run return 0
execute unless data entity @s {Age:0} run return 0
execute store result score #roll slf.tmp run random value 1..3
execute if score #roll slf.tmp matches 1 run function slf:mob/vorpal_bunny/convert
