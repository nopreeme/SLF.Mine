# Admin: /function slf:altar/place — builds the Altar of Awakening four blocks south of where you stand.
# The pack raises an altar by itself when the first player reaches level 99 (altar/create); use this to choose
# the spot instead. One altar per world: placing a new one retires the old marker (its blocks are left alone).
kill @e[type=minecraft:marker,tag=slf.altar_placed]
kill @e[type=minecraft:text_display,tag=slf.altar_placed]
execute align xyz positioned ~ ~ ~4 run function slf:altar/build
tellraw @s ["",{"text":"[SLF] ","color":"gold"},{"text":"Altar of Awakening placed at ","color":"yellow"},{"score":{"name":"#altar_x","objective":"slf.timer"}},{"text":" "},{"score":{"name":"#altar_y","objective":"slf.timer"}},{"text":" "},{"score":{"name":"#altar_z","objective":"slf.timer"}},{"text":". Players at level 99 who have defeated a boss awaken by walking up to it.","color":"yellow"}]
