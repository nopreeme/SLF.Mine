# Runs as a player: the nearest SLF NPC within 6 blocks talks to them. (Tests call this directly.)
function slf:player/init_scores
tag @e[tag=slf.npc,distance=..6,sort=nearest,limit=1] add slf.talking
execute if entity @e[tag=slf.talking,tag=slf.npc.elder] run function slf:npc/elder
execute if entity @e[tag=slf.talking,tag=slf.npc.alchemist] run function slf:npc/alchemist
execute if entity @e[tag=slf.talking,tag=slf.npc.guard_captain] run function slf:npc/guard_captain
execute if entity @e[tag=slf.talking,tag=slf.npc.farmer] run function slf:npc/farmer
execute if entity @e[tag=slf.talking,tag=slf.npc.daughter] run function slf:npc/daughter
execute if entity @e[tag=slf.talking,tag=slf.npc.garren] run function slf:npc/garren
tag @e[tag=slf.talking] remove slf.talking
