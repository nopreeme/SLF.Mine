# Every tick while the Mud Digger's model exists (skills/tick): the model follows the hitbox. While dug in, the model sits
# almost fully underground (only the dorsal fin cuts through the mud).
execute unless entity @e[tag=slf.mud_digger,limit=1] run return run kill @e[tag=slf.digger_part]
execute as @e[tag=slf.digger_part,limit=1] at @e[tag=slf.mud_digger,tag=!slf.dug,limit=1] run tp @s ~ ~ ~ ~ 0
execute as @e[tag=slf.digger_part,limit=1] at @e[tag=slf.mud_digger,tag=slf.dug,limit=1] run tp @s ~ ~-2.6 ~ ~ 0
execute as @e[tag=slf.mud_digger,limit=1] at @s run function slf:mob/boss/bar {id:"mud_digger"}
