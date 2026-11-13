# Every 20 ticks (mob/tick).
# Lycagon stays angry at the nearest player (a wolf is otherwise neutral).
execute as @e[tag=slf.boss_lycagon] at @s run function slf:mob/boss/lycagon/hunt
# Night bosses leave at dawn, without dropping anything. Only after they have seen a night, so one an admin
# spawns by day stays until the next morning.
execute if predicate slf:night run tag @e[tag=slf.night_boss] add slf.saw_night
execute unless predicate slf:night as @e[tag=slf.night_boss,tag=slf.saw_night] at @s run function slf:mob/boss/depart
# Hide the bar of any boss that is gone.
execute unless entity @e[tag=slf.boss_nightclaw] run bossbar set slf:nightclaw visible false
execute unless entity @e[tag=slf.boss_bilac] run bossbar set slf:bilac visible false
execute unless entity @e[tag=slf.boss_oriana] run bossbar set slf:oriana visible false
execute unless entity @e[tag=slf.boss_lycagon] run bossbar set slf:lycagon visible false
execute unless entity @e[tag=slf.boss_wethermon] run bossbar set slf:wethermon visible false
