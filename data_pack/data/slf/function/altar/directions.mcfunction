# As a player: where the world's altar stands, plus one compass that points to it.
tellraw @s ["",{"text":" The Altar of Awakening stands at ","color":"light_purple"},{"score":{"name":"#altar_x","objective":"slf.timer"},"color":"white"},{"text":" "},{"score":{"name":"#altar_y","objective":"slf.timer"},"color":"white"},{"text":" "},{"score":{"name":"#altar_z","objective":"slf.timer"},"color":"white"},{"text":". Walk up to it to awaken.","color":"light_purple"}]
execute if items entity @s container.* minecraft:compass[minecraft:custom_data~{slf_altar_compass:1b}] run return run tellraw @s {"text":" Your altar compass points the way.","color":"gray"}
execute if items entity @s weapon.offhand minecraft:compass[minecraft:custom_data~{slf_altar_compass:1b}] run return run tellraw @s {"text":" Your altar compass points the way.","color":"gray"}
function slf:altar/give_compass with storage slf:altar
tellraw @s {"text":" A compass pointing to it has been placed in your inventory.","color":"gray"}
