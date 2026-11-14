# Called by every skills/focus/* function right after it sets slf.threshold.
# TEC lowers the threshold by 1% per point, up to 50%.
execute unless score @s slf.stat.tec matches 1.. run return 0
scoreboard players operation #t slf.tmp = @s slf.stat.tec
execute if score #t slf.tmp matches 51.. run scoreboard players set #t slf.tmp 50
scoreboard players set #100 slf.tmp 100
scoreboard players operation #k slf.tmp = #100 slf.tmp
scoreboard players operation #k slf.tmp -= #t slf.tmp
scoreboard players operation @s slf.threshold *= #k slf.tmp
scoreboard players operation @s slf.threshold /= #100 slf.tmp
execute if score @s slf.threshold matches ..0 run scoreboard players set @s slf.threshold 1
