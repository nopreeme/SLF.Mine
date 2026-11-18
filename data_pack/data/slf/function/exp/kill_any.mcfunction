# Reward of advancement slf:exp/kill_any (player_killed_entity). Runs as the killer. The advancement is
# revoked straight away so it can fire again on the next kill.
advancement revoke @s only slf:exp/kill_any
# Every kill: 2 EXP. Tiered kills add their bonus on top (see kill_common / kill_elite / kill_boss).
scoreboard players add @s slf.exp 2
