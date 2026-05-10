# Slash Ignition: Strength II + Speed II on damage taken (upgraded Ignition)
execute unless score @s slf.raw.def = @s slf.ign.prev run effect give @s minecraft:strength 62 1 true
execute unless score @s slf.raw.def = @s slf.ign.prev run effect give @s minecraft:speed 62 1 true
scoreboard players operation @s slf.ign.prev = @s slf.raw.def
