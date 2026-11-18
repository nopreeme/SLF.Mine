# Reward of advancement slf:mob/mud_digger_kill: this player killed the Mud Digger. On top of the level-based EXP:
# +800 EXP (design doc V9).
advancement revoke @s only slf:mob/mud_digger_kill
scoreboard players add @s slf.exp 800
tellraw @a[distance=..64] ["",{"selector":"@s","color":"gold"},{"text":" has slain the Mud Digger! The road to Thirdrema is open.","color":"yellow"}]
# Path to Thirdrema
execute if score @s slf.q.thirdrema matches 1 run scoreboard players set @s slf.q.thirdrema 2
execute if score @s slf.q.thirdrema matches 2 run tellraw @s {"text":" Quest objective done: report to Garren.","color":"yellow"}
