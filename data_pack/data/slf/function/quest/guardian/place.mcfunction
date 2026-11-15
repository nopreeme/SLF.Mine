# Macro, as the player. Argument: yaw. The snake is summoned 50 blocks out, on the surface (its "bridge").
$execute rotated $(yaw) 0 positioned ^ ^ ^50 positioned over motion_blocking_no_leaves run function slf:mob/boss/ravenous_snake/spawn
