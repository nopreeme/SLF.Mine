# Tick down cooldown; block if still cooling
execute if score @s slf.lck_save_cd >= 1 run scoreboard players remove @s slf.lck_save_cd 1
execute if score @s slf.lck_save_cd >= 1 return 0

# Check health <= 2.0 (1 heart); data get * 10 converts float to int for score comparison
execute store result score @s slf.tmp run data get entity @s Health 10
execute unless score @s slf.tmp <= 20 return 0

# Roll 1-100; save triggers if roll <= LCK score (e.g. LCK 25 = 25% chance)
execute store result score @s slf.tmp run random value 1..100
execute if score @s slf.tmp <= @s slf.stat.lck run function slf:stats/lck_save
