scoreboard players set @s slf.q.miner 3
scoreboard players add @s slf.exp 300
scoreboard players add @s slf.mahni 100
give @s minecraft:iron_pickaxe[minecraft:item_name={text:"Iron Pickaxe (Reinforced)",color:"aqua",italic:false},minecraft:enchantments={"minecraft:efficiency":2,"minecraft:unbreaking":2}] 1
scoreboard players operation #me slf.pid = @s slf.pid
execute as @e[tag=slf.miner_site] if score @s slf.pid = #me slf.pid run kill @s
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"(reads the last page, and goes quiet) ...Red hoods. Watching. Take this to Halvor - now. Keep the pickaxe; Tomic would want it used.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"The Missing Miner","color":"gold","bold":true},{"text":"  +300 EXP, +100 Mahni, Iron Pickaxe (Reinforced), Tomic's Journal","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
scoreboard players enable @s slf.quest
tellraw @s ["",{"text":" Garren's quest: ","color":"gray"},{"text":"Red Hoods in the Reeds","color":"gold","bold":true},{"text":"  Show Tomic's journal to Guard Halvor, then lead a patrol into the marsh at nightfall.  ","color":"gray"},{"text":"Reward: 400 EXP, Unknown Sigil Banner, Redcap Iron Axe, 125 Mahni  ","color":"dark_gray"},{"text":"[Accept]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.quest set 17"},"hover_event":{"action":"show_text","value":"Accept \"Red Hoods in the Reeds\""}}]
