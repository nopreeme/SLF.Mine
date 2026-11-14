# Runs as the player at the site: a marker (for the coordinates) and the three finds, which never despawn.
summon minecraft:marker ~ ~ ~ {Tags:["slf.miner_site","slf.scene_new"]}
function slf:quest/miner/journal_item
summon minecraft:item ~1.5 ~0.2 ~ {Tags:["slf.scene_new"],Age:-32768s,PickupDelay:0s,Item:{id:"minecraft:bundle",count:1,components:{"minecraft:item_name":{text:"Torn Miner's Bag",italic:false}}}}
summon minecraft:item ~-1.5 ~0.2 ~ {Tags:["slf.scene_new"],Age:-32768s,PickupDelay:0s,Item:{id:"minecraft:iron_pickaxe",count:1,components:{"minecraft:damage":245,"minecraft:item_name":{text:"Broken Pickaxe",italic:false}}}}
scoreboard players operation @e[tag=slf.scene_new] slf.pid = #me slf.pid
tag @e[tag=slf.scene_new] remove slf.scene_new
