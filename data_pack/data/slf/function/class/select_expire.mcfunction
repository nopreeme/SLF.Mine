execute as @e[type=chest_minecart,tag=slf.class_menu] at @s unless entity @a[tag=slf.class_choosing,distance=..25] run data modify entity @s Items set value []
execute as @e[type=chest_minecart,tag=slf.class_menu] at @s unless entity @a[tag=slf.class_choosing,distance=..25] run kill @s
execute as @a[tag=slf.class_choosing] at @s unless entity @e[type=chest_minecart,tag=slf.class_menu,distance=..25] run tag @s remove slf.class_choosing
