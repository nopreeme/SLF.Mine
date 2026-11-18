# Every second while Big Tantrum is active (skills/passives), as the player: monsters within 48 blocks pick up the
# player from that far away, so they come.
execute as @e[type=#slf:exp_common,distance=..48] run attribute @s minecraft:follow_range base set 64
execute as @e[type=#slf:exp_elite,distance=..48] run attribute @s minecraft:follow_range base set 64
