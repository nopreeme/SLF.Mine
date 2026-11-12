execute as @a run function slf:weapons/pairs/check
# twins are display-only: remove any that get dropped
execute as @e[type=minecraft:item] if items entity @s contents *[minecraft:custom_data~{slf:{is_twin:1b}}] run kill @s
