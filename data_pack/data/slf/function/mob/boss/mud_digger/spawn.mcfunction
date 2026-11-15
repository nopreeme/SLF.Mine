# Summons the Mud Digger here (admins and tests: /function slf:mob/boss/mud_digger/spawn). Only one exists at a time.
# Natural encounters: mob/boss/roll (swamps, players level 14-30).
execute if entity @e[tag=slf.mud_digger,limit=1] run return fail
execute summon minecraft:ravager run function slf:mob/boss/mud_digger/init
