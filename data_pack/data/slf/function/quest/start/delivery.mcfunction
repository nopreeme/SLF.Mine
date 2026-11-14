scoreboard players set @s slf.q.delivery 1
give @s minecraft:paper[minecraft:item_model="slf:beef_package",minecraft:item_name={text:"Sealed Beef Package",color:"yellow",italic:false},minecraft:lore=[{text:"For Garren, at the armor shop in Secondil.",color:"gray",italic:true}]] 1
tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"His finest customer will be you, I'm sure. Secondil is a real city - brick, lamps, even a castle. Your journey's truly begun.","color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
