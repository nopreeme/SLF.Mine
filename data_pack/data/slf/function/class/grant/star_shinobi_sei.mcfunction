execute unless entity @s[tag=slf.was_shinobi] run return fail
scoreboard players set @s slf.class 53
tag @s add slf.title.apex_star_shinobi
tellraw @s {"text":"You have become Star Shinobi Sei.","color":"light_purple","bold":true}
tellraw @s {"text":"You have reached the pinnacle of this path. No further evolution exists — your mastery is complete.","color":"gold"}
playsound minecraft:ui.toast.challenge_complete master @s
