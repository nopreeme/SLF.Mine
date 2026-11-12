# Reward of advancement slf:exp/kill_player (player_killed_entity). Runs as the killer. The advancement is
# revoked straight away so it can fire again on the next kill.
advancement revoke @s only slf:exp/kill_player
# Player kill: karma +25 (mask data, deliberately not announced).
scoreboard players add @s slf.karma 25
