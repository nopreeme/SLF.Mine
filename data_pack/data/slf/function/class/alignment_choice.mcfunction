execute if entity @s[tag=slf.alignment_offered] run return fail
tag @s add slf.alignment_offered
scoreboard players enable @s slf.choose_class
tellraw @s ["",{"text":"━━━ ","color":"dark_gray"},{"text":"Choose Your Path","color":"gold","bold":true},{"text":" ━━━","color":"dark_gray"},{"text":"\n"},{"text":"[Swear to the Light — Holy Knight]","color":"yellow","bold":true,"click_event":{"action":"run_command","command":"trigger slf.choose_class set 41"},"hover_event":{"action":"show_text","value":"Parry mastery and stamina arts"}},{"text":" "},{"text":"[Embrace the Dark — Dark Knight]","color":"dark_gray","bold":true,"click_event":{"action":"run_command","command":"trigger slf.choose_class set 42"},"hover_event":{"action":"show_text","value":"Self-harm, blood war, and death arts"}}]
