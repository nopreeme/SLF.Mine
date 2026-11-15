execute unless score @s slf.mahni matches 15.. run return run tellraw @s ["",{"text":"[Lysa] ","color":"light_purple"},{"text":"Antidote is 15 Mahni. You have ","color":"white"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":".","color":"white"}]
scoreboard players remove @s slf.mahni 15
give @s minecraft:honey_bottle[minecraft:item_name={text:"Antidote",color:"green",italic:false},minecraft:lore=[{text:"Cures poison. Lysa makes them daily.",color:"gray",italic:true}]] 1
playsound minecraft:entity.villager.yes neutral @s ~ ~ ~ 0.6 1
tellraw @s ["",{"text":" Bought Antidote for 15 Mahni. ","color":"gray"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":" left.","color":"gray"}]
