# Every second, as a player at step 3 of Red Hoods in the Reeds: when their wave is down, the next comes; after the
# second wave, the camp's banner is left for them to take.
execute if score @s slf.q.wave matches 3 run return 0
scoreboard players operation #me slf.pid = @s slf.pid
scoreboard players set #alive slf.tmp 0
execute as @e[tag=slf.camp_redcap] if score @s slf.pid = #me slf.pid run scoreboard players add #alive slf.tmp 1
execute if score #alive slf.tmp matches 1.. run return 0
scoreboard players add @s slf.q.wave 1
execute if score @s slf.q.wave matches 2 at @e[tag=slf.reeds_camp] if score @e[tag=slf.reeds_camp,limit=1,sort=nearest] slf.pid = #me slf.pid run function slf:quest/reeds/wave
execute if score @s slf.q.wave matches 2 run tellraw @s {"text":" A horn sounds from the reeds - a second wave!","color":"red"}
execute if score @s slf.q.wave matches 3 as @e[tag=slf.reeds_camp] if score @s slf.pid = #me slf.pid at @s run loot spawn ~ ~0.5 ~ loot slf:quest/sigil_banner
execute if score @s slf.q.wave matches 3 run tellraw @s {"text":" The camp is cleared. Their banner lies in the mud - an unfamiliar sigil. Take it to Halvor.","color":"yellow"}
