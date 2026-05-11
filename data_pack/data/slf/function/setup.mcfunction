# SLF.Mine — runs on world load

# --- Class & Progression ---
scoreboard objectives add slf.class dummy "Class"
scoreboard objectives add slf.choose_class trigger "Choose Class"
scoreboard objectives add slf.focus_choose trigger "Focus Choose"
scoreboard objectives add slf.level dummy "Level"
scoreboard objectives add slf.exp dummy "EXP"
scoreboard objectives add slf.sp_points dummy "Stat Points"
scoreboard objectives add slf.boss_kills dummy "Boss Kills"

# --- Stat Attributes (8 spendable) ---
scoreboard objectives add slf.stat.str dummy "STR"
scoreboard objectives add slf.stat.dex dummy "DEX"
scoreboard objectives add slf.stat.vit dummy "VIT"
scoreboard objectives add slf.stat.agi dummy "AGI"
scoreboard objectives add slf.stat.tec dummy "TEC"
scoreboard objectives add slf.stat.lck dummy "LCK"
scoreboard objectives add slf.stat.stm dummy "STM"

# --- Stat spend triggers (clickable from /function slf:stats/menu) ---
scoreboard objectives add slf.stat_str trigger
scoreboard objectives add slf.stat_dex trigger
scoreboard objectives add slf.stat_vit trigger
scoreboard objectives add slf.stat_agi trigger
scoreboard objectives add slf.stat_tec trigger
scoreboard objectives add slf.stat_lck trigger
scoreboard objectives add slf.stat_stm trigger

# --- Motion Trace: vanilla criterion objectives ---
scoreboard objectives add slf.raw.dmg stat minecraft.custom:minecraft.damage_dealt
scoreboard objectives add slf.raw.move stat minecraft.custom:minecraft.sprint_one_cm
scoreboard objectives add slf.raw.evade stat minecraft.custom:minecraft.jump
scoreboard objectives add slf.raw.def stat minecraft.custom:minecraft.damage_taken

# --- Motion Trace: delta computation ---
scoreboard objectives add slf.dmg_prev dummy
scoreboard objectives add slf.dmg_delta dummy
scoreboard objectives add slf.move_prev dummy
scoreboard objectives add slf.move_delta dummy
scoreboard objectives add slf.evade_prev dummy
scoreboard objectives add slf.evade_delta dummy
scoreboard objectives add slf.def_prev dummy
scoreboard objectives add slf.def_delta dummy

# --- Skill Focus System ---
scoreboard objectives add slf.focus dummy "Focus"
scoreboard objectives add slf.focus_stat dummy "Focus Stat"
scoreboard objectives add slf.sp dummy "SP"
scoreboard objectives add slf.threshold dummy "Threshold"

# --- Level 99 Standby Gate ---
scoreboard objectives add slf.exp_extend dummy
scoreboard objectives add slf.standby dummy
scoreboard objectives add slf.boss_gate dummy
scoreboard objectives add slf.awakened dummy

# --- Mask Data ---
scoreboard objectives add slf.vorpal_soul dummy
scoreboard objectives add slf.karma dummy
scoreboard objectives add slf.karma_timer dummy
scoreboard objectives add slf.bt_kills dummy

# --- Knight Quest ---
scoreboard objectives add slf.knight_quest dummy
scoreboard objectives add slf.knight_trials dummy

# --- Mob Level (set on mob entities at spawn) ---
scoreboard objectives add slf.mob_level dummy

# --- Ignition detection (separate from def_prev) ---
scoreboard objectives add slf.ign.prev dummy

# --- Temp scratch ---
scoreboard objectives add slf.tmp dummy
scoreboard objectives add slf.lck_save_cd dummy

# --- Misc ---
scoreboard objectives add slf.timer dummy
scoreboard objectives add slf.hp dummy

tellraw @a[gamemode=creative] {"text":"[SLF] Shangri-La Frontier pack loaded.","color":"gold"}
