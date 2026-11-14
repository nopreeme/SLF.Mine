# Garren, Secondil's armorer: the Secondil Supply Delivery ends here (Brother's Beef), then his questline (design doc V9):
# The Iron Pickaxe -> Splitblade Set -> The Missing Miner -> Red Hoods in the Reeds (with Halvor) -> Path to Thirdrema.
execute if score @s slf.q.delivery matches 1 if items entity @s container.* minecraft:paper[minecraft:item_model="slf:beef_package"] run return run function slf:quest/turn_in/delivery
execute if score @s slf.q.delivery matches 1 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"My brother sent something? Then where is it, pioneer?","color":"white"}]
execute if score @s slf.q.pickaxe matches 1 run return run function slf:quest/garren/pickaxe_check
execute if score @s slf.q.splitblade matches 1 run return run function slf:quest/garren/splitblade_check
execute if score @s slf.q.miner matches 2 run return run function slf:quest/turn_in/miner
execute if score @s slf.q.miner matches 1 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Any sign of Tomic? Search the eastern reach of the marsh. Please.","color":"white"}]
execute if score @s slf.q.reeds matches 1..3 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Show that journal to Halvor. Whatever's out there, the guard has to know.","color":"white"}]
execute if score @s slf.q.thirdrema matches 2 run return run function slf:quest/turn_in/thirdrema
execute if score @s slf.q.thirdrema matches 1 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"The Mud Digger waits at the western edge of the marsh. Bring three friends, and stay on solid ground.","color":"white"}]
execute if score @s slf.q.thirdrema matches 3 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Thirdrema, then. Send word when you get there. And... thank you, pioneer.","color":"white"}]
execute if score @s slf.q.reeds matches 4 run return run function slf:quest/garren/offer_thirdrema
execute if score @s slf.q.miner matches 3 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Take Tomic's journal to Halvor at the gate. He needs to read that last page.","color":"white"}]
execute if score @s slf.q.splitblade matches 2 run return run function slf:quest/garren/offer_miner
execute if score @s slf.q.pickaxe matches 2 run return run function slf:quest/garren/offer_splitblade
execute if score @s slf.q.delivery matches 2 run return run function slf:quest/garren/offer_pickaxe
execute if entity @s[tag=slf.garren_quest_unlocked] run return run function slf:quest/garren/offer_pickaxe
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Armor shop's open, but my stock's thin. Come back when you've got a reason to.","color":"white"}]
