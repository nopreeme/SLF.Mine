execute unless score @s slf.mahni matches 5.. run return run tellraw @s ["",{"text":"[Bartender] ","color":"yellow"},{"text":"Secondil Stew is 5 Mahni. You have ","color":"white"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":".","color":"white"}]
scoreboard players remove @s slf.mahni 5
give @s minecraft:mushroom_stew[minecraft:item_name={text:"Secondil Stew",color:"white",italic:false}] 1
playsound minecraft:entity.villager.yes neutral @s ~ ~ ~ 0.6 1
tellraw @s ["",{"text":" Bought Secondil Stew for 5 Mahni. ","color":"gray"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":" left.","color":"gray"}]
