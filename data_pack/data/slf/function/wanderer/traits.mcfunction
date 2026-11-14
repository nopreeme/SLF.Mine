# The Wanderer's permanent traits (design doc V9, 6.1). Re-applied every second, so they survive respawning; adding one
# that is already there just fails quietly.
attribute @s minecraft:luck modifier add slf:wanderer_luck 2 add_value
attribute @s minecraft:armor modifier add slf:wanderer_defense -0.1 add_multiplied_total
