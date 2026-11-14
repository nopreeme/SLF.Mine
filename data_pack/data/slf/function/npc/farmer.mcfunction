# The Distressed Farmer (design doc V9): The Missing Herd, The Serpent's Shadow, Secondil Supply Delivery.
execute if entity @s[tag=slf.wanderer,tag=!slf.dreamt,tag=!slf.first_survivor] run return run function slf:wanderer/refuse/farmer
execute if entity @s[tag=slf.first_survivor,tag=!slf.greeted_farmer] run function slf:wanderer/greet/farmer
execute if entity @s[tag=slf.fellow_survivor] if score @s slf.q.letter matches 0 run return run function slf:wanderer/letter_offer
execute if score @s slf.q.herd matches 1 run return run function slf:quest/herd/farmer
execute if score @s slf.q.herd matches 2 if score @s slf.q.serpent matches 0 run return run function slf:npc/farmer_serpent
execute if score @s slf.q.serpent matches 1 run return run tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"Please - talk to the Guard Captain at the gates before you go anywhere near that bridge.","color":"white"}]
execute if score @s slf.q.guardian matches 2 if score @s slf.q.delivery matches 0 run return run function slf:npc/farmer_delivery
execute if score @s slf.q.delivery matches 1 run return run tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"My brother Garren runs the armor shop in Secondil. Mind the package - it's his favourite cut.","color":"white"}]
execute if score @s slf.q.herd matches 2 run return run tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"The cattle are settling and my girl is safe. I owe you more than I can pay.","color":"white"}]
tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"Pioneer, please! Goblins raided my pastures, drove off my cattle - and they took my daughter!","color":"white"}]
scoreboard players enable @s slf.quest
tellraw @s ["",{"text":" Main quest: ","color":"gray"},{"text":"The Missing Herd","color":"gold","bold":true},{"text":"  Find the goblin raiders in the woods, rescue the farmer's daughter, herd 3 cows back to the farm.  ","color":"gray"},{"text":"Reward: 120 EXP, Fresh Milk Bundle, 30 Mahni  ","color":"dark_gray"},{"text":"[Accept]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.quest set 4"},"hover_event":{"action":"show_text","value":"Accept \"The Missing Herd\""}}]
