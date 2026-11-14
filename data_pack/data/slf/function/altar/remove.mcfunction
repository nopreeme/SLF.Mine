# Admin: /function slf:altar/remove — retires the world's altar (run it near the altar so its chunk is loaded).
# The blocks stay. The next player to need an altar gets a new one raised.
kill @e[type=minecraft:marker,tag=slf.altar_placed]
kill @e[type=minecraft:text_display,tag=slf.altar_placed]
scoreboard players set #altar_placed slf.timer 0
tag @a remove slf.at_altar
tellraw @s ["",{"text":"[SLF] ","color":"gold"},{"text":"Altar of Awakening retired. A new one will rise when a player in Standby needs it.","color":"yellow"}]
