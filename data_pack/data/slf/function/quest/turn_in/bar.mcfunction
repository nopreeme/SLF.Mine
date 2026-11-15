scoreboard players set @s slf.q.bar 5
scoreboard players add @s slf.exp 60
scoreboard players add @s slf.mahni 20
give @s minecraft:potion[minecraft:potion_contents={custom_color:13145344,custom_effects:[{id:"minecraft:strength",duration:1200,amplifier:0},{id:"minecraft:nausea",duration:160,amplifier:0}]},minecraft:item_name={text:"Strong Ale",color:"gold",italic:false}] 1
tellraw @s ["",{"text":"[Bartender] ","color":"yellow"},{"text":"That's what I thought. A humming in the deep pools... something's out there. Here, on the house.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Bar Talk","color":"gold","bold":true},{"text":"  +60 EXP, +20 Mahni, Strong Ale","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
