# The candidate spot is not dry ground. Unload it and try the next one (16 in all).
function slf:altar/create_unload with storage slf:altar
scoreboard players add #altar_moves slf.timer 1
execute if score #altar_moves slf.timer matches 16.. run return run function slf:altar/create_give_up
function slf:altar/create_pick
