scoreboard players add #altar_tries slf.timer 1
execute if score #altar_tries slf.timer matches ..60 run return run schedule function slf:altar/create_try 20t
function slf:altar/create_unload with storage slf:altar
function slf:altar/create_give_up
