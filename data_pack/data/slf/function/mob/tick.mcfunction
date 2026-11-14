# Every 20 ticks (skills/tick). Wild rabbits near players get their one chance to become Vorpal Bunnies.
execute as @a at @s as @e[type=minecraft:rabbit,tag=!slf.seen,distance=..64] at @s run function slf:mob/rabbit_seen
# Wild swamp frogs near players are Mud Frogs (mob/frog_seen).
execute as @a at @s as @e[type=minecraft:frog,tag=!slf.seen,distance=..64] at @s run function slf:mob/frog_seen
# Wild surface zombies near players: goblins and Vorpal Bunnies in forests, Redcaps in swamps at night (mob/zombie_seen).
execute as @a at @s as @e[type=minecraft:zombie,tag=!slf.seen,distance=..64] at @s run function slf:mob/zombie_seen
# Bosses: upkeep every second, encounter rolls once a minute (mob/boss/roll)
function slf:mob/boss/tick
execute as @e[tag=slf.snake] at @s run function slf:mob/boss/ravenous_snake/second
execute as @e[tag=slf.mud_digger] at @s run function slf:mob/boss/mud_digger/second
scoreboard players add #boss_timer slf.timer 1
execute if score #boss_timer slf.timer matches 60.. as @a[gamemode=!creative,gamemode=!spectator] at @s run function slf:mob/boss/roll
execute if score #boss_timer slf.timer matches 60.. run scoreboard players set #boss_timer slf.timer 0
# Night-only mobs (Redcap Goblins) leave at dawn, once they have seen a night.
execute if predicate slf:night run tag @e[tag=slf.night_mob] add slf.saw_night
execute unless predicate slf:night as @e[tag=slf.night_mob,tag=slf.saw_night] at @s run function slf:mob/vanish
