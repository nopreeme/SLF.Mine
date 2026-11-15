# Runs as a player talking to Halvor at step 2. At night: the patrol sets out - two Secondil guards (iron golems that
# won't turn on you) and the player's own Redcap camp 50 blocks out: a banner and the first wave of three Redcaps.
execute unless predicate slf:night run return run tellraw @s ["",{"text":"[Guard Halvor] ","color":"aqua"},{"text":"Not in daylight - they only come out at night. Come back after dusk.","color":"white"}]
scoreboard players operation #me slf.pid = @s slf.pid
execute store result storage slf:quest yaw int 1 run random value 0..359
function slf:quest/reeds/place with storage slf:quest
execute positioned ~1 ~ ~1 run summon minecraft:iron_golem ~ ~ ~ {Tags:["slf.patrol","slf.scene_new"],PlayerCreated:1b,CustomName:{text:"Secondil Guard",color:"aqua"},CustomNameVisible:1b}
execute positioned ~-1 ~ ~1 run summon minecraft:iron_golem ~ ~ ~ {Tags:["slf.patrol","slf.scene_new"],PlayerCreated:1b,CustomName:{text:"Secondil Guard",color:"aqua"},CustomNameVisible:1b}
scoreboard players operation @e[tag=slf.scene_new] slf.pid = #me slf.pid
tag @e[tag=slf.scene_new] remove slf.scene_new
scoreboard players set @s slf.q.reeds 3
scoreboard players set @s slf.q.wave 1
tellraw @s ["",{"text":"[Guard Halvor] ","color":"aqua"},{"text":"These two go with you. Stay together. If they come in waves, hold the line.","color":"white"}]
execute as @e[tag=slf.reeds_camp] if score @s slf.pid = #me slf.pid store result score #x slf.tmp run data get entity @s Pos[0]
execute as @e[tag=slf.reeds_camp] if score @s slf.pid = #me slf.pid store result score #z slf.tmp run data get entity @s Pos[2]
tellraw @s ["",{"text":" Quest: the Redcap camp is near ","color":"yellow"},{"text":"x ","color":"gray"},{"score":{"name":"#x","objective":"slf.tmp"},"color":"white"},{"text":"  z ","color":"gray"},{"score":{"name":"#z","objective":"slf.tmp"},"color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
