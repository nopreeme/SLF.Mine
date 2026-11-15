scoreboard players set @s slf.q.brute 2
scoreboard players add @s slf.exp 150
scoreboard players add @s slf.mahni 40
give @s minecraft:leather_chestplate[minecraft:item_name={text:"Beginner Leather Chestplate",color:"white",italic:false}] 1
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Two orcs. That'll break their nerve. Wear this - you'll be going deeper soon.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"The Brute Threat","color":"gold","bold":true},{"text":"  +150 EXP, +40 Mahni, Beginner Leather Chestplate","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
