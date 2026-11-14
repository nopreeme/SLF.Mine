# Reward of advancement slf:mob/mud_digger_kill: this player killed the Mud Digger. On top of the level-based EXP:
# +800 EXP (design doc V9). A player who did it with nobody else within 32 blocks also gets the Solo Killer's Trophy and
# the title tag slf.title.solo_killer. Area bosses do not count toward the Altar of Awakening.
advancement revoke @s only slf:mob/mud_digger_kill
scoreboard players add @s slf.exp 800
tellraw @a[distance=..64] ["",{"selector":"@s","color":"gold"},{"text":" has slain the Mud Digger! The road to Thirdrema is open.","color":"yellow"}]
execute at @s unless entity @a[distance=0.01..32,gamemode=!spectator] run function slf:mob/boss/mud_digger/solo
