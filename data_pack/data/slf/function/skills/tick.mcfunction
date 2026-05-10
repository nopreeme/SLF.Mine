# --- Class selection ---
execute as @a[scores={slf.choose_class=1}]  run function slf:class/grant/swordsman
execute as @a[scores={slf.choose_class=2}]  run function slf:class/grant/warrior
execute as @a[scores={slf.choose_class=3}]  run function slf:class/grant/thief
execute as @a[scores={slf.choose_class=4}]  run function slf:class/grant/priest
execute as @a[scores={slf.choose_class=5}]  run function slf:class/grant/monk
execute as @a[scores={slf.choose_class=6}]  run function slf:class/grant/mage
execute as @a[scores={slf.choose_class=20}] run function slf:class/grant/fighter
execute as @a[scores={slf.choose_class=30}] run function slf:class/grant/mercenary
execute as @a[scores={slf.choose_class=41}] run function slf:class/grant/holy_knight
execute as @a[scores={slf.choose_class=42}] run function slf:class/grant/dark_knight
scoreboard players reset @a[scores={slf.choose_class=1..}] slf.choose_class
scoreboard players enable @a[tag=!slf.class_chosen] slf.choose_class

# --- Skill focus selection (via menu trigger) ---
execute as @a[scores={slf.focus_choose=1}]  run function slf:skills/focus/power_slash
execute as @a[scores={slf.focus_choose=2}]  run function slf:skills/focus/megaton_swing
execute as @a[scores={slf.focus_choose=3}]  run function slf:skills/focus/knuckle_rush
execute as @a[scores={slf.focus_choose=4}]  run function slf:skills/focus/manbufu
execute as @a[scores={slf.focus_choose=5}]  run function slf:skills/focus/sword_of_rough_waves
execute as @a[scores={slf.focus_choose=6}]  run function slf:skills/focus/spin_slash
execute as @a[scores={slf.focus_choose=7}]  run function slf:skills/focus/slide_step
execute as @a[scores={slf.focus_choose=8}]  run function slf:skills/focus/holy_shield
execute as @a[scores={slf.focus_choose=9}]  run function slf:skills/focus/iron_skin
execute as @a[scores={slf.focus_choose=10}] run function slf:skills/focus/paring_protect
execute as @a[scores={slf.focus_choose=11}] run function slf:skills/focus/flash_counter
execute as @a[scores={slf.focus_choose=12}] run function slf:skills/focus/total_body_takeshi
execute as @a[scores={slf.focus_choose=13}] run function slf:skills/focus/blaze_shot
execute as @a[scores={slf.focus_choose=14}] run function slf:skills/focus/ignition
execute as @a[scores={slf.focus_choose=15}] run function slf:skills/focus/duelism
execute as @a[scores={slf.focus_choose=16}] run function slf:skills/focus/one_inch_impact
execute as @a[scores={slf.focus_choose=20}] run function slf:skills/focus/lash_slash
execute as @a[scores={slf.focus_choose=21}] run function slf:skills/focus/gigaton_swing
execute as @a[scores={slf.focus_choose=22}] run function slf:skills/focus/strong_puncher
execute as @a[scores={slf.focus_choose=23}] run function slf:skills/focus/slash_ignition
execute as @a[scores={slf.focus_choose=24}] run function slf:skills/focus/formula_drift
execute as @a[scores={slf.focus_choose=25}] run function slf:skills/focus/big_tantrum
execute as @a[scores={slf.focus_choose=26}] run function slf:skills/focus/rechette_step
execute as @a[scores={slf.focus_choose=30}] run function slf:skills/focus/inexhaustible_beasts
execute as @a[scores={slf.focus_choose=31}] run function slf:skills/focus/terraton_corapsa
execute as @a[scores={slf.focus_choose=32}] run function slf:skills/focus/skatefoot
execute as @a[scores={slf.focus_choose=33}] run function slf:skills/focus/skywalker
scoreboard players reset @a[scores={slf.focus_choose=1..}] slf.focus_choose
scoreboard players enable @a[tag=slf.class_chosen] slf.focus_choose

# --- Knight alignment: only after 3 trials ---
execute as @a[tag=slf.was_knight,tag=!slf.was_holy_knight,tag=!slf.was_dark_knight,scores={slf.knight_trials=3..}] run function slf:class/alignment_choice

# --- 20t cycle ---
scoreboard players add #timer slf.timer 1
execute if score #timer slf.timer matches 20.. run function slf:skills/sp_tick
execute if score #timer slf.timer matches 20.. run function slf:skills/exp_tick
execute if score #timer slf.timer matches 20.. run function slf:skills/passives
execute if score #timer slf.timer matches 20.. run function slf:mask/karma_tick
execute if score #timer slf.timer matches 20.. run function slf:stats/apply
execute if score #timer slf.timer matches 20.. run scoreboard players set #timer slf.timer 0
