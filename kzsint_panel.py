import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import math
import os
import re
import json
import hashlib
import hmac
import secrets
import webbrowser
import requests
from pathlib import Path
from datetime import datetime

ctk.set_appearance_mode("dark")

# ───────────────────────── Palette / polices ─────────────────────────
# Thème Halloween
BG = "#0a0000"           # Noir profond avec légère teinte rouge
PANEL = "#0d0202"        # Noir très sombre
BORDER = "#ff6600"       # Orange Halloween pour les contours
WHITE = "#f3f3f6"
WHITE_H = "#d3d3d9"
TXT = "#ffaa66"          # Orange clair pour le texte
MUTED = "#994400"        # Orange sombre pour le texte muted
DIM = "#662200"          # Orange très sombre
GREEN = "#ff6600"        # Orange pour les accents
MONO = "Consolas"
SANS = "Segoe UI"


DISCORD_LOGO_B64 = (
    "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"
)


ICON_B64 = {
    "TÉLÉPHONE": (
        "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"
    ),
    "EMAIL": (
        "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"
    ),
    "SNAPCHAT": (
        "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"
    ),
    "NOM/PRENOM": (
        "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAFpElEQVR42u2aS2xUVRjH/98599x7Z6RUNAFJaDUm1vBqeDRMh0di"
        "CQRYmFhM0J0mGBZGo4lupBJFF7JhoQFCWLkxIZOYkBghumkaoC3kFnkYUWQjG4QERPq4r3PO56JtIESBdu6UOzj/fTvn+53zffd7"
        "AQ011FBDDTXU0P9V9Kh++NKlS97t27YJAKKI47VrFw4/9gCCIGjVWm0lonVE/CIzzQMYAEaY8ZuUYtBafaRUWn72sQJw/HjQ6vvq"
        "E0B0K+XOYbYwxsBaC4BARJBSQkqBOI5jIUSfMfGnpdLKgboHMDBwZouUzkHP81rjOJ4w+j4HIoLretA6DY3RPVeu/P7Vtm3bTF0C"
        "GBz8aYdS7n5mdrTWU/pbIQQ8z0MYhoccR7/T0dGR1uKMolbG9/cPbXYcdcAYM2XjAcBaiyiKUCwWd6Sp7KmrFzA4eG4BEfqldFq0"
        "ru7iJuJDaox+uVRa9kOdvAD+zPf9qo0HAGaGEEJZi729vb2zcg+gr+9CCxFtjeM4s/+ZJAk8z13s+0+tzz0Az9Ov+r7f/KBoPx1X"
        "APjNenCBdVkbDwDGGBBhxYkTJ5pyCyAIgiJAC40xNQEgpZhL5D6bWwBjY+IJIsxj5uzDKjOEkAWl/GdyC2BkZATMYNRQnDHdTAEo"
        "VUwAjIwHrIwTFiIw21QIO5xbABs3dvzNzL8KkX1sFUJAa33zxo3wcq6/AkQ4LaXMHICUEtbyxU2byn/l/DPofBvHcZy1G4y/KjpM"
        "RJxrAKXSkgvGmBOe52V6+3EcXyeSR3KfCBGRBahH6zTMKhYopcBsPy+X26/VRTFULi87pbXe6XkeqnWFYrGIKIoqYXjrYF31A8Lw"
        "1r4wDA8VCgUQiSqMDweMwbtdXV26rgB0dXXpK1cuvT06OrpbCNKu607J533fRxxHh40Z616zZtn1umqI3KuBgTNbHEftkVK2ExG0"
        "NrDWYDKpIyIIISClAyEIWqdXjeEvjh5dun/3brK1PNuMtcWDICgS+Ru0tm8QYYW1dr5SygOANE2ZCNeJxM8AKkI433V0LLo6E+d6"
        "JIORixcvNt2+bVullPMADeZ0JE3V5dWrl9xEQw011NAM6pEEQWamoaGhp4cnKvumplmYPVsMt7W1xY8dAGam06fPLnIctQpAu9am"
        "nZlnAfT8xGQYRALW2mtSimtE9AezPU8k+5ub3XO1hlIzAEEQtFrrbWPmVwDucF3XIyJYa8HMMMZiskyY6PdBCMJkARXHMRPRL0Q4"
        "Zq35plYj88wBDAwMtTuO+x6AbqXUHGst0jTFVFt54yMxB0o5iMenLH3W0t7OzqU/5hJAX18wv1BQHwkhtjuOKiZJgqzmA+Mjcxda"
        "azDje2OSneXyyvO5ATC5A+C6bmuWhv8XCGP0mNb242PH2r+stlaoCkClUpEtLS/schynh4imNQafVgkrBFzXRZomh7Uefb9cLl+b"
        "cQCVSkW2trYdKBaLO8IwArPFTOtOv2Cse7oQqBrjC4XCjiiKUItJ0MPK930kSTxtCFMGEASB0trZlwfj74UwOhpt7eoq/VnTjlCa"
        "yp5isZgb4wEgiiL4fqHs++7XQRComgHo7x/arJTaGYZhboyf1NjYGAqFwqap7hM9tAucPHl2ruNQkMXeT83SWiI4jkzTNN3U2bm8"
        "N9MXIITd5Xlebo2fTKmJhAJoz/iuQkYATp36abHjONuTJMl9eZskCXzfX5Wm8rXMABjDHyrlFmqV4WWt8XUa+uBhtsoeCGBw8NwC"
        "KWV3Pdz+nS9VCtd1F/v+7PUZvAB+3fO85nq5/bsDIiDeqgpApcISQHe9GT/5CojEut7ewQXTBtDScqZNCFqRpmndAbDWwvO8J33f"
        "21CFC4hOpTw/b0nPw7sBAOClKgDQCiLUrSaWK5fcLz1+UBBcXI/+f7cbAPTc8DCa0VBDDf2b/gHBxpu03lHVhgAAAABJRU5ErkJg"
        "gg=="
    ),
}


def sp(s):
    """Espacement des lettres (effet letter-spacing)."""
    return "\u2009".join(s)


def gray(v):
    v = max(0, min(255, int(v)))
    return f"#{v:02x}{v:02x}{v:02x}"


def hex_rgb(c):
    c = c.lstrip("#")
    return int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)


def mix(a, b, t):
    """Mélange 2 couleurs hex (t=0 → a, t=1 → b)."""
    t = max(0.0, min(1.0, t))
    ra, ga, ba = hex_rgb(a)
    rb, gb, bb = hex_rgb(b)
    return "#%02x%02x%02x" % (round(ra + (rb - ra) * t),
                              round(ga + (gb - ga) * t),
                              round(ba + (bb - ba) * t))


def ease_out(t):
    return 1 - (1 - t) ** 3


def fmt_price(p):
    return f"{p:.2f}".replace(".", ",") + " €"


PRODUCTS = [
    ("B", "kzSINT BASIC", 9.99, "10 scans / jour · 2 modules · support communautaire"),
    ("P", "kzSINT PRO", 29.99, "Scans illimités · tous les modules · alertes temps réel"),
    ("E", "kzSINT ELITE", 99.99, "Accès API · scans prioritaires · support dédié 24/7"),
    ("D", "SCAN DEEP-WEB", 4.99, "Analyse ponctuelle des fuites et forums fermés"),
    ("R", "RAPPORT OSINT", 19.99, "Dossier complet PDF généré sur une cible unique"),
]

# Couleurs supplémentaires pour le thème Halloween
ORANGE_BRIGHT = "#ff8800"
ORANGE_DARK = "#cc4400"
RED_DARK = "#330000"

# ───────────────────────── Comptes & clés de licence ─────────────────────────
# ⚠ CHANGE ce secret avant de distribuer l'app (et garde le même dans keygen.py,
#   qui l'importe d'ici). Toute clé générée avec un autre secret sera refusée.
KEY_SECRET = b"CHANGE-MOI-par-un-secret-long-et-aleatoire"

ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"      # 32 caractères, sans I/O/0/1
PLAN_CODES = {"B": "BASIC", "P": "PRO", "E": "ELITE"}
DUR_CODES = {"W": 7, "M": 30, "Q": 90, "Y": 365, "L": 36500}   # jours (L = à vie)
PLAN_LIMITS = {"BASIC": 10, "PRO": None, "ELITE": None}        # scans / jour
USERNAME_RE = re.compile(r"^[A-Za-z0-9_\-]{3,20}$")


def _key_sig(core):
    digest = hmac.new(KEY_SECRET, core.encode(), hashlib.sha256).digest()
    return "".join(ALPHABET[b % 32] for b in digest[:8])


def normalize_key(key):
    k = re.sub(r"[^A-Z0-9]", "", (key or "").upper())
    if k.startswith("KZ"):
        k = k[2:]
    if len(k) == 16 and all(ch in ALPHABET for ch in k):
        return k
    return None


def generate_key(plan, days=30):
    """Génère une clé signée. plan: BASIC/PRO/ELITE — days: 7, 30, 90, 365 ou 36500 (à vie)."""
    pc = next((k for k, v in PLAN_CODES.items() if v == plan.upper()), None)
    dc = next((k for k, v in DUR_CODES.items() if v == days), None)
    if not pc or not dc:
        raise ValueError("plan ou durée invalide")
    core = pc + dc + "".join(secrets.choice(ALPHABET) for _ in range(6))
    raw = core + _key_sig(core)
    return "KZ-" + "-".join(raw[i:i + 4] for i in range(0, 16, 4))


def parse_key(key):
    raw = normalize_key(key)
    if raw is None:
        return None
    core, sig = raw[:8], raw[8:]
    if not hmac.compare_digest(sig, _key_sig(core)):
        return None
    plan, days = PLAN_CODES.get(core[0]), DUR_CODES.get(core[1])
    if not plan or not days:
        return None
    return plan, days, raw


