# SLF.Mine — runs on world load

# --- Class & Progression ---
scoreboard objectives add slf.class dummy
scoreboard objectives add slf.choose_class trigger
scoreboard objectives add slf.focus_choose trigger
scoreboard objectives add slf.level dummy
scoreboard objectives add slf.exp dummy
scoreboard objectives add slf.sp_points dummy
scoreboard objectives add slf.boss_kills dummy

# --- Stat Attributes (9 spendable) ---
scoreboard objectives add slf.stat.hp dummy
scoreboard objectives add slf.stat.mp dummy
scoreboard objectives add slf.stat.str dummy
scoreboard objectives add slf.stat.dex dummy
scoreboard objectives add slf.stat.vit dummy
scoreboard objectives add slf.stat.agi dummy
scoreboard objectives add slf.stat.tec dummy
scoreboard objectives add slf.stat.lck dummy
scoreboard objectives add slf.stat.stm dummy

# --- Stat spend triggers (clickable from /function slf:stats/menu) ---
scoreboard objectives add slf.stat_hp trigger
scoreboard objectives add slf.stat_mp trigger
scoreboard objectives add slf.stat_str trigger
scoreboard objectives add slf.stat_dex trigger
scoreboard objectives add slf.stat_vit trigger
scoreboard objectives add slf.stat_agi trigger
scoreboard objectives add slf.stat_tec trigger
scoreboard objectives add slf.stat_lck trigger
scoreboard objectives add slf.stat_stm trigger

# --- Motion Trace: vanilla criterion objectives ---
scoreboard objectives add slf.raw.dmg minecraft.custom:minecraft.damage_dealt
scoreboard objectives add slf.raw.move minecraft.custom:minecraft.sprint_one_cm
scoreboard objectives add slf.raw.evade minecraft.custom:minecraft.jump
scoreboard objectives add slf.raw.def minecraft.custom:minecraft.damage_taken

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
scoreboard objectives add slf.focus dummy
scoreboard objectives add slf.focus_stat dummy
scoreboard objectives add slf.sp dummy
scoreboard objectives add slf.threshold dummy

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
# Level of the SLF mob a player just killed (mob/lv_bit/*, read by mob/kill_process)
scoreboard objectives add slf.kill_lv dummy
# Boss bars (mob/boss/bars); adding one that exists already just fails quietly on /reload
bossbar add slf:nightclaw {text:"Nightclaw",color:"dark_gray"}
bossbar set slf:nightclaw color white
bossbar set slf:nightclaw style notched_10
bossbar add slf:bilac {text:"Bilac the Full Moon Fangs",color:"gold"}
bossbar set slf:bilac color yellow
bossbar set slf:bilac style notched_10
bossbar add slf:oriana {text:"Oriana the Uncrowned",color:"dark_aqua"}
bossbar set slf:oriana color blue
bossbar set slf:oriana style notched_10
bossbar add slf:lycagon {text:"Lycagon the Nightslayer",color:"dark_purple"}
bossbar set slf:lycagon color purple
bossbar set slf:lycagon style notched_10
bossbar add slf:wethermon {text:"Wethermon the Tombguard",color:"dark_red"}
bossbar set slf:wethermon color red
bossbar set slf:wethermon style notched_10
bossbar add slf:ravenous_snake {text:"Ravenous Snake",color:"gold"}
bossbar set slf:ravenous_snake color yellow
bossbar set slf:ravenous_snake style notched_10
bossbar add slf:mud_digger {text:"Mud Digger",color:"dark_green"}
bossbar set slf:mud_digger color green
bossbar set slf:mud_digger style notched_10
bossbar add slf:ctarnidd {text:"Ctarnidd of the Abyss",color:"dark_blue"}
bossbar set slf:ctarnidd color blue
bossbar set slf:ctarnidd style notched_10
bossbar add slf:siegwurm {text:"Siegwurm the Sky Ruler",color:"aqua"}
bossbar set slf:siegwurm color white
bossbar set slf:siegwurm style notched_10

# --- Ignition detection (separate from def_prev) ---
scoreboard objectives add slf.ign.prev dummy

# --- Menus and evolution (triggers work without OP) ---
scoreboard objectives add slf.menu trigger
scoreboard objectives add slf.evolve trigger

# --- Join / death detection ---
scoreboard objectives add slf.leave minecraft.custom:minecraft.leave_game
scoreboard objectives add slf.deaths minecraft.custom:minecraft.deaths

# --- Derived stats: mana pool (MP), max-health bonus (HP), EXP needed for the next level ---
scoreboard objectives add slf.mana dummy
scoreboard objectives add slf.mana_max dummy
scoreboard objectives add slf.hp_applied dummy
scoreboard objectives add slf.exp_next dummy

# --- Temp scratch ---
scoreboard objectives add slf.tmp dummy
scoreboard objectives add slf.lck_save_cd dummy

# --- Misc ---
scoreboard objectives add slf.timer dummy
scoreboard objectives add slf.hp dummy

tellraw @a[gamemode=creative] {"text":"[SLF] Shangri-La Frontier pack loaded.","color":"gold"}
