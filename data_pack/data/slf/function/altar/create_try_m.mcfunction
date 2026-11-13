# Macro, once per second until the chosen chunk has generated. Gives up after a minute.
$execute unless score #altar_pending slf.timer matches 1 in minecraft:overworld run return run forceload remove $(cx) $(cz)
$execute in minecraft:overworld unless loaded $(cx) 64 $(cz) run return run function slf:altar/create_wait
$execute in minecraft:overworld positioned $(cx) 0 $(cz) positioned over world_surface align xyz run function slf:altar/build
$execute in minecraft:overworld run forceload remove $(cx) $(cz)
tellraw @a[scores={slf.standby=1}] ["",{"text":"[SLF] ","color":"gold"},{"text":"An Altar of Awakening has risen.","color":"light_purple","bold":true}]
execute as @a[scores={slf.standby=1}] run function slf:altar/directions
