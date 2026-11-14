"""Minimal Minecraft Java client for automated datapack tests.

Logs a player into a local offline-mode server and keeps the connection alive (keep-alives, teleport confirms,
respawns). Beyond that it can sprint, walk, jump and melee an entity, which is enough to exercise the statistics the
pack reads (sprint distance, jumps, damage dealt). Tests drive everything else through RCON and read results back from
RCON and from the chat lines this client records. Packet ids come from the server's own report (`--reports` -> packets.json).
"""
import socket, struct, threading, time, uuid, zlib


def varint(n):
    n &= 0xFFFFFFFF; out = b""
    while True:
        b = n & 0x7F; n >>= 7
        out += bytes([b | (0x80 if n else 0)])
        if not n: return out


class Reader:
    def __init__(self, data): self.d, self.i = data, 0
    def varint(self):
        n = shift = 0
        while True:
            b = self.d[self.i]; self.i += 1; n |= (b & 0x7F) << shift; shift += 7
            if not b & 0x80: return n - (1 << 32) if n & (1 << 31) else n
    def take(self, k): v = self.d[self.i:self.i + k]; self.i += k; return v
    def string(self): return self.take(self.varint()).decode("utf-8", "replace")
    def rest(self): return self.d[self.i:]


def read_nbt(r, tag=None):
    """Network NBT (nameless root). Returns plain Python values."""
    if tag is None:
        tag = r.take(1)[0]
        if tag == 0: return None
    if tag == 1: return struct.unpack(">b", r.take(1))[0]
    if tag == 2: return struct.unpack(">h", r.take(2))[0]
    if tag == 3: return struct.unpack(">i", r.take(4))[0]
    if tag == 4: return struct.unpack(">q", r.take(8))[0]
    if tag == 5: return struct.unpack(">f", r.take(4))[0]
    if tag == 6: return struct.unpack(">d", r.take(8))[0]
    if tag == 7: return r.take(struct.unpack(">i", r.take(4))[0])
    if tag == 8: return r.take(struct.unpack(">H", r.take(2))[0]).decode("utf-8", "replace")
    if tag == 9:
        et = r.take(1)[0]; n = struct.unpack(">i", r.take(4))[0]
        return [read_nbt(r, et) for _ in range(n)]
    if tag == 10:
        out = {}
        while True:
            t = r.take(1)[0]
            if t == 0: return out
            name = r.take(struct.unpack(">H", r.take(2))[0]).decode("utf-8", "replace"); out[name] = read_nbt(r, t)
    if tag == 11: return [struct.unpack(">i", r.take(4))[0] for _ in range(struct.unpack(">i", r.take(4))[0])]
    if tag == 12: return [struct.unpack(">q", r.take(8))[0] for _ in range(struct.unpack(">i", r.take(4))[0])]
    raise ValueError(f"bad nbt tag {tag}")


def component_text(c):
    """Flatten a text component to what a player would read."""
    if c is None: return ""
    if isinstance(c, str): return c
    if isinstance(c, list): return "".join(component_text(x) for x in c)
    if isinstance(c, dict):
        s = c.get("text", "") + str(c.get("", ""))   # {"": "x"} is how a bare string is sent inside a mixed list
        if "translate" in c:
            s += c["translate"] + ("(" + ", ".join(component_text(w) for w in c.get("with", [])) + ")" if c.get("with") else "")
        return s + "".join(component_text(x) for x in c.get("extra", []))
    return str(c)


def component_clicks(c, out=None):
    """All (label, command) click_events in a text component, in order: what the menu buttons would run."""
    out = [] if out is None else out
    if isinstance(c, list):
        for x in c: component_clicks(x, out)
    elif isinstance(c, dict):
        ev = c.get("click_event")
        if isinstance(ev, dict) and "command" in ev:
            out.append((component_text({k: v for k, v in c.items() if k != "extra"}), ev["command"]))
        for x in c.get("extra", []): component_clicks(x, out)
    return out


