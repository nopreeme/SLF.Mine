# Runs as a night boss at dawn: it leaves (dies without loot, so nobody gets a free drop).
tellraw @a[distance=..96] ["",{"selector":"@s"},{"text":" vanishes with the dawn.","color":"gray","italic":true}]
particle minecraft:large_smoke ~ ~1 ~ 1 1 1 0.05 60
data modify entity @s DeathLootTable set value "minecraft:empty"
tag @s remove slf.mob
kill @s
