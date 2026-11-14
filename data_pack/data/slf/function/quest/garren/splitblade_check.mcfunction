execute store result score #skins slf.tmp run clear @s minecraft:book[minecraft:custom_model_data={strings:["slf.mud_frog_skin"]}] 0
execute if score #skins slf.tmp matches ..3 run return run tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Four Mud Frog Skins. You've got ","color":"white"},{"score":{"name":"#skins","objective":"slf.tmp"},"color":"yellow"},{"text":".","color":"white"}]
clear @s minecraft:book[minecraft:custom_model_data={strings:["slf.mud_frog_skin"]}] 4
scoreboard players set @s slf.q.splitblade 2
scoreboard players add @s slf.exp 250
scoreboard players add @s slf.mahni 50
give @s minecraft:leather_chestplate[minecraft:custom_model_data={strings:["slf.chest_splitblade"]},minecraft:item_name={translate:"item.slf.chest_splitblade",italic:false}] 1
give @s minecraft:leather_leggings[minecraft:custom_model_data={strings:["slf.pants_splitblade"]},minecraft:item_name={translate:"item.slf.pants_splitblade",italic:false}] 1
give @s minecraft:leather_helmet[minecraft:custom_model_data={strings:["slf.mask_splitblade"]},minecraft:item_name={translate:"item.slf.mask_splitblade",italic:false}] 1
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Splitblade leather - body, pants and mask. A blade slides right off it. Wear it in the marsh.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Splitblade Set","color":"gold","bold":true},{"text":"  +250 EXP, +50 Mahni, Splitblade Leather Set","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
