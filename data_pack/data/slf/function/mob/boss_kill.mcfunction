# Reward of advancement slf:mob/boss_kill: this player killed an SLF boss. On top of the level-based EXP
# (mob/kill_process): +2400 EXP, a boss kill, the Altar of Awakening's boss gate and a Knight Trial.
advancement revoke @s only slf:mob/boss_kill
scoreboard players add @s slf.exp 2400
scoreboard players add @s slf.boss_kills 1
execute unless score @s slf.boss_gate matches 1 run tellraw @s ["",{"text":"A worthy foe has fallen. ","color":"gold","bold":true},{"text":"The Altar of Awakening will answer you once you reach level 99.","color":"yellow"}]
scoreboard players set @s slf.boss_gate 1
execute if entity @s[tag=slf.was_knight] run function slf:class/knight_trial_complete
