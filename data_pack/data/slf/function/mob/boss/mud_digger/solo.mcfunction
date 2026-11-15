# Runs as a player who killed the Mud Digger alone.
give @s minecraft:paper[minecraft:item_model="slf:solo_killers_trophy",minecraft:item_name={text:"Solo Killer's Trophy",color:"gold",italic:false},minecraft:lore=[{text:"Defeated the Mud Digger alone. Brave, or foolish.",color:"gray",italic:true}],minecraft:rarity="epic"] 1
tag @s add slf.title.solo_killer
tellraw @a ["",{"selector":"@s","color":"gold"},{"text":" defeated the Solo Killer alone and earned the title ","color":"yellow"},{"text":"Solo Killer","color":"gold","bold":true},{"text":".","color":"yellow"}]
