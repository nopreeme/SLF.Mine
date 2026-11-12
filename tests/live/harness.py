"""Starts a throwaway local Minecraft server with the data pack(s) loaded and a test player connected.

Needs a dedicated server jar and a Java runtime that can run it:

    SLF_MC_SERVER_DIR   folder containing server.jar (a scratch folder; a world is created and deleted inside it)
    SLF_JAVA            path to the java executable (default: "java")

Using the server means accepting Mojang's EULA; this writes eula=true into that scratch folder for you.
The server only listens on 127.0.0.1, in offline mode, and is stopped when the context exits.
"""
import os, re, shutil, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mcbot import Bot, Rcon

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PORT, RCON_PORT, RCON_PASSWORD = 25599, 25575, "slftest"
PROPERTIES = f"""server-ip=127.0.0.1
server-port={PORT}
online-mode=false
enable-rcon=true
rcon.port={RCON_PORT}
rcon.password={RCON_PASSWORD}
broadcast-rcon-to-ops=false
function-permission-level=4
spawn-protection=0
view-distance=3
simulation-distance=3
pause-when-empty-seconds=-1
max-tick-time=-1
sync-chunk-writes=false
gamemode=survival
difficulty=normal
"""


class LiveServer:
    def __init__(self, datapacks=None, player="TestBot", keep_world=False):
        self.dir = os.environ.get("SLF_MC_SERVER_DIR"); self.java = os.environ.get("SLF_JAVA", "java")
        if not self.dir or not os.path.exists(os.path.join(self.dir, "server.jar")):
            raise RuntimeError("set SLF_MC_SERVER_DIR to a folder containing server.jar (see tests/live/README.md)")
        self.datapacks = datapacks or {"SLF": os.path.join(REPO, "data_pack")}
        self.player, self.keep_world, self.proc, self.rcon, self.bot = player, keep_world, None, None, None

    def __enter__(self):
        world = os.path.join(self.dir, "world")
        if not self.keep_world: shutil.rmtree(world, ignore_errors=True)
        for name, src in self.datapacks.items():
            dst = os.path.join(world, "datapacks", name); shutil.rmtree(dst, ignore_errors=True); shutil.copytree(src, dst)
        with open(os.path.join(self.dir, "eula.txt"), "w") as f: f.write("eula=true\n")
        with open(os.path.join(self.dir, "server.properties"), "w") as f: f.write(PROPERTIES)
        self.log_path = os.path.join(self.dir, "live_test.log")
        self.log = open(self.log_path, "w", encoding="utf-8", errors="replace")
        self.proc = subprocess.Popen([self.java, "-Xmx2G", "-jar", "server.jar", "nogui"], cwd=self.dir,
                                     stdin=subprocess.PIPE, stdout=self.log, stderr=subprocess.STDOUT)
        deadline = time.time() + 180
        while time.time() < deadline:
            if self.proc.poll() is not None: raise RuntimeError("server exited during startup, see " + self.log_path)
            if re.search(r"RCON running on", self.read_log()): break
            time.sleep(0.5)
        else:
            raise TimeoutError("server did not start, see " + self.log_path)
        self.rcon = Rcon(port=RCON_PORT, password=RCON_PASSWORD)
        self.bot = Bot(self.player, port=PORT).connect()
        return self

    def __exit__(self, *exc):
        try:
            if self.bot: self.bot.close()
            if self.rcon: self.rcon.cmd("stop"); self.rcon.close()
        except Exception:
            pass
        try: self.proc.wait(timeout=60)
        except Exception: self.proc.kill()
        self.log.close()
        if not self.keep_world: shutil.rmtree(os.path.join(self.dir, "world"), ignore_errors=True)

    # ---- helpers
    def read_log(self):
        with open(self.log_path, encoding="utf-8", errors="replace") as f: return f.read()

    def cmd(self, command): return self.rcon.cmd(command)

    def as_player(self, command): return self.cmd(f"execute as {self.player} at @s run {command}")

    def score(self, objective, holder=None):
        out = self.cmd(f"scoreboard players get {holder or self.player} {objective}")
        m = re.search(r" has (-?\d+) ", out); return int(m.group(1)) if m else None

    def tags(self):
        out = self.cmd(f"tag {self.player} list"); m = re.search(r"tags?: (.*)$", out)
        return set(t.strip() for t in m.group(1).split(",")) if m else set()

    def effects(self):
        """{effect id: amplifier} currently on the player (amplifier 0 is omitted in the game's data)."""
        out = self.cmd(f"data get entity {self.player} active_effects"); found = {}
        for entry in re.findall(r"\{[^{}]*\}", out):
            m = re.search(r'id: "minecraft:([a-z_]+)"', entry)
            if m: a = re.search(r"amplifier: (-?\d+)b", entry); found[m.group(1)] = int(a.group(1)) if a else 0
        return found

    def attribute(self, name, what="get"):
        out = self.cmd(f"attribute {self.player} minecraft:{name} {what}"); m = re.search(r" is (-?[\d.]+)", out)
        return float(m.group(1)) if m else None

    def wait_ticks(self, ticks): time.sleep(ticks / 20 + 0.15)

    def wait_cycle(self):
        """Wait for the pack's once-per-second cycle to have run at least once."""
        self.wait_ticks(26)
