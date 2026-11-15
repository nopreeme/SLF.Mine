# The Mud Digger waits 60 blocks out (unless it is already about).
scoreboard players set @s slf.q.thirdrema 1
execute unless entity @e[tag=slf.mud_digger] store result storage slf:quest yaw int 1 run random value 0..359
execute unless entity @e[tag=slf.mud_digger] run function slf:quest/thirdrema/place with storage slf:quest
tag @e[tag=slf.boss_new] remove slf.boss_new
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"Go. Come back alive.","color":"white"}]
execute as @e[tag=slf.mud_digger,limit=1] store result score #x slf.tmp run data get entity @s Pos[0]
execute as @e[tag=slf.mud_digger,limit=1] store result score #z slf.tmp run data get entity @s Pos[2]
tellraw @s ["",{"text":" Quest: the Mud Digger is near ","color":"yellow"},{"text":"x ","color":"gray"},{"score":{"name":"#x","objective":"slf.tmp"},"color":"white"},{"text":"  z ","color":"gray"},{"score":{"name":"#z","objective":"slf.tmp"},"color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
