# Runs as a player who clicked [Accept] on a quest offer (/trigger slf.quest set <n>). Each quest can only be taken once,
# and The Brute Threat only after Clearing the Outskirts.
scoreboard players operation #q slf.tmp = @s slf.quest
scoreboard players set @s slf.quest 0
# a trigger switches itself off after one use: keep it on, so a click on an offer that isn't available yet doesn't break the next one
scoreboard players enable @s slf.quest
function slf:player/init_scores
execute if score #q slf.tmp matches 1 if score @s slf.q.awaken matches 0 run return run function slf:quest/start/awaken
execute if score #q slf.tmp matches 2 if score @s slf.q.outskirts matches 0 run return run function slf:quest/start/outskirts
execute if score #q slf.tmp matches 3 if score @s slf.q.outskirts matches 2 if score @s slf.q.brute matches 0 run return run function slf:quest/start/brute
execute if score #q slf.tmp matches 4 if score @s slf.q.herd matches 0 run return run function slf:quest/start/herd
execute if score #q slf.tmp matches 5 if score @s slf.q.herd matches 2 if score @s slf.q.serpent matches 0 run return run function slf:quest/start/serpent
execute if score #q slf.tmp matches 6 if score @s slf.q.serpent matches 2 if score @s slf.q.guardian matches 0 run return run function slf:quest/start/guardian
execute if score #q slf.tmp matches 7 if score @s slf.q.guardian matches 2 if score @s slf.q.delivery matches 0 run return run function slf:quest/start/delivery
execute if score #q slf.tmp matches 8 if score @s slf.q.bed matches 0 run return run function slf:quest/start/bed
execute if score #q slf.tmp matches 9 if score @s slf.q.antidote matches 0 run return run function slf:quest/start/antidote
execute if score #q slf.tmp matches 10 if score @s slf.q.watch matches 0 run return run function slf:quest/start/watch
execute if score #q slf.tmp matches 11 if score @s slf.q.bar matches 0 run return run function slf:quest/start/bar
execute if score #q slf.tmp matches 12 if score @s slf.q.bar matches 4 run return run function slf:quest/turn_in/bar
execute if score #q slf.tmp matches 13 if score @s slf.q.bar matches 4 run return run tellraw @s ["",{"text":"[Bartender] ","color":"yellow"},{"text":"Nonsense? Funny - a miner told me the same thing last week. Think again.","color":"white"}]
execute if score #q slf.tmp matches 14 if score @s slf.q.pickaxe matches 0 run return run function slf:quest/start/pickaxe
execute if score #q slf.tmp matches 15 if score @s slf.q.pickaxe matches 2 if score @s slf.q.splitblade matches 0 run return run function slf:quest/start/splitblade
execute if score #q slf.tmp matches 16 if score @s slf.q.splitblade matches 2 if score @s slf.q.miner matches 0 run return run function slf:quest/start/miner
execute if score #q slf.tmp matches 17 if score @s slf.q.miner matches 3 if score @s slf.q.reeds matches 0 run return run function slf:quest/start/reeds
execute if score #q slf.tmp matches 18 if score @s slf.q.reeds matches 4 if score @s slf.q.thirdrema matches 0 run return run function slf:quest/start/thirdrema
