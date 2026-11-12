# Admin: /function slf:altar/place — builds the Altar of Awakening four blocks south of where you stand.
# There is one altar per world; placing a new one retires the old marker (its blocks are left alone).
kill @e[type=minecraft:marker,tag=slf.altar]
kill @e[type=minecraft:text_display,tag=slf.altar_label]
execute align xyz positioned ~ ~ ~4 run function slf:altar/build
tellraw @s ["",{"text":"[SLF] ","color":"gold"},{"text":"Altar of Awakening placed at ","color":"yellow"},{"score":{"name":"#altar_x","objective":"slf.timer"}},{"text":" "},{"score":{"name":"#altar_y","objective":"slf.timer"}},{"text":" "},{"score":{"name":"#altar_z","objective":"slf.timer"}},{"text":". Players at level 99 who have defeated a boss awaken by walking up to it.","color":"yellow"}]
