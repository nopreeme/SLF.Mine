# Runs at the altar's centre block (block-aligned). 5x5 footprint, 4 tall.
fill ~-2 ~ ~-2 ~2 ~3 ~2 minecraft:air
fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:polished_blackstone_bricks
# Foundation: on a slope or over a hollow, fill the gap under the base so no corner hangs in the air
fill ~-2 ~-6 ~-2 ~2 ~-2 ~2 minecraft:polished_blackstone_bricks replace #minecraft:replaceable
fill ~-2 ~-6 ~-2 ~2 ~-2 ~2 minecraft:polished_blackstone_bricks replace #minecraft:leaves
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
summon minecraft:marker ~0.5 ~ ~0.5 {Tags:["slf.altar","slf.altar_placed"]}
summon minecraft:text_display ~0.5 ~3.4 ~0.5 {Tags:["slf.altar_label","slf.altar_placed"],billboard:"center",text:{text:"Altar of Awakening",color:"light_purple",bold:true}}
# Remember that an altar exists and where, for the menu
scoreboard players set #altar_placed slf.timer 1
execute store result score #altar_x slf.timer run data get entity @e[type=minecraft:marker,tag=slf.altar_placed,limit=1,sort=nearest] Pos[0]
execute store result score #altar_y slf.timer run data get entity @e[type=minecraft:marker,tag=slf.altar_placed,limit=1,sort=nearest] Pos[1]
execute store result score #altar_z slf.timer run data get entity @e[type=minecraft:marker,tag=slf.altar_placed,limit=1,sort=nearest] Pos[2]
execute store result storage slf:altar ax int 1 run scoreboard players get #altar_x slf.timer
execute store result storage slf:altar ay int 1 run scoreboard players get #altar_y slf.timer
execute store result storage slf:altar az int 1 run scoreboard players get #altar_z slf.timer
# A placed or raised altar replaces any altar that was still being raised
scoreboard players set #altar_pending slf.timer 0
