# Reward of advancement slf:exp/kill_elite (player_killed_entity). Runs as the killer. The advancement is
# revoked straight away so it can fire again on the next kill.
advancement revoke @s only slf:exp/kill_elite
# Elite monsters (#slf:exp_elite): 40 EXP in total, treated as level 40. Each one is a Knight Trial.
scoreboard players add @s slf.exp 38
scoreboard players set #dying_mob_lv slf.mob_level 40
execute if score @s slf.level matches 1.. run function slf:mask/vorpal_kill_check
execute if entity @s[tag=slf.was_knight] run function slf:class/knight_trial_complete
