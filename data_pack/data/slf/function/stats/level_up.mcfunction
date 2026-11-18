# Called when a player's exp meets the current level threshold
# Increments level, spends the EXP requirement (surplus carries over), awards stat points (5 a level, +50 at 99, 10 a level above 99)
scoreboard players add @s slf.level 1
scoreboard players operation @s slf.exp -= @s slf.exp_next
execute if score @s slf.exp matches ..-1 run scoreboard players set @s slf.exp 0
# Stat points as in the series: 5 a level up to 99, a 50-point bonus on reaching 99, 10 a level above 99
execute if score @s slf.level matches ..99 run scoreboard players add @s slf.sp_points 5
execute if score @s slf.level matches 99 run scoreboard players add @s slf.sp_points 50
execute if score @s slf.level matches 100.. run scoreboard players add @s slf.sp_points 10

tellraw @s ["",{"text":"Level Up! ","color":"gold","bold":true},{"text":"Now level ","color":"yellow"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"yellow"}]

# Cap at 99 until awakened, 150 after
execute unless score @s slf.awakened matches 1 if score @s slf.level matches 99.. run scoreboard players set @s slf.level 99
execute if score @s slf.level matches 150.. run scoreboard players set @s slf.level 150
playsound minecraft:entity.player.levelup player @s
