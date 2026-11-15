# The Farmer's Daughter: rescued once her captors (this player's raiders) are gone; she runs home to the farmer.
scoreboard players operation #me slf.pid = @s slf.pid
execute unless score @e[tag=slf.talking,limit=1] slf.pid = #me slf.pid run return run tellraw @s ["",{"text":"[Farmer's Daughter] ","color":"light_purple"},{"text":"Who are you? Papa will be looking for me...","color":"white"}]
scoreboard players set #raiders slf.tmp 0
execute as @e[tag=slf.raider] if score @s slf.pid = #me slf.pid run scoreboard players add #raiders slf.tmp 1
execute if score #raiders slf.tmp matches 1.. run return run tellraw @s ["",{"text":"[Farmer's Daughter] ","color":"light_purple"},{"text":"The goblins are still here! Please, get rid of them first!","color":"white"}]
scoreboard players set @s slf.q.daughter 1
tellraw @s ["",{"text":"[Farmer's Daughter] ","color":"light_purple"},{"text":"You saved me! I'll run straight home to Papa - please bring the cows!","color":"white"}]
execute as @e[tag=slf.talking] at @s run particle minecraft:poof ~ ~0.5 ~ 0.3 0.3 0.3 0.02 10
execute as @e[tag=slf.talking] run tp @s @e[tag=slf.npc.farmer,limit=1,sort=nearest]
execute as @e[tag=slf.talking] at @s run tp @s ^1 ^ ^1
tellraw @s {"text":" Quest updated: the daughter is safe. Now lead the 3 cows back to the farmer.","color":"yellow"}
