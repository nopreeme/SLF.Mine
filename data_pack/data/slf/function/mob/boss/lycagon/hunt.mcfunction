# Runs as Lycagon every second: angry at the nearest survival player within 48 blocks for the next 30 seconds.
execute store result score #t slf.tmp run time query gametime
scoreboard players add #t slf.tmp 600
execute if entity @p[gamemode=!creative,gamemode=!spectator,distance=..48] store result entity @s anger_end_time long 1 run scoreboard players get #t slf.tmp
data modify entity @s angry_at set from entity @p[gamemode=!creative,gamemode=!spectator,distance=..48] UUID
