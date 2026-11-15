# The Town Elder: gives A Pioneer's Awakening (design doc V9: speak with the Local Alchemist, gather 5 Wild Herbs).
execute if entity @s[tag=slf.wanderer,tag=!slf.dreamt,tag=!slf.first_survivor] run return run function slf:wanderer/refuse/elder
execute if entity @s[tag=slf.first_survivor,tag=!slf.greeted_elder] run function slf:wanderer/greet/elder
execute if score @s slf.q.awaken matches 3 run return run tellraw @s ["",{"text":"[Town Elder] ","color":"gold"},{"text":"Firstia is safer for your being here, pioneer. The forest still grows bolder by the day.","color":"white"}]
execute if score @s slf.q.awaken matches 2 run return run function slf:quest/turn_in/awaken
execute if score @s slf.q.awaken matches 1 run return run tellraw @s ["",{"text":"[Town Elder] ","color":"gold"},{"text":"Have you found the Alchemist yet? She keeps her stall at the edge of the square.","color":"white"}]
tellraw @s ["",{"text":"[Town Elder] ","color":"gold"},{"text":"Welcome to Firstia, pioneer. Monsters block the trade roads and our medicine runs short.","color":"white"}]
scoreboard players enable @s slf.quest
tellraw @s ["",{"text":" Quest: ","color":"gray"},{"text":"A Pioneer's Awakening","color":"gold","bold":true},{"text":"  Speak with the Local Alchemist, then gather 5 Wild Herbs.  ","color":"gray"},{"text":"Reward: 50 EXP, 3 Basic Health Potions  ","color":"dark_gray"},{"text":"[Accept]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.quest set 1"},"hover_event":{"action":"show_text","value":"Accept \"A Pioneer's Awakening\""}}]
