# --- Class selection ---
# Trigger-based (alignment_choice + admin direct grants)
execute as @a if score @s slf.choose_class = 1  run function slf:class/grant/swordsman
execute as @a if score @s slf.choose_class = 2  run function slf:class/grant/warrior
execute as @a if score @s slf.choose_class = 3  run function slf:class/grant/bandit
execute as @a if score @s slf.choose_class = 4  run function slf:class/grant/priest
execute as @a if score @s slf.choose_class = 5  run function slf:class/grant/monk
execute as @a if score @s slf.choose_class = 6  run function slf:class/grant/mage
execute as @a if score @s slf.choose_class = 20 run function slf:class/grant/fighter
execute as @a if score @s slf.choose_class = 30 run function slf:class/grant/mercenary
execute as @a if score @s slf.choose_class = 41 run function slf:class/grant/holy_knight
execute as @a if score @s slf.choose_class = 42 run function slf:class/grant/dark_knight
execute as @a if score @s slf.choose_class >= 1 run scoreboard players reset @s slf.choose_class
scoreboard players enable @a[tag=!slf.class_chosen] slf.choose_class

# --- Skill focus selection ---
execute as @a if score @s slf.focus_choose = 1  run function slf:skills/focus/power_slash
execute as @a if score @s slf.focus_choose = 2  run function slf:skills/focus/megaton_swing
execute as @a if score @s slf.focus_choose = 3  run function slf:skills/focus/knuckle_rush
execute as @a if score @s slf.focus_choose = 4  run function slf:skills/focus/manbufu
execute as @a if score @s slf.focus_choose = 5  run function slf:skills/focus/sword_of_rough_waves
execute as @a if score @s slf.focus_choose = 6  run function slf:skills/focus/spin_slash
execute as @a if score @s slf.focus_choose = 7  run function slf:skills/focus/slide_step
execute as @a if score @s slf.focus_choose = 8  run function slf:skills/focus/holy_shield
execute as @a if score @s slf.focus_choose = 9  run function slf:skills/focus/iron_skin
execute as @a if score @s slf.focus_choose = 10 run function slf:skills/focus/paring_protect
execute as @a if score @s slf.focus_choose = 11 run function slf:skills/focus/flash_counter
execute as @a if score @s slf.focus_choose = 12 run function slf:skills/focus/total_body_takeshi
execute as @a if score @s slf.focus_choose = 13 run function slf:skills/focus/blaze_shot
execute as @a if score @s slf.focus_choose = 14 run function slf:skills/focus/ignition
execute as @a if score @s slf.focus_choose = 15 run function slf:skills/focus/duelism
execute as @a if score @s slf.focus_choose = 16 run function slf:skills/focus/one_inch_impact
execute as @a if score @s slf.focus_choose = 20 run function slf:skills/focus/lash_slash
execute as @a if score @s slf.focus_choose = 21 run function slf:skills/focus/gigaton_swing
execute as @a if score @s slf.focus_choose = 22 run function slf:skills/focus/strong_puncher
execute as @a if score @s slf.focus_choose = 23 run function slf:skills/focus/slash_ignition
execute as @a if score @s slf.focus_choose = 24 run function slf:skills/focus/formula_drift
execute as @a if score @s slf.focus_choose = 25 run function slf:skills/focus/big_tantrum
execute as @a if score @s slf.focus_choose = 26 run function slf:skills/focus/rechette_step
execute as @a if score @s slf.focus_choose = 30 run function slf:skills/focus/inexhaustible_beasts
execute as @a if score @s slf.focus_choose = 31 run function slf:skills/focus/terraton_corapsa
execute as @a if score @s slf.focus_choose = 32 run function slf:skills/focus/skatefoot
execute as @a if score @s slf.focus_choose = 33 run function slf:skills/focus/skywalker
execute as @a if score @s slf.focus_choose >= 1 run scoreboard players reset @s slf.focus_choose
scoreboard players enable @a[tag=slf.class_chosen] slf.focus_choose

