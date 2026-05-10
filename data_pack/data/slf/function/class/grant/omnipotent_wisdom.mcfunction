execute unless entity @s[tag=slf.was_sage] run return fail
scoreboard players set @s slf.class 62
tag @s add slf.title.apex_omni_wisdom
tellraw @s {"text":"You have become Omnipotent Wisdom.","color":"blue","bold":true}
tellraw @s {"text":"You have reached the pinnacle of this path. No further evolution exists — your mastery is complete.","color":"gold"}
playsound minecraft:ui.toast.challenge_complete master @s
