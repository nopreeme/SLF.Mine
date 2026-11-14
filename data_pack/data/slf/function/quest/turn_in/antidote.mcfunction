execute store result score #b slf.tmp run clear @s minecraft:paper[minecraft:item_model="slf:antidote_bundle"] 0
execute if score #b slf.tmp matches ..2 run return run tellraw @s ["",{"text":"[Innkeeper Marrow] ","color":"gold"},{"text":"Lysa always sends three. You've only got ","color":"white"},{"score":{"name":"#b","objective":"slf.tmp"},"color":"yellow"},{"text":".","color":"white"}]
clear @s minecraft:paper[minecraft:item_model="slf:antidote_bundle"] 3
scoreboard players set @s slf.q.antidote 2
scoreboard players add @s slf.exp 100
scoreboard players add @s slf.mahni 30
give @s minecraft:honey_bottle[minecraft:item_name={text:"Antidote",color:"green",italic:false},minecraft:lore=[{text:"Cures poison. Lysa makes them daily.",color:"gray",italic:true}]] 2
tellraw @s ["",{"text":"[Innkeeper Marrow] ","color":"gold"},{"text":"Bless that girl. There are two upstairs who'll live because of these. Here - Lysa wanted you to have a couple.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Antidote Run","color":"gold","bold":true},{"text":"  +100 EXP, +30 Mahni, 2 Antidotes","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
