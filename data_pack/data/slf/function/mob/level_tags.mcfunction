# Runs as an SLF mob. Writes slf.mob_level onto the mob as tags slf.lvb0..slf.lvb7 (its bits, 0-255).
# A dead mob can't be selected by @e, so the kill advancements (advancement/mob/lv_bit*) read these tags off the
# dying mob and each add their bit to the killer's slf.kill_lv. See mob/kill_process.
scoreboard players operation #lv slf.tmp = @s slf.mob_level
scoreboard players set #2 slf.tmp 2
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb0
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb1
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb2
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb3
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb4
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb5
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb6
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
scoreboard players operation #bit slf.tmp = #lv slf.tmp
scoreboard players operation #bit slf.tmp %= #2 slf.tmp
execute if score #bit slf.tmp matches 1 run tag @s add slf.lvb7
scoreboard players operation #lv slf.tmp /= #2 slf.tmp
