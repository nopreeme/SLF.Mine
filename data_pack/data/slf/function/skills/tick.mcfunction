# --- Class selection trigger handler ---
execute as @a[scores={slf.choose_class=1}] run function slf:class/grant/swordsman
execute as @a[scores={slf.choose_class=2}] run function slf:class/grant/warrior
execute as @a[scores={slf.choose_class=3}] run function slf:class/grant/thief
execute as @a[scores={slf.choose_class=4}] run function slf:class/grant/priest
execute as @a[scores={slf.choose_class=5}] run function slf:class/grant/monk
execute as @a[scores={slf.choose_class=6}] run function slf:class/grant/mage
execute as @a[scores={slf.choose_class=20}] run function slf:class/grant/fighter
execute as @a[scores={slf.choose_class=30}] run function slf:class/grant/mercenary
scoreboard players reset @a[scores={slf.choose_class=1..}] slf.choose_class
scoreboard players enable @a[tag=!slf.class_chosen] slf.choose_class

# --- Passive skill effects (every 20 ticks) ---
scoreboard players add #timer slf.timer 1
execute if score #timer slf.timer matches 20.. run function slf:skills/passives
execute if score #timer slf.timer matches 20.. run scoreboard players set #timer slf.timer 0
