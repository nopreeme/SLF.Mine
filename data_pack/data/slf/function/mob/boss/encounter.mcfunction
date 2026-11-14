# Macro, runs as a player at the player. Arguments: id, place (surface / under / sky).
# Spawns the boss up to 24 blocks away and warns everyone nearby.
$function slf:mob/boss/$(id)/spawn
execute store result storage slf:mob y int 1 run data get entity @s Pos[1] 1
$function slf:mob/boss/place_$(place)
tellraw @a[distance=..96] ["",{"text":"⚠ ","color":"red"},{"selector":"@e[tag=slf.boss_new]"},{"text":" has appeared!","color":"red","bold":true}]
playsound minecraft:entity.wither.spawn hostile @a[distance=..96] ~ ~ ~ 0.6 0.7
tag @e[tag=slf.boss_new] remove slf.boss_new
