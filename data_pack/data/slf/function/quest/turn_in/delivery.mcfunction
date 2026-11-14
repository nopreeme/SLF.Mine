clear @s minecraft:paper[minecraft:item_model="slf:beef_package"] 1
scoreboard players set @s slf.q.delivery 2
scoreboard players add @s slf.exp 250
scoreboard players add @s slf.mahni 50
give @s minecraft:chainmail_chestplate[minecraft:item_name={text:"Basic Armor Piece",color:"white",italic:false}] 1
tag @s add slf.garren_customer
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Beef from home... from my brother. How is he? And the little one?","color":"white"}]
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"...Thank you. I won't forget this. You'll always get a fair price on repairs here.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Secondil Supply Delivery","color":"gold","bold":true},{"text":"  +150 EXP, Basic Armor Piece, Garren's shop unlocked","color":"yellow"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Brother's Beef (Conclusion)","color":"gold","bold":true},{"text":"  +100 EXP, +50 Mahni, Garren as a recurring vendor","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
