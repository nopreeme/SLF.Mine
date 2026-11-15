scoreboard players set @s slf.q.brute 1
scoreboard players set @s slf.q.orcs 0
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Orcs lead those goblin parties - bigger, meaner, slower. Bring down two of them near the tree line.","color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
