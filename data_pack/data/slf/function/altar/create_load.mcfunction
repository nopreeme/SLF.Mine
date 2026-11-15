# Macro: $(cx) $(cz) = chosen spot.
$execute in minecraft:overworld run forceload add $(cx) $(cz)
schedule function slf:altar/create_try 20t
