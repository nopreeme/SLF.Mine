# Strength scales with missing HP — runs as each tagged player
execute store result score @s slf.hp run data get entity @s Health 1
execute if score @s slf.hp matches ..6 run effect give @s minecraft:strength 3 2 true
execute if score @s slf.hp matches 7..13 run effect give @s minecraft:strength 3 1 true
execute if score @s slf.hp matches 14.. run effect give @s minecraft:strength 3 0 true
