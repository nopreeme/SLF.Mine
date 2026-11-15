execute store result score #ore slf.tmp run clear @s minecraft:raw_iron 0
execute if score #ore slf.tmp matches ..4 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Five raw iron, pioneer. You've got ","color":"white"},{"score":{"name":"#ore","objective":"slf.tmp"},"color":"yellow"},{"text":".","color":"white"}]
clear @s minecraft:raw_iron 5
scoreboard players set @s slf.q.pickaxe 2
scoreboard players add @s slf.exp 200
scoreboard players add @s slf.mahni 75
tag @s add slf.diremarsh_unlocked
give @s minecraft:iron_chestplate[minecraft:item_name={text:"Basic Iron Chestplate",color:"white",italic:false}] 1
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Five! Half the marsh's miners can't manage that in a week. Here - you've earned a proper chestplate.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"The Iron Pickaxe","color":"gold","bold":true},{"text":"  +200 EXP, +75 Mahni, Basic Iron Chestplate, the Diremarsh unlocked","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
