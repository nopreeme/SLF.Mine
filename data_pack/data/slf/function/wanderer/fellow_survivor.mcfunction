# Fellow Survivor (design doc V9, 6.5): Garren recognises a Wanderer who made it through the bridge, and opens his questline
# without the beef delivery.
tellraw @s {"text":"(Garren sees you through the shop window - the mud, the half-healed poison - and opens the door without a word.)","color":"gray","italic":true}
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Eat. Before you fall over. (He sets a bowl of stew down and doesn't ask anything.)","color":"white"}]
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"...I've a brother in Firstia I haven't seen in years. And I had a friend - a Wanderer, like you. He didn't make it past the bridge.","color":"white"}]
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"There's work, if you want it. Ore from the marsh. I pay fair.","color":"white"}]
scoreboard players set @s slf.q.delivery 2
tag @s add slf.fellow_survivor
tag @s add slf.garren_customer
scoreboard players add @s slf.exp 150
scoreboard players add @s slf.mahni 75
give @s minecraft:mushroom_stew[minecraft:item_name={text:"Garren's Full Meal",color:"gold",italic:false},minecraft:consumable={consume_seconds:1.6f,animation:"eat",sound:"minecraft:entity.generic.eat",has_consume_particles:true,on_consume_effects:[{type:"minecraft:apply_effects",effects:[{id:"minecraft:instant_health",amplifier:2,duration:1},{id:"minecraft:saturation",amplifier:4,duration:1}]}]}] 1
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Fellow Survivor","color":"gold","bold":true},{"text":"  +150 EXP, +75 Mahni, Garren's Full Meal, Garren as your armorer","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
