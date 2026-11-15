scoreboard players set @s slf.q.letter 1
give @s minecraft:paper[minecraft:item_model="slf:sealed_letter",minecraft:item_name={text:"A Sealed Letter",color:"yellow",italic:false},minecraft:lore=[{text:"From the farmer in Firstia, for his brother Garren.",color:"gray",italic:true}]] 1
tellraw @s ["",{"text":" Quest: ","color":"gray"},{"text":"A Brother's Letter","color":"gold","bold":true},{"text":"  Carry it back across the Rampant Forest and give it to Garren yourself.","color":"gray"}]
