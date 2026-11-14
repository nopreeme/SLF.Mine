# Runs as a player who died (slf.deaths is a deathCount objective). Despair leaves a mark: Vorpal Soul -5.
scoreboard players set @s slf.deaths 0
execute if score @s slf.vorpal_soul matches 1.. run scoreboard players remove @s slf.vorpal_soul 5
execute if score @s slf.vorpal_soul matches ..-1 run scoreboard players set @s slf.vorpal_soul 0
tag @s remove slf.tantrum_active
# The Dream Penalty: a Wanderer who dies before registering at Secondil's inn wakes in Firstia, and it was all a dream
execute if entity @s[tag=slf.wandering] run function slf:wanderer/dream
