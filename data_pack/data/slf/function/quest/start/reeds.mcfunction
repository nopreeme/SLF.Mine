scoreboard players set @s slf.q.reeds 1
scoreboard players set @s slf.q.wave 0
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Halvor's at the western gate. Show him the journal.","color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
