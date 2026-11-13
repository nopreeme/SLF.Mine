# Runs as a rabbit: turns it into a Vorpal Bunny. Called by spawn, mob/rabbit_seen (wild forest rabbits) and replace_zombie.
# Faster than a plain rabbit (movement 0.38 vs 0.3); design doc V9: stronger and faster than goblins, rare.
# The Vorpal Bunny is vanilla's Killer Bunny (RabbitType 99): white, red-eyed, hostile to players, armour 8.
# Level 8-30, so a fresh player who wins against one earns a Vorpal Soul (mob level >= player level + 20).
execute store result score @s slf.mob_level run random value 8..30
execute if score #spawn_lv slf.mob_level matches 1.. run scoreboard players operation @s slf.mob_level = #spawn_lv slf.mob_level
scoreboard players set #spawn_lv slf.mob_level 0
data merge entity @s {RabbitType:99,DeathLootTable:"slf:vorpal_bunny_drops",PersistenceRequired:1b,CustomNameVisible:1b}
tag @s add slf.mob
tag @s add slf.vorpal_bunny
tag @s add slf.forest_mob
tag @s add slf.seen
# Stats from level: health 6 + level (14-36), attack 2 + level/6 (3-7)
scoreboard players operation #hp slf.tmp = @s slf.mob_level
scoreboard players add #hp slf.tmp 6
execute store result storage slf:mob hp int 1 run scoreboard players get #hp slf.tmp
scoreboard players operation #atk slf.tmp = @s slf.mob_level
scoreboard players set #6 slf.tmp 6
scoreboard players operation #atk slf.tmp /= #6 slf.tmp
scoreboard players add #atk slf.tmp 2
execute store result storage slf:mob atk int 1 run scoreboard players get #atk slf.tmp
execute store result storage slf:mob lv int 1 run scoreboard players get @s slf.mob_level
data modify storage slf:mob name set value "Vorpal Bunny"
data modify storage slf:mob color set value "red"
attribute @s minecraft:movement_speed base set 0.38
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
