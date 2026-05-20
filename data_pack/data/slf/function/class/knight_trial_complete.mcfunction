# Call this function when a Knight player completes a trial step
# (wire to quest advancement rewards or NPC interaction)
execute unless entity @s[tag=slf.was_knight] run return fail
execute if score @s slf.knight_trials >= 3 run return fail
scoreboard players add @s slf.knight_trials 1
tellraw @s ["",{"text":"Knight Trial complete. ","color":"gold"},{"score":{"name":"@s","objective":"slf.knight_trials"},"color":"white"},{"text":"/3","color":"gray"}]
execute if score @s slf.knight_trials >= 3 run tellraw @s {"text":"All trials complete. Your alignment awaits.","color":"gold","bold":true}
