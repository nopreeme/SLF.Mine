# Runs as the freshly summoned wolf: makes it Lycagon the Nightslayer, level 90.
data merge entity @s {variant:"minecraft:black"}
tag @s add slf.night_boss
function slf:mob/boss/init {id:"lycagon",name:"Lycagon the Nightslayer",color:"dark_purple",lv:90,scale:3.0,loot:"slf:boss/lycagon"}
# A wolf resets its base max health to 8 whenever its data is loaded (mob/boss/lycagon/hunt writes it every second),
# so Lycagon's health is a modifier on top of that base: 8 + 352 = 360 (4 x level).
attribute @s minecraft:max_health base set 8
attribute @s minecraft:max_health modifier add slf:lycagon_health 352 add_value
effect give @s minecraft:instant_health 1 7 true
