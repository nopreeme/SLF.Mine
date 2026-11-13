# Reward of advancement slf:mob/forest_kill: the mob this player just killed is a Rampant Forest monster
# (Goblin, Vorpal Bunny). Read by mob/kill_process on the next tick.
advancement revoke @s only slf:mob/forest_kill
tag @s add slf.forest_kill
