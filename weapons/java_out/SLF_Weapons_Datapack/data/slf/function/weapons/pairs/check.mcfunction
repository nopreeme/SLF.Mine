# Runs as each player, every tick. Keeps the off-hand twin of a paired weapon in sync.
# Marsh Daggers
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"marsh_dagger"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"marsh_dagger"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"marsh_dagger"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:marsh_dagger",minecraft:item_name="Marsh Daggers",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"marsh_dagger",is_twin:1b}}]
# Mercenary's Blades
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"mercenary_blade"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"mercenary_blade"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"mercenary_blade"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:mercenary_blade",minecraft:item_name="Mercenary's Blades",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"mercenary_blade",is_twin:1b}}]
# Vorpal Choppers
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"vorpal_chopper"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"vorpal_chopper"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"vorpal_chopper"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:vorpal_chopper",minecraft:item_name="Vorpal Choppers",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"vorpal_chopper",is_twin:1b}}]
