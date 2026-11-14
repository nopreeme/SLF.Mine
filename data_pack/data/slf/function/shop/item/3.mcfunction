execute unless score @s slf.mahni matches 10.. run return run tellraw @s ["",{"text":"[Bartender] ","color":"yellow"},{"text":"Strong Ale is 10 Mahni. You have ","color":"white"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":".","color":"white"}]
scoreboard players remove @s slf.mahni 10
give @s minecraft:potion[minecraft:potion_contents={custom_color:13145344,custom_effects:[{id:"minecraft:strength",duration:1200,amplifier:0},{id:"minecraft:nausea",duration:160,amplifier:0}]},minecraft:item_name={text:"Strong Ale",color:"gold",italic:false}] 1
playsound minecraft:entity.villager.yes neutral @s ~ ~ ~ 0.6 1
tellraw @s ["",{"text":" Bought Strong Ale for 10 Mahni. ","color":"gray"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":" left.","color":"gray"}]
