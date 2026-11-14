# Runs as a player on step 2 talking to the Elder: hand in 5 Wild Herbs if they have them.
execute store result score #herbs slf.tmp run clear @s minecraft:paper[minecraft:item_model="slf:wild_herb"] 0
execute if score #herbs slf.tmp matches ..4 run return run tellraw @s ["",{"text":"[Town Elder] ","color":"gold"},{"text":"Five Wild Herbs, pioneer. You have ","color":"white"},{"score":{"name":"#herbs","objective":"slf.tmp"},"color":"yellow"},{"text":".","color":"white"}]
clear @s minecraft:paper[minecraft:item_model="slf:wild_herb"] 5
scoreboard players set @s slf.q.awaken 3
scoreboard players add @s slf.exp 50
give @s minecraft:potion[minecraft:potion_contents={potion:"minecraft:healing"},minecraft:item_name={text:"Basic Health Potion",color:"red",italic:false}] 3
tellraw @s ["",{"text":"[Town Elder] ","color":"gold"},{"text":"These will see our people through the week. Thank you - take these potions, you'll need them out there.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"A Pioneer's Awakening","color":"gold","bold":true},{"text":"  +50 EXP, 3 Basic Health Potions","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
