# Runs as the Mud Digger, at the spot where it bursts out of the ground (called from emerge after it has moved).
particle minecraft:block{block_state:"minecraft:mud"} ~ ~1 ~ 1.5 1 1.5 0.4 120
playsound minecraft:entity.ravager.roar hostile @a[distance=..32] ~ ~ ~ 2 0.7
# Everyone within 3 blocks is rammed (6 damage) and thrown; in Phase 2 the target is launched sky-high
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s 6 minecraft:mob_attack by @e[tag=slf.mud_digger,limit=1]
execute unless entity @s[tag=slf.phase2] as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run effect give @s minecraft:levitation 1 4 true
execute if entity @s[tag=slf.phase2] as @a[tag=slf.digger_target] run effect give @s minecraft:levitation 1 24 true
tag @a remove slf.digger_target
