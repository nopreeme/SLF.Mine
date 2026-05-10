# Runs as the killing player; #dying_mob_lv is set by the mob's own death function
# before calling this. If mob level >= player level + 20, increment vorpal_soul.
scoreboard players operation #req_lv slf.tmp = @s slf.level
scoreboard players add #req_lv slf.tmp 20
execute if score #dying_mob_lv slf.mob_level >= #req_lv slf.tmp run scoreboard players add @s slf.vorpal_soul 1
