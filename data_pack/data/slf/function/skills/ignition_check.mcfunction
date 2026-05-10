# Apply Strength I + Speed I for ~3s when damage is taken (refreshes each cycle while in combat)
# Uses slf.ign.prev (NOT slf.def_prev) to avoid collision with sp_tick's delta tracking
execute unless score @s slf.raw.def = @s slf.ign.prev run effect give @s minecraft:strength 62 0 true
execute unless score @s slf.raw.def = @s slf.ign.prev run effect give @s minecraft:speed 62 0 true
scoreboard players operation @s slf.ign.prev = @s slf.raw.def
