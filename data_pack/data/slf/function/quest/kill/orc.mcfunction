# Reward of advancement slf:quest/orc_kill: counts toward the active quest.
advancement revoke @s only slf:quest/orc_kill
execute unless score @s slf.q.brute matches 1 run return 0
scoreboard players add @s slf.q.orcs 1
title @s actionbar ["",{"text":"Orcs ","color":"gray"},{"score":{"name":"@s","objective":"slf.q.orcs"},"color":"yellow"},{"text":"/2","color":"gray"}]
execute if score @s slf.q.orcs matches 2 run tellraw @s {"text":" Quest objective done: report to the Guard Captain.","color":"yellow"}
