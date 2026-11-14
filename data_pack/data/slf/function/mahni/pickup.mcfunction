# Reward of advancement slf:mahni/pickup: a Mahni Purse reached this player's inventory. Every purse is emptied into
# their Mahni (10 each) at once.
advancement revoke @s only slf:mahni/pickup
execute store result score #purses slf.tmp run clear @s minecraft:paper[minecraft:item_model="slf:mahni_purse"]
scoreboard players operation #gain slf.tmp = #purses slf.tmp
scoreboard players set #10 slf.tmp 10
scoreboard players operation #gain slf.tmp *= #10 slf.tmp
scoreboard players operation @s slf.mahni += #gain slf.tmp
playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.6
title @s actionbar ["",{"text":"+","color":"gold"},{"score":{"name":"#gain","objective":"slf.tmp"},"color":"gold"},{"text":" Mahni  ","color":"gold"},{"text":"(","color":"dark_gray"},{"score":{"name":"@s","objective":"slf.mahni"},"color":"yellow"},{"text":")","color":"dark_gray"}]
