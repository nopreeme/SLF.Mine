# Runs as a zombie: turns it into a Red Hat Goblin, a goblin chief in a blood-red cap: tougher, faster, better armed. Called by spawn and mob/zombie_seen.
# Body: a zombie at 0.6 size (goblin height) in a dyed leather cap, which also keeps it from burning by day.
execute store result score @s slf.mob_level run random value 12..20
execute if score #spawn_lv slf.mob_level matches 1.. run scoreboard players operation @s slf.mob_level = #spawn_lv slf.mob_level
scoreboard players set #spawn_lv slf.mob_level 0
data merge entity @s {IsBaby:0b,CanBreakDoors:0b,DeathLootTable:"slf:red_hat_goblin_drops",CustomNameVisible:1b,equipment:{head:{id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":11546150}},mainhand:{id:"minecraft:iron_sword",count:1}},drop_chances:{head:0.0f,mainhand:0.0f}}
tag @s add slf.mob
tag @s add slf.red_hat_goblin
tag @s add slf.seen
attribute @s minecraft:scale base set 0.6
attribute @s minecraft:movement_speed base set 0.28
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
data modify storage slf:mob name set value "Red Hat Goblin"
data modify storage slf:mob color set value "red"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
