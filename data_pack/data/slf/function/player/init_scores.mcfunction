# Makes sure every score a player can see exists, as 0 if it was never set. A score that does not exist
# shows as nothing in chat and on the status line ("EXP /100"). 'add 0' never changes an existing value.
# Called once per second for players with a class, and at the top of the menus that print scores.
scoreboard players add @s slf.exp 0
scoreboard players add @s slf.sp_points 0
scoreboard players add @s slf.sp 0
scoreboard players add @s slf.threshold 0
scoreboard players add @s slf.focus 0
scoreboard players add @s slf.mana 0
scoreboard players add @s slf.mana_max 0
scoreboard players add @s slf.karma 0
scoreboard players add @s slf.mahni 0
scoreboard players add @s slf.q.awaken 0
scoreboard players add @s slf.q.outskirts 0
scoreboard players add @s slf.q.goblins 0
scoreboard players add @s slf.q.brute 0
scoreboard players add @s slf.q.orcs 0
scoreboard players add @s slf.vorpal_soul 0
scoreboard players add @s slf.boss_kills 0
scoreboard players add @s slf.bt_kills 0
scoreboard players add @s slf.exp_extend 0
scoreboard players add @s slf.standby 0
scoreboard players add @s slf.awakened 0
scoreboard players add @s slf.knight_trials 0
scoreboard players add @s slf.stat.hp 0
scoreboard players add @s slf.stat.mp 0
scoreboard players add @s slf.stat.str 0
scoreboard players add @s slf.stat.dex 0
scoreboard players add @s slf.stat.vit 0
scoreboard players add @s slf.stat.agi 0
scoreboard players add @s slf.stat.tec 0
scoreboard players add @s slf.stat.lck 0
scoreboard players add @s slf.stat.stm 0
execute unless score @s slf.level matches 1.. run scoreboard players set @s slf.level 1
# Values that are normally worked out once per second: work them out now so a brand-new class shows them at once
function slf:stats/exp_next
execute unless score @s slf.mana_max matches 1.. run function slf:stats/apply_derived
