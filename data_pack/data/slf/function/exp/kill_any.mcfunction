# Reward of advancement slf:exp/kill_any (player_killed_entity). Runs as the killer. The advancement is
# revoked straight away so it can fire again on the next kill.
advancement revoke @s only slf:exp/kill_any
# Every kill: 2 EXP. Tiered kills add their bonus on top (see kill_common / kill_elite / kill_boss).
scoreboard players add @s slf.exp 2
# Kills made while a Tantrum is active count toward Grand Tantrum
execute if entity @s[tag=slf.tantrum_active] run scoreboard players add @s slf.bt_kills 1
execute if entity @s[tag=slf.skill.big_tantrum,tag=!slf.skill.grand_tantrum] if score @s slf.bt_kills matches 50.. run function slf:skills/learn/grand_tantrum
