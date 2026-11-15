scoreboard players set @s slf.q.herd 2
scoreboard players add @s slf.exp 120
scoreboard players add @s slf.mahni 30
give @s minecraft:milk_bucket[minecraft:item_name={text:"Fresh Milk Bundle",color:"white",italic:false}] 1
scoreboard players operation #me slf.pid = @s slf.pid
execute as @e[tag=slf.herd] if score @s slf.pid = #me slf.pid run data remove entity @s CustomName
execute as @e[tag=slf.herd] if score @s slf.pid = #me slf.pid run tag @s remove slf.herd
execute as @e[tag=slf.npc.daughter] if score @s slf.pid = #me slf.pid run kill @s
tellraw @s ["",{"text":"[Distressed Farmer] ","color":"yellow"},{"text":"My girl - and my cattle! Pioneer, take this, it's the best we have.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"The Missing Herd","color":"gold","bold":true},{"text":"  +120 EXP, +30 Mahni, Fresh Milk Bundle","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
function slf:npc/farmer_serpent
