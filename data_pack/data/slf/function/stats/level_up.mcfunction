# Called when a player's exp meets the current level threshold
# Increments level, resets exp, awards 3 stat points (5 at level milestones)
scoreboard players add @s slf.level 1
scoreboard players set @s slf.exp 0
scoreboard players add @s slf.sp_points 3

# Milestone bonus: every 10 levels award 2 extra stat points
execute if score @s slf.level matches 10 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 20 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 30 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 40 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 50 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 60 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 70 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 80 run scoreboard players add @s slf.sp_points 2
execute if score @s slf.level matches 90 run scoreboard players add @s slf.sp_points 2

tellraw @s ["",{"text":"Level Up! ","color":"gold","bold":true},{"text":"Now level ","color":"yellow"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":". +3 stat points.","color":"yellow"}]

# Cap at 99 (standby flag set in exp_tick next cycle)
execute if score @s slf.level matches 99.. run scoreboard players set @s slf.level 99
