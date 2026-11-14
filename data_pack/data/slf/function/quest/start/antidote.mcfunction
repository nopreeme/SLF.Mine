scoreboard players set @s slf.q.antidote 1
give @s minecraft:paper[minecraft:item_model="slf:antidote_bundle",minecraft:item_name={text:"Antidote Bundle",color:"green",italic:false},minecraft:lore=[{text:"For the inn. Lysa's Antidote Run.",color:"gray",italic:true}]] 3
tellraw @s ["",{"text":"[Lysa] ","color":"light_purple"},{"text":"Three bundles. Marrow will know what to do with them. Thank you!","color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
