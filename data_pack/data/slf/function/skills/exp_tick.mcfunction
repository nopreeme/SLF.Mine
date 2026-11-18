# Runs every 20t — EXP processing, level-up, the 99 Extend gate
# EXP comes from kills (advancements slf:exp/kill_* -> functions slf:exp/kill_*).

# EXP needed for the next level (also shown on the HUD and status sheet)
# L1->2: 100, L2->3: 200, L3->4: 350, L4->5: 550, L5->6: 850, L6->7: 1300, L7->8: 2000, L8->9: 3000, L9->10: 4500, then 5000 per level
execute as @a run function slf:stats/exp_next

# Level cap 99. EXP earned at the cap is lost until the player reaches 99 Extend (slf.standby=1) by defeating a level
# 100+ monster (stats/extend_check); from then on it is banked into exp_extend for the Altar of Awakening.
# (Tests for 'not 1' rather than '0' so players whose scores were never initialised still work.)
execute as @a if score @s slf.level matches 99.. unless score @s slf.awakened matches 1 unless score @s slf.standby matches 1 run scoreboard players set @s slf.exp 0
# Newly at 99 Extend: tell the player about the Altar of Awakening (raising the world's altar if there is none yet)
execute as @a[scores={slf.standby=1},tag=!slf.altar_told] run function slf:altar/first_standby
execute as @a if score @s slf.standby matches 1 if score @s slf.exp matches 1.. run scoreboard players operation @s slf.exp_extend += @s slf.exp
execute as @a if score @s slf.standby matches 1 if score @s slf.exp matches 1.. run scoreboard players set @s slf.exp 0

# Level up when EXP reaches the requirement: levels 1-98 normally, 99-149 once awakened. One level per cycle;
# surplus EXP carries over (see stats/level_up).
execute as @a unless score @s slf.standby matches 1 if score @s slf.level matches 1..98 if score @s slf.exp >= @s slf.exp_next run function slf:stats/level_up
execute as @a if score @s slf.awakened matches 1 if score @s slf.level matches 99..149 if score @s slf.exp >= @s slf.exp_next run function slf:stats/level_up
