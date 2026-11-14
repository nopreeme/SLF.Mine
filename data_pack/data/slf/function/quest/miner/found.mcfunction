# Reward of advancement slf:quest/journal: this player picked up Tomic's journal.
advancement revoke @s only slf:quest/journal
execute unless score @s slf.q.miner matches 1 run return 0
scoreboard players set @s slf.q.miner 2
tellraw @s {"text":" A torn bag, a broken pickaxe... and Tomic's journal, half-buried in the mud. No sign of Tomic. Read the last page, then take it to Garren.","color":"yellow","italic":true}
