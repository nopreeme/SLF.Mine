execute unless entity @s[tag=slf.was_thief] run return fail
scoreboard players set @s slf.class 31
tag @s add slf.was_veteran
tag @s add slf.title.apex_veteran
tellraw @s {"text":"You have become a Veteran.","color":"dark_green","bold":true}
tellraw @s {"text":"You have reached the pinnacle of this path. No further evolution exists — your mastery is complete.","color":"gold"}
playsound minecraft:ui.toast.challenge_complete master @s