# --- Stat spend triggers ---
# Fail message if trying to spend with 0 points
execute as @a if score @s slf.stat_str >= 1 if score @s slf.sp_points <= 0 run tellraw @s {"text":"You don't have any stat points to spend!","color":"red"}
execute as @a if score @s slf.stat_dex >= 1 if score @s slf.sp_points <= 0 run tellraw @s {"text":"You don't have any stat points to spend!","color":"red"}
execute as @a if score @s slf.stat_vit >= 1 if score @s slf.sp_points <= 0 run tellraw @s {"text":"You don't have any stat points to spend!","color":"red"}
execute as @a if score @s slf.stat_agi >= 1 if score @s slf.sp_points <= 0 run tellraw @s {"text":"You don't have any stat points to spend!","color":"red"}
execute as @a if score @s slf.stat_tec >= 1 if score @s slf.sp_points <= 0 run tellraw @s {"text":"You don't have any stat points to spend!","color":"red"}
execute as @a if score @s slf.stat_lck >= 1 if score @s slf.sp_points <= 0 run tellraw @s {"text":"You don't have any stat points to spend!","color":"red"}
execute as @a if score @s slf.stat_stm >= 1 if score @s slf.sp_points <= 0 run tellraw @s {"text":"You don't have any stat points to spend!","color":"red"}

# Success execution
execute as @a if score @s slf.stat_str >= 1 if score @s slf.sp_points >= 1 run function slf:stats/spend_str
execute as @a if score @s slf.stat_dex >= 1 if score @s slf.sp_points >= 1 run function slf:stats/spend_dex
execute as @a if score @s slf.stat_vit >= 1 if score @s slf.sp_points >= 1 run function slf:stats/spend_vit
execute as @a if score @s slf.stat_agi >= 1 if score @s slf.sp_points >= 1 run function slf:stats/spend_agi
execute as @a if score @s slf.stat_tec >= 1 if score @s slf.sp_points >= 1 run function slf:stats/spend_tec
execute as @a if score @s slf.stat_lck >= 1 if score @s slf.sp_points >= 1 run function slf:stats/spend_lck
execute as @a if score @s slf.stat_stm >= 1 if score @s slf.sp_points >= 1 run function slf:stats/spend_stm
execute as @a if score @s slf.stat_str >= 1 run scoreboard players reset @s slf.stat_str
execute as @a if score @s slf.stat_dex >= 1 run scoreboard players reset @s slf.stat_dex
execute as @a if score @s slf.stat_vit >= 1 run scoreboard players reset @s slf.stat_vit
execute as @a if score @s slf.stat_agi >= 1 run scoreboard players reset @s slf.stat_agi
execute as @a if score @s slf.stat_tec >= 1 run scoreboard players reset @s slf.stat_tec
execute as @a if score @s slf.stat_lck >= 1 run scoreboard players reset @s slf.stat_lck
execute as @a if score @s slf.stat_stm >= 1 run scoreboard players reset @s slf.stat_stm
scoreboard players enable @a[tag=slf.class_chosen] slf.stat_str
scoreboard players enable @a[tag=slf.class_chosen] slf.stat_dex
scoreboard players enable @a[tag=slf.class_chosen] slf.stat_vit
scoreboard players enable @a[tag=slf.class_chosen] slf.stat_agi
scoreboard players enable @a[tag=slf.class_chosen] slf.stat_tec
scoreboard players enable @a[tag=slf.class_chosen] slf.stat_lck
scoreboard players enable @a[tag=slf.class_chosen] slf.stat_stm

# --- Knight alignment: only after 3 trials ---
execute as @a[tag=slf.was_knight,tag=!slf.was_holy_knight,tag=!slf.was_dark_knight] if score @s slf.knight_trials >= 3 run function slf:class/alignment_choice

# --- 20t cycle ---
scoreboard players add #timer slf.timer 1
execute if score #timer slf.timer >= 20 run function slf:skills/sp_tick
execute if score #timer slf.timer >= 20 run function slf:skills/exp_tick
execute if score #timer slf.timer >= 20 run function slf:skills/passives
execute if score #timer slf.timer >= 20 run function slf:mask/karma_tick
execute if score #timer slf.timer >= 20 run function slf:stats/apply
execute if score #timer slf.timer >= 20 as @a if score @s slf.stat.lck >= 1 run function slf:stats/lck_check
execute if score #timer slf.timer >= 20 run function slf:class/select_expire
execute if score #timer slf.timer >= 20 run scoreboard players set #timer slf.timer 0
