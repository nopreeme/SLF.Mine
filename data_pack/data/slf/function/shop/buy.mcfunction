# Runs as a player who clicked a buy button (/trigger slf.shop set <item>). Mahni is checked and taken here.
scoreboard players operation #item slf.tmp = @s slf.shop
scoreboard players set @s slf.shop 0
scoreboard players enable @s slf.shop
function slf:player/init_scores
execute if score #item slf.tmp matches 1 run return run function slf:shop/item/1
execute if score #item slf.tmp matches 2 run return run function slf:shop/item/2
execute if score #item slf.tmp matches 3 run return run function slf:shop/item/3
execute if score #item slf.tmp matches 4 run return run function slf:shop/item/4
