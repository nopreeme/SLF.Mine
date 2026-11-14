execute if entity @s[tag=slf.hud_off] run return run function slf:menu/hud_on
tag @s add slf.hud_off
title @s actionbar ""
tellraw @s {"text":"Status line hidden. Use the menu to show it again.","color":"gray"}
