# Runs as a player accepting The Missing Miner: their own search site 60 blocks out - a torn bag, a broken pickaxe and
# Tomic's journal, half-buried. Picking up the journal (advancement slf:quest/journal) is the find.
scoreboard players set @s slf.q.miner 1
scoreboard players operation #me slf.pid = @s slf.pid
execute store result storage slf:quest yaw int 1 run random value 0..359
function slf:quest/miner/place with storage slf:quest
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Find him. Or... find what's left. I'd rather know.","color":"white"}]
execute as @e[tag=slf.miner_site] if score @s slf.pid = #me slf.pid store result score #x slf.tmp run data get entity @s Pos[0]
execute as @e[tag=slf.miner_site] if score @s slf.pid = #me slf.pid store result score #z slf.tmp run data get entity @s Pos[2]
tellraw @s ["",{"text":" Quest: Tomic's last dig site is near ","color":"yellow"},{"text":"x ","color":"gray"},{"score":{"name":"#x","objective":"slf.tmp"},"color":"white"},{"text":"  z ","color":"gray"},{"score":{"name":"#z","objective":"slf.tmp"},"color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
