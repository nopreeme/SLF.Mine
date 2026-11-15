# Places Garren here, facing the nearest player (admins: /function slf:npc/place/garren).
summon minecraft:villager ~ ~ ~ {Tags:["slf.npc","slf.npc.garren","slf.npc_new"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomNameVisible:1b,CustomName:{text:"Garren",color:"gold"},VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]}}
execute as @e[tag=slf.npc_new] at @s run tp @s ~ ~ ~ facing entity @p[distance=..16] feet
tag @e[tag=slf.npc_new] remove slf.npc_new
