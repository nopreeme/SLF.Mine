# Runs as a Vorpal Bunny, at it: gives it its visible body. The rabbit itself becomes an invisible hitbox (a little
# larger than a plain rabbit's, to fit the upright model) and one 3D model (an item display, tools/gen_mob_models.py)
# rides on it. Called by mob/vorpal_bunny/convert, and by mob/tick for Vorpal Bunnies from before the model existed.
tag @s add slf.bodied
effect give @s minecraft:invisibility infinite 0 true
attribute @s minecraft:scale base set 1.6
summon minecraft:item_display ~ ~ ~ {Tags:["slf.mob_body","slf.body_bunny","slf.body_new"],item_display:"none",item:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"slf:vorpal_bunny"}},transformation:{left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],translation:[0f,-0.5f,0f],scale:[0.6f,0.6f,0.6f]}}
ride @e[tag=slf.body_new,distance=..2,limit=1,sort=nearest] mount @s
tag @e[tag=slf.body_new] remove slf.body_new
