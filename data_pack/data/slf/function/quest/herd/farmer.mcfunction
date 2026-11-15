# The farmer, while The Missing Herd is on.
execute if score @s slf.q.daughter matches 1 if score @s slf.q.cows matches 3.. run return run function slf:quest/turn_in/herd
tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"My daughter: ","color":"white"}]
execute if score @s slf.q.daughter matches 1 run tellraw @s {"text":"   safe at home","color":"green"}
execute if score @s slf.q.daughter matches 0 run tellraw @s {"text":"   still with the raiders","color":"red"}
tellraw @s ["",{"text":"   Cows back at the farm: ","color":"white"},{"score":{"name":"@s","objective":"slf.q.cows"},"color":"yellow"},{"text":"/3","color":"white"}]
