# Runs as a player who clicked an origin (/trigger slf.origin set <n>).
scoreboard players operation #o slf.tmp = @s slf.origin
scoreboard players set @s slf.origin 0
execute if entity @s[tag=slf.origin_chosen] run return run tellraw @s {"text":"Your origin is already chosen.","color":"gray"}
scoreboard players enable @s slf.origin
execute if score #o slf.tmp matches 4 run return run function slf:wanderer/origin_menu
execute if score #o slf.tmp matches 1 run return run function slf:wanderer/become_citizen
execute if score #o slf.tmp matches 2 run return run function slf:wanderer/warning
execute if score #o slf.tmp matches 3 run return run function slf:wanderer/become_wanderer
