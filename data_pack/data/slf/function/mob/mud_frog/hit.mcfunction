# Reward of advancement slf:mob/mud_frog_hit: this player just hit a Mud Frog.
#  - Swords slide off the mud coating: the frog heals back 4 of the damage (an iron sword does 2 instead of 6).
#  - It hits back: a splash of mud (2 damage, Slowness for 3 seconds) if the player is within 4 blocks.
advancement revoke @s only slf:mob/mud_frog_hit
execute if items entity @s weapon.mainhand #minecraft:swords as @e[tag=slf.mud_frog,distance=..8,nbt={HurtTime:10s}] run effect give @s minecraft:instant_health 1 0 true
execute at @s if entity @e[tag=slf.mud_frog,distance=..4,nbt={HurtTime:10s}] run function slf:mob/mud_frog/splash
