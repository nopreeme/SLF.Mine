# Runs every 20t — translates stat scores into Minecraft effect equivalents
# Effects use short duration (3) so they expire if stats are removed; refreshed each cycle

# AGI -> Speed: 5 AGI = Speed I, 10 = Speed II, 20 = Speed III
execute as @a[scores={slf.stat.agi=5..9}]   run effect give @s minecraft:speed 3 0 true
execute as @a[scores={slf.stat.agi=10..19}]  run effect give @s minecraft:speed 3 1 true
execute as @a[scores={slf.stat.agi=20..}]    run effect give @s minecraft:speed 3 2 true

# STM -> Haste / Saturation: 5 STM = Saturation I; 10+ = Haste I
execute as @a[scores={slf.stat.stm=5..}]     run effect give @s minecraft:saturation 3 0 true
execute as @a[scores={slf.stat.stm=10..}]    run effect give @s minecraft:haste 3 0 true

# VIT -> Max HP: each 5 VIT = 1 extra heart (max hearts handled via Health attribute)
# Approximation via absorption as a stand-in until attribute commands are wired in
execute as @a[scores={slf.stat.vit=5..9}]   run effect give @s minecraft:absorption 3 0 true
execute as @a[scores={slf.stat.vit=10..19}]  run effect give @s minecraft:absorption 3 1 true
execute as @a[scores={slf.stat.vit=20..29}]  run effect give @s minecraft:absorption 3 2 true
execute as @a[scores={slf.stat.vit=30..}]    run effect give @s minecraft:absorption 3 3 true

# STR -> raw Strength effect (stacks with skill-granted strength, fine since effects merge)
execute as @a[scores={slf.stat.str=10..19}]  run effect give @s minecraft:strength 3 0 true
execute as @a[scores={slf.stat.str=20..}]    run effect give @s minecraft:strength 3 1 true
