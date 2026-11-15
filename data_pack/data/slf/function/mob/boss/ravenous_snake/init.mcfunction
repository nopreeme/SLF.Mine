# Runs as the freshly summoned ravager: it becomes the Ravenous Snake's invisible, silent hitbox and brain (always hostile,
# never burns or hides). What players see is the 3D body: a head and a chain of segments (item displays) that follow it.
# Design doc V9: area boss of the Rampant Forest, recommended level 10 in a party of three.
tag @s add slf.mob
tag @s add slf.area_boss
tag @s add slf.snake
tag @s add slf.boss_ravenous_snake
tag @s add slf.boss_new
tag @s add slf.seen
scoreboard players set @s slf.mob_level 15
scoreboard players set @s slf.timer 0
data merge entity @s {Silent:1b,PersistenceRequired:1b,CustomNameVisible:1b,DeathLootTable:"slf:ravenous_snake_drops"}
effect give @s minecraft:invisibility infinite 0 true
attribute @s minecraft:scale base set 0.8
attribute @s minecraft:knockback_resistance base set 1
attribute @s minecraft:follow_range base set 32
attribute @s minecraft:movement_speed base set 0.3
data modify storage slf:mob hp set value 150
data modify storage slf:mob atk set value 6
data modify storage slf:mob lv set value 15
data modify storage slf:mob name set value "Ravenous Snake"
data modify storage slf:mob color set value "gold"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
function slf:mob/boss/ravenous_snake/body
