# Runs as a player: the nearest SLF NPC within 6 blocks talks to them. (Tests call this directly.)
function slf:player/init_scores
tag @e[tag=slf.npc,distance=..6,sort=nearest,limit=1] add slf.talking
execute if entity @e[tag=slf.talking,tag=slf.npc.elder] run function slf:npc/elder
execute if entity @e[tag=slf.talking,tag=slf.npc.alchemist] run function slf:npc/alchemist
execute if entity @e[tag=slf.talking,tag=slf.npc.guard_captain] run function slf:npc/guard_captain
execute if entity @e[tag=slf.talking,tag=slf.npc.farmer] run function slf:npc/farmer
execute if entity @e[tag=slf.talking,tag=slf.npc.daughter] run function slf:npc/daughter
execute if entity @e[tag=slf.talking,tag=slf.npc.garren] run function slf:npc/garren
execute if entity @e[tag=slf.talking,tag=slf.npc.marrow] run function slf:npc/marrow
execute if entity @e[tag=slf.talking,tag=slf.npc.lysa] run function slf:npc/lysa
execute if entity @e[tag=slf.talking,tag=slf.npc.halvor] run function slf:npc/halvor
execute if entity @e[tag=slf.talking,tag=slf.npc.borric] run function slf:npc/borric
execute if entity @e[tag=slf.talking,tag=slf.npc.bartender] run function slf:npc/bartender
tag @e[tag=slf.talking] remove slf.talking
