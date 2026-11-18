# Runs as a player arriving at the Altar of Awakening.
tag @s add slf.at_altar
execute if score @s slf.awakened matches 1 run return run tellraw @s {"text":"The altar recognises you. You have already awakened.","color":"light_purple"}
execute unless score @s slf.standby matches 1 unless score @s slf.level matches 99.. run return run tellraw @s {"text":"The altar is silent. Return when you have reached level 99.","color":"gray"}
execute unless score @s slf.standby matches 1 run return run tellraw @s {"text":"The altar is dormant. Defeat a monster above level 100 to reach 99 Extend first.","color":"dark_red"}
function slf:stats/altar
execute if score @s slf.awakened matches 1 at @s run particle minecraft:end_rod ~ ~1 ~ 0.6 1 0.6 0.05 80
