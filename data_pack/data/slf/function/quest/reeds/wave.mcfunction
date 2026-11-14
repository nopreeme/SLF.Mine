# At the camp (marker position), as the player: a wave of Redcaps that belong to this player and stay until killed
# or dawn. Wave 1 is three, wave 2 is four (q.wave says which).
execute positioned ~2 ~ ~ summon minecraft:zombie run function slf:quest/reeds/redcap
execute positioned ~-2 ~ ~ summon minecraft:zombie run function slf:quest/reeds/redcap
execute positioned ~ ~ ~2 summon minecraft:zombie run function slf:quest/reeds/redcap
execute if score @s slf.q.wave matches 2 positioned ~ ~ ~-2 summon minecraft:zombie run function slf:quest/reeds/redcap
