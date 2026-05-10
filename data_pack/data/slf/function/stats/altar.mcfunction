# Altar of Awakening — converts exp_extend into post-99 levels (100-150)
# Requires: slf.standby=1 AND slf.boss_gate=1
execute unless entity @s[scores={slf.standby=1}] run return fail
execute unless entity @s[scores={slf.boss_gate=1}] run tellraw @s {"text":"The altar is dormant. Prove yourself against a worthy foe first.","color":"dark_red"}
execute unless entity @s[scores={slf.boss_gate=1}] run return fail

scoreboard players set @s slf.standby 0
scoreboard players set @s slf.awakened 1
# Convert exp_extend to level gains at 5000 per level (excess is discarded)
scoreboard players operation @s slf.exp += @s slf.exp_extend
scoreboard players set @s slf.exp_extend 0
tellraw @s ["",{"text":"Awakening!","color":"gold","bold":true},{"text":" Your power beyond the limit has been unlocked. Levels 100-150 are now accessible.","color":"yellow"}]
playsound minecraft:ui.toast.challenge_complete master @s
