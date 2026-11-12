# Menu option 6, as a player in Standby. Points at an altar; only awakens on the spot if the world has none in reach.
execute if score #altar_placed slf.timer matches 1 run return run tellraw @s ["",{"text":" The Altar of Awakening stands at ","color":"light_purple"},{"score":{"name":"#altar_x","objective":"slf.timer"},"color":"white"},{"text":" "},{"score":{"name":"#altar_y","objective":"slf.timer"},"color":"white"},{"text":" "},{"score":{"name":"#altar_z","objective":"slf.timer"},"color":"white"},{"text":". Walk up to it to awaken.","color":"light_purple"}]
# Nearest generated altar: /locate returns the distance (0 when none is found)
execute at @s store result score #dist slf.tmp run locate structure slf:altar
execute if score #dist slf.tmp matches ..0 run return run function slf:stats/altar
tellraw @s ["",{"text":" The nearest Altar of Awakening is about ","color":"light_purple"},{"score":{"name":"#dist","objective":"slf.tmp"},"color":"white"},{"text":" blocks away. Walk up to it to awaken.","color":"light_purple"}]
# One explorer map per player at a time (same mechanism as a cartographer's map)
execute if items entity @s container.* minecraft:filled_map[minecraft:custom_data~{slf_altar_map:1b}] run return run tellraw @s {"text":" Your map to the altar shows the way.","color":"gray"}
execute if items entity @s weapon.offhand minecraft:filled_map[minecraft:custom_data~{slf_altar_map:1b}] run return run tellraw @s {"text":" Your map to the altar shows the way.","color":"gray"}
execute at @s run loot give @s loot slf:altar_map
tellraw @s {"text":" A map to it has been placed in your inventory.","color":"gray"}
