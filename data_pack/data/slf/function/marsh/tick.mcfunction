# Every 4 ticks (skills/tick). The Diremarsh's walking state (design doc V9): in a swamp or mangrove swamp, a survival player
# standing on marsh ground has one leg stuck in the mud at all times - slow, short jumps. Higher ground (#slf:solid_ground:
# rock, logs, planks) frees them.
execute as @a[gamemode=!creative,gamemode=!spectator] at @s run function slf:marsh/check
execute as @a[tag=slf.in_marsh,gamemode=creative] run function slf:marsh/free
execute as @a[tag=slf.in_marsh,gamemode=spectator] run function slf:marsh/free
