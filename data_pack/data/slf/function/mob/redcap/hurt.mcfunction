# Reward of advancement slf:mob/redcap_hurt: this player just hit a Redcap Goblin. The Redcap it hit (the one
# still flinching) calls for help, once.
advancement revoke @s only slf:mob/redcap_hurt
execute as @e[tag=slf.red_hat_goblin,tag=!slf.called,distance=..8,nbt={HurtTime:10s}] at @s run function slf:mob/redcap/call
