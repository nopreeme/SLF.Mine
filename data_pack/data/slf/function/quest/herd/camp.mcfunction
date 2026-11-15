# Runs as the player, at the camp spot.
summon minecraft:villager ~ ~ ~ {Tags:["slf.npc","slf.npc.daughter","slf.scene_new"],Age:-24000,AgeLocked:1b,NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomNameVisible:1b,CustomName:{text:"Farmer's Daughter",color:"light_purple"},VillagerData:{profession:"minecraft:none",level:1,type:"minecraft:plains"},Offers:{Recipes:[]}}
summon minecraft:cow ~3 ~ ~2 {Tags:["slf.herd","slf.scene_new"],PersistenceRequired:1b,CustomName:{text:"Farmer's Cow",color:"yellow"}}
summon minecraft:cow ~-3 ~ ~2 {Tags:["slf.herd","slf.scene_new"],PersistenceRequired:1b,CustomName:{text:"Farmer's Cow",color:"yellow"}}
summon minecraft:cow ~ ~ ~4 {Tags:["slf.herd","slf.scene_new"],PersistenceRequired:1b,CustomName:{text:"Farmer's Cow",color:"yellow"}}
execute positioned ~2 ~ ~-2 run function slf:quest/herd/raider
execute positioned ~-2 ~ ~-2 run function slf:quest/herd/raider
execute positioned ~ ~ ~-4 run function slf:quest/herd/raider
scoreboard players operation @e[tag=slf.scene_new] slf.pid = #me slf.pid
tag @e[tag=slf.scene_new] remove slf.scene_new
