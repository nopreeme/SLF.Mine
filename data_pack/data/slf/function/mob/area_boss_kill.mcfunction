# Reward of advancement slf:mob/area_boss_kill: this player killed the Ravenous Snake (the Mud Digger has its own). On top of the
# level-based EXP (mob/kill_process): +300 EXP, the design doc's reward for "The Rampant Forest Guardian". Area bosses
# guard the way between zones; they do not count toward the Altar of Awakening.
advancement revoke @s only slf:mob/area_boss_kill
scoreboard players add @s slf.exp 300
tellraw @a[distance=..64] ["",{"selector":"@s","color":"gold"},{"text":" has slain the Ravenous Snake! The way through the forest is open.","color":"yellow"}]
# The Rampant Forest Guardian quest
execute if score @s slf.q.guardian matches 1 run scoreboard players set @s slf.q.snake 1
execute if score @s slf.q.guardian matches 1 run tellraw @s {"text":" Quest objective done: report to the Guard Captain.","color":"yellow"}
