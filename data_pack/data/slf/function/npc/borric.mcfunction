# Old Borric, half-drunk and full of stories: Bar Talk. Three stories, then the bartender wants the truth of it.
execute if score @s slf.q.bar matches 0 run return run function slf:npc/borric_offer
execute if score @s slf.q.bar matches 4.. run return run tellraw @s ["",{"text":"[Old Borric] ","color":"gray"},{"text":"Humming, I tell you. Nobody listens to Old Borric.","color":"white"}]
scoreboard players add @s slf.q.bar 1
execute if score @s slf.q.bar matches 2 run tellraw @s ["",{"text":"[Old Borric] ","color":"gray"},{"text":"Did I ever tell you about the time I out-drank a Vorpal Bunny? It hopped off with my boots. True story.","color":"white"}]
execute if score @s slf.q.bar matches 3 run tellraw @s ["",{"text":"[Old Borric] ","color":"gray"},{"text":"The castle up the hill? Full of gold. And dragons. And a dragon made of gold. Ask anyone. (Nobody agrees.)","color":"white"}]
execute if score @s slf.q.bar matches 4 run tellraw @s ["",{"text":"[Old Borric] ","color":"gray"},{"text":"Now this one's true. At night, by the marsh's deep pools... a humming. Low, like a song with no singer. Heard it with my own ears.","color":"white"}]
execute if score @s slf.q.bar matches 4 run tellraw @s {"text":" Quest updated: tell the Bartender whether Borric's marsh story is true.","color":"yellow"}
