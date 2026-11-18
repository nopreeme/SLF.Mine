# Runs as a player meeting a Colossus for the first time (mob/boss/bar tags them slf.ume_<id> right after).
scoreboard players add @s slf.sp_points 20
tellraw @s ["",{"text":"Unique Monster Encounter! ","color":"gold","bold":true},{"text":"+20 stat points.","color":"yellow"}]
