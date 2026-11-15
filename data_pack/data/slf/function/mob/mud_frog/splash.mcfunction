# Runs as the player a Mud Frog is hitting back.
damage @s 2 minecraft:mob_attack by @e[tag=slf.mud_frog,distance=..4,limit=1,sort=nearest]
effect give @s minecraft:slowness 3 0
particle minecraft:block{block_state:"minecraft:mud"} ~ ~1 ~ 0.3 0.4 0.3 0.1 20
