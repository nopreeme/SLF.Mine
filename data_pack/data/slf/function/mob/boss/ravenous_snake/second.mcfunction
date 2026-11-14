# Runs as the snake every second (mob/tick). Every 5 seconds, with a survival player within 12 blocks, the lock on its
# tail opens like a flower and releases a purple ooze of poison (design doc V9).
scoreboard players add @s slf.timer 1
execute if score @s slf.timer matches 5.. if entity @a[gamemode=!creative,gamemode=!spectator,distance=..12] run function slf:mob/boss/ravenous_snake/poison
