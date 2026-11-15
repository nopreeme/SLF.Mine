# Runs as the snake: a pool of poison under its tail. The poison lasts 30 seconds, so it is still on you after the fight.
scoreboard players set @s slf.timer 0
execute at @e[tag=slf.seg8,limit=1] run summon minecraft:area_effect_cloud ~ ~0.2 ~ {Tags:["slf.snake_poison"],Radius:3.5f,RadiusPerTick:0f,Duration:120,WaitTime:0,ReapplicationDelay:20,potion_contents:{custom_color:9846962,custom_effects:[{id:"minecraft:poison",duration:600,amplifier:1}]}}
execute at @e[tag=slf.seg8,limit=1] run particle minecraft:dust{color:[0.6,0.24,0.7],scale:2.0} ~ ~1 ~ 1 0.5 1 0 40
execute at @e[tag=slf.seg8,limit=1] run playsound minecraft:entity.puffer_fish.blow_out hostile @a[distance=..24] ~ ~ ~ 1 0.6
