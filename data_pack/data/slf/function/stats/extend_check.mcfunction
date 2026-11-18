# Runs as a player who just killed a monster whose level is in #dying_mob_lv. At level 99, a level 100+ kill reaches
# 99 Extend (series: the level cap waits to be released, and EXP is banked for the Altar of Awakening).
execute unless score @s slf.level matches 99 run return 0
execute if score @s slf.awakened matches 1 run return 0
execute if score @s slf.standby matches 1 run return 0
execute unless score #dying_mob_lv slf.mob_level matches 100.. run return 0
scoreboard players set @s slf.standby 1
