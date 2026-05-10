# T4 evolution of Big Tantrum (gated by slf.bt_kills >= 50)
execute unless entity @s[scores={slf.bt_kills=50..}] run tellraw @s {"text":"Not yet. Prove yourself with Big Tantrum first.","color":"red"}
execute unless entity @s[scores={slf.bt_kills=50..}] run return fail
tag @s remove slf.skill.big_tantrum
tag @s add slf.skill.grand_tantrum
scoreboard players set @s slf.focus 0
scoreboard players set @s slf.sp 0
tellraw @s ["",{"text":"Skill evolved: ","color":"green"},{"text":"Grand Tantrum","color":"gold"},{"text":" (replaced Big Tantrum)","color":"dark_gray"}]
playsound minecraft:ui.toast.challenge_complete master @s
