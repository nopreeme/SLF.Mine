# The Bartender: the end of Bar Talk, and the bar's shop.
execute if score @s slf.q.bar matches 4 run function slf:npc/bartender_ask
execute unless score @s slf.q.bar matches 4 run tellraw @s ["",{"text":"[Bartender] ","color":"yellow"},{"text":"What'll it be?","color":"white"}]
scoreboard players enable @s slf.shop
tellraw @s ["",{"text":" Bartender's wares: ","color":"gray"},{"text":"[Strong Ale - 10 M]","color":"gold","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.shop set 3"},"hover_event":{"action":"show_text","value":"Buy Strong Ale for 10 Mahni"}},{"text":" "},{"text":"[Secondil Stew - 5 M]","color":"gold","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.shop set 4"},"hover_event":{"action":"show_text","value":"Buy Secondil Stew for 5 Mahni"}},{"text":" "}]
