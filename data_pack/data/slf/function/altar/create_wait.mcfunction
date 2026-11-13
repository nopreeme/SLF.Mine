scoreboard players add #altar_tries slf.timer 1
execute if score #altar_tries slf.timer matches ..60 run return run schedule function slf:altar/create_try 20t
scoreboard players set #altar_pending slf.timer 0
tellraw @a[scores={slf.standby=1}] {"text":"[SLF] The Altar of Awakening could not rise. Ask an admin to place one with /function slf:altar/place.","color":"red"}
