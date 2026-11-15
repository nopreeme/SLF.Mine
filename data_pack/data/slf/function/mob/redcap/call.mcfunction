# Runs as a Redcap Goblin that was just hurt: it calls two more Redcaps, unless five are already within 24 blocks.
# Design doc V9: "it will call additional Redcaps to its aid".
tag @s add slf.called
playsound minecraft:item.goat_horn.sound.2 hostile @a[distance=..48] ~ ~ ~ 0.8 1.4
particle minecraft:angry_villager ~ ~1.2 ~ 0.3 0.3 0.3 0 4
execute store result score #near slf.tmp if entity @e[tag=slf.red_hat_goblin,distance=..24]
execute if score #near slf.tmp matches ..4 positioned ~3 ~ ~ run function slf:mob/red_hat_goblin/spawn
execute if score #near slf.tmp matches ..3 positioned ~-3 ~ ~2 run function slf:mob/red_hat_goblin/spawn
