# Runs as the Mud Digger in Phase 2, as it dives: a marsh-wide quake. Anyone standing in mud or water is paralysed for
# 3 seconds (#slf:marsh_ground); anyone on solid ground (a rock outcrop, a stump) can still move - the design doc's counter.
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..32] at @s if block ~ ~-0.2 ~ #slf:marsh_ground run function slf:mob/boss/mud_digger/paralyse
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..32] at @s if block ~ ~ ~ #slf:marsh_ground run function slf:mob/boss/mud_digger/paralyse
playsound minecraft:entity.warden.emerge hostile @a[distance=..32] ~ ~ ~ 2 0.6
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..32] at @s run particle minecraft:block{block_state:"minecraft:mud"} ~ ~ ~ 2 0.1 2 0 40
