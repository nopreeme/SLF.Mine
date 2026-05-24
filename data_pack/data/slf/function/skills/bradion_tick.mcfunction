# Critical Speed - Bradion: sprint momentum -> Haste
# move_delta tracks sprint_one_cm change this cycle (high = actively sprinting fast)
execute if score @s slf.move_delta matches 500.. run effect give @s minecraft:haste 3 1 true
execute if score @s slf.move_delta matches 200..499 run effect give @s minecraft:haste 3 0 true
execute if score @s slf.move_delta matches ..50 run effect clear @s minecraft:haste
