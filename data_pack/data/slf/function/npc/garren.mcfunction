# Garren, Secondil's armorer and the farmer's brother: the Secondil Supply Delivery ends here, with his Brother's Beef
# conclusion (design doc V9, section 4). His own questline (The Iron Pickaxe onwards) is not built yet.
execute if score @s slf.q.delivery matches 1 if items entity @s container.* minecraft:paper[minecraft:item_model="slf:beef_package"] run return run function slf:quest/turn_in/delivery
execute if score @s slf.q.delivery matches 1 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"My brother sent something? Then where is it, pioneer?","color":"white"}]
execute if score @s slf.q.delivery matches 2 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"The back room's full of armour with no metal to finish it. Ore from the Diremarsh has slowed to nothing... I'll need your help soon.","color":"white"}]
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Armor shop's open, but my stock's thin. Come back when you've got a reason to.","color":"white"}]
