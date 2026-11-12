# Runs when a player comes back (slf.leave counts minecraft.custom:leave_game).
scoreboard players set @s slf.leave 0
execute unless entity @s[tag=slf.class_chosen] run function slf:class/select
