# Gives this player a number of their own (slf.pid), once.
scoreboard players add #next slf.pid 1
scoreboard players operation @s slf.pid = #next slf.pid
