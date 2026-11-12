# Reward of advancement slf:exp/kill_boss (player_killed_entity). Runs as the killer. The advancement is
# revoked straight away so it can fire again on the next kill.
advancement revoke @s only slf:exp/kill_boss
# Bosses (#slf:exp_boss): 2500 EXP in total, treated as level 120. Opens the Altar of Awakening.
scoreboard players add @s slf.exp 2498
scoreboard players set #dying_mob_lv slf.mob_level 120
execute if score @s slf.level matches 1.. run function slf:mask/vorpal_kill_check
scoreboard players add @s slf.boss_kills 1
execute unless score @s slf.boss_gate matches 1 run tellraw @s ["",{"text":"A worthy foe has fallen. ","color":"gold","bold":true},{"text":"The Altar of Awakening will answer you once you reach level 99.","color":"yellow"}]
scoreboard players set @s slf.boss_gate 1
execute if entity @s[tag=slf.was_knight] run function slf:class/knight_trial_complete
