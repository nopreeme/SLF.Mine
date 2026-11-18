# Tick down cooldown; block if still cooling
execute if score @s slf.lck_save_cd matches 1.. run scoreboard players remove @s slf.lck_save_cd 1
execute if score @s slf.lck_save_cd matches 1.. run return 0

# Check health <= 2.0 (1 heart); data get * 10 converts float to int for score comparison
execute store result score @s slf.tmp run data get entity @s Health 10
execute unless score @s slf.tmp matches ..20 run return 0

# Clench (食いしばり): at LUC 50+ the save always triggers. Below that, roll 1-100: it triggers if roll <= LUC
# (e.g. LUC 25 = 25% chance)
execute if score @s slf.stat.lck matches 50.. run return run function slf:stats/lck_save
execute store result score @s slf.tmp run random value 1..100
execute if score @s slf.tmp <= @s slf.stat.lck run function slf:stats/lck_save
