# Runs once per wild zombie near a player (mob/tick), at the zombie. Design doc V9:
#   Rampant Forest (forests and taiga above y=55): 8 in 20 become Goblins, 1 in 20 is replaced by a rare Vorpal Bunny
#   Diremarsh (swamps above y=55), at night only: 1 in 2 become Redcap Goblins
# Named, baby, AI-less zombies and zombies elsewhere stay zombies.
tag @s add slf.seen
execute if data entity @s CustomName run return 0
execute if data entity @s {IsBaby:1b} run return 0
execute if data entity @s {NoAI:1b} run return 0
execute unless entity @s[y=55,dy=400] run return 0
execute store result score #roll slf.tmp run random value 1..20
execute if predicate slf:night if biome ~ ~ ~ minecraft:swamp if score #roll slf.tmp matches 1..10 run return run function slf:mob/red_hat_goblin/convert
execute if predicate slf:night if biome ~ ~ ~ minecraft:mangrove_swamp if score #roll slf.tmp matches 1..10 run return run function slf:mob/red_hat_goblin/convert
execute unless biome ~ ~ ~ #minecraft:is_forest unless biome ~ ~ ~ #minecraft:is_taiga run return 0
execute if score #roll slf.tmp matches 1 run return run function slf:mob/vorpal_bunny/replace_zombie
execute if score #roll slf.tmp matches 2..9 run function slf:mob/goblin/convert
