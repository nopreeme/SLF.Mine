# As the player who first needs an altar. Picks a spot about 320 blocks away in a random direction, loads that
# chunk and builds once it is ready (altar/create_try). Only one altar is raised at a time.
scoreboard players set #altar_pending slf.timer 1
scoreboard players set #altar_tries slf.timer 0
execute store result score #ax slf.tmp run data get entity @s Pos[0]
execute store result score #az slf.tmp run data get entity @s Pos[2]
execute store result score #dir slf.tmp run random value 0..7
execute if score #dir slf.tmp matches 0 run scoreboard players add #az slf.tmp 320
execute if score #dir slf.tmp matches 1 run scoreboard players add #ax slf.tmp 226
execute if score #dir slf.tmp matches 1 run scoreboard players add #az slf.tmp 226
execute if score #dir slf.tmp matches 2 run scoreboard players add #ax slf.tmp 320
execute if score #dir slf.tmp matches 3 run scoreboard players add #ax slf.tmp 226
execute if score #dir slf.tmp matches 3 run scoreboard players remove #az slf.tmp 226
execute if score #dir slf.tmp matches 4 run scoreboard players remove #az slf.tmp 320
execute if score #dir slf.tmp matches 5 run scoreboard players remove #ax slf.tmp 226
execute if score #dir slf.tmp matches 5 run scoreboard players remove #az slf.tmp 226
execute if score #dir slf.tmp matches 6 run scoreboard players remove #ax slf.tmp 320
execute if score #dir slf.tmp matches 7 run scoreboard players remove #ax slf.tmp 226
execute if score #dir slf.tmp matches 7 run scoreboard players add #az slf.tmp 226
execute store result storage slf:altar cx int 1 run scoreboard players get #ax slf.tmp
execute store result storage slf:altar cz int 1 run scoreboard players get #az slf.tmp
function slf:altar/create_load with storage slf:altar
