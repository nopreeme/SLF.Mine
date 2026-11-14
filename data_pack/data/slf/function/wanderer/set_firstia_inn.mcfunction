# Admin: marks where you stand as Firstia's inn - where Wanderers wake from the dream.
execute store result storage slf:world firstia.x int 1 run data get entity @s Pos[0]
execute store result storage slf:world firstia.y int 1 run data get entity @s Pos[1]
execute store result storage slf:world firstia.z int 1 run data get entity @s Pos[2]
tellraw @s {"text":"Firstia's inn is here: Wanderers wake here from the dream.","color":"gold"}
