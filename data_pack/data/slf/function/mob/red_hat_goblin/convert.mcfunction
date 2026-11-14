# Runs as a zombie: turns it into a Redcap Goblin (design doc V9, Diremarsh): a disciplined goblin in a deep red hood
# with a forged iron axe. Higher HP, faster, night only (leaves at dawn), calls other Redcaps when hurt (mob/redcap/*).
# Called by spawn and mob/zombie_seen.
# Body: a zombie at 0.6 size (goblin height). Its head slot holds an item drawn as the 3D goblin head (resource pack model slf:item/red_hat_goblin_head, tools/gen_mob_models.py), which also keeps it from burning by day; dyed leather makes the tunic and bandaged feet.
execute store result score @s slf.mob_level run random value 14..22
execute if score #spawn_lv slf.mob_level matches 1.. run scoreboard players operation @s slf.mob_level = #spawn_lv slf.mob_level
scoreboard players set #spawn_lv slf.mob_level 0
data merge entity @s {IsBaby:0b,CanBreakDoors:0b,DeathLootTable:"slf:red_hat_goblin_drops",CustomNameVisible:1b,equipment:{head:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"slf:red_hat_goblin_head"}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":8280650}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":7228992}},feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":13617332}},mainhand:{id:"minecraft:iron_axe",count:1,components:{"minecraft:item_name":"Redcap Iron Axe"}}},drop_chances:{head:0.0f,chest:0.0f,legs:0.0f,feet:0.0f,mainhand:0.0f}}
tag @s add slf.mob
tag @s add slf.red_hat_goblin
tag @s add slf.night_mob
tag @s add slf.seen
attribute @s minecraft:scale base set 0.6
attribute @s minecraft:movement_speed base set 0.3
attribute @s minecraft:spawn_reinforcements base set 0
# Stats from level: health 10 + level, attack 2 + level/3
scoreboard players operation #hp slf.tmp = @s slf.mob_level
scoreboard players add #hp slf.tmp 10
execute store result storage slf:mob hp int 1 run scoreboard players get #hp slf.tmp
scoreboard players operation #atk slf.tmp = @s slf.mob_level
scoreboard players set #3 slf.tmp 3
scoreboard players operation #atk slf.tmp /= #3 slf.tmp
scoreboard players add #atk slf.tmp 2
execute store result storage slf:mob atk int 1 run scoreboard players get #atk slf.tmp
execute store result storage slf:mob lv int 1 run scoreboard players get @s slf.mob_level
data modify storage slf:mob name set value "Redcap Goblin"
data modify storage slf:mob color set value "red"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
