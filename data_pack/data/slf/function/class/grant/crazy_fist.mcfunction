execute unless entity @s[tag=slf.was_destroyer] run return fail
scoreboard players set @s slf.class 22
tag @s add slf.skill.strong_puncher
tag @s remove slf.skill.knuckle_rush
tag @s add slf.skill.one_inch_impact
tag @s add slf.skill.hundred_sounding
tag @s add slf.title.apex_crazy_fist
tellraw @s {"text":"You have become Crazy Fist.","color":"dark_red","bold":true}
tellraw @s {"text":"You have reached the pinnacle of this path. No further evolution exists — your mastery is complete.","color":"gold"}
playsound minecraft:ui.toast.challenge_complete master @s
