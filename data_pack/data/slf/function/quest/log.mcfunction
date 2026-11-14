# The quest log (/trigger slf.menu set 10): every quest the player has started.
function slf:player/init_scores
tellraw @s ["",{"text":"━━━ ","color":"dark_gray"},{"text":"Quests","color":"gold","bold":true},{"text":" ━━━","color":"dark_gray"}]
execute if score @s slf.q.awaken matches 0 if score @s slf.q.outskirts matches 0 run tellraw @s {"text":" No quests yet. Talk to the people of Firstia: the Town Elder and the Guard Captain.","color":"gray"}
execute if score @s slf.q.awaken matches 1 run tellraw @s ["",{"text":" A Pioneer's Awakening: ","color":"gold"},{"text":"speak with the Local Alchemist","color":"yellow"}]
execute if score @s slf.q.awaken matches 2 run tellraw @s ["",{"text":" A Pioneer's Awakening: ","color":"gold"},{"text":"bring 5 Wild Herbs to the Town Elder","color":"yellow"}]
execute if score @s slf.q.awaken matches 3 run tellraw @s ["",{"text":" A Pioneer's Awakening: ","color":"gold"},{"text":"complete","color":"green"}]
execute if score @s slf.q.outskirts matches 1 run tellraw @s ["",{"text":" Clearing the Outskirts: ","color":"gold"},{"text":"Goblins ","color":"yellow"},{"score":{"name":"@s","objective":"slf.q.goblins"},"color":"white"},{"text":"/5, then the Guard Captain","color":"yellow"}]
execute if score @s slf.q.outskirts matches 2 run tellraw @s ["",{"text":" Clearing the Outskirts: ","color":"gold"},{"text":"complete","color":"green"}]
execute if score @s slf.q.brute matches 1 run tellraw @s ["",{"text":" The Brute Threat: ","color":"gold"},{"text":"Orcs ","color":"yellow"},{"score":{"name":"@s","objective":"slf.q.orcs"},"color":"white"},{"text":"/2, then the Guard Captain","color":"yellow"}]
execute if score @s slf.q.brute matches 2 run tellraw @s ["",{"text":" The Brute Threat: ","color":"gold"},{"text":"complete","color":"green"}]
tellraw @s ["",{"text":"[Back]","color":"dark_gray","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.menu set 1"},"hover_event":{"action":"show_text","value":"Main menu"}}]
