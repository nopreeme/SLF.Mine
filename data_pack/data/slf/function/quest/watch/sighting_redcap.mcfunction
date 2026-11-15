# Runs as a freshly summoned zombie at the tree line: a Redcap that stands and watches the city (no AI), belongs to the
# watching player (#me), and stays even if that player is far away. Like every Redcap it leaves at dawn.
function slf:mob/red_hat_goblin/convert
tag @s add slf.sighting
data merge entity @s {NoAI:1b,PersistenceRequired:1b}
scoreboard players operation @s slf.pid = #me slf.pid
