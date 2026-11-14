# Runs as a player on watch who hit a Redcap: the watch starts over ("eyes, not soldiers").
scoreboard players set @s slf.q.watch 1
scoreboard players set @s slf.q.watch_t 0
tellraw @s {"text":" You engaged! Halvor wanted eyes, not swords. The watch starts over.","color":"red"}
tag @s remove slf.watch_sighted
