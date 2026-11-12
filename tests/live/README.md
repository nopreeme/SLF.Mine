# Live tests

`tests/test_datapack.py` and `tests/test_resource_pack.py` read files only. These tests go further: they start a real
Minecraft 26.2 server, log a real player in, and drive the pack through the same `/trigger` commands the chat menus
run, then read back scores, tags, effects, attributes and the chat the player received.

## Setup

You need a dedicated server jar for the pack's Minecraft version and a Java runtime that can run it (26.2 needs Java 25).

1. Make an empty scratch folder and put `server.jar` in it (download it from minecraft.net).
2. Point the tests at it:

   ```
   set SLF_MC_SERVER_DIR=C:\path\to\scratch\folder
   set SLF_JAVA=C:\path\to\java.exe
   ```

3. Run from the repo root:

   ```
   python -m unittest tests.live.test_live -v
   ```

About two and a half minutes. Without `SLF_MC_SERVER_DIR` the module is skipped.

Running the server means accepting Mojang's EULA; the harness writes `eula=true` into the scratch folder. The server
listens on 127.0.0.1 only (game port 25599, RCON 25575), runs in offline mode, and its world is deleted afterwards.

## How it works

- `mcbot.py` is a minimal protocol client: it logs in, answers keep-alives and teleport confirmations, respawns after
  death, and records chat. It cannot move or attack. Packet ids are for 26.2; after a Minecraft update, regenerate
  them with `java -DbundlerMainClass=net.minecraft.data.Main -jar server.jar --reports` and read `packets.json`.
- `harness.py` starts the server with the data packs copied in, connects RCON and the player, and offers helpers
  (`score`, `tags`, `effects`, `attribute`, `as_player`, `wait_cycle`).
- Tests click menu buttons by reading the `click_event` commands out of the chat the player received, so a broken
  menu fails the test the same way it would fail a player.
- Kills are simulated with `/damage ... by <player>`, which credits the kill to the player.

## Not covered

Anything that needs real movement or real melee hits: the sprint/jump/damage statistics that feed skill progress are
set directly on the scoreboard, and the `slf:ideal_motion` predicate (airborne while sprinting) is not exercised.
