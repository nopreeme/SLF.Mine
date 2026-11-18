effect give @s minecraft:instant_health 1 1 true
effect give @s minecraft:resistance 3 4 true
scoreboard players set @s slf.lck_save_cd 100
tellraw @s [{"text":"Clench! ","color":"gold","bold":true},{"text":"You hold on at the edge of death.","color":"yellow"}]
