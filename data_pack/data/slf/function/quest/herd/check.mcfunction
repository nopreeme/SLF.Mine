# Every second, as a player on The Missing Herd: how many of their cows are within 12 blocks of the farmer.
scoreboard players operation #me slf.pid = @s slf.pid
scoreboard players set #near slf.tmp 0
execute as @e[tag=slf.herd] if score @s slf.pid = #me slf.pid at @s if entity @e[tag=slf.npc.farmer,distance=..12] run scoreboard players add #near slf.tmp 1
execute unless score @s slf.q.cows = #near slf.tmp run title @s actionbar ["",{"text":"Cows home ","color":"gray"},{"score":{"name":"#near","objective":"slf.tmp"},"color":"yellow"},{"text":"/3","color":"gray"}]
scoreboard players operation @s slf.q.cows = #near slf.tmp
