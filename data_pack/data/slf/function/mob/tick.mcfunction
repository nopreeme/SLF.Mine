# Every 20 ticks (skills/tick). Wild rabbits near players get their one chance to become Vorpal Bunnies.
execute as @a at @s as @e[type=minecraft:rabbit,tag=!slf.seen,distance=..64] run function slf:mob/rabbit_seen
# Bosses: upkeep every second, encounter rolls once a minute (mob/boss/roll)
function slf:mob/boss/tick
scoreboard players add #boss_timer slf.timer 1
execute if score #boss_timer slf.timer matches 60.. as @a[gamemode=!creative,gamemode=!spectator] at @s run function slf:mob/boss/roll
execute if score #boss_timer slf.timer matches 60.. run scoreboard players set #boss_timer slf.timer 0
