# Runs at the altar's centre block (block-aligned). 5x5 footprint, 4 tall.
fill ~-2 ~ ~-2 ~2 ~3 ~2 minecraft:air
fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:polished_blackstone_bricks
fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:polished_blackstone_brick_slab
setblock ~ ~ ~ minecraft:gilded_blackstone
setblock ~ ~1 ~ minecraft:crying_obsidian
setblock ~ ~2 ~ minecraft:end_rod[facing=up]
setblock ~2 ~ ~2 minecraft:polished_blackstone_wall
setblock ~2 ~1 ~2 minecraft:soul_lantern
setblock ~-2 ~ ~2 minecraft:polished_blackstone_wall
setblock ~-2 ~1 ~2 minecraft:soul_lantern
setblock ~2 ~ ~-2 minecraft:polished_blackstone_wall
setblock ~2 ~1 ~-2 minecraft:soul_lantern
setblock ~-2 ~ ~-2 minecraft:polished_blackstone_wall
setblock ~-2 ~1 ~-2 minecraft:soul_lantern
summon minecraft:marker ~0.5 ~ ~0.5 {Tags:["slf.altar"]}
summon minecraft:text_display ~0.5 ~3.4 ~0.5 {Tags:["slf.altar_label"],billboard:"center",text:{text:"Altar of Awakening",color:"light_purple",bold:true}}
# Remember that an altar exists and where, for the menu
scoreboard players set #altar_placed slf.timer 1
execute store result score #altar_x slf.timer run data get entity @e[type=minecraft:marker,tag=slf.altar,limit=1,sort=nearest] Pos[0]
execute store result score #altar_y slf.timer run data get entity @e[type=minecraft:marker,tag=slf.altar,limit=1,sort=nearest] Pos[1]
execute store result score #altar_z slf.timer run data get entity @e[type=minecraft:marker,tag=slf.altar,limit=1,sort=nearest] Pos[2]
