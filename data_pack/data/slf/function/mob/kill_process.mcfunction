# Runs as a player who killed an SLF mob last tick. slf.kill_lv holds the mob's level (from its slf.lvb* tags).
# EXP: the mob's level (plus the 2 every kill gives in exp/kill_any). Forest monsters give a quarter of that from
# player level 12 (design doc V9, Rampant Forest). Vorpal Soul if mob level >= player level + 20.
tag @s remove slf.mob_kill
scoreboard players operation #dying_mob_lv slf.mob_level = @s slf.kill_lv
scoreboard players operation #gain slf.tmp = @s slf.kill_lv
scoreboard players set #4 slf.tmp 4
execute if entity @s[tag=slf.forest_kill] if score @s slf.level matches 12.. run scoreboard players operation #gain slf.tmp /= #4 slf.tmp
tag @s remove slf.forest_kill
scoreboard players operation @s slf.exp += #gain slf.tmp
execute if score @s slf.level matches 1.. run function slf:mask/vorpal_kill_check
scoreboard players set @s slf.kill_lv 0
