# Runs as the player at the camp spot: a marker, the camp's banner on a post, and the first wave.
summon minecraft:marker ~ ~ ~ {Tags:["slf.reeds_camp","slf.scene_new"]}
scoreboard players operation @e[tag=slf.scene_new] slf.pid = #me slf.pid
tag @e[tag=slf.scene_new] remove slf.scene_new
function slf:quest/reeds/wave
