# Critical Speed - Bradion: consecutive sprint steps build Haste stacks
# Uses slf.move_delta to detect active sprinting; resets on low movement
execute if score @s slf.move_delta matches 200.. run scoreboard players add @s slf.bt_kills 0
execute if score @s slf.move_delta matches 200.. run effect give @s minecraft:haste 3 0 true
execute if score @s slf.move_delta matches 500.. run effect give @s minecraft:haste 3 1 true
execute if score @s slf.move_delta matches ..50  run effect clear @s minecraft:haste
