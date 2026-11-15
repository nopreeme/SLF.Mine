# Runs as a frog: turns it into a Mud Frog (design doc V9, Diremarsh). Body: vanilla's green (cold) frog at 1.6 size,
# "below knee level". Non-aggressive: it only hits back when attacked (mob/mud_frog/hit). Its mud coating makes swords
# nearly useless; blunt, piercing and fire weapons do full damage. Drops Mud Frog Skin for the Splitblade set.
execute store result score @s slf.mob_level run random value 14..18
execute if score #spawn_lv slf.mob_level matches 1.. run scoreboard players operation @s slf.mob_level = #spawn_lv slf.mob_level
scoreboard players set #spawn_lv slf.mob_level 0
data merge entity @s {variant:"minecraft:cold",DeathLootTable:"slf:mud_frog_drops",CustomNameVisible:1b}
tag @s add slf.mob
tag @s add slf.mud_frog
tag @s add slf.seen
attribute @s minecraft:scale base set 1.6
# Health 6 + level (20-24); a frog's own attack (10) only matters to slimes, so it is left alone
scoreboard players operation #hp slf.tmp = @s slf.mob_level
scoreboard players add #hp slf.tmp 6
execute store result storage slf:mob hp int 1 run scoreboard players get #hp slf.tmp
scoreboard players operation #atk slf.tmp = @s slf.mob_level
scoreboard players set #d slf.tmp 1000
scoreboard players operation #atk slf.tmp /= #d slf.tmp
scoreboard players add #atk slf.tmp 10
execute store result storage slf:mob atk int 1 run scoreboard players get #atk slf.tmp
execute store result storage slf:mob lv int 1 run scoreboard players get @s slf.mob_level
data modify storage slf:mob name set value "Mud Frog"
data modify storage slf:mob color set value "dark_aqua"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
attribute @s minecraft:attack_damage base set 10
