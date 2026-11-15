# Runs as the watching player, at the tree line: two Redcaps stand watching the city. They leave at dawn.
tag @s add slf.watch_sighted
scoreboard players operation #me slf.pid = @s slf.pid
execute positioned ~ ~ ~1 summon minecraft:zombie run function slf:quest/watch/sighting_redcap
execute positioned ~ ~ ~-1 summon minecraft:zombie run function slf:quest/watch/sighting_redcap
tellraw @s {"text":" Something moves at the tree line to the west... red hoods. Iron glints. Don't engage.","color":"red","italic":true}
