scoreboard players set @s slf.q.watch 1
scoreboard players set @s slf.q.watch_t 0
tellraw @s ["",{"text":"[Guard Halvor] ","color":"aqua"},{"text":"Come back after dark and stay near me. Watch the tree line to the west.","color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
