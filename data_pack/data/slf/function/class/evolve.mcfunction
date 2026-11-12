# Class evolution menu. Runs as the player. Shows every evolution open to their lineage;
# requirements are enforced in class/evolve_apply (level) and class/grant/* (lineage).
execute unless entity @s[tag=slf.class_chosen] run return run function slf:class/select
scoreboard players enable @s slf.evolve
tellraw @s ["",{"text":"━━━ ","color":"dark_gray"},{"text":"Class Evolution","color":"gold","bold":true},{"text":" ━━━","color":"dark_gray"},{"text":"\nYour level: ","color":"gray"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"}]
scoreboard players set #shown slf.tmp 0
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_swordsman] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 10 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Sword Master]","color":"aqua","click_event":{"action":"run_command","command":"trigger slf.evolve set 10"},"hover_event":{"action":"show_text","value":"From Swordsman — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_swordsman] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 11 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Magic Swordsman]","color":"aqua","click_event":{"action":"run_command","command":"trigger slf.evolve set 11"},"hover_event":{"action":"show_text","value":"From Swordsman — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_warrior] run scoreboard players set #ok slf.tmp 1
execute if entity @s[tag=slf.was_fighter] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 14 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Barbarian]","color":"red","click_event":{"action":"run_command","command":"trigger slf.evolve set 14"},"hover_event":{"action":"show_text","value":"From Warrior or Fighter — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_fighter] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 21 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Destroyer]","color":"dark_red","click_event":{"action":"run_command","command":"trigger slf.evolve set 21"},"hover_event":{"action":"show_text","value":"From Fighter — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_mercenary] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 31 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Veteran]","color":"dark_green","click_event":{"action":"run_command","command":"trigger slf.evolve set 31"},"hover_event":{"action":"show_text","value":"From Mercenary — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_bandit] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 50 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Thief]","color":"dark_green","click_event":{"action":"run_command","command":"trigger slf.evolve set 50"},"hover_event":{"action":"show_text","value":"From Bandit — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_bandit] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 51 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Ninja]","color":"dark_green","click_event":{"action":"run_command","command":"trigger slf.evolve set 51"},"hover_event":{"action":"show_text","value":"From Bandit — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_priest] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 18 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Bishop]","color":"white","click_event":{"action":"run_command","command":"trigger slf.evolve set 18"},"hover_event":{"action":"show_text","value":"From Priest — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_monk] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 60 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Monk Soldier]","color":"dark_purple","click_event":{"action":"run_command","command":"trigger slf.evolve set 60"},"hover_event":{"action":"show_text","value":"From Monk — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_mage] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 70 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Sage]","color":"blue","click_event":{"action":"run_command","command":"trigger slf.evolve set 70"},"hover_event":{"action":"show_text","value":"From Mage — requires level 20"}},{"text":"  level 20+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_sword_master] run scoreboard players set #ok slf.tmp 1
execute if entity @s[tag=slf.was_magic_swordsman] run scoreboard players set #ok slf.tmp 1
execute if entity @s[tag=slf.was_barbarian] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 40 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Knight]","color":"gold","click_event":{"action":"run_command","command":"trigger slf.evolve set 40"},"hover_event":{"action":"show_text","value":"From Sword Master or Magic Swordsman or Barbarian — requires level 30"}},{"text":"  level 30+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_sword_master] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 12 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Kansei]","color":"aqua","click_event":{"action":"run_command","command":"trigger slf.evolve set 12"},"hover_event":{"action":"show_text","value":"From Sword Master — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_magic_swordsman] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 13 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Mysterious Sword user]","color":"aqua","click_event":{"action":"run_command","command":"trigger slf.evolve set 13"},"hover_event":{"action":"show_text","value":"From Magic Swordsman — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_barbarian] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 15 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[War King]","color":"red","click_event":{"action":"run_command","command":"trigger slf.evolve set 15"},"hover_event":{"action":"show_text","value":"From Barbarian — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_destroyer] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 22 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Crazy Fist]","color":"dark_red","click_event":{"action":"run_command","command":"trigger slf.evolve set 22"},"hover_event":{"action":"show_text","value":"From Destroyer — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_thief] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 16 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Assassin]","color":"dark_green","click_event":{"action":"run_command","command":"trigger slf.evolve set 16"},"hover_event":{"action":"show_text","value":"From Thief — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_ninja] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 52 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Shinobi]","color":"dark_green","click_event":{"action":"run_command","command":"trigger slf.evolve set 52"},"hover_event":{"action":"show_text","value":"From Ninja — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_bishop] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 19 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Saint]","color":"white","click_event":{"action":"run_command","command":"trigger slf.evolve set 19"},"hover_event":{"action":"show_text","value":"From Bishop — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_monk_soldier] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 61 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Spirit Fist]","color":"dark_purple","click_event":{"action":"run_command","command":"trigger slf.evolve set 61"},"hover_event":{"action":"show_text","value":"From Monk Soldier — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_sage] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 62 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Omnipotent Wisdom]","color":"blue","click_event":{"action":"run_command","command":"trigger slf.evolve set 62"},"hover_event":{"action":"show_text","value":"From Sage — requires level 50"}},{"text":"  level 50+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_holy_knight] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 43 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[King's Knight]","color":"gold","click_event":{"action":"run_command","command":"trigger slf.evolve set 43"},"hover_event":{"action":"show_text","value":"From Holy Knight — requires level 70"}},{"text":"  level 70+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_dark_knight] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 44 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Black Death]","color":"dark_gray","click_event":{"action":"run_command","command":"trigger slf.evolve set 44"},"hover_event":{"action":"show_text","value":"From Dark Knight — requires level 70"}},{"text":"  level 70+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_assassin] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 17 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Killing Joke]","color":"dark_green","click_event":{"action":"run_command","command":"trigger slf.evolve set 17"},"hover_event":{"action":"show_text","value":"From Assassin — requires level 80"}},{"text":"  level 80+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
scoreboard players set #ok slf.tmp 0
execute if entity @s[tag=slf.was_shinobi] run scoreboard players set #ok slf.tmp 1
execute if score @s slf.class matches 53 run scoreboard players set #ok slf.tmp 0
execute if score #ok slf.tmp matches 1 run tellraw @s [" ",{"text":"[Star Shinobi Sei]","color":"light_purple","click_event":{"action":"run_command","command":"trigger slf.evolve set 53"},"hover_event":{"action":"show_text","value":"From Shinobi — requires level 80"}},{"text":"  level 80+","color":"gray"}]
execute if score #ok slf.tmp matches 1 run scoreboard players set #shown slf.tmp 1
# Knights pick Holy or Dark through the trials, not from this list
execute if entity @s[tag=slf.was_knight,tag=!slf.was_holy_knight,tag=!slf.was_dark_knight] run tellraw @s ["",{"text":" Knight Trials: ","color":"gold"},{"score":{"name":"@s","objective":"slf.knight_trials"},"color":"white"},{"text":"/3","color":"gray"},{"text":"  — defeat elite monsters as a Knight to earn your alignment.","color":"gray"}]
execute if entity @s[tag=slf.was_knight,tag=!slf.was_holy_knight,tag=!slf.was_dark_knight] run scoreboard players set #shown slf.tmp 1
execute if score #shown slf.tmp matches 0 run tellraw @s {"text":" Your current path has no further evolution.","color":"gray"}
tellraw @s ["",{"text":"[Back]","color":"dark_gray","click_event":{"action":"run_command","command":"trigger slf.menu set 1"},"hover_event":{"action":"show_text","value":"Main menu"}}]
