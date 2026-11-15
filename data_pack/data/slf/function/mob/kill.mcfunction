# Reward of advancement slf:mob/kill: this player killed an SLF mob. The level bits (mob/lv_bit/*) may be
# awarded after this one, so the kill is settled at the start of the next tick by mob/kill_process.
advancement revoke @s only slf:mob/kill
tag @s add slf.mob_kill
