# As the player who first needs an altar. Candidate spots lie on two rings around this player: 8 directions at 320
# blocks, then 8 at 480, starting from a random direction. The first one that is dry ground gets the altar
# (altar/create_try); only one altar is raised at a time.
scoreboard players set #altar_pending slf.timer 1
scoreboard players set #altar_moves slf.timer 0
execute store result storage slf:altar px int 1 run data get entity @s Pos[0]
execute store result storage slf:altar pz int 1 run data get entity @s Pos[2]
execute store result score #altar_dir slf.timer run random value 0..7
function slf:altar/create_pick
