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
