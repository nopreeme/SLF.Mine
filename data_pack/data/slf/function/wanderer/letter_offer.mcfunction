# The Long Way Back (design doc V9, 6.6): the farmer has held a letter for months. He doesn't ask - he sets it on the table.
tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"Garren... is he well? (He takes a sealed letter from a drawer, sets it on the table, and says nothing more.)","color":"white"}]
scoreboard players enable @s slf.quest
tellraw @s ["",{"text":" ","color":"gray"},{"text":"[Pick up the letter]","color":"yellow","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.quest set 19"},"hover_event":{"action":"show_text","value":"A Brother's Letter: carry it back across the forest to Garren"}}]
