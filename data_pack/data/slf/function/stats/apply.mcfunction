# Runs every 20t — translates stat scores into Minecraft effect equivalents
# Effects use short duration (3) so they expire if stats are removed; refreshed each cycle

# AGI -> Speed: 5 AGI = Speed I, 10 = Speed II, 20 = Speed III
execute as @a if score @s slf.stat.agi matches 5..9 run effect give @s minecraft:speed 3 0 true
execute as @a if score @s slf.stat.agi matches 10..19 run effect give @s minecraft:speed 3 1 true
execute as @a if score @s slf.stat.agi matches 20.. run effect give @s minecraft:speed 3 2 true

# STM -> Haste / Saturation: 5 STM = Saturation I; 10+ = Haste I
execute as @a if score @s slf.stat.stm matches 5.. run effect give @s minecraft:saturation 3 0 true
execute as @a if score @s slf.stat.stm matches 10.. run effect give @s minecraft:haste 3 0 true

# VIT -> Max HP: each 5 VIT = 1 extra heart (max hearts handled via Health attribute)
# Approximation via absorption as a stand-in until attribute commands are wired in
execute as @a if score @s slf.stat.vit matches 5..9 run effect give @s minecraft:absorption 3 0 true
execute as @a if score @s slf.stat.vit matches 10..19 run effect give @s minecraft:absorption 3 1 true
execute as @a if score @s slf.stat.vit matches 20..29 run effect give @s minecraft:absorption 3 2 true
execute as @a if score @s slf.stat.vit matches 30.. run effect give @s minecraft:absorption 3 3 true

# STR -> raw Strength effect (stacks with skill-granted strength, fine since effects merge)
execute as @a if score @s slf.stat.str matches 10..19 run effect give @s minecraft:strength 3 0 true
execute as @a if score @s slf.stat.str matches 20.. run effect give @s minecraft:strength 3 1 true

# DEX -> attack speed: remove stale modifier then re-add at correct tier
execute as @a run attribute @s minecraft:attack_speed modifier remove slf:dex_speed
execute as @a if score @s slf.stat.dex matches 5..9 run attribute @s minecraft:attack_speed modifier add slf:dex_speed 0.4 add_value
execute as @a if score @s slf.stat.dex matches 10..19 run attribute @s minecraft:attack_speed modifier add slf:dex_speed 0.8 add_value
execute as @a if score @s slf.stat.dex matches 20.. run attribute @s minecraft:attack_speed modifier add slf:dex_speed 1.2 add_value

# LCK -> Minecraft luck attribute (affects loot table rolls)
execute as @a run attribute @s minecraft:luck base set 0
execute as @a if score @s slf.stat.lck matches 10..19 run attribute @s minecraft:luck base set 1
execute as @a if score @s slf.stat.lck matches 20..39 run attribute @s minecraft:luck base set 2
execute as @a if score @s slf.stat.lck matches 40..59 run attribute @s minecraft:luck base set 3
execute as @a if score @s slf.stat.lck matches 60.. run attribute @s minecraft:luck base set 4
