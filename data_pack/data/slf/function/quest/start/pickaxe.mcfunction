scoreboard players set @s slf.q.pickaxe 1
give @s minecraft:iron_pickaxe[minecraft:item_name={text:"Garren's Iron Pickaxe",color:"white",italic:false},minecraft:lore=[{text:"On loan. Bring back ore.",color:"gray",italic:true}]] 1
tellraw @s ["",{"text":"[Garren] ","color":"gold"},{"text":"The marsh traps your legs - one foot's always stuck till the other finds solid ground. Fight carefully. And be back before dusk.","color":"white"}]
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.4 1.6
