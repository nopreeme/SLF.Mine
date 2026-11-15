scoreboard players set @s slf.q.guardian 2
scoreboard players add @s slf.exp 300
scoreboard players add @s slf.mahni 100
give @s minecraft:paper[minecraft:item_model="slf:devourers_scale",minecraft:item_name={text:"Devourer's Scale",color:"gold",italic:false},minecraft:lore=[{text:"A square piece of hardened scale from the Ravenous Snake.",color:"gray",italic:true}]] 1
give @s minecraft:paper[minecraft:item_model="slf:python_white_hair",minecraft:item_name={text:"Python White Hair",color:"gold",italic:false},minecraft:lore=[{text:"A lock of white hair from the Ravenous Snake's mane.",color:"gray",italic:true}]] 1
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"The snake is dead? Then the bridge is open, Pioneer - and you've earned the right to cross it.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"The Rampant Forest Guardian","color":"gold","bold":true},{"text":"  +300 EXP, +100 Mahni, Devourer's Scale, Python White Hair","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
