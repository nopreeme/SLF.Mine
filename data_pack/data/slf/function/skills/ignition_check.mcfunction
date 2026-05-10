# Apply Strength I + Speed I for ~3s whenever damage is taken (refreshes each second while in combat)
execute unless score @s slf.dmg_taken = @s slf.dmg_prev run effect give @s minecraft:strength 62 0 true
execute unless score @s slf.dmg_taken = @s slf.dmg_prev run effect give @s minecraft:speed 62 0 true
scoreboard players operation @s slf.dmg_prev = @s slf.dmg_taken
