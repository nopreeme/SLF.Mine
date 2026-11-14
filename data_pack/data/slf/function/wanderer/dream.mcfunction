# Runs as a Wanderer who died before sleeping at Secondil's inn (design doc V9, 6.2). Everything since the forest is
# erased: what they dropped, their level, EXP, Mahni, stat points and skill progress. They keep their class, their skills
# and the Wanderer traits, and wake at Firstia's inn (their respawn point) free to play on as a citizen would.
execute at @s run kill @e[type=minecraft:item,distance=..8]
clear @s
scoreboard players set @s slf.level 1
scoreboard players set @s slf.exp 0
scoreboard players set @s slf.exp_extend 0
scoreboard players set @s slf.standby 0
scoreboard players set @s slf.sp_points 0
scoreboard players set @s slf.mahni 0
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.stat.hp 0
scoreboard players set @s slf.stat.mp 0
scoreboard players set @s slf.stat.str 0
scoreboard players set @s slf.stat.dex 0
scoreboard players set @s slf.stat.vit 0
scoreboard players set @s slf.stat.agi 0
scoreboard players set @s slf.stat.tec 0
scoreboard players set @s slf.stat.lck 0
scoreboard players set @s slf.stat.stm 0
tag @s remove slf.wandering
tag @s add slf.dreamt
title @s times 10 80 20
title @s title {"text":"...only a dream","color":"gray","italic":true}
tellraw @s {"text":"You wake in an inn in Firstia - a town you have never seen. A system message flickers: your adventure was only a dream. Everything since the forest is gone.","color":"gray","italic":true}
