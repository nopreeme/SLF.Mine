# Admin: /function slf:altar/remove — retires the altar (run it near the altar so its chunk is loaded).
# The blocks stay; awakening goes back to the menu button.
kill @e[type=minecraft:marker,tag=slf.altar]
kill @e[type=minecraft:text_display,tag=slf.altar_label]
scoreboard players set #altar_placed slf.timer 0
tag @a remove slf.at_altar
tellraw @s ["",{"text":"[SLF] ","color":"gold"},{"text":"Altar of Awakening retired. Players can awaken from the menu again.","color":"yellow"}]
