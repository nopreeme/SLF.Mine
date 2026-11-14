# Every second, as a player on The Night Watch: at night, within 24 blocks of Halvor, the watch goes on. At 10 seconds
# two Redcaps appear at the tree line 30 blocks west (this player's own sighting); after 45 seconds they've seen enough.
execute unless predicate slf:night run return 0
execute unless entity @e[tag=slf.npc.halvor,distance=..24] run return run title @s actionbar {"text":"Stand the watch near Guard Halvor","color":"aqua"}
scoreboard players add @s slf.q.watch_t 1
title @s actionbar ["",{"text":"On watch ","color":"aqua"},{"score":{"name":"@s","objective":"slf.q.watch_t"},"color":"white"},{"text":"/45 s","color":"gray"}]
execute if score @s slf.q.watch_t matches 10.. unless entity @s[tag=slf.watch_sighted] at @e[tag=slf.npc.halvor,limit=1,sort=nearest] positioned ~-30 ~ ~ positioned over motion_blocking_no_leaves run function slf:quest/watch/sighting
execute if score @s slf.q.watch_t matches 45.. run function slf:quest/watch/seen
