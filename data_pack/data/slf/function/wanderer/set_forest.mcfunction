# Admin: marks where you stand as the centre of the Rampant Forest - Wanderers start within 64 blocks of it.
execute store result storage slf:world forest.x int 1 run data get entity @s Pos[0]
execute store result storage slf:world forest.y int 1 run data get entity @s Pos[1]
execute store result storage slf:world forest.z int 1 run data get entity @s Pos[2]
tellraw @s {"text":"The Rampant Forest is here: Wanderers start within 64 blocks.","color":"gold"}
