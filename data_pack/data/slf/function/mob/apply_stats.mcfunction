# Macro, runs as an SLF mob. Arguments (storage slf:mob): hp, atk, lv, name, color.
$attribute @s minecraft:max_health base set $(hp)
$attribute @s minecraft:attack_damage base set $(atk)
$data modify entity @s Health set value $(hp)f
$data modify entity @s CustomName set value {text:"$(name) Lv.$(lv)",color:"$(color)"}
