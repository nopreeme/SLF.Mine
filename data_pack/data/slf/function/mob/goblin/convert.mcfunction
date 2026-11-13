# Runs as a zombie: turns it into a Goblin, a small, quick forest raider in a mossy cap. Called by spawn and mob/zombie_seen.
# Body: a zombie at 0.6 size (goblin height) in a dyed leather cap, which also keeps it from burning by day.
execute store result score @s slf.mob_level run random value 3..10
execute if score #spawn_lv slf.mob_level matches 1.. run scoreboard players operation @s slf.mob_level = #spawn_lv slf.mob_level
scoreboard players set #spawn_lv slf.mob_level 0
data merge entity @s {IsBaby:0b,CanBreakDoors:0b,DeathLootTable:"slf:goblin_drops",CustomNameVisible:1b,equipment:{head:{id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":3825419}},mainhand:{id:"minecraft:wooden_sword",count:1}},drop_chances:{head:0.0f,mainhand:0.0f}}
tag @s add slf.mob
tag @s add slf.goblin
tag @s add slf.seen
attribute @s minecraft:scale base set 0.6
attribute @s minecraft:movement_speed base set 0.26
attribute @s minecraft:spawn_reinforcements base set 0
# Stats from level: health 8 + level, attack 1 + level/3
scoreboard players operation #hp slf.tmp = @s slf.mob_level
scoreboard players add #hp slf.tmp 8
execute store result storage slf:mob hp int 1 run scoreboard players get #hp slf.tmp
scoreboard players operation #atk slf.tmp = @s slf.mob_level
scoreboard players set #3 slf.tmp 3
scoreboard players operation #atk slf.tmp /= #3 slf.tmp
scoreboard players add #atk slf.tmp 1
execute store result storage slf:mob atk int 1 run scoreboard players get #atk slf.tmp
execute store result storage slf:mob lv int 1 run scoreboard players get @s slf.mob_level
data modify storage slf:mob name set value "Goblin"
data modify storage slf:mob color set value "green"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
