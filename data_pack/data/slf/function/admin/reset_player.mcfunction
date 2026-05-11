# Wipes all SLF state from the executing player — use between test runs

# Class tags
tag @s remove slf.class_chosen
tag @s remove slf.was_swordsman
tag @s remove slf.was_warrior
tag @s remove slf.was_fighter
tag @s remove slf.was_mercenary
tag @s remove slf.was_thief
tag @s remove slf.was_priest
tag @s remove slf.was_monk
tag @s remove slf.was_mage
tag @s remove slf.was_sword_master
tag @s remove slf.was_magic_swordsman
tag @s remove slf.was_barbarian
tag @s remove slf.was_destroyer
tag @s remove slf.was_bandit
tag @s remove slf.was_ninja
tag @s remove slf.was_veteran
tag @s remove slf.was_bishop
tag @s remove slf.was_monk_soldier
tag @s remove slf.was_sage
tag @s remove slf.was_war_king
tag @s remove slf.was_mysterious_sword
tag @s remove slf.was_assassin
tag @s remove slf.was_shinobi
tag @s remove slf.was_knight
tag @s remove slf.was_holy_knight
tag @s remove slf.was_dark_knight
tag @s remove slf.alignment_offered

# Skill tags
tag @s remove slf.skill.power_slash
tag @s remove slf.skill.sword_of_rough_waves
tag @s remove slf.skill.spin_slash
tag @s remove slf.skill.megaton_swing
tag @s remove slf.skill.rigid_strength
tag @s remove slf.skill.front_position
tag @s remove slf.skill.dual_impact
tag @s remove slf.skill.crash_upper
tag @s remove slf.skill.knuckle_rush
tag @s remove slf.skill.manbufu
tag @s remove slf.skill.duelism
tag @s remove slf.skill.overheat
tag @s remove slf.skill.ignition
tag @s remove slf.skill.stealth_assault
tag @s remove slf.skill.slide_step
tag @s remove slf.skill.quick_spin
tag @s remove slf.skill.breath_of_anti_harm
tag @s remove slf.skill.phalanx
tag @s remove slf.skill.protect_charge
tag @s remove slf.skill.tasram_fist
tag @s remove slf.skill.skull_shaker
tag @s remove slf.skill.tanda_breathing
tag @s remove slf.skill.wisdoms_divine_eye
tag @s remove slf.skill.chanting_and_memorizing
tag @s remove slf.skill.lash_slash
tag @s remove slf.skill.lion_fall
tag @s remove slf.skill.shakudanzan
tag @s remove slf.skill.slash_ignition
tag @s remove slf.skill.sword_dance
tag @s remove slf.skill.gigaton_swing
tag @s remove slf.skill.fortress_breaker
tag @s remove slf.skill.gobus_courage
tag @s remove slf.skill.meteor_fall
tag @s remove slf.skill.zanzui_flying_blade_leg
tag @s remove slf.skill.grapple_train
tag @s remove slf.skill.dirty_sword
tag @s remove slf.skill.assassin_pierce
tag @s remove slf.skill.big_tantrum
tag @s remove slf.skill.formula_drift
tag @s remove slf.skill.skatefoot
tag @s remove slf.skill.rechette_step
tag @s remove slf.skill.guardian_heart
tag @s remove slf.skill.protect_smash
tag @s remove slf.skill.shield_bashing
tag @s remove slf.skill.infight
tag @s remove slf.skill.meditation
tag @s remove slf.skill.instant_vision
tag @s remove slf.skill.hegemony_world
tag @s remove slf.skill.analyze_legacy
tag @s remove slf.skill.inexhaustible_beasts
tag @s remove slf.skill.hekaton_slash
tag @s remove slf.skill.spectrum_slash
tag @s remove slf.skill.sword_dance_reincarnation
tag @s remove slf.skill.sword_god_danba
tag @s remove slf.skill.asura_kagura
tag @s remove slf.skill.terraton_corapsa
tag @s remove slf.skill.break_attack
tag @s remove slf.skill.tsujizanri
tag @s remove slf.skill.strong_puncher
tag @s remove slf.skill.one_inch_impact
tag @s remove slf.skill.hundred_sounding
tag @s remove slf.skill.desperate_sting
tag @s remove slf.skill.masakuru_byte
tag @s remove slf.skill.hate_trumple
tag @s remove slf.skill.skywalker
tag @s remove slf.skill.after_all_unyo
tag @s remove slf.skill.burnout
tag @s remove slf.skill.embrace_of_devil
tag @s remove slf.skill.causal_accumulation
tag @s remove slf.skill.unbreakable
tag @s remove slf.skill.hand_of_fortune
tag @s remove slf.skill.kings_silver_arm
tag @s remove slf.skill.flash_counter
tag @s remove slf.skill.paring_protect
tag @s remove slf.skill.total_body_takeshi
tag @s remove slf.skill.holy_shield
tag @s remove slf.skill.iron_skin
tag @s remove slf.skill.gravity_zero
tag @s remove slf.skill.acrobat
tag @s remove slf.skill.managarm_pride
tag @s remove slf.skill.bradion
tag @s remove slf.skill.reflexus
tag @s remove slf.skill.grand_tantrum
tag @s remove slf.skill.duelism
tag @s remove slf.skill.blaze_shot
tag @s remove slf.skill.iggist_requiem
tag @s remove slf.skill.fatal_gain
tag @s remove slf.skill.serial_killer
tag @s remove slf.skill.limit_break_rees
tag @s remove slf.skill.ablaze_advanced_ale
tag @s remove slf.tantrum_active

# Title tags
tag @s remove slf.title.apex_crazy_fist
tag @s remove slf.title.apex_veteran
tag @s remove slf.title.apex_star_shinobi
tag @s remove slf.title.apex_omni_wisdom
tag @s remove slf.title.tombguard_destroyer

# Scores
scoreboard players set @s slf.class 0
scoreboard players set @s slf.level 1
scoreboard players set @s slf.exp 0
scoreboard players set @s slf.sp_points 0
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.focus_stat 0
scoreboard players set @s slf.sp 0
scoreboard players set @s slf.threshold 0
scoreboard players set @s slf.stat.str 0
scoreboard players set @s slf.stat.dex 0
scoreboard players set @s slf.stat.vit 0
scoreboard players set @s slf.stat.agi 0
scoreboard players set @s slf.stat.int 0
scoreboard players set @s slf.stat.tec 0
scoreboard players set @s slf.stat.lck 0
scoreboard players set @s slf.stat.stm 0
scoreboard players set @s slf.karma 0
scoreboard players set @s slf.knight_trials 0
scoreboard players set @s slf.standby 0
scoreboard players set @s slf.exp_extend 0
scoreboard players set @s slf.awakened 0

tellraw @s {"text":"[SLF] Player state reset.","color":"gray"}
