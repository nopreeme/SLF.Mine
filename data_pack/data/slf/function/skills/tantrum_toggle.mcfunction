# Toggle Big / Grand Tantrum. Runs as the player (menu option 8). Costs mana: 10 to start, 3 per second after.
execute unless entity @s[tag=slf.skill.big_tantrum] unless entity @s[tag=slf.skill.grand_tantrum] run return run tellraw @s {"text":"You have not learned a Tantrum skill.","color":"red"}
execute if entity @s[tag=slf.tantrum_active] run return run function slf:skills/tantrum_end
execute unless score @s slf.mana matches 10.. run return run tellraw @s ["",{"text":"Not enough mana. Tantrum needs 10, you have ","color":"red"},{"score":{"name":"@s","objective":"slf.mana"},"color":"white"},{"text":".","color":"red"}]
scoreboard players remove @s slf.mana 10
tag @s add slf.tantrum_active
playsound minecraft:entity.ravager.roar player @s
tellraw @s ["",{"text":"Tantrum! ","color":"red","bold":true},{"text":"Every enemy can see you. Kills now count toward Grand Tantrum.","color":"yellow"}]
