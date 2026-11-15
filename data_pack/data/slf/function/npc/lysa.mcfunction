# Lysa the Florist: Antidote Run, and a shop (antidotes, health potions).
execute if score @s slf.q.antidote matches 0 run function slf:npc/lysa_offer
execute if score @s slf.q.antidote matches 1 run tellraw @s ["",{"text":"[Lysa] ","color":"light_purple"},{"text":"The bundles go to Marrow at the inn. Quickly, please - someone's always waiting on them.","color":"white"}]
execute if score @s slf.q.antidote matches 2 run tellraw @s ["",{"text":"[Lysa] ","color":"light_purple"},{"text":"Antidotes, salves, potions. The Ravenous Snake's venom claims more pioneers than the snake ever did.","color":"white"}]
scoreboard players enable @s slf.shop
tellraw @s ["",{"text":" Lysa's wares: ","color":"gray"},{"text":"[Antidote - 15 M]","color":"gold","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.shop set 1"},"hover_event":{"action":"show_text","value":"Buy Antidote for 15 Mahni"}},{"text":" "},{"text":"[Basic Health Potion - 20 M]","color":"gold","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.shop set 2"},"hover_event":{"action":"show_text","value":"Buy Basic Health Potion for 20 Mahni"}},{"text":" "}]
