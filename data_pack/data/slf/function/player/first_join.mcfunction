# Runs once for every player the pack has not seen before (tag slf.joined).
tag @s add slf.joined
scoreboard players set @s slf.leave 0
tellraw @s ["",{"text":"[SLF] ","color":"gold"},{"text":"Welcome to Shangri-La Frontier. Open the menu any time with ","color":"yellow"},{"text":"/trigger slf.menu","color":"aqua","click_event":{"action":"run_command","command":"trigger slf.menu"},"hover_event":{"action":"show_text","value":"Click to open the menu"}}]
execute unless entity @s[tag=slf.class_chosen] run function slf:class/select
