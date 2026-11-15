scoreboard players set @s slf.q.outskirts 2
scoreboard players add @s slf.exp 100
scoreboard players add @s slf.mahni 20
give @s minecraft:iron_sword[minecraft:item_model="slf:iron_dagger",minecraft:item_name={text:"Starter Iron Dagger",color:"white",italic:false},minecraft:attribute_modifiers=[{type:"minecraft:attack_damage",id:"minecraft:base_attack_damage",amount:3,operation:"add_value",slot:"mainhand"},{type:"minecraft:attack_speed",id:"minecraft:base_attack_speed",amount:-1.6,operation:"add_value",slot:"mainhand"}],minecraft:custom_data={slf:{weapon:"iron_dagger"}}] 1
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Five of them? The farmers will sleep tonight. Here - a proper blade, and your pay.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Clearing the Outskirts","color":"gold","bold":true},{"text":"  +100 EXP, +20 Mahni, Starter Iron Dagger","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
