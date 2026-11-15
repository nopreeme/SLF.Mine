# Runs as a mob body whose mob just landed: back to the standing model.
tag @s remove slf.leaping
execute if entity @s[tag=slf.body_bunny] run data modify entity @s item.components."minecraft:item_model" set value "slf:vorpal_bunny"
execute if entity @s[tag=slf.body_frog] run data modify entity @s item.components."minecraft:item_model" set value "slf:mud_frog"
