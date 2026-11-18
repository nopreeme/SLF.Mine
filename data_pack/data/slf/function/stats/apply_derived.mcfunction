# Runs every 20t as each player with a class. HP -> max health, MP -> mana pool.

# HP: +1 max health (half a heart) per 2 points, capped at +40. Only touches the attribute when the value changes.
scoreboard players set #2 slf.tmp 2
scoreboard players set #10 slf.tmp 10
scoreboard players set #v slf.tmp 0
execute if score @s slf.stat.hp matches 1.. run scoreboard players operation #v slf.tmp = @s slf.stat.hp
scoreboard players operation #v slf.tmp /= #2 slf.tmp
execute if score #v slf.tmp matches 41.. run scoreboard players set #v slf.tmp 40
execute unless score @s slf.hp_applied = #v slf.tmp run function slf:stats/apply_hp

# MP: mana pool of 20 + 2 per point; regenerates 1 + (MP / 10) per second.
scoreboard players set #m slf.tmp 0
execute if score @s slf.stat.mp matches 1.. run scoreboard players operation #m slf.tmp = @s slf.stat.mp
scoreboard players operation #r slf.tmp = #m slf.tmp
scoreboard players operation #r slf.tmp /= #10 slf.tmp
scoreboard players add #r slf.tmp 1
scoreboard players operation #m slf.tmp *= #2 slf.tmp
scoreboard players add #m slf.tmp 20
# Skills that deepen the pool or speed up regeneration
function slf:skills/mana_bonus
scoreboard players operation @s slf.mana_max = #m slf.tmp
scoreboard players operation @s slf.mana += #r slf.tmp
execute if score @s slf.mana > @s slf.mana_max run scoreboard players operation @s slf.mana = @s slf.mana_max
execute if score @s slf.mana matches ..-1 run scoreboard players set @s slf.mana 0
