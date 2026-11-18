# Reward of advancement slf:mob/boss_kill: this player killed an SLF boss. On top of the level-based EXP
# (mob/kill_process): +2400 EXP, 200 stat points (UMB, Unique Monster Break), a boss kill and a Knight Trial.
advancement revoke @s only slf:mob/boss_kill
scoreboard players add @s slf.exp 2400
scoreboard players add @s slf.boss_kills 1
scoreboard players add @s slf.sp_points 200
tellraw @s ["",{"text":"Unique Monster Break! ","color":"gold","bold":true},{"text":"+200 stat points.","color":"yellow"}]
scoreboard players set @s slf.boss_gate 1
execute if entity @s[tag=slf.was_knight] run function slf:class/knight_trial_complete
