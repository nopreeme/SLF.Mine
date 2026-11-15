loot spawn ~ ~0.2 ~ loot slf:quest/tomic_journal
execute as @e[type=minecraft:item,distance=..1,limit=1,sort=nearest] run data merge entity @s {Age:-32768s,PickupDelay:0s,Tags:["slf.scene_new"]}
