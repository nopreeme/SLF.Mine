# Sets storage cx/cz to candidate number #altar_moves (direction #altar_dir + moves, ring by moves) and loads it.
execute store result score #ax slf.tmp run data get storage slf:altar px
execute store result score #az slf.tmp run data get storage slf:altar pz
scoreboard players operation #d slf.tmp = #altar_dir slf.timer
scoreboard players operation #d slf.tmp += #altar_moves slf.timer
scoreboard players set #8 slf.tmp 8
scoreboard players operation #d slf.tmp %= #8 slf.tmp
scoreboard players set #r slf.tmp 0
execute if score #altar_moves slf.timer matches 8.. run scoreboard players set #r slf.tmp 1
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 0 run scoreboard players add #az slf.tmp 320
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 1 run scoreboard players add #ax slf.tmp 226
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 1 run scoreboard players add #az slf.tmp 226
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 2 run scoreboard players add #ax slf.tmp 320
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 3 run scoreboard players add #ax slf.tmp 226
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 3 run scoreboard players remove #az slf.tmp 226
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 4 run scoreboard players remove #az slf.tmp 320
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 5 run scoreboard players remove #ax slf.tmp 226
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 5 run scoreboard players remove #az slf.tmp 226
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 6 run scoreboard players remove #ax slf.tmp 320
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 7 run scoreboard players remove #ax slf.tmp 226
execute if score #r slf.tmp matches 0 if score #d slf.tmp matches 7 run scoreboard players add #az slf.tmp 226
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 0 run scoreboard players add #az slf.tmp 480
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 1 run scoreboard players add #ax slf.tmp 339
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 1 run scoreboard players add #az slf.tmp 339
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 2 run scoreboard players add #ax slf.tmp 480
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 3 run scoreboard players add #ax slf.tmp 339
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 3 run scoreboard players remove #az slf.tmp 339
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 4 run scoreboard players remove #az slf.tmp 480
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 5 run scoreboard players remove #ax slf.tmp 339
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 5 run scoreboard players remove #az slf.tmp 339
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 6 run scoreboard players remove #ax slf.tmp 480
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 7 run scoreboard players remove #ax slf.tmp 339
execute if score #r slf.tmp matches 1 if score #d slf.tmp matches 7 run scoreboard players add #az slf.tmp 339
execute store result storage slf:altar cx int 1 run scoreboard players get #ax slf.tmp
execute store result storage slf:altar cz int 1 run scoreboard players get #az slf.tmp
scoreboard players set #altar_tries slf.timer 0
function slf:altar/create_load with storage slf:altar
