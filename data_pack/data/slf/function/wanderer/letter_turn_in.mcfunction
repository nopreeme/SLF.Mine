clear @s minecraft:paper[minecraft:item_model="slf:sealed_letter"] 1
scoreboard players set @s slf.q.letter 2
scoreboard players add @s slf.exp 250
scoreboard players add @s slf.mahni 100
tag @s add slf.trusted_of_garren
give @s minecraft:bread[minecraft:item_name={text:"Fresh-Baked Bread",color:"gold",italic:false},minecraft:rarity="rare",minecraft:lore=[{text:"From home. A full heal.",color:"gray",italic:true}],minecraft:consumable={consume_seconds:1.6f,animation:"eat",sound:"minecraft:entity.generic.eat",has_consume_particles:true,on_consume_effects:[{type:"minecraft:apply_effects",effects:[{id:"minecraft:instant_health",amplifier:4,duration:1}]}]}] 1
tellraw @s {"text":"(Garren breaks the seal and reads it in front of you. He doesn't share a word of it.)","color":"gray","italic":true}
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"...Thank you. (His voice is softer than you've heard it.) Thank you. (He turns back to the forge so you can't see his face.)","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"A Brother's Letter","color":"gold","bold":true},{"text":"  +250 EXP, +100 Mahni, Fresh-Baked Bread, Trusted of Garren","color":"yellow"}]
