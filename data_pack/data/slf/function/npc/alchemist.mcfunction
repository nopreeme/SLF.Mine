# The Local Alchemist: step one of A Pioneer's Awakening.
execute if score @s slf.q.awaken matches 1 run return run function slf:quest/step/alchemist
execute if score @s slf.q.awaken matches 2 run return run tellraw @s ["",{"text":"[Local Alchemist] ","color":"light_purple"},{"text":"Five Wild Herbs - they grow among the grass and ferns outside town. Take them to the Elder.","color":"white"}]
tellraw @s ["",{"text":"[Local Alchemist] ","color":"light_purple"},{"text":"Potions, salves, antidotes... if the Ravenous Snake ever gets you, come see me. Or better: don't let it.","color":"white"}]
