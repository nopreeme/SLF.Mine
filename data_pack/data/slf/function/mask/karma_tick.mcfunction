# Runs every 20t
# Decay: 60 cycles of 20t = 1200t = 60s
scoreboard players add #karma_timer slf.karma_timer 1
execute as @a if score @s slf.karma >= 1 if score #karma_timer slf.karma_timer >= 60 run scoreboard players remove @s slf.karma 1
execute if score #karma_timer slf.karma_timer >= 60 run scoreboard players set #karma_timer slf.karma_timer 0

# Bounty hunter spawn at 100+ karma
execute as @a if score @s slf.karma >= 100 at @s run function slf:mask/spawn_bounty_hunter

# Cap karma at 200
execute as @a if score @s slf.karma >= 201 run scoreboard players set @s slf.karma 200
