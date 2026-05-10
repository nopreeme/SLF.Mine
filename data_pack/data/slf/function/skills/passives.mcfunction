# Skywalker — Jump Boost I + Slow Falling (Shinobi tier 3)
effect give @a[tag=slf.skill.skywalker] minecraft:jump_boost 3 0 true
effect give @a[tag=slf.skill.skywalker] minecraft:slow_falling 3 0 true

# Formula Drift — Speed II while tagged (Ninja tier 2)
effect give @a[tag=slf.skill.formula_drift] minecraft:speed 3 1 true

# Gravity Zero — Slow Falling (boss drop, Siegwurm)
effect give @a[tag=slf.skill.gravity_zero] minecraft:slow_falling 3 0 true

# Acrobat — Resistance I while airborne (boss drop, Vorpal Bunny)
execute as @a[tag=slf.skill.acrobat,nbt={OnGround:0b}] run effect give @s minecraft:resistance 3 0 true

# Managarm Pride — Strength scales with missing HP (boss drop, Lycagon)
execute as @a[tag=slf.skill.managarm_pride] run function slf:skills/managarm_check

# Ignition — Strength I + Speed I on combat hit (Mercenary base)
execute as @a[tag=slf.skill.ignition] run function slf:skills/ignition_check
