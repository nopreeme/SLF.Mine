# A swimmer: stays in the water near the player, moved 8 blocks off and a little deeper when there is water there.
execute as @e[tag=slf.boss_new] at @s if block ~8 ~-3 ~ minecraft:water if block ~8 ~-1 ~ minecraft:water run tp @s ~8 ~-3 ~
