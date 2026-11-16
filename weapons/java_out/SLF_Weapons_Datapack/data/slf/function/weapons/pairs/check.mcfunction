# Runs as each player, every tick. Keeps the off-hand twin of a paired weapon in sync.
# Marsh Daggers
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"marsh_dagger"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"marsh_dagger"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"marsh_dagger"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:marsh_dagger",minecraft:item_name="Marsh Daggers",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"marsh_dagger",is_twin:1b}}]
# Mercenary Twinblades
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"mercenary_blade"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"mercenary_blade"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"mercenary_blade"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:mercenary_blade",minecraft:item_name="Mercenary Twinblades",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"mercenary_blade",is_twin:1b}}]
# Vorpal Choppers
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"vorpal_chopper"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"vorpal_chopper"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"vorpal_chopper"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:vorpal_chopper",minecraft:item_name="Vorpal Choppers",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"vorpal_chopper",is_twin:1b}}]
# Sunraku's Blades
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"sunraku_blade"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"sunraku_blade"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"sunraku_blade"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:sunraku_blade",minecraft:item_name="Sunraku's Blades",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"sunraku_blade",is_twin:1b}}]
# Togetsu
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"togetsu"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"togetsu"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"togetsu"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:togetsu_twin",minecraft:item_name="Togetsu",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"togetsu",is_twin:1b}}]
# Ducusram
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"ducusram"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"ducusram"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"ducusram"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:ducusram",minecraft:item_name="Ducusram",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"ducusram",is_twin:1b}}]
# Empire Bee Twinblade
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"empire_bee_twinblade"}}] run clear @s *[minecraft:custom_data~{slf:{twin:"empire_bee_twinblade"}}]
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{slf:{pair:"empire_bee_twinblade"}}] unless items entity @s weapon.offhand * run item replace entity @s weapon.offhand with minecraft:stick[minecraft:item_model="slf:empire_bee_twinblade_twin",minecraft:item_name="Empire Bee Twinblade",minecraft:max_stack_size=1,minecraft:custom_data={slf:{twin:"empire_bee_twinblade",is_twin:1b}}]
