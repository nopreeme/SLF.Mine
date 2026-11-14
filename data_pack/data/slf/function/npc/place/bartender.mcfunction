# Places Bartender (Secondil) here, facing the nearest player (admins: /function slf:npc/place/bartender).
summon minecraft:villager ~ ~ ~ {Tags:["slf.npc","slf.npc.bartender","slf.npc_new"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomNameVisible:1b,CustomName:{text:"Bartender",color:"yellow"},VillagerData:{profession:"minecraft:butcher",level:5,type:"minecraft:plains"},Offers:{Recipes:[]}}
execute as @e[tag=slf.npc_new] at @s run tp @s ~ ~ ~ facing entity @p[distance=..16] feet
tag @e[tag=slf.npc_new] remove slf.npc_new
