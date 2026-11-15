# Macro, runs as a boss at the boss. Argument: id (the bar is slf:<id>, created in setup).
$bossbar set slf:$(id) players @a[distance=..64]
$execute store result bossbar slf:$(id) max run attribute @s minecraft:max_health get
$execute store result bossbar slf:$(id) value run data get entity @s Health
$bossbar set slf:$(id) visible true
