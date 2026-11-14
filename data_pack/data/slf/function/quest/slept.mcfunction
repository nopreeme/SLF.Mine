# Reward of advancement slf:quest/slept: this player lay down in a bed (vanilla sets their respawn point there).
advancement revoke @s only slf:quest/slept
execute unless score @s slf.q.bed matches 1 run return 0
scoreboard players set @s slf.q.bed 2
scoreboard players add @s slf.exp 75
tag @s add slf.secondil_spawn
give @s minecraft:mushroom_stew[minecraft:item_name={text:"Secondil Stew",color:"white",italic:false}] 1
tellraw @s {"text":" Respawn point registered: Secondil.","color":"green"}
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"A Soft Bed at Last","color":"gold","bold":true},{"text":"  +75 EXP, Secondil respawn point, Secondil Stew","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
