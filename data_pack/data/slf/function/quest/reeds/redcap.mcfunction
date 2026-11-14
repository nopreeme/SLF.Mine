function slf:mob/red_hat_goblin/convert
tag @s add slf.camp_redcap
tag @s add slf.called
data merge entity @s {PersistenceRequired:1b}
scoreboard players operation @s slf.pid = #me slf.pid
