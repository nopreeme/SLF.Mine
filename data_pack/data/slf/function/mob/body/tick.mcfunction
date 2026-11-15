# Every tick while any mob body exists (skills/tick). A body is the 3D model riding an invisible mob (mob/body/bunny, frog).
# A body whose mob has died is no longer riding anything: remove it.
kill @e[tag=slf.mob_body,predicate=!slf:has_vehicle]
# Face the way the mob faces (a riding display does not turn by itself).
execute as @e[tag=slf.mob_body] on vehicle rotated as @s on passengers run rotate @s ~ 0
# Leaping pose while the mob is off the ground, standing pose once it lands.
execute as @e[tag=slf.mob_body,tag=!slf.leaping] on vehicle unless predicate slf:on_ground on passengers run function slf:mob/body/leap
execute as @e[tag=slf.mob_body,tag=slf.leaping] on vehicle if predicate slf:on_ground on passengers run function slf:mob/body/land
