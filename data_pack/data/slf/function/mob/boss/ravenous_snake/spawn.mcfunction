# Summons the Ravenous Snake here (admins and tests: /function slf:mob/boss/ravenous_snake/spawn). Only one exists at a time.
# Natural encounters: mob/boss/roll (forests, players level 8-25).
execute if entity @e[tag=slf.snake,limit=1] run return fail
execute summon minecraft:ravager run function slf:mob/boss/ravenous_snake/init