class Store:
    """Comptes (mots de passe hachés PBKDF2) + licences, dans %APPDATA%/kzSINT/users.json."""

    def __init__(self):
        base = Path(os.environ.get("APPDATA") or Path.home()) / "kzSINT"
        base.mkdir(parents=True, exist_ok=True)
        self.path = base / "users.json"
        self.data = {"users": {}, "used_keys": {}}
        self.fails = {}
        self.load()

    def load(self):
        if not self.path.exists():
            return
        try:
            d = json.loads(self.path.read_text(encoding="utf-8"))
            self.data["users"] = d.get("users", {})
            self.data["used_keys"] = d.get("used_keys", {})
        except Exception:
            try:
                self.path.replace(self.path.with_suffix(".bak"))
            except OSError:
                pass

    def save(self):
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=2), encoding="utf-8")
        os.replace(tmp, self.path)

    @staticmethod
    def _hash(password, salt):
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)

    def register(self, username, password):
        if not USERNAME_RE.match(username):
            return False, "Pseudo : 3 à 20 caractères (lettres, chiffres, _ ou -)."
        if len(password) < 6:
            return False, "Mot de passe : 6 caractères minimum."
        key = username.lower()
        if key in self.data["users"]:
            return False, "Ce nom d'utilisateur est déjà pris."
        salt = secrets.token_bytes(16)
        self.data["users"][key] = {
            "name": username, "salt": salt.hex(),
            "hash": self._hash(password, salt).hex(),
            "created": time.time(), "license": None,
            "usage": {"date": "", "count": 0},
        }
        self.save()
        return True, username

    def login(self, username, password):
        key = username.lower()
        f = self.fails.get(key, {"n": 0, "until": 0})
        if f["until"] > time.time():
            return False, f"Trop d'essais. Réessaie dans {int(f['until'] - time.time()) + 1} s."
        u = self.data["users"].get(key)
        salt = bytes.fromhex(u["salt"]) if u else b"\x00" * 16
        h = self._hash(password, salt).hex()
        if not u or not hmac.compare_digest(h, u["hash"]):
            f["n"] += 1
            if f["n"] >= 5:
                f = {"n": 0, "until": time.time() + 30}
            self.fails[key] = f
            return False, "Identifiants incorrects."
        self.fails.pop(key, None)
        return True, u["name"]

    # ── licences
    def active_license(self, username):
        u = self.data["users"].get((username or "").lower())
        lic = u.get("license") if u else None
        if lic and lic["expires"] > time.time():
            return lic
        return None

    def redeem(self, username, key):
        parsed = parse_key(key)
        if not parsed:
            return False, "Clé invalide."
        plan, days, raw = parsed
        uname = username.lower()
        h = hashlib.sha256(raw.encode()).hexdigest()
        owner = self.data["used_keys"].get(h)
        if owner == uname:
            return False, "Tu as déjà activé cette clé."
        if owner:
            return False, "Cette clé a déjà été utilisée."
        user = self.data["users"][uname]
        now = time.time()
        cur = self.active_license(username)
        base = cur["expires"] if cur and cur["plan"] == plan else now
        expires = base + days * 86400
        user["license"] = {"plan": plan, "expires": expires, "activated": now}
        self.data["used_keys"][h] = uname
        self.save()
        return True, f"Licence {plan} activée."

    def scans_left(self, username):
        lic = self.active_license(username)
        if not lic:
            return 0
        limit = PLAN_LIMITS.get(lic["plan"])
        if limit is None:
            return None
        usage = self.data["users"][username.lower()].get("usage", {})
        if usage.get("date") != datetime.now().strftime("%Y-%m-%d"):
            return limit
        return max(0, limit - usage.get("count", 0))

    def consume_scan(self, username):
        lic = self.active_license(username)
        if not lic:
            return False, "Licence inactive."
        limit = PLAN_LIMITS.get(lic["plan"])
        if limit is None:
            return True, ""
        user = self.data["users"][username.lower()]
        today = datetime.now().strftime("%Y-%m-%d")
        usage = user.get("usage") or {}
        if usage.get("date") != today:
            usage = {"date": today, "count": 0}
        if usage["count"] >= limit:
            return False, f"Quota journalier atteint ({limit} scans). Reviens demain ou passe à PRO."
        usage["count"] += 1
        user["usage"] = usage
        self.save()
        return True, ""


# ───────────────────────── Dropdown animé ─────────────────────────
_ICON_CACHE = {}


def icon_img(name, size=20):
    """Icône (CTkImage) d'un type de recherche, depuis ICON_B64."""
    key = (name, size)
    if key not in _ICON_CACHE:
        from PIL import Image as _I
        import base64 as _b, io as _io
        im = _I.open(_io.BytesIO(_b.b64decode("".join(ICON_B64[name]))))
        im = im.convert("RGBA")
        _ICON_CACHE[key] = ctk.CTkImage(light_image=im, dark_image=im, size=(size, size))
    return _ICON_CACHE[key]


class SmoothDropdown(ctk.CTkFrame):
    """Menu déroulant arrondi : chevron qui pivote, ouverture fluide (fondu + déploiement),
    items en cascade, survol animé. Remplace CTkComboBox."""
    KEY = "#010203"            # couleur transparente (Windows)
    ICONS = {"TÉLÉPHONE": "📞", "EMAIL": "✉", "SNAPCHAT": "👻", "NOM/PRENOM": "👤"}
    ROW_H = 42

    def __init__(self, master, app, variable, values, width=176, height=56, enabled=True):
        super().__init__(master, width=width, height=height, corner_radius=16,
                         border_width=1, fg_color="#08080a", border_color=BORDER)
        self.app, self.var, self.values = app, variable, values
        self.w, self.h = width, height
        self.enabled = enabled
        self.popup = None
        self.is_open = False
        self._angle = 0.0
        self._closing = False
        self.pack_propagate(False)

        self.icon = ctk.CTkLabel(self, text="", image=icon_img(variable.get()),
                                 width=24)
        self.icon.pack(side="left", padx=(16, 0))
        self.label = ctk.CTkLabel(self, text="", font=(MONO, 12, "bold"),
                                  text_color=TXT, anchor="w")
        self.label.pack(side="left", padx=(8, 0), fill="x", expand=True)
        self.chev = tk.Canvas(self, width=22, height=22, bg="#08080a",
                              highlightthickness=0, bd=0)
        self.chev.pack(side="right", padx=(0, 14))
        self._draw_chevron(0.0)
        self._refresh()
        self.var.trace_add("write", lambda *a: self._refresh())

        for w in (self, self.icon, self.label, self.chev):
            w.bind("<Button-1>", lambda e: self.toggle(), add="+")
            w.bind("<Enter>", lambda e: self._hover(True), add="+")
            w.bind("<Leave>", lambda e: self._hover(False), add="+")
            try:
                w.configure(cursor="hand2" if enabled else "arrow")
            except tk.TclError:
                pass
        self.set_enabled(enabled)

    # ── API compatible
    def get(self):
        return self.var.get()

    def set(self, v):
        self.var.set(v)

    def set_enabled(self, on):
        self.enabled = on
        c = TXT if on else DIM
        self.label.configure(text_color=c)
        pass

    # ── rendu
    def _refresh(self):
        v = self.var.get()
        try:
            self.label.configure(text=v)
            self.icon.configure(image=icon_img(v), text="")
        except tk.TclError:
            pass

    def _draw_chevron(self, t):
        c = self.chev
        c.delete("all")
        a = math.pi * t
        pts = []
        for x, y in ((5, 8), (11, 14), (17, 8)):
            dx, dy = x - 11, y - 11
            pts += [11 + dx * math.cos(a) - dy * math.sin(a),
                    11 + dx * math.sin(a) + dy * math.cos(a)]
        col = mix(MUTED, WHITE, 0.4 + 0.6 * t)
        c.create_line(*pts, fill=col, width=2, capstyle="round", joinstyle="round")

    def _hover(self, on):
        if not self.enabled or self.is_open:
            return
        a, b = (BORDER, "#4a4a52") if on else ("#4a4a52", BORDER)
        self.app.glow(self, a, b, 160)

    # ── ouverture / fermeture
    def toggle(self):
        if not self.enabled or self._closing:
            return
        self.close() if self.is_open else self.open()

    def open(self):
        if self.is_open:
            return
        self.is_open = True
        root = self.winfo_toplevel()
        n = len(self.values)
        full = n * self.ROW_H + 16
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.h + 8

        pop = tk.Toplevel(root)
        pop.withdraw()
        pop.overrideredirect(True)
        pop.configure(bg=self.KEY)
        try:
            pop.attributes("-topmost", True)
            pop.attributes("-transparentcolor", self.KEY)
            pop.attributes("-alpha", 0.0)
        except tk.TclError:
            pass
        self.popup = pop

        card = ctk.CTkFrame(pop, width=self.w, height=full, corner_radius=18,
                            border_width=1, border_color="#2a2a30",
                            fg_color="#0c0c0f", bg_color=self.KEY)
        card.place(x=0, y=0)
        card.pack_propagate(False)

        self.rows = []
        cur = self.var.get()
        for i, v in enumerate(self.values):
            row = ctk.CTkButton(
                card, text="", width=self.w - 16, height=self.ROW_H - 4, corner_radius=12,
                fg_color="#0c0c0f", hover=False, anchor="w",
                image=icon_img(v), compound="left",
                text_color="#0c0c0f", font=(MONO, 12, "bold"),
                command=lambda v=v: self._pick(v))
            row.place(x=8, y=8 + i * self.ROW_H)
            row._kzfx = True
            row._val = v
            row._sel = (v == cur)
            row._bg = "#0c0c0f"
            row._fg = WHITE if row._sel else "#b4b4bb"
            row.configure(text=f"   {v}" + ("      ✓" if row._sel else ""))
            row.bind("<Enter>", lambda e, r=row: self._row_hover(r, True), add="+")
            row.bind("<Leave>", lambda e, r=row: self._row_hover(r, False), add="+")
            self.rows.append(row)
            # apparition en cascade
            self.after(40 + i * 45, lambda r=row: self._row_in(r))

        pop.geometry(f"{self.w}x1+{x}+{y}")
        pop.deiconify()
        pop.lift()

        self.app.glow(self, BORDER, "#8a8a92", 180)

        def upd(t):
            if not self.popup:
                return
            hh = max(1, int(full * t))
            pop.geometry(f"{self.w}x{hh}+{x}+{y + int((1 - t) * -6)}")
            try:
                pop.attributes("-alpha", min(1.0, t * 1.2))
            except tk.TclError:
                pass
            self._draw_chevron(t)
        self.app.animate_value((id(self), "dd"), 260, upd, ease=lambda t: 1 - (1 - t) ** 4)

        root.bind("<Button-1>", self._outside, add="+")
        root.bind("<Configure>", lambda e: self._soft_close(), add="+")
        root.bind("<Escape>", lambda e: self.close(), add="+")
        pop.bind("<Escape>", lambda e: self.close())

    def _row_in(self, row):
        if not self.popup:
            return
        self.app.animate_value(
            (id(row), "in"), 220,
            lambda t: row.configure(text_color=mix("#0c0c0f", row._fg, t)))

    def _row_hover(self, row, on):
        if not self.popup:
            return
        a = row.cget("fg_color")
        b = "#1b1b21" if on else "#0c0c0f"
        c0, c1 = row._fg, (WHITE if on else ("#b4b4bb" if not row._sel else WHITE))
        row._fg = c1
        self.app.animate_value(
            (id(row), "hv"), 140,
            lambda t: row.configure(fg_color=mix(a, b, t), text_color=mix(c0, c1, t)))

    def _pick(self, v):
        self.var.set(v)
        self.close()

    def _outside(self, e):
        if self.is_open:
            self.close()

    def _soft_close(self):
        if self.is_open and not self._closing:
            self.close(fast=True)

    def close(self, fast=False):
        if not self.is_open or self._closing:
            return
        self._closing = True
        pop = self.popup
        root = self.winfo_toplevel()
        try:
            full = pop.winfo_height()
            x, y = pop.winfo_x(), pop.winfo_y()
        except tk.TclError:
            full, x, y = 1, 0, 0

        def upd(t):
            hh = max(1, int(full * (1 - t)))
            try:
                pop.geometry(f"{self.w}x{hh}+{x}+{y}")
                pop.attributes("-alpha", max(0.0, 1 - t))
            except tk.TclError:
                pass
            self._draw_chevron(1 - t)

        def fin():
            self.is_open = False
            self._closing = False
            try:
                pop.destroy()
            except tk.TclError:
                pass
            self.popup = None
            self.app.glow(self, "#8a8a92", BORDER, 200)
        self.app.animate_value((id(self), "dd"), 90 if fast else 170, upd, fin)


class kzSINTApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("kzSINT - OSINT Tool 🎃")
        self.geometry("1280x800")
        self.minsize(1000, 700)
        self.configure(fg_color=BG)

        self.store = Store()
        self.current_user = None
        self.auth_mode = "login"
        self.header_visible = False
        self.plan_chip = None
        self.search_type = ctk.StringVar(value="TÉLÉPHONE")
        self.cart = []
        self.current_page = None
        self.page_widgets = []
        self.layouts = []
        self.scanning = False
        self.terminal_output = None
        self.chat_scroll = None
        self.last_user_message = ""

        # animations
        self._anims = {}
        self._pending = set()
        self._animating = set()
        self.place_kw = {}
        self.page_gen = 0
        self.nav_state = {}
        self.card_intro = 1.0
        self.typing_holder = None
        self.term_queue = []
        self.term_cur = ""
        self.term_typing = False
        self.term_gen = 0

        # état de la carte 3D
        self.card_tilt = [0.0, 0.0]
        self.card_dirty = True
        self.cw = self.ch = 400
        self.ccx = self.ccy = 300

        # étoiles
        self.star_data = [
            (random.random(), random.random(),
             random.choice([0.8, 1, 1, 1.4, 1.8]), random.randint(70, 200))
            for _ in range(150)
        ]
        self.star_items = []
        self.meteor = None

        self.create_header()
        self.create_stage()
        self.show_page("LOGIN")
        self.animate()

    # ───────────────────────── Header ─────────────────────────
    def icon_btn(self, parent, text, cmd, w=42, color=TXT):
        return ctk.CTkButton(parent, text=text, width=w, height=42, corner_radius=12,
                             fg_color="#0d0202", hover_color="#330000",
                             border_width=1, border_color="#ff6600",
                             text_color=color, font=(SANS, 15), command=cmd)

    def create_header(self):
        header = ctk.CTkFrame(self, height=66, fg_color=BG, corner_radius=0)
        header.pack_propagate(False)
        self.header = header
        self.header_sep = ctk.CTkFrame(self, height=1, fg_color="#ff6600", corner_radius=0)

        # Logo
        logo = ctk.CTkFrame(header, fg_color="transparent")
        logo.pack(side="left", padx=(34, 0))
        ctk.CTkLabel(logo, text="kz", font=(MONO, 22, "bold"),
                     text_color=WHITE).pack(side="left")
        ctk.CTkLabel(logo, text="SINT", font=(MONO, 22),
                     text_color=MUTED).pack(side="left")

        # Navigation (pilule centrale)
        nav = ctk.CTkFrame(header, fg_color=BG, border_width=1,
                           border_color="#ff6600", corner_radius=24)
        nav.place(relx=0.5, rely=0.5, anchor="center")
        self.nav_buttons = {}
        icons = {"SEARCH": "🔍", "BUY": "🛒", "HELP": "❓"}
        for page in ["SEARCH", "BUY", "HELP"]:
            btn = ctk.CTkButton(
                nav, text=f"{icons[page]}  {sp(page)}", font=(MONO, 12, "bold"),
                width=124, height=36, corner_radius=18,
                fg_color=BG, text_color=MUTED, hover=False,
                command=lambda p=page: self.show_page(p))
            btn.pack(side="left", padx=4, pady=5)
            self.nav_buttons[page] = btn
            btn._kzfx = True
            self.nav_state[page] = (BG, MUTED)

            def nav_hover(on, b=btn, pg=page):
                if self.current_page == pg:
                    return
                z = ("#330000", TXT) if on else (BG, MUTED)
                a = self.nav_state.get(pg, (BG, MUTED))
                self.nav_state[pg] = z
                self.animate_value(
                    (id(b), "nav"), 150,
                    lambda t: b.configure(fg_color=mix(a[0], z[0], t),
                                          text_color=mix(a[1], z[1], t)))
            btn.bind("<Enter>", lambda e, f=nav_hover: f(True), add="+")
            btn.bind("<Leave>", lambda e, f=nav_hover: f(False), add="+")

        # Zone utilisateur
        right = ctk.CTkFrame(header, fg_color="transparent")
        right.pack(side="right", padx=(0, 30))

        self.cart_btn = self.icon_btn(right, "🛒", self.show_cart)
        self.cart_btn.pack(side="left", padx=5)

        pill = ctk.CTkFrame(right, fg_color="#0a0a0d", border_width=1,
                            border_color="#ff6600", corner_radius=14, height=42)
        pill.pack(side="left", padx=5)
        ctk.CTkLabel(pill, text="●", font=(SANS, 10), text_color="#ff6600").pack(
            side="left", padx=(14, 6), pady=8)
        self.user_label = ctk.CTkLabel(pill, text=self.current_user or "",
                                       font=(MONO, 13, "bold"), text_color=TXT)
        self.user_label.pack(side="left", padx=(0, 16), pady=8)

        self.icon_btn(right, "↩", self.logout).pack(side="left", padx=5)
        self.apply_fx(self.header)

    # ───────────────────────── Fond étoilé ─────────────────────────
    def create_stage(self):
        self.stage = tk.Canvas(self, bg=BG, highlightthickness=0, bd=0)
        self.stage.pack(fill="both", expand=True)
        self.stage.bind("<Configure>", self.on_resize)

    def on_resize(self, e):
        c = self.stage
        c.delete("star")
        self.star_items = []
        for fx, fy, r, b in self.star_data:
            x, y = fx * e.width, fy * e.height
            it = c.create_oval(x - r, y - r, x + r, y + r,
                               fill=gray(b), outline="", tags="star")
            self.star_items.append((it, b))
        c.tag_lower("star")
        self.card_dirty = True
        self.apply_layout()

    def twinkle(self):
        if not self.star_items:
            return
        for _ in range(4):
            it, b = random.choice(self.star_items)
            self.stage.itemconfigure(it, fill=gray(b + random.randint(-45, 35)))

    def shoot(self):
        c = self.stage
        w, h = c.winfo_width(), c.winfo_height()
        c.delete("shoot")
        if self.meteor is None:
            if w > 50 and random.random() < 0.008:
                x = random.uniform(0.2, 0.9) * w
                y = random.uniform(0.0, 0.3) * h
                dx = random.choice([-1, 1])
                self.meteor = [x, y, dx * random.uniform(9, 13),
                               random.uniform(5, 8), 0]
            return
        m = self.meteor
        m[0] += m[2]
        m[1] += m[3]
        m[4] += 1
        if m[4] > 70 or m[0] < -50 or m[0] > w + 50 or m[1] > h + 50:
            self.meteor = None
            return
        x, y, vx, vy, _ = m
        ts = [0, 2, 4, 6, 9, 12]
        gs = [235, 175, 125, 85, 50]
        for i in range(len(gs)):
            c.create_line(x - vx * ts[i], y - vy * ts[i],
                          x - vx * ts[i + 1], y - vy * ts[i + 1],
                          fill=gray(gs[i]), width=1.5, tags="shoot")
        c.create_oval(x - 2, y - 2, x + 2, y + 2, fill=gray(240), outline="", tags="shoot")
        c.tag_lower("shoot")

    def animate(self):
        try:
            self.twinkle()
            self.shoot()
            if self.current_page == "BUY":
                self.update_card()
        except tk.TclError:
            pass
        self.after(33, self.animate)

    # ───────────────────────── Carte 3D "Kz" ─────────────────────────
    def card_geometry(self):
        w = max(self.stage.winfo_width(), 600)
        self.cw = min(w * 0.38, 580)
        self.ch = self.cw * 0.64
        self.ccx = w * 0.265
        self.ccy = 175 + self.ch / 2

    def proj(self, u, v):
        tx, ty = self.card_tilt
        d = -(u * tx + v * ty) * 0.10
        e = self.card_intro
        s = 1 / (1 + d) * (0.9 + 0.1 * e)
        x = u * self.cw / 2 * s
        y = v * self.ch / 2 * s
        a = -0.035 + tx * 0.02
        ca, sa = math.cos(a), math.sin(a)
        return (self.ccx + x * ca - y * sa + tx * 8,
                self.ccy + x * sa + y * ca + ty * 6 + (1 - e) * 34)

    def rrect(self, u0, v0, u1, v1, r_px, n=6):
        ru = r_px / (self.cw / 2)
        rv = r_px / (self.ch / 2)
        corners = [(u1 - ru, v0 + rv, -90), (u1 - ru, v1 - rv, 0),
                   (u0 + ru, v1 - rv, 90), (u0 + ru, v0 + rv, 180)]
        pts = []
        for cu, cv, start in corners:
            for i in range(n + 1):
                ang = math.radians(start + 90 * i / n)
                pts.append(self.proj(cu + ru * math.cos(ang), cv + rv * math.sin(ang)))
        return [coord for p in pts for coord in p]

    def draw_card(self):
        c = self.stage
        c.delete("card")
        self.card_geometry()
        cw = self.cw

        tx, ty = self.card_tilt
        OR = "#ff7a2e"

        # halo orangé + corps (dégradé bord chaud → centre sombre)
        c.create_polygon(self.rrect(-1.05, -1.06, 1.05, 1.07, 40),
                         fill="#0a0604", outline="", tags="card")
        layers = 9
        for k in range(layers):
            t = k / (layers - 1)
            ins = 0.0 + k * 0.012
            col = mix("#2a1708", "#0e0a08", ease_out(t))
            c.create_polygon(self.rrect(-1 + ins, -1 + ins, 1 - ins, 1 - ins, max(14, 38 - k * 1.2)),
                             fill=col, outline="#7a431a" if k == 0 else "", width=1.5,
                             tags="card")

        # reflet diagonal (suit l'inclinaison)
        sh = 0.30 + tx * 0.35
        for i, (w_, col) in enumerate(((0.34, "#15100c"), (0.26, "#1c1510"),
                                       (0.18, "#2a2018"), (0.10, "#3b2e22"),
                                       (0.045, "#52412f"))):
            top0, top1 = sh - w_ / 2 + 0.20, sh + w_ / 2 + 0.20
            bot0, bot1 = sh - w_ / 2 - 0.40, sh + w_ / 2 - 0.40
            pts = [self.proj(top0, -0.96), self.proj(top1, -0.96),
                   self.proj(bot1, 0.96), self.proj(bot0, 0.96)]
            c.create_polygon([q for p in pts for q in p], fill=col, outline="", tags="card")

        # liseré chaud en haut
        x1, y1 = self.proj(-0.78, -0.975)
        x2, y2 = self.proj(0.78, -0.975)
        c.create_line(x1, y1, x2, y2, fill="#ff8a3c", width=1, tags="card")

        f = lambda k, w_="bold", fam=MONO: (fam, -max(8, int(cw * k)), w_)

        # puce dégradée
        c.create_polygon(self.rrect(-0.80, -0.62, -0.46, -0.20, 8),
                         fill="#c9561f", outline="#ff9a52", width=1, tags="card")
        c.create_polygon(self.rrect(-0.78, -0.59, -0.48, -0.23, 6),
                         fill="#f08a3c", outline="", tags="card")
        c.create_polygon(self.rrect(-0.78, -0.59, -0.48, -0.40, 6),
                         fill="#f79c4f", outline="", tags="card")
        for (ua, va, ub, vb) in ((-0.78, -0.41, -0.48, -0.41),
                                 (-0.675, -0.59, -0.675, -0.23),
                                 (-0.585, -0.59, -0.585, -0.23)):
            xa, ya = self.proj(ua, va)
            xb, yb = self.proj(ub, vb)
            c.create_line(xa, ya, xb, yb, fill="#b8501c", width=1.5, tags="card")
        c.create_polygon(self.rrect(-0.70, -0.50, -0.56, -0.32, 3),
                         fill="", outline="#b8501c", width=1.5, tags="card")

        # « KZ API »
        c.create_text(*self.proj(0.88, -0.70), text=sp("KZ CARD"), anchor="e",
                      fill="#b8662c", font=f(0.021), tags="card")

        # barres
        c.create_polygon(self.rrect(-0.81, 0.36, -0.12, 0.45, 5),
                         fill="#7d5230", outline="", tags="card")
        c.create_polygon(self.rrect(-0.81, 0.54, -0.39, 0.61, 4),
                         fill="#5e3d24", outline="", tags="card")

        # pastille « K »
        rpx = cw * 0.085
        ccu, ccv = 0.62, 0.50

        def disc(dr, du=0.0, dv=0.0, n=36):
            pts = []
            for i in range(n):
                ang = 2 * math.pi * i / n
                pts.append(self.proj(ccu + du + (rpx * dr * math.cos(ang)) / (cw / 2),
                                     ccv + dv + (rpx * dr * math.sin(ang)) / (self.ch / 2)))
            return [q for p in pts for q in p]
        c.create_polygon(disc(1.18), fill="#3a1d0a", outline="", tags="card")
        c.create_polygon(disc(1.0), fill="#e8702a", outline="", tags="card")
        c.create_polygon(disc(0.86, -0.01, -0.03), fill="#fa9448", outline="", tags="card")
        c.create_polygon(disc(0.60, -0.02, -0.06), fill="#ffb066", outline="", tags="card")
        c.create_polygon(disc(0.92), fill="", outline="#ff9a52", width=1, tags="card")
        c.create_text(*self.proj(ccu, ccv), text="K", fill="#1a0d05",
                      font=(SANS, -int(cw * 0.085), "bold"), tags="card")

        # légende sous la carte
        cy = self.ccy + self.ch / 2 + 62 + (1 - self.card_intro) * 34
        c.create_text(self.ccx, cy, text=sp("LA CARTE ") + "  " + sp("kzSINT"),
                      fill=TXT, font=(MONO, 13, "bold"), tags="card")
        c.create_text(self.ccx, cy + 48,
                      text="Accès premium à tous les modules, priorité de scan et support dédié.\n"
                           "Bouge ta souris sur la carte, elle te suit.",
                      fill=MUTED, font=(SANS, 11), justify="center", tags="card")
        c.tag_lower("shoot")
        c.tag_lower("star")
        self.card_dirty = False

    def update_card(self):
        c = self.stage
        w, h = max(c.winfo_width(), 1), max(c.winfo_height(), 1)
        px = c.winfo_pointerx() - c.winfo_rootx()
        py = c.winfo_pointery() - c.winfo_rooty()
        tx = max(-1.0, min(1.0, (px - self.ccx) / (w * 0.5)))
        ty = max(-1.0, min(1.0, (py - self.ccy) / (h * 0.5)))
        cx, cy = self.card_tilt
        nx = cx + (tx - cx) * 0.12
        ny = cy + (ty - cy) * 0.12
        if abs(nx - cx) + abs(ny - cy) > 0.002 or self.card_dirty:
            self.card_tilt = [nx, ny]
            self.draw_card()

    # ───────────────────────── Pages ─────────────────────────
    def put(self, widget, **place):
        widget.place(**place)
        self.place_kw[id(widget)] = dict(place)
        self.page_widgets.append(widget)
        return widget

    def put_box(self, widget, x, y, wfn, hfn):
        """Place un widget CTk avec une taille calculée (width/height interdits dans place())."""
        self.page_widgets.append(widget)
        self.layouts.append((widget, x, y, wfn, hfn))
        self.apply_layout()
        return widget

    def apply_layout(self):
        W = max(self.stage.winfo_width(), 1000)
        H = max(self.stage.winfo_height(), 700)
        for widget, x, y, wfn, hfn in self.layouts:
            try:
                kw = {}
                if wfn:
                    kw["width"] = max(60, int(wfn(W)))
                if hfn:
                    kw["height"] = max(60, int(hfn(H)))
                widget.configure(**kw)
                if id(widget) in self._pending or id(widget) in self._animating:
                    continue
                widget.place(x=x(W) if callable(x) else x, y=y)
            except tk.TclError:
                pass

    def page_title(self, title, subtitle):
        self.put(ctk.CTkLabel(self.stage, text="/ /  " + " ".join(title),
                              font=(MONO, 26, "bold"), text_color=WHITE,
                              fg_color=BG), x=44, y=34)
        self.put(ctk.CTkLabel(self.stage, text=subtitle, font=(SANS, 13),
                              text_color=MUTED, fg_color=BG), x=46, y=86)

    def show_page(self, name, soft=False):
        if name != "LOGIN" and not self.current_user:
            name = "LOGIN"
        self.page_gen += 1
        for w in self.page_widgets:
            try:
                w.destroy()
            except tk.TclError:
                pass
        self.page_widgets = []
        self.layouts = []
        self.place_kw = {}
        self._pending = set()
        self._animating = set()
        self.terminal_output = None
        self.chat_scroll = None
        self.plan_chip = None
        self.typing_holder = None
        self.term_gen += 1
        self.term_queue = []
        self.term_cur = ""
        self.term_typing = False
        self.stage.delete("card")
        self.current_page = name
        self.card_tilt = [0.0, 0.0]
        self.card_dirty = True

        self.set_nav(name)

        if name == "LOGIN":
            self.hide_header()
            self.build_login()
        else:
            self.show_header()
            if name == "SEARCH":
                self.build_search()
            elif name == "BUY":
                self.build_buy()
            elif name == "HELP":
                self.build_help()

        for w in self.page_widgets:
            if isinstance(w, ctk.CTkButton):
                self.fx_button(w)
            self.apply_fx(w)
        self.intro(soft)

    # ───────────────────────── Moteur d'animation ─────────────────────────
    def animate_value(self, key, dur, update, done=None, ease=ease_out):
        """Anime une valeur de 0 à 1 en `dur` ms. Une nouvelle animation de même clé remplace l'ancienne."""
        old = self._anims.pop(key, None)
        if old is not None:
            try:
                self.after_cancel(old)
            except (tk.TclError, ValueError):
                pass
        t0 = time.perf_counter()

        def tick():
            t = min(1.0, (time.perf_counter() - t0) * 1000 / dur)
            try:
                update(ease(t))
            except tk.TclError:
                self._anims.pop(key, None)
                return
            if t < 1.0:
                self._anims[key] = self.after(16, tick)
            else:
                self._anims.pop(key, None)
                if done:
                    try:
                        done()
                    except tk.TclError:
                        pass
        tick()

    def set_nav(self, name):
        for n, btn in self.nav_buttons.items():
            tgt = (WHITE, "#0a0a0a") if n == name else (BG, MUTED)
            cur = self.nav_state.get(n, (BG, MUTED))
            self.nav_state[n] = tgt
            self.animate_value(
                (id(btn), "nav"), 240,
                lambda t, b=btn, a=cur, z=tgt: b.configure(
                    fg_color=mix(a[0], z[0], t), text_color=mix(a[1], z[1], t)))

    def fx_button(self, btn):
        """Survol / clic fluides sur un bouton (transitions de couleur)."""
        if getattr(btn, "_kzfx", False):
            return
        try:
            base = btn.cget("fg_color")
        except tk.TclError:
            return
        if not (isinstance(base, str) and base.startswith("#")):
            return
        btn._kzfx = True
        r, g, b = hex_rgb(base)
        lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
        if lum > 0.6:
            hover, press = "#ffffff", mix(base, "#000000", 0.25)
        else:
            hover, press = mix(base, "#ffffff", 0.07), mix(base, "#ffffff", 0.16)
        state = {"cur": base}

        def go(target, dur=160):
            start = state["cur"]

            def upd(t):
                c = mix(start, target, t)
                state["cur"] = c
                btn.configure(fg_color=c)
            self.animate_value((id(btn), "fx"), dur, upd)

        def enabled():
            try:
                return btn.cget("state") != "disabled"
            except tk.TclError:
                return False

        btn._kz_go = go
        btn._kz_sync = lambda c: state.__setitem__("cur", c)
        try:
            btn.configure(hover=False)
        except (tk.TclError, ValueError):
            pass
        btn.bind("<Enter>", lambda e: enabled() and go(hover, 140), add="+")
        btn.bind("<Leave>", lambda e: enabled() and go(base, 220), add="+")
        btn.bind("<ButtonPress-1>", lambda e: enabled() and go(press, 60), add="+")
        btn.bind("<ButtonRelease-1>", lambda e: enabled() and go(hover, 180), add="+")

    def apply_fx(self, root):
        try:
            children = root.winfo_children()
        except tk.TclError:
            return
        for w in children:
            if isinstance(w, ctk.CTkButton):
                self.fx_button(w)
            self.apply_fx(w)

    def glow(self, widget, a, b, dur=180):
        self.animate_value((id(widget), "glow"), dur,
                           lambda t: widget.configure(border_color=mix(a, b, t)))

    def fade_text(self, label, text, color, dur=240):
        try:
            label.configure(text=text)
        except tk.TclError:
            return
        self.animate_value((id(label), "txt"), dur,
                           lambda t: label.configure(text_color=mix(BG, color, t)))

    def shake(self, w):
        kw = self.place_kw.get(id(w))
        if not kw:
            return
        seq = [-10, 10, -8, 8, -5, 5, -2, 0]

        def step(i):
            try:
                k = dict(kw)
                k["x"] = k.get("x", 0) + seq[i]
                w.place(**k)
                if i + 1 < len(seq):
                    self.after(32, lambda: step(i + 1))
            except tk.TclError:
                pass
        step(0)

    def _cget(self, w, prop):
        try:
            v = w.cget(prop)
        except (tk.TclError, ValueError, AttributeError):
            return None
        return v if isinstance(v, str) and v.startswith("#") and len(v) == 7 else None

    def fade_targets(self, root):
        out = []

        def walk(w):
            if isinstance(w, ctk.CTkScrollableFrame):
                return
            if isinstance(w, ctk.CTkLabel):
                c = self._cget(w, "text_color")
                if c:
                    out.append((w, "text_color", c))
            elif isinstance(w, ctk.CTkButton):
                for prop in ("fg_color", "text_color"):
                    c = self._cget(w, prop)
                    if c:
                        out.append((w, prop, c))
            elif isinstance(w, ctk.CTkFrame):
                try:
                    bw = w.cget("border_width")
                except tk.TclError:
                    bw = 0
                c = self._cget(w, "border_color") if bw else None
                if c:
                    out.append((w, "border_color", c))
                f = self._cget(w, "fg_color")          # cadres clairs (ex. bulle « vous »)
                if f and sum(hex_rgb(f)) > 300:
                    out.append((w, "fg_color", f))
            try:
                for ch in w.winfo_children():
                    walk(ch)
            except tk.TclError:
                pass
        walk(root)
        return out

    def fade_in(self, root, dur=280, extra=None, done=None, gen=None, targets=None):
        """Fondu d'apparition (couleurs BG → couleurs finales) du widget et de son contenu."""
        if targets is None:
            targets = self.fade_targets(root)

        def upd(t):
            if gen is not None and gen != self.page_gen:
                raise tk.TclError("page changée")
            if extra:
                extra(t)
            for w, prop, final in targets:
                try:
                    w.configure(**{prop: final if t >= 1 else mix(BG, final, t)})
                except tk.TclError:
                    pass

        def fin():
            for w, prop, final in targets:
                if prop == "fg_color" and hasattr(w, "_kz_sync"):
                    w._kz_sync(final)
            if done:
                done()
        self.animate_value((id(root), "fade"), dur, upd, fin)

    def _target_place(self, w):
        for widget, x, y, wfn, hfn in self.layouts:
            if widget is w:
                W = max(self.stage.winfo_width(), 1000)
                return {"x": x(W) if callable(x) else x, "y": y}
        kw = self.place_kw.get(id(w))
        return dict(kw) if kw else None

    def intro(self, soft=False):
        """Entrée de page : chaque élément glisse vers le haut en fondu, en cascade."""
        gen = self.page_gen
        items = []
        for w in self.page_widgets:
            kw = self._target_place(w)
            if kw is not None:
                items.append((w, kw))
        for w, kw in items:
            self._pending.add(id(w))
            try:
                w.place_forget()
            except tk.TclError:
                pass
        off0 = 8 if soft else 22
        dur = 240 if soft else 340
        for i, (w, kw) in enumerate(items):
            delay = 0 if soft else min(i * 45, 300)
            self.after(delay, lambda w=w, kw=kw: self._reveal(w, kw, gen, off0, dur))

    def _reveal(self, w, kw, gen, off0, dur):
        if gen != self.page_gen:
            return
        wid = id(w)
        self._pending.discard(wid)
        self._animating.add(wid)

        def slide(t):
            k = dict(kw)
            k["y"] = k.get("y", 0) + (1 - t) * off0
            w.place(**k)

        def finish():
            self._animating.discard(wid)
            w.place(**(self._target_place(w) or kw))

        self.fade_in(w, dur, extra=slide, done=finish, gen=gen)

    # ── chat : bulle « écrit… »
    def _scroll_chat(self):
        self.after(60, lambda: self.chat_scroll is not None
                   and self.chat_scroll.winfo_exists()
                   and self.chat_scroll._parent_canvas.yview_moveto(1.0))

    def show_typing(self):
        if self.typing_holder is not None or self.chat_scroll is None:
            return
        try:
            holder = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
            holder.pack(fill="x", pady=5)
            bubble = ctk.CTkFrame(holder, corner_radius=14, border_width=1,
                                  fg_color="#121215", border_color="#25252a")
            bubble.pack(anchor="w", padx=8)
            lab = ctk.CTkLabel(bubble, text="●  ○  ○", font=(SANS, 10), text_color=MUTED)
            lab.pack(padx=18, pady=10)
            self.typing_holder = holder
            self._scroll_chat()
            frames = ["●  ○  ○", "○  ●  ○", "○  ○  ●"]

            def tick(n=0):
                try:
                    if self.typing_holder is not holder or not holder.winfo_exists():
                        return
                    lab.configure(text=frames[n % 3])
                    self.after(260, lambda: tick(n + 1))
                except tk.TclError:
                    pass
            tick()
        except tk.TclError:
            self.typing_holder = None

    def hide_typing(self):
        h, self.typing_holder = self.typing_holder, None
        if h is not None:
            try:
                h.destroy()
            except tk.TclError:
                pass

    def _bot_reply(self, response):
        self.hide_typing()
        self.add_bubble("kzBot", response)

    # ───────────────────────── AUTH ─────────────────────────
    def show_header(self):
        if not self.header_visible:
            self.header.pack(fill="x", before=self.stage)
            self.header_sep.pack(fill="x", before=self.stage)
            self.header_visible = True

    def hide_header(self):
        if self.header_visible:
            self.header.pack_forget()
            self.header_sep.pack_forget()
            self.header_visible = False

    def logout(self):
        self.current_user = None
        self.cart = []
        self.refresh_cart_badge()
        self.auth_mode = "login"
        self.show_page("LOGIN")

    def on_login(self, username):
        self.current_user = username
        self.user_label.configure(text=username)
        self.show_page("SEARCH")

    def set_auth_mode(self, mode):
        self.auth_mode = mode
        self.show_page("LOGIN", soft=True)

    def field(self, parent, icon, placeholder, secret=False):
        box = ctk.CTkFrame(parent, fg_color="#08080a", border_width=1,
                           border_color="#222226", corner_radius=14, height=52)
        box.pack_propagate(False)
        ctk.CTkLabel(box, text=icon, font=(SANS, 14), text_color=MUTED,
                     width=30).pack(side="left", padx=(14, 0))
        entry = ctk.CTkEntry(box, fg_color="transparent", border_width=0,
                             placeholder_text=placeholder, placeholder_text_color=DIM,
                             text_color=TXT, font=(SANS, 14), show="•" if secret else "")
        entry.pack(side="left", fill="both", expand=True, padx=(4, 12))
        entry.bind("<FocusIn>", lambda e: self.glow(box, "#222226", "#8a8a92"))
        entry.bind("<FocusOut>", lambda e: self.glow(box, "#8a8a92", "#222226"))
        return box, entry

    def small_label(self, parent, text, pady):
        ctk.CTkLabel(parent, text=sp(text), font=(MONO, 10, "bold"),
                     text_color=MUTED, anchor="w").pack(fill="x", padx=38, pady=pady)

    def build_login(self):
        register = self.auth_mode == "register"
        card = ctk.CTkFrame(self.stage, width=440, height=650 if register else 570,
                            fg_color="#08080b", border_width=1,
                            border_color="#26262b", corner_radius=26)
        card.pack_propagate(False)
        self.put(card, relx=0.5, rely=0.47, anchor="center")
        self.auth_card = card

        logo = ctk.CTkFrame(card, fg_color="transparent")
        logo.pack(pady=(34, 0))
        ctk.CTkLabel(logo, text="kz", font=(SANS, 36, "bold"), text_color=WHITE).pack(side="left")
        ctk.CTkLabel(logo, text="SINT", font=(SANS, 36, "bold"), text_color="#b4b4ba").pack(side="left")
        ctk.CTkLabel(card, text="\u2005".join("ESPACE MEMBRE"), font=(MONO, 11, "bold"),
                     text_color=MUTED).pack(pady=(4, 0))

        tabs = ctk.CTkFrame(card, fg_color=BG, border_width=1,
                            border_color="#ff6600", corner_radius=16)
        tabs.pack(fill="x", padx=36, pady=(22, 0))
        for mode, label in (("login", "CONNEXION"), ("register", "CRÉER UN COMPTE")):
            active = self.auth_mode == mode
            ctk.CTkButton(tabs, text=sp(label), font=(MONO, 11, "bold"), height=38,
                          corner_radius=12,
                          fg_color=WHITE if active else "transparent",
                          hover_color=WHITE if active else "#330000",
                          text_color="#0a0a0a" if active else "#b4b4ba",
                          command=lambda m=mode: self.set_auth_mode(m)).pack(
                side="left", expand=True, fill="x", padx=5, pady=5)

        self.small_label(card, "NOM D'UTILISATEUR", (22, 4))
        box, self.auth_user = self.field(card, "👤", "Ton pseudo")
        box.pack(fill="x", padx=36)

        self.small_label(card, "MOT DE PASSE", (14, 4))
        box, self.auth_pass = self.field(card, "🔒", "••••••••", secret=True)
        box.pack(fill="x", padx=36)

        self.auth_confirm = None
        if register:
            self.small_label(card, "CONFIRMER LE MOT DE PASSE", (14, 4))
            box, self.auth_confirm = self.field(card, "🔒", "••••••••", secret=True)
            box.pack(fill="x", padx=36)

        for e in (self.auth_user, self.auth_pass, self.auth_confirm):
            if e is not None:
                e.bind("<Return>", lambda ev: self.submit_auth())

        ctk.CTkButton(card, text=sp("CRÉER LE COMPTE" if register else "SE CONNECTER"),
                      font=(MONO, 12, "bold"), height=54, corner_radius=12,
                      fg_color=WHITE, hover_color=WHITE_H, text_color="#0a0a0a",
                      command=self.submit_auth).pack(fill="x", padx=36, pady=(20, 0))

        self.auth_status = ctk.CTkLabel(card, text="", font=(SANS, 12),
                                        text_color="#ff6b6b", wraplength=360)
        self.auth_status.pack(pady=(10, 0))

        ctk.CTkButton(card, font=(SANS, 12), height=28, fg_color="transparent",
                      hover_color="#330000", text_color=MUTED,
                      text="Déjà un compte ? Connecte-toi." if register
                      else "Pas encore de compte ? Crée-en un en quelques secondes.",
                      command=lambda: self.set_auth_mode("login" if register else "register")
                      ).pack(pady=(4, 0))

        self.put(ctk.CTkLabel(self.stage, text="kzSINT v1.3.0", font=(MONO, 10),
                              text_color="#ff6600", fg_color=BG),
                 relx=0.5, rely=1.0, y=-18, anchor="s")
        self.after(120, self.auth_user.focus)

    def auth_error(self, msg):
        self.fade_text(self.auth_status, msg, "#ff6b6b")
        self.shake(self.auth_card)

    def submit_auth(self):
        username = self.auth_user.get().strip()
        password = self.auth_pass.get()
        if not username or not password:
            self.auth_error("Remplis tous les champs.")
            return
        if self.auth_mode == "register":
            if password != self.auth_confirm.get():
                self.auth_error("Les mots de passe ne correspondent pas.")
                return
            ok, res = self.store.register(username, password)
        else:
            ok, res = self.store.login(username, password)
        if ok:
            self.on_login(res)
        else:
            self.auth_error(res)

    # ───────────────────────── SEARCH ─────────────────────────
    def build_search_row(self, enabled):
        combo = SmoothDropdown(
            self.stage, self, self.search_type,
            ["TÉLÉPHONE", "EMAIL", "SNAPCHAT", "NOM/PRENOM"],
            width=176, height=56, enabled=enabled)
        self.put(combo, x=46, y=132)

        self.target_entry = ctk.CTkEntry(
            self.stage, height=56, corner_radius=14, border_width=1,
            fg_color="#08080a", border_color=BORDER, text_color=TXT,
            placeholder_text="cible : pseudo, email, domaine...",
            placeholder_text_color=DIM, font=(MONO, 13),
            state="normal" if enabled else "disabled")
        self.put_box(self.target_entry, 232, 132, lambda W: W - (232 + 46 + 190 + 16), None)
        if enabled:
            self.target_entry.bind("<Return>", lambda e: self.start_scan())
            self.target_entry.bind("<FocusIn>", lambda e: self.glow(self.target_entry, BORDER, "#8a8a92"))
            self.target_entry.bind("<FocusOut>", lambda e: self.glow(self.target_entry, "#8a8a92", BORDER))

        self.scan_btn = ctk.CTkButton(
            self.stage, text=sp("SCANNER"), font=(MONO, 13, "bold"),
            width=190, height=56, corner_radius=14,
            fg_color=WHITE if enabled else "#330000", hover_color=WHITE_H,
            text_color="#0a0a0a", text_color_disabled="#55555b",
            state="normal" if enabled else "disabled", command=self.start_scan)
        self.put(self.scan_btn, relx=1.0, x=-46, y=132, anchor="ne")

    def plan_text(self):
        lic = self.store.active_license(self.current_user)
        if not lic:
            return ""
        t = f"●  PLAN {lic['plan']}"
        if lic["expires"] > time.time() + 20000 * 86400:
            t += "  ·  licence à vie"
        else:
            t += f"  ·  expire le {datetime.fromtimestamp(lic['expires']).strftime('%d/%m/%Y')}"
        limit = PLAN_LIMITS.get(lic["plan"])
        if limit:
            t += f"  ·  {self.store.scans_left(self.current_user)}/{limit} scans aujourd'hui"
        return t

    def refresh_plan_chip(self):
        try:
            if self.plan_chip is not None and self.plan_chip.winfo_exists():
                self.plan_chip.configure(text=self.plan_text())
        except tk.TclError:
            pass

    def build_search(self):
        lic = self.store.active_license(self.current_user)
        self.page_title("SEARCH",
                        "Recherche de renseignements en sources ouvertes — moteur d'analyse kzSINT")
        self.build_search_row(enabled=bool(lic))
        if not lic:
            self.build_locked()
            return

        self.plan_chip = self.put(
            ctk.CTkLabel(self.stage, text=self.plan_text(), font=(MONO, 11),
                         text_color=MUTED, fg_color=BG),
            relx=1.0, x=-46, y=92, anchor="ne")

        # Terminal
        term = ctk.CTkFrame(self.stage, fg_color="#07070a", border_width=1,
                            border_color="#202024", corner_radius=18)
        term.pack_propagate(False)
        self.put_box(term, 46, 212, lambda W: W * 0.6, lambda H: H - (212 + 40))

        bar = ctk.CTkFrame(term, fg_color="transparent", height=44)
        bar.pack(fill="x")
        for col in ("#330000", "#ffaa66", "#ff6600"):
            ctk.CTkLabel(bar, text="●", font=(SANS, 11), text_color=col).pack(
                side="left", padx=(14 if col == "#2a2a2e" else 2, 2), pady=10)
        ctk.CTkLabel(bar, text="kzSINT://terminal", font=(MONO, 12),
                     text_color=MUTED).pack(side="left", padx=12)
        ctk.CTkFrame(term, height=1, fg_color="#1a1a1e", corner_radius=0).pack(fill="x")

        self.terminal_output = ctk.CTkTextbox(
            term, font=(MONO, 12), fg_color="#07070a", text_color="#d6d6da",
            border_width=0, corner_radius=0, wrap="word",
            scrollbar_button_color="#222226", scrollbar_button_hover_color="#33333a")
        self.terminal_output.pack(fill="both", expand=True, padx=18, pady=(12, 16))
        self.terminal_output.insert("0.0", "$ en attente d'une cible...\n")
        self.terminal_output.configure(state="disabled")

    def build_locked(self):
        card = ctk.CTkFrame(self.stage, width=600, height=390, fg_color="#07070a",
                            border_width=1, border_color="#202024", corner_radius=18)
        card.pack_propagate(False)
        self.put(card, x=46, y=212)
        self.key_card = card

        ctk.CTkLabel(card, text="🔒", font=(SANS, 30), text_color=TXT).pack(pady=(26, 2))
        ctk.CTkLabel(card, text=sp("ACCÈS VERROUILLÉ"), font=(MONO, 14, "bold"),
                     text_color=WHITE).pack()
        ctk.CTkLabel(card, text="Une clé de licence active est requise pour utiliser "
                                "le moteur d'analyse kzSINT.",
                     font=(SANS, 12), text_color=MUTED, wraplength=480).pack(pady=(8, 18))

        box, self.key_entry = self.field(card, "🔑", "KZ-XXXX-XXXX-XXXX-XXXX")
        box.pack(fill="x", padx=50)
        self.key_entry.configure(font=(MONO, 14))
        self.key_entry.bind("<Return>", lambda e: self.activate_key())

        ctk.CTkButton(card, text=sp("ACTIVER LA CLÉ"), font=(MONO, 12, "bold"),
                      height=50, corner_radius=12, fg_color=WHITE, hover_color=WHITE_H,
                      text_color="#0a0a0a", command=self.activate_key).pack(
            fill="x", padx=50, pady=(16, 0))

        self.key_status = ctk.CTkLabel(card, text="", font=(SANS, 12),
                                       text_color="#ff6b6b", wraplength=480)
        self.key_status.pack(pady=(10, 0))

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(pady=(4, 0))
        ctk.CTkLabel(row, text="Pas de clé ?", font=(SANS, 12),
                     text_color=DIM).pack(side="left")
        ctk.CTkButton(row, text="Voir la boutique →", font=(SANS, 12, "bold"),
                      width=10, height=28, fg_color="transparent",
                      hover_color="#330000", text_color=TXT,
                      command=lambda: self.show_page("BUY")).pack(side="left", padx=4)

    def activate_key(self):
        ok, msg = self.store.redeem(self.current_user, self.key_entry.get())
        if ok:
            messagebox.showinfo("Clé activée", msg + "\nLa recherche est débloquée.")
            self.show_page("SEARCH")
        else:
            self.fade_text(self.key_status, msg, "#ff6b6b")
            self.shake(self.key_card)

    def start_scan(self):
        if self.scanning:
            return
        if not self.store.active_license(self.current_user):
            messagebox.showwarning("Licence", "Ta licence a expiré ou n'est pas activée.")
            self.show_page("SEARCH")
            return
        target = self.target_entry.get().strip()
        search_type = self.search_type.get()

        if not target:
            messagebox.showwarning("Attention", "Veuillez entrer une cible valide")
            return

        ok, msg = self.store.consume_scan(self.current_user)
        if not ok:
            messagebox.showwarning("Quota atteint", msg)
            return
        self.refresh_plan_chip()

        self.scanning = True
        self.scan_btn.configure(state="disabled", text=sp("SCAN"))
        go = getattr(self.scan_btn, "_kz_go", None)
        if go:
            go("#330000", 250)
        self.scan_dots()

        self.term_reset()
        for line in ("$ Initialisation du scan...",
                     f"$ Type: {search_type}",
                     f"$ Cible: {target}",
                     f"$ Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                     "$ " + "-" * 50):
            self.update_terminal(line)

        threading.Thread(target=self.run_scan, args=(target, search_type), daemon=True).start()

    def run_scan(self, target, search_type):
        self.after(0, self.update_terminal, "[*] Connexion à l'API OSINT...")
        
        try:
            api_key = "69db89a6e2048c4d485e35b4b25fd2e1"
            headers = {
                "X-API-Key": api_key
            }
            
            # Utiliser l'API spécifique Snapchat si demandé
            if search_type == "SNAPCHAT":
                api_url = "https://api.lookup2bz.xyz/api/v1/snapchat"
                params = {
                    "query": target
                }
                self.after(0, self.update_terminal, "[*] Recherche Snapchat...")
            else:
                api_url = "https://api.lookup2bz.xyz/api/v1/query"
                params = {
                    "query": target,
                    "limit": 150
                }
                self.after(0, self.update_terminal, "[*] Analyse des sources...")
            
            # Appel à l'API
            response = requests.get(api_url, params=params, headers=headers, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                
                self.after(0, self.update_terminal, f"[+] Connexion réussie")
                self.after(0, self.update_terminal, f"[+] Temps de réponse: {data.get('time_ms', 0)}ms")
                self.after(0, self.update_terminal, "\n" + "="*50)
                
                # Affichage selon le type de recherche
                if search_type == "SNAPCHAT":
                    self.after(0, self.display_snapchat_results, data)
                else:
                    count = data.get("count", 0)
                    results = data.get("results", [])
                    self.after(0, self.update_terminal, f"[+] {count} résultats trouvés")
                    self.after(0, self.display_structured_results, results, count)
                
            else:
                self.after(0, self.update_terminal, f"[!] Erreur API: {response.status_code}")
                self.after(0, self.update_terminal, f"[!] Message: {response.text}")
                self.after(0, self.end_scan)
            
        except requests.exceptions.Timeout:
            self.after(0, self.update_terminal, "[!] Timeout: La requête a pris trop de temps")
            self.after(0, self.end_scan)
        except requests.exceptions.RequestException as e:
            self.after(0, self.update_terminal, f"[!] Erreur de connexion: {str(e)}")
            self.after(0, self.end_scan)
        except Exception as e:
            self.after(0, self.update_terminal, f"[!] Erreur inattendue: {str(e)}")
            self.after(0, self.end_scan)
    
    def display_snapchat_results(self, data):
        """Affiche les résultats Snapchat de manière structurée"""
        success = data.get("success", False)
        query = data.get("query", "")
        result = data.get("result", {})
        
        if not success or not result:
            self.update_terminal("[!] Aucun résultat Snapchat trouvé")
            self.end_scan()
            return
        
        self.update_terminal(f"\n📱 RÉSULTATS SNAPCHAT")
        self.update_terminal(f"{'='*60}")
        self.update_terminal(f"Query: {query}\n")
        
        # Profil principal
        profile = result.get("profile", {})
        if profile:
            self.update_terminal("📁 PROFIL")
            self.update_terminal("-" * 40)
            self.update_terminal(f"  USERNAME: {profile.get('username', 'N/A')}")
            self.update_terminal(f"  USER ID: {profile.get('user_id', 'N/A')}")
            self.update_terminal(f"  VÉRIFIÉ: {'Oui' if profile.get('verified') else 'Non'}")
            self.update_terminal(f"  ÂGE DU COMPTE: {profile.get('account_age_days', 'N/A')} jours")
            self.update_terminal(f"  CRÉÉ LE: {profile.get('created_at', 'N/A')}")
            self.update_terminal(f"  MIS À JOUR: {profile.get('updated_at', 'N/A')}")
            self.update_terminal(f"  SPOTLIGHT HIGHLIGHTS: {'Oui' if profile.get('has_spotlight_highlights') else 'Non'}")
        
        # Anciens pseudos
        prevnames = result.get("prevname_result", [])
        if prevnames:
            self.update_terminal(f"\n📁 ANCIENS PSEUDOS ({len(prevnames)})")
            self.update_terminal("-" * 40)
            for i, prev in enumerate(prevnames):
                self.update_terminal(f"  [{i+1}] Username: {prev.get('username', 'N/A')}")
                self.update_terminal(f"      Display Name: {prev.get('display_name', 'N/A')}")
                self.update_terminal(f"      User ID: {prev.get('user_id', 'N/A')}")
        
        self.update_terminal(f"\n{'='*60}")
        self.update_terminal("[+] Scan Snapchat terminé avec succès")
        self.update_terminal("\n$ Profil Snapchat analysé")
        self.end_scan()
    
    def display_structured_results(self, results, total_count):
        """Affiche TOUS les résultats de manière structurée par catégories"""
        if not results:
            self.update_terminal("[!] Aucun résultat trouvé")
            self.end_scan()
            return
        
        self.update_terminal(f"\n📊 Affichage de {total_count} résultats complets\n")
        
        # Afficher chaque résultat individuellement
        for i, result in enumerate(results):
            source = result.get("source", "inconnu")
            data = result.get("data", {})
            
            if not isinstance(data, dict):
                continue
            
            self.update_terminal(f"\n{'='*60}")
            self.update_terminal(f"RÉSULTAT #{i+1} - Source: {source}")
            self.update_terminal(f"{'='*60}")
            
            # Organiser par catégories pour ce résultat
            categories = {
                "NOM": {},
                "CONTACT": {},
                "LOCALISATION": {},
                "FINANCE & DOCUMENTS": {},
                "AUTRES": {}
            }
            
            # Extraire toutes les données
            for key, value in data.items():
                if key in ["nom_complet", "prenom", "nom", "date_naissance", "genre", "civilite"]:
                    categories["NOM"][key.upper()] = value
                elif key in ["email", "courriel", "telephone", "mobilephone", "telephone_1", "telephone_2"]:
                    categories["CONTACT"][key.upper()] = value
                elif key == "adresse" and isinstance(value, dict):
                    addr = value
                    for addr_key, addr_val in addr.items():
                        categories["LOCALISATION"][addr_key.upper()] = addr_val
                elif key in ["matricule", "id", "id_psp", "numero", "code_organisme"]:
                    categories["FINANCE & DOCUMENTS"][key.upper()] = value
                else:
                    categories["AUTRES"][key.upper()] = value
            
            # Afficher les catégories
            for cat_name, fields in categories.items():
                if fields:
                    self.update_terminal(f"\n📁 {cat_name}")
                    self.update_terminal("-" * 40)
                    for label, value in fields.items():
                        # Tronquer les valeurs trop longues
                        if isinstance(value, str) and len(value) > 100:
                            value = value[:97] + "..."
                        elif isinstance(value, dict):
                            value = str(value)[:100] + "..."
                        self.update_terminal(f"  {label}: {value}")
        
        self.update_terminal(f"\n{'='*60}")
        self.update_terminal("[+] Scan terminé avec succès")
        self.update_terminal(f"[+] Risque: {random.choice(['FAIBLE', 'MOYEN', 'ÉLEVÉ'])}")
        self.update_terminal(f"[+] {total_count} résultats affichés")
        self.update_terminal("\n$ Rapport complet disponible dans l'API")
        self.end_scan()

    def scan_dots(self, n=0):
        if not self.scanning:
            return
        try:
            if not self.scan_btn.winfo_exists():
                return
            self.scan_btn.configure(text=sp("SCAN" + "." * (n % 4)))
        except (tk.TclError, AttributeError):
            return
        self.after(280, lambda: self.scan_dots(n + 1))

    def end_scan(self):
        self.scanning = False
        try:
            self.scan_btn.configure(state="normal", text=sp("SCANNER"))
            go = getattr(self.scan_btn, "_kz_go", None)
            if go:
                go(WHITE, 300)
        except (tk.TclError, AttributeError):
            pass

    def term_reset(self):
        self.term_gen += 1
        self.term_queue = []
        self.term_cur = ""
        self.term_typing = False
        t = self.terminal_output
        t.configure(state="normal")
        t.delete("0.0", "end")
        t.configure(state="disabled")

    def update_terminal(self, text):
        """Ajoute une ligne au terminal avec un effet machine à écrire."""
        try:
            if self.terminal_output is None or not self.terminal_output.winfo_exists():
                return
        except tk.TclError:
            return
        self.term_queue.append(text + "\n")
        if not self.term_typing:
            self.term_typing = True
            self._type_tick(self.term_gen)

    def _type_tick(self, gen):
        if gen != self.term_gen:
            return
        try:
            if not self.term_cur:
                if not self.term_queue:
                    self.term_typing = False
                    return
                self.term_cur = self.term_queue.pop(0)
            n = 3 + 8 * len(self.term_queue)      # plus il y a de retard, plus on tape vite
            chunk, self.term_cur = self.term_cur[:n], self.term_cur[n:]
            t = self.terminal_output
            t.configure(state="normal")
            t.insert("end", chunk)
            t.see("end")
            t.configure(state="disabled")
        except (tk.TclError, AttributeError):
            self.term_typing = False
            return
        self.after(10, lambda: self._type_tick(gen))

    # ───────────────────────── BUY ─────────────────────────
    def build_buy(self):
        self.page_title("BUY", "Boutique officielle kzSINT — accès, outils et abonnements")
        self.card_intro = 0.0
        self.draw_card()

        def card_up(t):
            self.card_intro = t
            self.card_dirty = True
        self.animate_value("card", 700, card_up)

        self.put(ctk.CTkLabel(self.stage, text=sp("MAGASIN"), font=(MONO, 13, "bold"),
                              text_color=TXT, fg_color=BG), relx=0.52, y=152)
        self.put(ctk.CTkButton(self.stage, text="Voir le panier", font=(MONO, 12, "bold"),
                               width=190, height=42, corner_radius=12, border_width=1,
                               border_color="#ff6600", fg_color=BG, hover_color="#330000",
                               text_color=TXT, command=self.show_cart),
                 relx=0.97, y=140, anchor="ne")

        sf = ctk.CTkScrollableFrame(
            self.stage, fg_color=BG, corner_radius=0,
            scrollbar_button_color="#1c1c20", scrollbar_button_hover_color="#2a2a30")
        self.put_box(sf, lambda W: W * 0.52, 196, lambda W: W * 0.46, lambda H: H - (196 + 12))
        self.buy_sf = sf

        gen = self.page_gen
        for i, prod in enumerate(PRODUCTS):
            self.after(260 + i * 80, lambda a=prod: self._add_row(sf, a, gen))

    def _add_row(self, sf, prod, gen):
        if gen != self.page_gen:
            return
        try:
            row = self.product_row(sf, *prod)
            self.apply_fx(row)
            self.fade_in(row, 320, gen=gen)
        except tk.TclError:
            pass

    def product_row(self, parent, letter, name, price, desc):
        row = ctk.CTkFrame(parent, fg_color="#09090c", border_width=1,
                           border_color="#1c1c20", corner_radius=20)
        row.pack(fill="x", pady=6, padx=2)
        row.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(row, text=letter, width=56, height=56, corner_radius=14,
                     fg_color="#dcdce0", text_color="#0a0a0a",
                     font=(SANS, 17, "bold")).grid(row=0, column=0, padx=(22, 16), pady=22)

        info = ctk.CTkFrame(row, fg_color="transparent")
        info.grid(row=0, column=1, sticky="w")
        ctk.CTkLabel(info, text=name, font=(SANS, 15, "bold"),
                     text_color=WHITE, anchor="w").pack(anchor="w")
        ctk.CTkLabel(info, text=desc, font=(SANS, 12), text_color=MUTED,
                     wraplength=280, justify="left", anchor="w").pack(anchor="w", pady=(2, 0))

        ctk.CTkLabel(row, text=fmt_price(price), font=(MONO, 14, "bold"),
                     text_color=WHITE).grid(row=0, column=2, padx=12)

        btn = ctk.CTkButton(row, text=sp("ACHETER"), font=(MONO, 11, "bold"),
                            width=120, height=44, corner_radius=10,
                            fg_color=WHITE, hover_color=WHITE_H, text_color="#0a0a0a")
        btn.configure(command=lambda b=btn: self.buy_product(name, price, b))
        btn.grid(row=0, column=3, padx=(8, 22))
        return row

    def buy_product(self, name, price, btn):
        self.cart.append((name, price))
        self.refresh_cart_badge()
        self.glow(self.cart_btn, "#ffffff", "#ff6600", 600)
        btn.configure(text=sp("AJOUTÉ ✓"))
        self.after(1000, lambda: btn.winfo_exists() and btn.configure(text=sp("ACHETER")))

    def refresh_cart_badge(self):
        n = len(self.cart)
        self.cart_btn.configure(text=f"🛒 {n}" if n else "🛒", width=62 if n else 42)

    def show_cart(self):
        if not self.cart:
            messagebox.showinfo("Panier", "Votre panier est vide.")
            return
        total = sum(p for _, p in self.cart)
        lines = "\n".join(f"• {n} — {fmt_price(p)}" for n, p in self.cart)
        if messagebox.askyesno("Panier",
                               f"{lines}\n\nTotal : {fmt_price(total)}\n\n"
                               "Passer au paiement ?"):
            messagebox.showinfo("Achat", "Redirection vers le paiement...\n\nAprès paiement, tu recevras ta clé de licence à activer dans SEARCH.")
            self.cart.clear()
            self.refresh_cart_badge()

    # ───────────────────────── HELP ─────────────────────────
    def build_help(self):
        self.page_title("HELP", "Support kzSINT — assistance en direct et communauté")

        # ── Chat
        chat = ctk.CTkFrame(self.stage, fg_color=PANEL, border_width=1,
                            border_color="#ff6600", corner_radius=20)
        chat.pack_propagate(False)
        self.put_box(chat, 46, 132, lambda W: W * 0.52, lambda H: H - (132 + 30))

        head = ctk.CTkFrame(chat, fg_color="transparent", height=80)
        head.pack(fill="x")
        head.pack_propagate(False)
        ctk.CTkLabel(head, text="B", width=52, height=52, corner_radius=14,
                     fg_color="#dcdce0", text_color="#0a0a0a",
                     font=(SANS, 17, "bold")).pack(side="left", padx=(26, 14))
        who = ctk.CTkFrame(head, fg_color="transparent")
        who.pack(side="left")
        ctk.CTkLabel(who, text="kzBot", font=(SANS, 15, "bold"),
                     text_color=WHITE, anchor="w").pack(anchor="w")
        ctk.CTkLabel(who, text="●  en ligne — répond en quelques secondes",
                     font=(SANS, 11), text_color=MUTED, anchor="w").pack(anchor="w")
        ctk.CTkFrame(chat, height=1, fg_color="#1a1a1e", corner_radius=0).pack(fill="x")

        # entrée (en bas)
        inp = ctk.CTkFrame(chat, fg_color="transparent")
        inp.pack(side="bottom", fill="x", padx=18, pady=(6, 18))
        self.chat_input = ctk.CTkEntry(
            inp, height=50, corner_radius=14, border_width=1,
            fg_color="#08080a", border_color=BORDER, text_color=TXT,
            placeholder_text="Écris ton message...", placeholder_text_color=DIM,
            font=(MONO, 12))
        self.chat_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.chat_input.bind("<Return>", self.send_message)
        self.chat_input.bind("<FocusIn>", lambda e: self.glow(self.chat_input, BORDER, "#8a8a92"))
        self.chat_input.bind("<FocusOut>", lambda e: self.glow(self.chat_input, "#8a8a92", BORDER))
        ctk.CTkButton(inp, text=sp("ENVOYER"), font=(MONO, 11, "bold"),
                      width=120, height=50, corner_radius=14,
                      fg_color=WHITE, hover_color=WHITE_H, text_color="#0a0a0a",
                      command=self.send_message).pack(side="right")

        # suggestions
        chips = ctk.CTkFrame(chat, fg_color="transparent")
        chips.pack(side="bottom", fill="x", padx=14, pady=(0, 6))
        for topic in ["Prix et offres ?", "Le Discord ?", "Comment créer un compte ?", "Signaler un bug"]:
            ctk.CTkButton(chips, text=topic, font=(MONO, 10), height=32,
                          corner_radius=16, border_width=1, border_color="#2a2a2f",
                          fg_color=PANEL, hover_color="#330000", text_color="#ffaa66",
                          command=lambda t=topic: self.ask_topic(t)).pack(side="left", padx=4)

        # messages
        self.chat_scroll = ctk.CTkScrollableFrame(
            chat, fg_color=PANEL, corner_radius=0,
            scrollbar_button_color="#1c1c20", scrollbar_button_hover_color="#2a2a30")
        self.chat_scroll.pack(fill="both", expand=True, padx=10, pady=(10, 4))
        g = self.page_gen
        self.after(520, lambda: g == self.page_gen and self.add_bubble(
            "kzBot", "Bienvenue sur le support kzSINT. Comment pouvons-nous t'aider ?"))

        # ── Discord
        dc = ctk.CTkFrame(self.stage, fg_color=PANEL, border_width=1,
                          border_color="#ff6600", corner_radius=24, height=370)
        self.put(dc, relx=0.58, y=132, relwidth=0.39)
        dc.pack_propagate(False)

        from PIL import Image as _PILImage
        import base64 as _b64, io as _io
        _img = _PILImage.open(_io.BytesIO(_b64.b64decode(DISCORD_LOGO_B64))).convert("RGBA")
        self._discord_img = ctk.CTkImage(light_image=_img, dark_image=_img, size=(76, 76))
        logo = ctk.CTkLabel(dc, text="", image=self._discord_img, fg_color="transparent")
        logo.pack(pady=(32, 12))

        ctk.CTkLabel(dc, text="Rejoins notre Discord", font=(SANS, 17, "bold"),
                     text_color=WHITE).pack(pady=(4, 10))
        ctk.CTkLabel(dc, text="Annonces, entraide OSINT, support communautaire et accès "
                              "anticipé aux mises à jour.",
                     font=(SANS, 12), text_color=MUTED, wraplength=330,
                     justify="center").pack(padx=24)
        ctk.CTkButton(dc, text=sp("OUVRIR LE DISCORD"), font=(MONO, 12, "bold"),
                      height=54, corner_radius=12, fg_color=WHITE, hover_color=WHITE_H,
                      text_color="#0a0a0a", command=self.open_discord).pack(
            fill="x", padx=36, pady=(26, 14))
        ctk.CTkLabel(dc, text="discord.gg/kzsint", font=(MONO, 11),
                     text_color=DIM).pack()

    def add_bubble(self, sender, text):
        try:
            if self.chat_scroll is None or not self.chat_scroll.winfo_exists():
                return
            mine = sender == "vous"
            holder = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
            holder.pack(fill="x", pady=5)
            bubble = ctk.CTkFrame(
                holder, corner_radius=14, border_width=1,
                fg_color="#dcdce0" if mine else "#121215",
                border_color="#dcdce0" if mine else "#25252a")
            bubble.pack(anchor="e" if mine else "w", padx=8)
            ctk.CTkLabel(bubble, text=text, font=(SANS, 13), wraplength=400,
                         justify="left", anchor="w",
                         text_color="#0a0a0a" if mine else TXT).pack(
                anchor="w", padx=16, pady=(12, 2))
            ctk.CTkLabel(bubble, text=f"{sender} • {datetime.now().strftime('%H:%M')}",
                         font=(MONO, 10), text_color="#55555b" if mine else DIM).pack(
                anchor="w", padx=16, pady=(0, 10))
            self.fade_in(bubble, 260)
            self._scroll_chat()
        except tk.TclError:
            pass

    def send_message(self, event=None):
        message = self.chat_input.get().strip()
        if not message:
            return
        self.chat_input.delete(0, "end")
        self.last_user_message = message
        self.add_bubble("vous", message)
        self.show_typing()
        threading.Thread(target=self.bot_response, daemon=True).start()

    def bot_response(self):
        time.sleep(random.uniform(0.5, 1.5))
        
        # Récupérer le dernier message de l'utilisateur
        if hasattr(self, 'last_user_message'):
            user_msg = self.last_user_message.lower()
            response = self.get_smart_response(user_msg)
        else:
            response = "Comment puis-je vous aider ?"
        
        self.after(0, self._bot_reply, response)
    
    def get_smart_response(self, message):
        """Génère une réponse intelligente basée sur les informations du panel"""
        
        # Réponses intelligentes basées sur le panel
        if "prix" in message or "offre" in message or "tarif" in message:
            response = """📦 NOS OFFRES

Voici nos plans disponibles :

🟢 kzSINT BASIC - 9.99€
• 10 scans / jour
• 2 modules
• Support communautaire

🔵 kzSINT PRO - 29.99€
• Scans illimités
• Tous les modules
• Alertes temps réel

🔴 kzSINT ELITE - 99.99€
• Accès API complet
• Scans prioritaires
• Support dédié 24/7

🟠 SCAN DEEP-WEB - 4.99€
• Analyse ponctuelle des fuites
• Scan des forums fermés

🟣 RAPPORT OSINT - 19.99€
• Dossier complet PDF
• Analyse experte sur une cible

Tu peux acheter ces offres dans la section BUY !"""
        
        elif "discord" in message:
            response = """🎮 DISCORD

Rejoins notre communauté Discord !

Avantages :
• 📢 Annonces exclusives
• 💬 Entraide OSINT
• 🆘 Support communautaire
• ⚡ Accès anticipé aux mises à jour

Clique sur le bouton "OUVRIR LE DISCORD" à droite pour nous rejoindre !
discord.gg/VFpJYY3XCG"""
        
        elif "compte" in message or "créer" in message or "inscription" in message:
            response = """👤 CRÉER UN COMPTE

Pour créer un compte kzSINT :

1️⃣ Va sur la page de connexion
2️⃣ Clique sur "CRÉER UN COMPTE"
3️⃣ Choisis un pseudo (3-20 caractères)
4️⃣ Choisis un mot de passe (min. 6 caractères)
5️⃣ Confirme ton mot de passe
6️⃣ Clique sur "CRÉER LE COMPTE"

💡 Une fois inscrit, tu pourras :
• Activer une clé de licence
• Effectuer des scans OSINT
• Accéder à toutes les fonctionnalités

C'est gratuit de créer un compte !"""
        
        elif "bug" in message or "problème" in message or "erreur" in message:
            response = """🐛 SIGNALER UN BUG

Tu as rencontré un problème ? Voici comment nous aider :

1️⃣ Décris le bug en détail
2️⃣ Indique la page où ça s'est produit (SEARCH, BUY, HELP)
3️⃣ Explique ce que tu faisais quand le bug est survenu
4️⃣ Envoie-nous une capture d'écran si possible

📧 Tu peux aussi nous contacter directement sur Discord pour un support plus rapide.

Nous traitons tous les rapports dans les plus brefs délais !"""
        
        elif "licence" in message or "clé" in message or "cle" in message:
            response = """🔑 ACTIVER UNE LICENCE

Pour activer une clé de licence :

1️⃣ Connecte-toi à ton compte
2️⃣ Va dans la section SEARCH
3️⃣ Si aucune licence n'est active, entre ta clé
4️⃣ Clique sur "ACTIVER LA CLÉ"

💡 Où trouver une clé ?
• Achète un plan dans la section BUY
• Après paiement, tu recevras ta clé par email
• Colle la clé dans le champ d'activation

Types de clés :
• BASIC : 10 scans/jour
• PRO : Scans illimités
• ELITE : Accès API + priorité"""
        
        elif "scan" in message or "recherche" in message or "osint" in message:
            response = """🔍 FONCTIONNEMENT DU SCAN

Notre moteur de recherche OSINT permet de :

📞 Téléphone : Informations liées au numéro
✉️ Email : Comptes et données associés
👻 Snapchat : Profil et anciens pseudos
👤 Nom/Prénom : Informations personnelles

Comment scanner :
1️⃣ Choisis le type de recherche
2️⃣ Entre ta cible (pseudo, email, numéro...)
3️⃣ Clique sur "SCANNER"
4️⃣ Attends les résultats dans le terminal

⚠️ Attention : Une licence active est requise pour effectuer des scans."""
        
        elif "api" in message:
            response = """🔌 API kzSINT

Notre API permet aux développeurs d'intégrer kzSINT dans leurs applications.

Endpoints disponibles :
• /api/v1/query - Recherche générale
• /api/v1/snapchat - Recherche Snapchat

L'accès API est inclus dans le plan ELITE.

Documentation complète disponible sur demande. Contacter-nous sur Discord pour plus d'infos !"""
        
        else:
            response = random.choice([
                "Je n'ai pas compris ta question. Essaie de reformuler ou choisis une des suggestions ci-dessous !",
                "Hmm, je ne suis pas sûr d'avoir compris. Peux-tu être plus précis ?",
                "Je peux t'aider avec les prix, le Discord, la création de compte ou signaler un bug. Que souhaites-tu savoir ?",
                "Pour une meilleure réponse, essaie les boutons rapides en bas du chat !",
            ])
        
        return response

    def ask_topic(self, topic):
        self.chat_input.delete(0, "end")
        self.chat_input.insert(0, topic)
        self.send_message()

    def open_discord(self):
        webbrowser.open("https://discord.gg/kzsint")


if __name__ == "__main__":
    app = kzSINTApp()
    app.mainloop()