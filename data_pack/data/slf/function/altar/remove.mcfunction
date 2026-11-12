# Admin: /function slf:altar/remove — retires the altar placed with altar/place (run it near that altar so its
# chunk is loaded). The blocks stay. Naturally generated altars are not affected.
kill @e[type=minecraft:marker,tag=slf.altar_placed]
kill @e[type=minecraft:text_display,tag=slf.altar_placed]
scoreboard players set #altar_placed slf.timer 0
tag @a remove slf.at_altar
tellraw @s ["",{"text":"[SLF] ","color":"gold"},{"text":"Placed Altar of Awakening retired. The menu now points players to the nearest generated altar.","color":"yellow"}]
