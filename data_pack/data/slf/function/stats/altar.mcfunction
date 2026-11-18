# Altar of Awakening — converts exp_extend into post-99 levels (100-150)
# Reached by walking up to an altar (altar/enter), or from the menu when the world has no altar in reach (altar/guide).
# Requires 99 Extend (slf.standby=1): level 99 and a level 100+ monster defeated
execute unless score @s slf.standby matches 1 if score @s slf.level matches 99 unless score @s slf.awakened matches 1 run tellraw @s {"text":"The altar is dormant. Defeat a monster above level 100 to reach 99 Extend first.","color":"dark_red"}
execute unless score @s slf.standby matches 1 run return fail

scoreboard players set @s slf.standby 0
scoreboard players set @s slf.awakened 1
# Convert exp_extend to level gains at 5000 per level (excess is discarded)
scoreboard players operation @s slf.exp += @s slf.exp_extend
scoreboard players set @s slf.exp_extend 0
tellraw @s ["",{"text":"Awakening!","color":"gold","bold":true},{"text":" Your power beyond the limit has been unlocked. Levels 100-150 are now accessible.","color":"yellow"}]
playsound minecraft:ui.toast.challenge_complete master @s
