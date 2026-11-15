# As a player in Standby (menu option 6, and automatically on entering Standby).
execute if score #altar_placed slf.timer matches 1 run return run function slf:altar/directions
execute if score #altar_pending slf.timer matches 1 run return run tellraw @s {"text":" The Altar of Awakening is rising. You will be told where it stands in a moment.","color":"light_purple"}
function slf:altar/create
tellraw @s {"text":" An Altar of Awakening is rising somewhere in the world. You will be told where it stands in a moment.","color":"light_purple"}
