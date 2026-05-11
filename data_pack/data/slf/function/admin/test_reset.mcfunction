function slf:admin/reset_player
function slf:class/grant/swordsman
scoreboard players set @s slf.sp_points 10
scoreboard players set @s slf.level 5
tellraw @s {"text":"[TEST] Reset complete — swordsman, lvl 5, 10 stat points.","color":"aqua"}
