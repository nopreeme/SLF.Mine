# Runs every 20t. A player who walks up to the altar is handled once per visit (tag slf.at_altar).
execute as @a[tag=!slf.at_altar] at @s if entity @e[type=minecraft:marker,tag=slf.altar,distance=..4] run function slf:altar/enter
execute as @a[tag=slf.at_altar] at @s unless entity @e[type=minecraft:marker,tag=slf.altar,distance=..6] run tag @s remove slf.at_altar
