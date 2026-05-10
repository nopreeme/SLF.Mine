execute unless entity @s[tag=slf.was_shinobi] run return fail
scoreboard players set @s slf.class 53
tag @s add slf.skill.hermes_boot
tag @s add slf.skill.weda_tengengen
tag @s add slf.skill.neck_roll
tellraw @s {"text":"You have reached Star Shinobi Sei.","color":"dark_green","bold":true}
