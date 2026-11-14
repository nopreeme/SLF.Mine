# Reward of advancement slf:exp/kill_common (player_killed_entity). Runs as the killer. The advancement is
# revoked straight away so it can fire again on the next kill.
advancement revoke @s only slf:exp/kill_common
# Common monsters (#slf:exp_common): 10 EXP in total, treated as level 10.
scoreboard players add @s slf.exp 8
scoreboard players set #dying_mob_lv slf.mob_level 10
execute if score @s slf.level matches 1.. run function slf:mask/vorpal_kill_check
