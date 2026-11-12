# Runs as a player who used /trigger slf.menu. Triggers work without OP, unlike /function.
scoreboard players operation #id slf.tmp = @s slf.menu
scoreboard players reset @s slf.menu
execute if score #id slf.tmp matches 1 run return run function slf:menu/main
execute if score #id slf.tmp matches 2 run return run function slf:class/select
execute if score #id slf.tmp matches 3 run return run function slf:skills/menu
execute if score #id slf.tmp matches 4 run return run function slf:stats/menu
execute if score #id slf.tmp matches 5 run return run function slf:class/evolve
execute if score #id slf.tmp matches 6 run return run function slf:altar/guide
execute if score #id slf.tmp matches 7 run return run function slf:menu/status
execute if score #id slf.tmp matches 8 run return run function slf:skills/tantrum_toggle
execute if score #id slf.tmp matches 9 run return run function slf:menu/toggle_hud
function slf:menu/main
