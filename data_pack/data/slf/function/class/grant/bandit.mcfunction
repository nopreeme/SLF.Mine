execute unless entity @s[tag=slf.was_thief] run return fail
scoreboard players set @s slf.class 50
tag @s add slf.was_bandit
tag @s add slf.skill.dirty_sword
tag @s add slf.skill.assassin_pierce
tag @s add slf.skill.big_tantrum
tellraw @s {"text":"You have become a Bandit.","color":"dark_green","bold":true}