class Bot:
    PROTOCOL = 776   # Minecraft 26.2
    # clientbound (L_/C_/P_) and serverbound (LS_/CS_/PS_) packet ids per phase, 26.2
    L_DISCONNECT, L_FINISHED, L_COMPRESSION, LS_ACK = 0, 2, 3, 3
    C_DISCONNECT, C_FINISH, C_KEEPALIVE, C_PING, C_KNOWN_PACKS = 2, 3, 4, 5, 14
    CS_FINISH, CS_KEEPALIVE, CS_PONG, CS_KNOWN_PACKS = 3, 4, 5, 7
    P_CHUNK_BATCH, P_DISCONNECT, P_KEEPALIVE, P_PING, P_POSITION, P_HEALTH, P_START_CONFIG, P_CHAT = 11, 32, 44, 61, 72, 104, 118, 121
    PS_TELEPORT, PS_CHUNK_BATCH, PS_RESPAWN, PS_CONFIG_ACK, PS_KEEPALIVE, PS_LOADED, PS_PONG = 0, 11, 12, 16, 28, 44, 45
    P_ADD_ENTITY, P_LOGIN = 1, 49
    PS_ATTACK, PS_MOVE_POS, PS_MOVE_STATUS, PS_PLAYER_COMMAND = 1, 30, 33, 42
    START_SPRINTING, STOP_SPRINTING = 1, 2

    def __init__(self, name="TestBot", host="127.0.0.1", port=25599):
        self.name, self.host, self.port = name, host, port
        self.threshold = -1; self.state = "login"; self.chat = []; self.raw_chat = []; self.error = None
        self.in_game = threading.Event(); self.closed = False; self.lock = threading.Lock(); self.deaths = 0
        self.entity_id = None; self.pos = None; self.entities = {}   # entities: uuid bytes -> network id

    # ---- framing
    def _send(self, pid, payload=b""):
        data = varint(pid) + payload
        if self.threshold >= 0:
            data = varint(0) + data if len(data) < self.threshold else varint(len(data)) + zlib.compress(data)
        with self.lock: self.sock.sendall(varint(len(data)) + data)

    def _recv_exact(self, n):
        buf = b""
        while len(buf) < n:
            chunk = self.sock.recv(n - len(buf))
            if not chunk: raise ConnectionError("server closed the connection")
            buf += chunk
        return buf

    def _recv(self):
        n = shift = 0
        while True:
            b = self._recv_exact(1)[0]; n |= (b & 0x7F) << shift; shift += 7
            if not b & 0x80: break
        r = Reader(self._recv_exact(n))
        if self.threshold >= 0:
            size = r.varint(); body = r.rest()
            r = Reader(zlib.decompress(body) if size else body)
        return r.varint(), r

    # ---- lifecycle
    def connect(self, timeout=30):
        self.sock = socket.create_connection((self.host, self.port), timeout=10); self.sock.settimeout(120)
        host = self.host.encode()
        self._send(0, varint(self.PROTOCOL) + varint(len(host)) + host + struct.pack(">H", self.port) + varint(2))
        nm = self.name.encode()
        self._send(0, varint(len(nm)) + nm + uuid.uuid3(uuid.NAMESPACE_DNS, "OfflinePlayer:" + self.name).bytes)
        threading.Thread(target=self._loop, daemon=True).start()
        if not self.in_game.wait(timeout): raise TimeoutError(f"bot did not reach the game: {self.error}")
        return self

    def close(self):
        self.closed = True
        try: self.sock.close()
        except OSError: pass

    def _loop(self):
        try:
            while not self.closed:
                pid, r = self._recv(); getattr(self, "_on_" + self.state)(pid, r)
        except Exception as e:   # surfaced through self.error
            if not self.closed: self.error = repr(e)

    def _on_login(self, pid, r):
        if pid == self.L_COMPRESSION: self.threshold = r.varint()
        elif pid == self.L_FINISHED: self._send(self.LS_ACK); self.state = "config"
        elif pid == self.L_DISCONNECT: raise ConnectionError("login refused: " + r.string())

    def _on_config(self, pid, r):
        if pid == self.C_KNOWN_PACKS: self._send(self.CS_KNOWN_PACKS, varint(0))   # we know none: server sends full registries
        elif pid == self.C_KEEPALIVE: self._send(self.CS_KEEPALIVE, r.take(8))
        elif pid == self.C_PING: self._send(self.CS_PONG, r.take(4))
        elif pid == self.C_FINISH: self._send(self.CS_FINISH); self.state = "play"
        elif pid == self.C_DISCONNECT: raise ConnectionError("kicked in configuration: " + component_text(read_nbt(r)))

    def _on_play(self, pid, r):
        if pid == self.P_KEEPALIVE: self._send(self.PS_KEEPALIVE, r.take(8))
        elif pid == self.P_PING: self._send(self.PS_PONG, r.take(4))
        elif pid == self.P_LOGIN: self.entity_id = struct.unpack(">i", r.take(4))[0]
        elif pid == self.P_ADD_ENTITY:
            eid = r.varint(); self.entities[bytes(r.take(16))] = eid
        elif pid == self.P_POSITION:
            tid = r.varint(); self.pos = list(struct.unpack(">ddd", r.take(24)))   # absolute: tests only teleport with absolute coordinates
            self._send(self.PS_TELEPORT, varint(tid))
            self._move(False)   # a real client reports its position right after a teleport; the server only then loads the area
            if not self.in_game.is_set(): self._send(self.PS_LOADED); self.in_game.set()
        elif pid == self.P_CHUNK_BATCH: self._send(self.PS_CHUNK_BATCH, struct.pack(">f", 20.0))
        elif pid == self.P_CHAT:
            c = read_nbt(r); self.raw_chat.append(c); self.chat.append(component_text(c))
        elif pid == self.P_HEALTH:
            if struct.unpack(">f", r.take(4))[0] <= 0: self.deaths += 1; self._send(self.PS_RESPAWN, varint(0))
        elif pid == self.P_START_CONFIG: self._send(self.PS_CONFIG_ACK); self.state = "config"
        elif pid == self.P_DISCONNECT: raise ConnectionError("kicked: " + component_text(read_nbt(r)))

    # ---- acting in the world
    def _move(self, on_ground): self._send(self.PS_MOVE_POS, struct.pack(">dddB", *self.pos, 1 if on_ground else 0))

    def sprint(self, on=True):
        self._send(self.PS_PLAYER_COMMAND, varint(self.entity_id) + varint(self.START_SPRINTING if on else self.STOP_SPRINTING) + varint(0))

    def walk(self, blocks, step=0.2):
        """Walk along +x on the ground, one small step per game tick."""
        for _ in range(round(blocks / step)):
            self.pos[0] += step; self._move(True); time.sleep(0.05)

    def leave_ground(self, height=0.42):
        """The first packet of a jump: up, and no longer on the ground. Call land() to come back down."""
        self.pos[1] += height; self._move(False); self._air = height

    def land(self): self.pos[1] -= self._air; self._move(True)

    def hold_air(self, seconds):
        """Stay airborne the way a real client does: report 'not on the ground' every tick. Without this the server
        decides a silent player has landed after about half a second."""
        end = time.time() + seconds
        while time.time() < end: self._send(self.PS_MOVE_STATUS, bytes([0])); time.sleep(0.05)

    def jump(self):
        """One full jump. The server needs a few ticks on the ground between jumps to count each one."""
        self.leave_ground(); self.hold_air(0.25); self.land(); time.sleep(0.25)

    def attack(self, entity_uuid): self._send(self.PS_ATTACK, varint(self.entities[entity_uuid]))

    # ---- helpers for tests
    def mark(self): return len(self.chat)
    def chat_since(self, mark): return self.chat[mark:]
    def clicks_since(self, mark): return [x for c in self.raw_chat[mark:] for x in component_clicks(c)]


class Rcon:
    def __init__(self, host="127.0.0.1", port=25575, password="slftest"):
        self.sock = socket.create_connection((host, port), timeout=10); self.sock.settimeout(30); self.rid = 0
        if self._call(3, password)[0] == -1: raise PermissionError("rcon login failed")

    def _exact(self, n):
        buf = b""
        while len(buf) < n:
            chunk = self.sock.recv(n - len(buf))
            if not chunk: raise ConnectionError("rcon closed")
            buf += chunk
        return buf

    def _call(self, kind, body):
        self.rid += 1; payload = struct.pack("<ii", self.rid, kind) + body.encode("utf-8") + b"\x00\x00"
        self.sock.sendall(struct.pack("<i", len(payload)) + payload)
        data = self._exact(struct.unpack("<i", self._exact(4))[0])
        return struct.unpack("<i", data[:4])[0], data[8:-2].decode("utf-8", "replace")

    def cmd(self, command): return self._call(2, command)[1]
    def close(self): self.sock.close()
