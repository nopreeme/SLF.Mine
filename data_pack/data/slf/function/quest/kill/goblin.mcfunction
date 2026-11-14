# Reward of advancement slf:quest/goblin_kill: counts toward the active quest.
advancement revoke @s only slf:quest/goblin_kill
execute unless score @s slf.q.outskirts matches 1 run return 0
scoreboard players add @s slf.q.goblins 1
title @s actionbar ["",{"text":"Goblins ","color":"gray"},{"score":{"name":"@s","objective":"slf.q.goblins"},"color":"yellow"},{"text":"/5","color":"gray"}]
execute if score @s slf.q.goblins matches 5 run tellraw @s {"text":" Quest objective done: report to the Guard Captain.","color":"yellow"}
