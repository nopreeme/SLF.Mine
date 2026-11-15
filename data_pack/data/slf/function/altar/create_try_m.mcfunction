# Macro, once per second until the chosen chunk has generated. Gives up after a minute.
$execute unless score #altar_pending slf.timer matches 1 in minecraft:overworld run return run forceload remove $(cx) $(cz)
$execute in minecraft:overworld unless loaded $(cx) 64 $(cz) run return run function slf:altar/create_wait
# Only on dry, open ground: water and lava count as surface for this heightmap, trunks stick up through forests
$execute in minecraft:overworld positioned $(cx) 0 $(cz) positioned over motion_blocking_no_leaves if block ~ ~-1 ~ minecraft:water run return run function slf:altar/create_move
$execute in minecraft:overworld positioned $(cx) 0 $(cz) positioned over motion_blocking_no_leaves if block ~ ~-1 ~ minecraft:lava run return run function slf:altar/create_move
$execute in minecraft:overworld positioned $(cx) 0 $(cz) positioned over motion_blocking_no_leaves if block ~ ~-1 ~ #minecraft:logs run return run function slf:altar/create_move
$execute in minecraft:overworld positioned $(cx) 0 $(cz) positioned over motion_blocking_no_leaves if block ~ ~-1 ~ #minecraft:leaves run return run function slf:altar/create_move
$execute in minecraft:overworld positioned $(cx) 0 $(cz) positioned over motion_blocking_no_leaves align xyz run function slf:altar/build
$execute in minecraft:overworld run forceload remove $(cx) $(cz)
tellraw @a[scores={slf.standby=1}] ["",{"text":"[SLF] ","color":"gold"},{"text":"An Altar of Awakening has risen.","color":"light_purple","bold":true}]
execute as @a[scores={slf.standby=1}] run function slf:altar/directions
