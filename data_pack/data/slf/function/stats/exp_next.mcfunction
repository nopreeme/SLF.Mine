# EXP needed for the next level, as the player. Used by skills/exp_tick and player/init_scores.
# L1->2: 100, L2->3: 200, L3->4: 350, L4->5: 550, L5->6: 850, L6->7: 1300, L7->8: 2000, L8->9: 3000, L9->10: 4500, then 5000 per level
execute if score @s slf.level matches 1 run scoreboard players set @s slf.exp_next 100
execute if score @s slf.level matches 2 run scoreboard players set @s slf.exp_next 200
execute if score @s slf.level matches 3 run scoreboard players set @s slf.exp_next 350
execute if score @s slf.level matches 4 run scoreboard players set @s slf.exp_next 550
execute if score @s slf.level matches 5 run scoreboard players set @s slf.exp_next 850
execute if score @s slf.level matches 6 run scoreboard players set @s slf.exp_next 1300
execute if score @s slf.level matches 7 run scoreboard players set @s slf.exp_next 2000
execute if score @s slf.level matches 8 run scoreboard players set @s slf.exp_next 3000
execute if score @s slf.level matches 9 run scoreboard players set @s slf.exp_next 4500
execute if score @s slf.level matches 10.. run scoreboard players set @s slf.exp_next 5000
