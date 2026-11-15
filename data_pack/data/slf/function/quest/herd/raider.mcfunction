# A goblin raider guarding the camp (a normal Goblin, level 4-8, that stays around).
execute store result score #spawn_lv slf.mob_level run random value 4..8
function slf:mob/goblin/spawn
tag @e[tag=slf.goblin,tag=!slf.raider,distance=..1.5,limit=1,sort=nearest] add slf.scene_new
tag @e[tag=slf.scene_new,tag=slf.goblin] add slf.raider
execute as @e[tag=slf.raider,tag=slf.scene_new] run data merge entity @s {PersistenceRequired:1b}
