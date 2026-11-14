# Places the Local Alchemist here, facing the nearest player (admins: /function slf:npc/place/alchemist). NPCs stand still, can't be hurt,
# never despawn and have no trades: right-clicking one talks to it (advancement slf:npc/talk).
summon minecraft:villager ~ ~ ~ {Tags:["slf.npc","slf.npc.alchemist","slf.npc_new"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomNameVisible:1b,CustomName:{text:"Local Alchemist",color:"light_purple"},VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:plains"},Offers:{Recipes:[]}}
execute as @e[tag=slf.npc_new] at @s run tp @s ~ ~ ~ facing entity @p[distance=..16] feet
tag @e[tag=slf.npc_new] remove slf.npc_new
