# Toggle Big Tantrum (大癇癪). Runs as the player (menu option 8). Series: it draws other monsters to you.
execute unless entity @s[tag=slf.skill.big_tantrum] run return run tellraw @s {"text":"You have not learned Big Tantrum.","color":"red"}
execute if entity @s[tag=slf.tantrum_active] run return run function slf:skills/tantrum_end
tag @s add slf.tantrum_active
playsound minecraft:entity.ravager.roar player @s
tellraw @s ["",{"text":"Big Tantrum! ","color":"red","bold":true},{"text":"Every monster nearby can hear you. Toggle it again to calm down.","color":"yellow"}]
