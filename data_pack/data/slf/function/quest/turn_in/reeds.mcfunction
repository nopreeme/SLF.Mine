scoreboard players set @s slf.q.reeds 4
scoreboard players add @s slf.exp 400
scoreboard players add @s slf.mahni 125
give @s minecraft:iron_axe[minecraft:item_name={text:"Redcap Iron Axe",color:"red",italic:false},minecraft:lore=[{text:"Forged iron. Someone is teaching them.",color:"gray",italic:true}]] 1
scoreboard players operation #me slf.pid = @s slf.pid
execute as @e[tag=slf.patrol] if score @s slf.pid = #me slf.pid run tp @s ~ -400 ~
execute as @e[tag=slf.reeds_camp] if score @s slf.pid = #me slf.pid run kill @s
tellraw @s ["",{"text":"[Guard Halvor] ","color":"aqua"},{"text":"Forged tools, a banner, waves that come on a horn... that's no goblin rabble. Keep the banner - nobody here knows that sigil. Garren thinks Thirdrema might.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"Red Hoods in the Reeds","color":"gold","bold":true},{"text":"  +400 EXP, +125 Mahni, Redcap Iron Axe; keep the Unknown Sigil Banner","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
