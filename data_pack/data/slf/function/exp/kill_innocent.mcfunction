# Reward of advancement slf:exp/kill_innocent (player_killed_entity). Runs as the killer. The advancement is
# revoked straight away so it can fire again on the next kill.
advancement revoke @s only slf:exp/kill_innocent
# Villagers, traders and golems (#slf:innocent): karma +5.
scoreboard players add @s slf.karma 5
