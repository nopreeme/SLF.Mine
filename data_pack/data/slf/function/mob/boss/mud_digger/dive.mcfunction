# Runs as the Mud Digger: it dives underground and vanishes (it can't be hurt while under).
tag @s add slf.dug
data merge entity @s {Invulnerable:1b,NoAI:1b,CustomNameVisible:0b}
particle minecraft:block{block_state:"minecraft:mud"} ~ ~0.5 ~ 1.5 0.5 1.5 0.2 80
playsound minecraft:block.mud.break hostile @a[distance=..32] ~ ~ ~ 2 0.5
execute if entity @s[tag=slf.phase2] run function slf:mob/boss/mud_digger/quake
