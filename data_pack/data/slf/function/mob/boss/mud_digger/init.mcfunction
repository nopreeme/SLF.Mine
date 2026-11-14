# Runs as the freshly summoned ravager: the Mud Digger's invisible, silent hitbox. What players see is one 3D model
# (an item display) riding on it: shark head, whiskers and fins on a long-legged mole body (tools/gen_mob_models.py).
# Design doc V9: "Solo Killer", area boss of the Diremarsh, a party of 3-4 strongly recommended.
tag @s add slf.mob
tag @s add slf.area_boss
tag @s add slf.mud_digger
tag @s add slf.boss_mud_digger
tag @s add slf.boss_new
tag @s add slf.seen
scoreboard players set @s slf.mob_level 25
scoreboard players set @s slf.timer 0
data merge entity @s {Silent:1b,PersistenceRequired:1b,CustomNameVisible:1b,DeathLootTable:"slf:mud_digger_drops"}
effect give @s minecraft:invisibility infinite 0 true
attribute @s minecraft:knockback_resistance base set 1
attribute @s minecraft:follow_range base set 32
attribute @s minecraft:movement_speed base set 0.32
data modify storage slf:mob hp set value 400
data modify storage slf:mob atk set value 9
data modify storage slf:mob lv set value 25
data modify storage slf:mob name set value "Mud Digger"
data modify storage slf:mob color set value "dark_green"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
summon minecraft:item_display ~ ~ ~ {Tags:["slf.digger_part"],teleport_duration:2,item_display:"none",item:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"slf:mud_digger"}},transformation:{left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],translation:[0f,1.6f,0f],scale:[3.2f,3.2f,3.2f]}}
