execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_choosing
execute at @s rotated as @s run summon minecraft:chest_minecart ^ ^0 ^1.5 {Tags:["slf.class_menu"],CustomName:'{"text":"Class Selection","color":"gold","italic":false}',Invulnerable:1b}
execute at @s run function slf:class/select_fill
tellraw @s {"text":"Right-click the chest to choose your class.","color":"gray","italic":true}
