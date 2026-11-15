# Runs as a Mud Frog, at it: gives it its visible body. The frog itself becomes an invisible hitbox and one 3D model
# (an item display, tools/gen_mob_models.py) rides on it. Called by mob/mud_frog/convert, and by mob/tick for Mud Frogs
# from before the model existed.
tag @s add slf.bodied
effect give @s minecraft:invisibility infinite 0 true
summon minecraft:item_display ~ ~ ~ {Tags:["slf.mob_body","slf.body_frog","slf.body_new"],item_display:"none",item:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"slf:mud_frog"}},transformation:{left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],translation:[0f,-0.25f,0f],scale:[1.1f,1.1f,1.1f]}}
ride @e[tag=slf.body_new,distance=..2,limit=1,sort=nearest] mount @s
tag @e[tag=slf.body_new] remove slf.body_new
