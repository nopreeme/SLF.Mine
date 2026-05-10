execute unless entity @s[tag=slf.was_barbarian] run return fail
scoreboard players set @s slf.class 15
tag @s add slf.was_war_king
tag @s add slf.skill.terraton_corapsa
tag @s add slf.skill.break_attack
tag @s add slf.skill.tsujizanri
tellraw @s {"text":"You have become a War King.","color":"red","bold":true}
