tag @s remove slf.wandering
tellraw @s {"text":" The dream can't touch you now. Secondil remembers you.","color":"dark_green","italic":true}
execute if entity @s[tag=slf.slew_snake] run tag @s add slf.first_survivor
execute if entity @s[tag=slf.first_survivor] run tellraw @s ["",{"text":" First Survivor: ","color":"gold","bold":true},{"text":"you crossed the forest alone, killed the Ravenous Snake and reached Secondil. Some people here will see it on you.","color":"yellow"}]
