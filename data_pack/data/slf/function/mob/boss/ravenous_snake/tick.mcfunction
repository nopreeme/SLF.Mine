# Every tick while any part of the snake exists (skills/tick). Its parts go when the snake does; otherwise the head
# sits on the ravager and each segment stays a fixed distance behind the one in front, facing it.
execute unless entity @e[tag=slf.snake,limit=1] run return run kill @e[tag=slf.snake_part]
execute as @e[tag=slf.seg0,limit=1] at @e[tag=slf.snake,limit=1] run tp @s ~ ~ ~ ~ 0
execute as @e[tag=slf.seg1,limit=1] at @e[tag=slf.seg0,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg0,limit=1] feet
execute as @e[tag=slf.seg2,limit=1] at @e[tag=slf.seg1,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg1,limit=1] feet
execute as @e[tag=slf.seg3,limit=1] at @e[tag=slf.seg2,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg2,limit=1] feet
execute as @e[tag=slf.seg4,limit=1] at @e[tag=slf.seg3,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg3,limit=1] feet
execute as @e[tag=slf.seg5,limit=1] at @e[tag=slf.seg4,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg4,limit=1] feet
execute as @e[tag=slf.seg6,limit=1] at @e[tag=slf.seg5,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg5,limit=1] feet
execute as @e[tag=slf.seg7,limit=1] at @e[tag=slf.seg6,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg6,limit=1] feet
execute as @e[tag=slf.seg8,limit=1] at @e[tag=slf.seg7,limit=1] facing entity @s feet run tp @s ^ ^ ^1.5 facing entity @e[tag=slf.seg7,limit=1] feet
execute as @e[tag=slf.snake,limit=1] at @s run function slf:mob/boss/bar {id:"ravenous_snake"}
