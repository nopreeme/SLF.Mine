execute unless score @s slf.mahni matches 20.. run return run tellraw @s ["",{"text":"[Lysa] ","color":"light_purple"},{"text":"Basic Health Potion is 20 Mahni. You have ","color":"white"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":".","color":"white"}]
scoreboard players remove @s slf.mahni 20
give @s minecraft:potion[minecraft:potion_contents={potion:"minecraft:healing"},minecraft:item_name={text:"Basic Health Potion",color:"red",italic:false}] 1
playsound minecraft:entity.villager.yes neutral @s ~ ~ ~ 0.6 1
tellraw @s ["",{"text":" Bought Basic Health Potion for 20 Mahni. ","color":"gray"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":" left.","color":"gray"}]
