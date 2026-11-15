# Runs as a mob body whose mob just left the ground: switch to the leaping model.
tag @s add slf.leaping
execute if entity @s[tag=slf.body_bunny] run data modify entity @s item.components."minecraft:item_model" set value "slf:vorpal_bunny_leap"
execute if entity @s[tag=slf.body_frog] run data modify entity @s item.components."minecraft:item_model" set value "slf:mud_frog_leap"
