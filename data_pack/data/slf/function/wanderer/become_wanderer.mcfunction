# Runs as a player confirming the Wanderer origin: traits, the Dream Penalty (tag slf.wandering), Firstia's inn as their
# respawn point (where the dream ends), and a drop into the Rampant Forest.
tag @s add slf.origin_chosen
tag @s add slf.wanderer
tag @s add slf.wandering
function slf:wanderer/traits
execute if data storage slf:world firstia run function slf:wanderer/firstia_spawnpoint with storage slf:world firstia
scoreboard players set @s slf.wtry 0
execute if data storage slf:world forest run function slf:wanderer/drop_at with storage slf:world forest
execute unless data storage slf:world forest at @s run function slf:wanderer/drop
tellraw @s {"text":"You wake among the trees with nothing but your gear. Somewhere beyond the forest is Secondil. Don't die before you sleep there.","color":"dark_green","italic":true}
playsound minecraft:ambient.cave ambient @s ~ ~ ~ 1 0.8
