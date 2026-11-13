# Macro, runs as a new boss. Arguments: id, name, color, lv, scale, loot.
# Stats from level: health 4 x level, attack 4 + level/10, plus size, knockback resistance and a long follow range.
$tag @s add slf.boss_$(id)
tag @s add slf.mob
tag @s add slf.boss
tag @s add slf.boss_new
tag @s add slf.seen
$scoreboard players set @s slf.mob_level $(lv)
$data merge entity @s {DeathLootTable:"$(loot)",PersistenceRequired:1b,CustomNameVisible:1b}
$attribute @s minecraft:scale base set $(scale)
attribute @s minecraft:knockback_resistance base set 0.8
attribute @s minecraft:follow_range base set 48
scoreboard players set #4 slf.tmp 4
scoreboard players set #10 slf.tmp 10
scoreboard players operation #hp slf.tmp = @s slf.mob_level
scoreboard players operation #hp slf.tmp *= #4 slf.tmp
execute store result storage slf:mob hp int 1 run scoreboard players get #hp slf.tmp
scoreboard players operation #atk slf.tmp = @s slf.mob_level
scoreboard players operation #atk slf.tmp /= #10 slf.tmp
scoreboard players add #atk slf.tmp 4
execute store result storage slf:mob atk int 1 run scoreboard players get #atk slf.tmp
execute store result storage slf:mob lv int 1 run scoreboard players get @s slf.mob_level
$data modify storage slf:mob name set value "$(name)"
$data modify storage slf:mob color set value "$(color)"
function slf:mob/apply_stats with storage slf:mob
function slf:mob/level_tags
