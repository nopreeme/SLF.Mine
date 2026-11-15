# #v slf.tmp = bonus max health for @s (0..40). Replaces the slf:hp_bonus modifier.
scoreboard players operation @s slf.hp_applied = #v slf.tmp
attribute @s minecraft:max_health modifier remove slf:hp_bonus
execute store result storage slf:tmp hp int 1 run scoreboard players get #v slf.tmp
execute if score #v slf.tmp matches 1.. run function slf:stats/apply_hp_macro with storage slf:tmp
