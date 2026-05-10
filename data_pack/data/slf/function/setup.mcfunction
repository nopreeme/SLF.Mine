# SLF.Mine — runs on world load
scoreboard objectives add slf.class dummy "Class"
scoreboard objectives add slf.kills playerKillCount "Kills"
scoreboard objectives add slf.choose_class trigger "Choose Class"
scoreboard objectives add slf.dmg_taken stat minecraft.custom:minecraft.damage_taken
scoreboard objectives add slf.dmg_prev dummy
scoreboard objectives add slf.hp dummy
scoreboard objectives add slf.timer dummy
tellraw @a[gamemode=creative] {"text":"[SLF] Shangri-La Frontier pack loaded.","color":"gold"}
