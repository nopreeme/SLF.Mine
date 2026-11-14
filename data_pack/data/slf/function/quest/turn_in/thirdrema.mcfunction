scoreboard players set @s slf.q.thirdrema 3
scoreboard players add @s slf.exp 500
scoreboard players add @s slf.mahni 200
tag @s add slf.thirdrema_unlocked
give @s minecraft:paper[minecraft:item_model="slf:plated_vambraces",minecraft:item_name={text:"Garren's Plated Vambraces",color:"gold",italic:false},minecraft:lore=[{text:"Hold in your off hand: +4 armour, +10% knockback resistance.",color:"gray",italic:true}],minecraft:attribute_modifiers=[{type:"minecraft:armor",id:"slf:vambraces_armor",amount:4,operation:"add_value",slot:"offhand"},{type:"minecraft:knockback_resistance",id:"slf:vambraces_kb",amount:0.1,operation:"add_value",slot:"offhand"}],minecraft:max_stack_size=1] 1
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"The Solo Killer, dead? (laughs, then doesn't) ...Take these. My best work. The road to Thirdrema is yours.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Path to Thirdrema","color":"gold","bold":true},{"text":"  +500 EXP, +200 Mahni, Garren's Plated Vambraces, the road to Thirdrema","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
