execute if entity @s[tag=slf.class_chosen] run return fail
tag @s add slf.class_chosen
tag @s add slf.was_mercenary
scoreboard players set @s slf.class 30
tag @s add slf.skill.manbufu
tag @s add slf.skill.duelism
tag @s add slf.skill.overheat
tag @s add slf.skill.ignition
tellraw @s {"text":"You have become a Mercenary.","color":"yellow","bold":true}
function slf:class/select_cleanup
