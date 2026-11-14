# Runs as a player whose slf.evolve trigger is set to a class id. Checks the level requirement and
# lineage, then hands over to the normal grant function. Level requirements live here and nowhere else.
scoreboard players operation #id slf.tmp = @s slf.evolve
scoreboard players reset @s slf.evolve
execute unless entity @s[tag=slf.class_chosen] run return fail
# Sword Master (10)
execute if score #id slf.tmp matches 10 if score @s slf.class matches 10 run return run tellraw @s {"text":"You are already a Sword Master.","color":"yellow"}
execute if score #id slf.tmp matches 10 unless entity @s[tag=slf.was_swordsman] run return run tellraw @s {"text":"Sword Master is not on your path. It evolves from Swordsman.","color":"red"}
execute if score #id slf.tmp matches 10 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Sword Master requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 10 run return run function slf:class/grant/sword_master
# Magic Swordsman (11)
execute if score #id slf.tmp matches 11 if score @s slf.class matches 11 run return run tellraw @s {"text":"You are already a Magic Swordsman.","color":"yellow"}
execute if score #id slf.tmp matches 11 unless entity @s[tag=slf.was_swordsman] run return run tellraw @s {"text":"Magic Swordsman is not on your path. It evolves from Swordsman.","color":"red"}
execute if score #id slf.tmp matches 11 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Magic Swordsman requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 11 run return run function slf:class/grant/magic_swordsman
# Barbarian (14)
execute if score #id slf.tmp matches 14 if score @s slf.class matches 14 run return run tellraw @s {"text":"You are already a Barbarian.","color":"yellow"}
execute if score #id slf.tmp matches 14 unless entity @s[tag=slf.was_warrior] unless entity @s[tag=slf.was_fighter] run return run tellraw @s {"text":"Barbarian is not on your path. It evolves from Warrior or Fighter.","color":"red"}
execute if score #id slf.tmp matches 14 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Barbarian requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 14 run return run function slf:class/grant/barbarian
# Destroyer (21)
execute if score #id slf.tmp matches 21 if score @s slf.class matches 21 run return run tellraw @s {"text":"You are already a Destroyer.","color":"yellow"}
execute if score #id slf.tmp matches 21 unless entity @s[tag=slf.was_fighter] run return run tellraw @s {"text":"Destroyer is not on your path. It evolves from Fighter.","color":"red"}
execute if score #id slf.tmp matches 21 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Destroyer requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 21 run return run function slf:class/grant/destroyer
# Veteran (31)
execute if score #id slf.tmp matches 31 if score @s slf.class matches 31 run return run tellraw @s {"text":"You are already a Veteran.","color":"yellow"}
execute if score #id slf.tmp matches 31 unless entity @s[tag=slf.was_mercenary] run return run tellraw @s {"text":"Veteran is not on your path. It evolves from Mercenary.","color":"red"}
execute if score #id slf.tmp matches 31 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Veteran requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 31 run return run function slf:class/grant/veteran
# Thief (50)
execute if score #id slf.tmp matches 50 if score @s slf.class matches 50 run return run tellraw @s {"text":"You are already a Thief.","color":"yellow"}
execute if score #id slf.tmp matches 50 unless entity @s[tag=slf.was_bandit] run return run tellraw @s {"text":"Thief is not on your path. It evolves from Bandit.","color":"red"}
execute if score #id slf.tmp matches 50 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Thief requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 50 run return run function slf:class/grant/thief
# Ninja (51)
execute if score #id slf.tmp matches 51 if score @s slf.class matches 51 run return run tellraw @s {"text":"You are already a Ninja.","color":"yellow"}
execute if score #id slf.tmp matches 51 unless entity @s[tag=slf.was_bandit] run return run tellraw @s {"text":"Ninja is not on your path. It evolves from Bandit.","color":"red"}
execute if score #id slf.tmp matches 51 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Ninja requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 51 run return run function slf:class/grant/ninja
# Bishop (18)
execute if score #id slf.tmp matches 18 if score @s slf.class matches 18 run return run tellraw @s {"text":"You are already a Bishop.","color":"yellow"}
execute if score #id slf.tmp matches 18 unless entity @s[tag=slf.was_priest] run return run tellraw @s {"text":"Bishop is not on your path. It evolves from Priest.","color":"red"}
execute if score #id slf.tmp matches 18 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Bishop requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 18 run return run function slf:class/grant/bishop
# Monk Soldier (60)
execute if score #id slf.tmp matches 60 if score @s slf.class matches 60 run return run tellraw @s {"text":"You are already a Monk Soldier.","color":"yellow"}
execute if score #id slf.tmp matches 60 unless entity @s[tag=slf.was_monk] run return run tellraw @s {"text":"Monk Soldier is not on your path. It evolves from Monk.","color":"red"}
execute if score #id slf.tmp matches 60 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Monk Soldier requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 60 run return run function slf:class/grant/monk_soldier
# Sage (70)
execute if score #id slf.tmp matches 70 if score @s slf.class matches 70 run return run tellraw @s {"text":"You are already a Sage.","color":"yellow"}
execute if score #id slf.tmp matches 70 unless entity @s[tag=slf.was_mage] run return run tellraw @s {"text":"Sage is not on your path. It evolves from Mage.","color":"red"}
execute if score #id slf.tmp matches 70 unless score @s slf.level matches 20.. run return run tellraw @s ["",{"text":"Sage requires level 20. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 70 run return run function slf:class/grant/sage
# Knight (40)
execute if score #id slf.tmp matches 40 if score @s slf.class matches 40 run return run tellraw @s {"text":"You are already a Knight.","color":"yellow"}
execute if score #id slf.tmp matches 40 unless entity @s[tag=slf.was_sword_master] unless entity @s[tag=slf.was_magic_swordsman] unless entity @s[tag=slf.was_barbarian] run return run tellraw @s {"text":"Knight is not on your path. It evolves from Sword Master or Magic Swordsman or Barbarian.","color":"red"}
execute if score #id slf.tmp matches 40 unless score @s slf.level matches 30.. run return run tellraw @s ["",{"text":"Knight requires level 30. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 40 run return run function slf:class/grant/knight
# Kansei (12)
execute if score #id slf.tmp matches 12 if score @s slf.class matches 12 run return run tellraw @s {"text":"You are already a Kansei.","color":"yellow"}
execute if score #id slf.tmp matches 12 unless entity @s[tag=slf.was_sword_master] run return run tellraw @s {"text":"Kansei is not on your path. It evolves from Sword Master.","color":"red"}
execute if score #id slf.tmp matches 12 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Kansei requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 12 run return run function slf:class/grant/kansei
# Mysterious Sword user (13)
execute if score #id slf.tmp matches 13 if score @s slf.class matches 13 run return run tellraw @s {"text":"You are already a Mysterious Sword user.","color":"yellow"}
execute if score #id slf.tmp matches 13 unless entity @s[tag=slf.was_magic_swordsman] run return run tellraw @s {"text":"Mysterious Sword user is not on your path. It evolves from Magic Swordsman.","color":"red"}
execute if score #id slf.tmp matches 13 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Mysterious Sword user requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 13 run return run function slf:class/grant/mysterious_sword
# War King (15)
execute if score #id slf.tmp matches 15 if score @s slf.class matches 15 run return run tellraw @s {"text":"You are already a War King.","color":"yellow"}
execute if score #id slf.tmp matches 15 unless entity @s[tag=slf.was_barbarian] run return run tellraw @s {"text":"War King is not on your path. It evolves from Barbarian.","color":"red"}
execute if score #id slf.tmp matches 15 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"War King requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 15 run return run function slf:class/grant/war_king
# Crazy Fist (22)
execute if score #id slf.tmp matches 22 if score @s slf.class matches 22 run return run tellraw @s {"text":"You are already a Crazy Fist.","color":"yellow"}
execute if score #id slf.tmp matches 22 unless entity @s[tag=slf.was_destroyer] run return run tellraw @s {"text":"Crazy Fist is not on your path. It evolves from Destroyer.","color":"red"}
execute if score #id slf.tmp matches 22 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Crazy Fist requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 22 run return run function slf:class/grant/crazy_fist
# Assassin (16)
execute if score #id slf.tmp matches 16 if score @s slf.class matches 16 run return run tellraw @s {"text":"You are already an Assassin.","color":"yellow"}
execute if score #id slf.tmp matches 16 unless entity @s[tag=slf.was_thief] run return run tellraw @s {"text":"Assassin is not on your path. It evolves from Thief.","color":"red"}
execute if score #id slf.tmp matches 16 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Assassin requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 16 run return run function slf:class/grant/assassin
# Shinobi (52)
execute if score #id slf.tmp matches 52 if score @s slf.class matches 52 run return run tellraw @s {"text":"You are already a Shinobi.","color":"yellow"}
execute if score #id slf.tmp matches 52 unless entity @s[tag=slf.was_ninja] run return run tellraw @s {"text":"Shinobi is not on your path. It evolves from Ninja.","color":"red"}
execute if score #id slf.tmp matches 52 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Shinobi requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 52 run return run function slf:class/grant/shinobi
# Saint (19)
execute if score #id slf.tmp matches 19 if score @s slf.class matches 19 run return run tellraw @s {"text":"You are already a Saint.","color":"yellow"}
execute if score #id slf.tmp matches 19 unless entity @s[tag=slf.was_bishop] run return run tellraw @s {"text":"Saint is not on your path. It evolves from Bishop.","color":"red"}
execute if score #id slf.tmp matches 19 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Saint requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 19 run return run function slf:class/grant/saint
# Spirit Fist (61)
execute if score #id slf.tmp matches 61 if score @s slf.class matches 61 run return run tellraw @s {"text":"You are already a Spirit Fist.","color":"yellow"}
execute if score #id slf.tmp matches 61 unless entity @s[tag=slf.was_monk_soldier] run return run tellraw @s {"text":"Spirit Fist is not on your path. It evolves from Monk Soldier.","color":"red"}
execute if score #id slf.tmp matches 61 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Spirit Fist requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 61 run return run function slf:class/grant/spirit_fist
# Omnipotent Wisdom (62)
execute if score #id slf.tmp matches 62 if score @s slf.class matches 62 run return run tellraw @s {"text":"You are already an Omnipotent Wisdom.","color":"yellow"}
execute if score #id slf.tmp matches 62 unless entity @s[tag=slf.was_sage] run return run tellraw @s {"text":"Omnipotent Wisdom is not on your path. It evolves from Sage.","color":"red"}
execute if score #id slf.tmp matches 62 unless score @s slf.level matches 50.. run return run tellraw @s ["",{"text":"Omnipotent Wisdom requires level 50. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 62 run return run function slf:class/grant/omnipotent_wisdom
# King's Knight (43)
execute if score #id slf.tmp matches 43 if score @s slf.class matches 43 run return run tellraw @s {"text":"You are already a King's Knight.","color":"yellow"}
execute if score #id slf.tmp matches 43 unless entity @s[tag=slf.was_holy_knight] run return run tellraw @s {"text":"King's Knight is not on your path. It evolves from Holy Knight.","color":"red"}
execute if score #id slf.tmp matches 43 unless score @s slf.level matches 70.. run return run tellraw @s ["",{"text":"King's Knight requires level 70. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 43 run return run function slf:class/grant/kings_knight
# Black Death (44)
execute if score #id slf.tmp matches 44 if score @s slf.class matches 44 run return run tellraw @s {"text":"You are already a Black Death.","color":"yellow"}
execute if score #id slf.tmp matches 44 unless entity @s[tag=slf.was_dark_knight] run return run tellraw @s {"text":"Black Death is not on your path. It evolves from Dark Knight.","color":"red"}
execute if score #id slf.tmp matches 44 unless score @s slf.level matches 70.. run return run tellraw @s ["",{"text":"Black Death requires level 70. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 44 run return run function slf:class/grant/black_death
# Killing Joke (17)
execute if score #id slf.tmp matches 17 if score @s slf.class matches 17 run return run tellraw @s {"text":"You are already a Killing Joke.","color":"yellow"}
execute if score #id slf.tmp matches 17 unless entity @s[tag=slf.was_assassin] run return run tellraw @s {"text":"Killing Joke is not on your path. It evolves from Assassin.","color":"red"}
execute if score #id slf.tmp matches 17 unless score @s slf.level matches 80.. run return run tellraw @s ["",{"text":"Killing Joke requires level 80. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 17 run return run function slf:class/grant/killing_joke
# Star Shinobi Sei (53)
execute if score #id slf.tmp matches 53 if score @s slf.class matches 53 run return run tellraw @s {"text":"You are already a Star Shinobi Sei.","color":"yellow"}
execute if score #id slf.tmp matches 53 unless entity @s[tag=slf.was_shinobi] run return run tellraw @s {"text":"Star Shinobi Sei is not on your path. It evolves from Shinobi.","color":"red"}
execute if score #id slf.tmp matches 53 unless score @s slf.level matches 80.. run return run tellraw @s ["",{"text":"Star Shinobi Sei requires level 80. You are level ","color":"red"},{"score":{"name":"@s","objective":"slf.level"},"color":"white"},{"text":".","color":"red"}]
execute if score #id slf.tmp matches 53 run return run function slf:class/grant/star_shinobi_sei
tellraw @s {"text":"That class cannot be chosen here.","color":"red"}
