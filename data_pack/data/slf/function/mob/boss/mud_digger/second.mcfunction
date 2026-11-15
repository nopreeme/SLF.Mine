# Runs as the Mud Digger every second (mob/tick), only while players are near. Design doc V9:
#   It rockets out of the marsh, attacks, and dives back underground to vanish (8 s up, 3 s under, then it bursts out
#   beside its target). Fought solo, it always goes for that one player - the "Solo Killer".
#   Phase 2 (below 20% health): every dive starts with a quake that paralyses anyone standing in mud or water, and every
#   burst comes up right beneath a player and launches them high enough for the fall to kill.
execute unless entity @a[gamemode=!creative,gamemode=!spectator,distance=..32] run return 0
execute unless entity @s[tag=slf.phase2] store result score #hp slf.tmp run data get entity @s Health
execute unless entity @s[tag=slf.phase2] if score #hp slf.tmp matches ..79 run function slf:mob/boss/mud_digger/phase2
scoreboard players add @s slf.timer 1
execute if score @s slf.timer matches 8 run function slf:mob/boss/mud_digger/dive
execute if score @s slf.timer matches 11.. run function slf:mob/boss/mud_digger/emerge
