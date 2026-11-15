scoreboard players set @s slf.q.watch 3
scoreboard players add @s slf.exp 125
scoreboard players add @s slf.mahni 40
tag @s add slf.garren_quest_unlocked
give @s minecraft:leather_chestplate[minecraft:dyed_color=4876170,minecraft:item_name={text:"Guard Issue Cloak",color:"aqua",italic:false}] 1
scoreboard players operation #me slf.pid = @s slf.pid
execute as @e[tag=slf.sighting] if score @s slf.pid = #me slf.pid run kill @s
tellraw @s ["",{"text":"[Guard Halvor] ","color":"aqua"},{"text":"Red hoods. Iron. Watching the city... That's no ordinary goblin. Take this cloak, and go see Garren - he'll want to know.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"The Night Watch","color":"gold","bold":true},{"text":"  +125 EXP, +40 Mahni, Guard Issue Cloak, Garren's first quest unlocked","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
tag @s remove slf.watch_sighted
