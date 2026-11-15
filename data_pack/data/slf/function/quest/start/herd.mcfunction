# Runs as a player accepting The Missing Herd, near the farmer: sets up their own raiders' camp 40 blocks away in a random
# direction - the daughter, three of the farmer's cows and three goblin raiders, all carrying this player's slf.pid.
scoreboard players set @s slf.q.herd 1
scoreboard players set @s slf.q.daughter 0
scoreboard players set @s slf.q.cows 0
scoreboard players operation #me slf.pid = @s slf.pid
execute store result storage slf:quest yaw int 1 run random value 0..359
execute at @e[tag=slf.npc.farmer,limit=1,sort=nearest] run function slf:quest/herd/place with storage slf:quest
tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"They went into the woods - that way. My girl, and three of my best cows. Please hurry!","color":"white"}]
execute as @e[tag=slf.npc.daughter] if score @s slf.pid = #me slf.pid store result score #x slf.tmp run data get entity @s Pos[0]
execute as @e[tag=slf.npc.daughter] if score @s slf.pid = #me slf.pid store result score #z slf.tmp run data get entity @s Pos[2]
tellraw @s ["",{"text":" Quest: the raiders' camp is near ","color":"yellow"},{"text":"x ","color":"gray"},{"score":{"name":"#x","objective":"slf.tmp"},"color":"white"},{"text":"  z ","color":"gray"},{"score":{"name":"#z","objective":"slf.tmp"},"color":"white"},{"text":". Defeat the raiders, rescue the daughter, lead the cows home (wheat or a lead).","color":"yellow"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
