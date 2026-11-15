scoreboard players set @s slf.q.serpent 2
scoreboard players add @s slf.exp 50
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"So the farmer told you. He's right to be afraid: an Area Boss - the Ravenous Snake - has claimed the bridge to Secondil.","color":"white"}]
tellraw @s ["",{"text":"[Guard Captain] ","color":"aqua"},{"text":"It doesn't kill with its fangs. Its tail spits poison brewed from every toxic plant it eats, and it stays in your blood.","color":"white"}]
tellraw @s ["",{"text":"✔ Quest complete: ","color":"green"},{"text":"The Serpent's Shadow","color":"gold","bold":true},{"text":"  +50 EXP","color":"yellow"}]
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
scoreboard players enable @s slf.quest
tellraw @s ["",{"text":" Main quest: ","color":"gray"},{"text":"The Rampant Forest Guardian","color":"gold","bold":true},{"text":"  Defeat the Ravenous Snake. Recommended: level 10, a party of three.  ","color":"gray"},{"text":"Reward: 300 EXP, Devourer's Scale, Python White Hair, 100 Mahni  ","color":"dark_gray"},{"text":"[Accept]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger slf.quest set 6"},"hover_event":{"action":"show_text","value":"Accept \"The Rampant Forest Guardian\""}}]
