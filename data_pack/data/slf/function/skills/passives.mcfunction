# Skywalker — Jump Boost I + Slow Falling (AirStep T3)
effect give @a[tag=slf.skill.skywalker] minecraft:jump_boost 3 0 true
effect give @a[tag=slf.skill.skywalker] minecraft:slow_falling 3 0 true

# Skatefoot — Speed I (AirStep T2.5)
effect give @a[tag=slf.skill.skatefoot] minecraft:speed 3 0 true

# Formula Drift — Speed II (AirStep T2)
effect give @a[tag=slf.skill.formula_drift] minecraft:speed 3 1 true

# Slide Step — Speed I (AirStep T1)
effect give @a[tag=slf.skill.slide_step] minecraft:speed 3 0 true

# Gravity Zero — Slow Falling
effect give @a[tag=slf.skill.gravity_zero] minecraft:slow_falling 3 0 true

# Acrobat — Resistance I while airborne
execute as @a[tag=slf.skill.acrobat,nbt={OnGround:0b}] run effect give @s minecraft:resistance 3 0 true

# Managarm Pride — Strength scales with missing HP
execute as @a[tag=slf.skill.managarm_pride] run function slf:skills/managarm_check

# Ignition — Strength I + Speed I on damage taken
execute as @a[tag=slf.skill.ignition] run function slf:skills/ignition_check

# Slash Ignition — Strength II + Speed II on damage taken
execute as @a[tag=slf.skill.slash_ignition] run function slf:skills/slash_ignition_check

# Holy Shield — Resistance I
effect give @a[tag=slf.skill.holy_shield] minecraft:resistance 3 0 true

# Iron Skin — Resistance II
effect give @a[tag=slf.skill.iron_skin] minecraft:resistance 3 1 true

# Rechette Step — Speed I + Jump Boost I
effect give @a[tag=slf.skill.rechette_step] minecraft:speed 3 0 true
effect give @a[tag=slf.skill.rechette_step] minecraft:jump_boost 3 0 true

# Big Tantrum — Glowing while tantrum_active tag is set
execute as @a[tag=slf.skill.big_tantrum,tag=slf.tantrum_active] run effect give @s minecraft:glowing 3 0 true

# Grand Tantrum — Glowing + Strength I while active
execute as @a[tag=slf.skill.grand_tantrum,tag=slf.tantrum_active] run effect give @s minecraft:glowing 3 0 true
execute as @a[tag=slf.skill.grand_tantrum,tag=slf.tantrum_active] run effect give @s minecraft:strength 3 0 true

# Inexhaustible Beasts — Strength I passive
effect give @a[tag=slf.skill.inexhaustible_beasts] minecraft:strength 3 0 true

# Terraton Corapsa — Strength I passive
effect give @a[tag=slf.skill.terraton_corapsa] minecraft:strength 3 0 true

# Bradion
execute as @a[tag=slf.skill.bradion] run function slf:skills/bradion_tick

# Title passives — unconditional; each line selects only tagged players
function slf:titles/passives
