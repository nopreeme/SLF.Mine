# Runs as the Mud Digger underground: it picks its target (the only player near if there is just one - "Solo Killer" -
# otherwise a random one) and bursts out of the ground beside it; in Phase 2, right underneath it.
scoreboard players set @s slf.timer 0
execute store result score #n slf.tmp if entity @a[gamemode=!creative,gamemode=!spectator,distance=..32]
execute if score #n slf.tmp matches 1 run tag @p[gamemode=!creative,gamemode=!spectator,distance=..32] add slf.digger_target
execute if score #n slf.tmp matches 2.. run tag @r[gamemode=!creative,gamemode=!spectator,distance=..32] add slf.digger_target
execute unless entity @s[tag=slf.phase2] at @a[tag=slf.digger_target,limit=1] run tp @s ^ ^ ^2 facing entity @a[tag=slf.digger_target,limit=1] feet
execute if entity @s[tag=slf.phase2] at @a[tag=slf.digger_target,limit=1] run tp @s ~ ~ ~
tag @s remove slf.dug
data merge entity @s {Invulnerable:0b,NoAI:0b,CustomNameVisible:1b}
execute at @s run function slf:mob/boss/mud_digger/burst
