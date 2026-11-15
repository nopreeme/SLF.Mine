scoreboard players set @s slf.q.outskirts 1
scoreboard players set @s slf.q.goblins 0
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Good. Five goblins, around the western walls and the forest edge. Come back when it's done.","color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
