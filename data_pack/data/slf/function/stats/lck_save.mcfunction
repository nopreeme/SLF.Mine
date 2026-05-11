effect give @s minecraft:instant_health 1 1 true
effect give @s minecraft:resistance 3 4 true
scoreboard players set @s slf.lck_save_cd 100
tellraw @s [{"text":"Lucky! ","color":"gold","bold":true},{"text":"Fatal blow survived.","color":"yellow"}]
