# Runs once per wild frog near a player (mob/tick), at the frog. Every frog in a swamp or mangrove swamp (the Diremarsh)
# is a Mud Frog. Named frogs and frogs elsewhere stay frogs.
tag @s add slf.seen
execute if data entity @s CustomName run return 0
execute unless biome ~ ~ ~ minecraft:swamp unless biome ~ ~ ~ minecraft:mangrove_swamp run return 0
function slf:mob/mud_frog/convert
