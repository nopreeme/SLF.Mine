# Every tick while a boss exists (skills/tick): each boss bar follows its boss's health, shown to players within 64 blocks.
execute as @e[tag=slf.boss_nightclaw,limit=1] at @s run function slf:mob/boss/bar {id:"nightclaw"}
execute as @e[tag=slf.boss_bilac,limit=1] at @s run function slf:mob/boss/bar {id:"bilac"}
execute as @e[tag=slf.boss_oriana,limit=1] at @s run function slf:mob/boss/bar {id:"oriana"}
execute as @e[tag=slf.boss_lycagon,limit=1] at @s run function slf:mob/boss/bar {id:"lycagon"}
execute as @e[tag=slf.boss_wethermon,limit=1] at @s run function slf:mob/boss/bar {id:"wethermon"}
execute as @e[tag=slf.boss_ctarnidd,limit=1] at @s run function slf:mob/boss/bar {id:"ctarnidd"}
execute as @e[tag=slf.boss_siegwurm,limit=1] at @s run function slf:mob/boss/bar {id:"siegwurm"}
