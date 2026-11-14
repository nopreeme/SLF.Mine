# Runs as the Mud Digger the first time its health drops below 20% (80 of 400).
tag @s add slf.phase2
tellraw @a[gamemode=!creative,gamemode=!spectator,distance=..32] {"text":"The Mud Digger goes berserk and sinks into the marsh!","color":"dark_green","bold":true}
scoreboard players set @s slf.timer 7
