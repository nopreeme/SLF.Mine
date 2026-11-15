# Runs as a zombie: turns it into an Orc (design doc V9, Firstia / Rampant Forest): "larger, more aggressive Orcs have
# begun leading the goblin scouting parties". Body: a zombie at 1.25 size wearing the 3D orc head (tools/gen_mob_models.py),
# dark hide armour and a club (a mace). Slower than a goblin, hits much harder. Two goblins come with it.
execute store result score @s slf.mob_level run random value 10..14
execute if score #spawn_lv slf.mob_level matches 1.. run scoreboard players operation @s slf.mob_level = #spawn_lv slf.mob_level
scoreboard players set #spawn_lv slf.mob_level 0
data merge entity @s {IsBaby:0b,CanBreakDoors:0b,DeathLootTable:"slf:orc_drops",CustomNameVisible:1b,equipment:{head:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"slf:orc_head"}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":4864814}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":3484458}},feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":3484458}},mainhand:{id:"minecraft:mace",count:1,components:{"minecraft:item_name":"Orc Club"}}},drop_chances:{head:0.0f,chest:0.0f,legs:0.0f,feet:0.0f,mainhand:0.0f}}
tag @s add slf.mob
tag @s add slf.orc
tag @s add slf.forest_mob
tag @s add slf.seen
attribute @s minecraft:scale base set 1.25
attribute @s minecraft:movement_speed base set 0.22
attribute @s minecraft:spawn_reinforcements base set 0
attribute @s minecraft:knockback_resistance base set 0.4
# Stats from level: health 20 + level (30-34), attack 3 + level/3 (6-7)
scoreboard players operation #hp slf.tmp = @s slf.mob_level
scoreboard players add #hp slf.tmp 20
execute store result storage slf:mob hp int 1 run scoreboard players get #hp slf.tmp
scoreboard players operation #atk slf.tmp = @s slf.mob_level
scoreboard players set #d slf.tmp 3
scoreboard players operation #atk slf.tmp /= #d slf.tmp
scoreboard players add #atk slf.tmp 3
execute store result storage slf:mob atk int 1 run scoreboard players get #atk slf.tmp
execute store result storage slf:mob lv int 1 run scoreboard players get @s slf.mob_level
data modify storage slf:mob name set value "Orc"
data modify storage slf:mob color set value "dark_green"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
# its scouting party
execute positioned ~2 ~ ~1 run function slf:mob/goblin/spawn
execute positioned ~-2 ~ ~1 run function slf:mob/goblin/spawn
