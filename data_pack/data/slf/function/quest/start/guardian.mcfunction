# Runs as a player accepting the Ravenous Snake quest: the snake waits 50 blocks out (unless one is already about).
scoreboard players set @s slf.q.guardian 1
scoreboard players set @s slf.q.snake 0
execute unless entity @e[tag=slf.snake] store result storage slf:quest yaw int 1 run random value 0..359
execute unless entity @e[tag=slf.snake] run function slf:quest/guardian/place with storage slf:quest
tag @e[tag=slf.boss_new] remove slf.boss_new
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"Prove your worth as a Pioneer and reopen the path. Bring friends. And bring antidotes.","color":"white"}]
execute as @e[tag=slf.snake,limit=1] store result score #x slf.tmp run data get entity @s Pos[0]
execute as @e[tag=slf.snake,limit=1] store result score #z slf.tmp run data get entity @s Pos[2]
tellraw @s ["",{"text":" Quest: the Ravenous Snake is near ","color":"yellow"},{"text":"x ","color":"gray"},{"score":{"name":"#x","objective":"slf.tmp"},"color":"white"},{"text":"  z ","color":"gray"},{"score":{"name":"#z","objective":"slf.tmp"},"color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
