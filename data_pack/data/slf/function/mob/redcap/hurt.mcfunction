# Reward of advancement slf:mob/redcap_hurt: this player just hit a Redcap Goblin. The Redcap it hit (the one
# still flinching) calls for help, once.
advancement revoke @s only slf:mob/redcap_hurt
execute as @e[tag=slf.red_hat_goblin,tag=!slf.called,distance=..8,nbt={HurtTime:10s}] at @s run function slf:mob/redcap/call
# The Night Watch: hitting one while on watch spoils it
execute if score @s slf.q.watch matches 1 if score @s slf.q.watch_t matches 1.. run function slf:quest/watch/engaged
