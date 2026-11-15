# Reward of advancement slf:marsh/slashed: something with a sword or an axe just hit this player. Splitblade leather turns
# a blade (design doc V9): each piece worn gives back part of the hit - the full set (body, pants, mask) gives back 4 health,
# one or two pieces about 1-2 (a short burst of regeneration).
advancement revoke @s only slf:marsh/slashed
scoreboard players set #pieces slf.tmp 0
execute if items entity @s armor.chest *[minecraft:custom_model_data={strings:["slf.chest_splitblade"]}] run scoreboard players add #pieces slf.tmp 1
execute if items entity @s armor.legs *[minecraft:custom_model_data={strings:["slf.pants_splitblade"]}] run scoreboard players add #pieces slf.tmp 1
execute if items entity @s armor.head *[minecraft:custom_model_data={strings:["slf.mask_splitblade"]}] run scoreboard players add #pieces slf.tmp 1
execute if score #pieces slf.tmp matches 3 run effect give @s minecraft:instant_health 1 0 true
execute if score #pieces slf.tmp matches 1..2 run effect give @s minecraft:regeneration 1 2 true
execute if score #pieces slf.tmp matches 1.. run particle minecraft:crit ~ ~1 ~ 0.3 0.4 0.3 0.1 8
