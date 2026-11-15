execute if biome ~ ~ ~ minecraft:swamp unless block ~ ~-0.2 ~ #slf:solid_ground unless block ~ ~-1.2 ~ #slf:solid_ground run return run function slf:marsh/stuck
execute if biome ~ ~ ~ minecraft:mangrove_swamp unless block ~ ~-0.2 ~ #slf:solid_ground unless block ~ ~-1.2 ~ #slf:solid_ground run return run function slf:marsh/stuck
execute if entity @s[tag=slf.in_marsh] run function slf:marsh/free
