# Every 20 ticks (skills/tick). Wild rabbits near players get their one chance to become Vorpal Bunnies.
execute as @a at @s as @e[type=minecraft:rabbit,tag=!slf.seen,distance=..64] run function slf:mob/rabbit_seen
