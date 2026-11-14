# The Guard Captain: gives Clearing the Outskirts (5 Goblins), then The Brute Threat (2 Orcs). Main quests come first:
# The Serpent's Shadow ends here, and he gives The Rampant Forest Guardian.
execute if score @s slf.q.serpent matches 1 run return run function slf:quest/turn_in/serpent
execute if score @s slf.q.guardian matches 1 if score @s slf.q.snake matches 1 run return run function slf:quest/turn_in/guardian
execute if score @s slf.q.guardian matches 1 run return run tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"The Ravenous Snake still holds the bridge. Be careful of the tail.","color":"white"}]
execute if score @s slf.q.serpent matches 2 if score @s slf.q.guardian matches 0 run function slf:quest/turn_in/serpent_reoffer
execute if score @s slf.q.outskirts matches 1 if score @s slf.q.goblins matches 5.. run return run function slf:quest/turn_in/outskirts
execute if score @s slf.q.outskirts matches 1 run return run tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Goblins down: ","color":"white"},{"score":{"name":"@s","objective":"slf.q.goblins"},"color":"yellow"},{"text":"/5. Keep at it.","color":"white"}]
execute if score @s slf.q.brute matches 1 if score @s slf.q.orcs matches 2.. run return run function slf:quest/turn_in/brute
execute if score @s slf.q.brute matches 1 run return run tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Orcs down: ","color":"white"},{"score":{"name":"@s","objective":"slf.q.orcs"},"color":"yellow"},{"text":"/2.","color":"white"}]
execute if score @s slf.q.brute matches 2 run return run tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"The goblins are scattering, but something bigger has the bridge to Secondil. Get stronger before you go near it.","color":"white"}]
execute if score @s slf.q.outskirts matches 2 run return run function slf:npc/guard_captain_brute
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Goblins have been scouting the western walls, stealing supplies and harassing farmers. I need the gates secured.","color":"white"}]
scoreboard players enable @s slf.quest
tellraw @s ["",{"text":" Quest: ","color":"gray"},{"text":"Clearing the Outskirts","color":"gold","bold":true},{"text":"  Defeat 5 Goblins.  ","color":"gray"},{"text":"Reward: 100 EXP, Starter Iron Dagger, 20 Mahni  ","color":"dark_gray"},{"text":"[Accept]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.quest set 2"},"hover_event":{"action":"show_text","value":"Accept \"Clearing the Outskirts\""}}]
