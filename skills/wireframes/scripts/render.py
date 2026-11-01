#!/usr/bin/env python3
"""POC Studio · wireframes: render low-fidelity wireframes from a JSON layout spec straight to PNG (no browser, no HTML).

usage: render.py <spec.json> <out_dir>
writes: <out_dir>/png/<page-id>.png (one per page), <out_dir>/<slug>-wireframes.pdf (all pages),
        <out_dir>/wireframe-manifest.json (the closed component list the design system builds from)
"""
import json, os, random, sys
from collections import OrderedDict
from PIL import Image, ImageDraw, ImageFont

# ---------- look: greys only, one font, fixed sizes ----------
BG, PANEL, LINE, FILL, FILL2, INK, MUTED, DARK = "#f3f3f1", "#ffffff", "#c4c4bf", "#e7e7e3", "#d6d6d1", "#2f2f2d", "#8a8a85", "#4a4a47"
HERE = os.path.dirname(os.path.abspath(__file__))
def _font(names, size):
    for n in names:
        for p in (os.path.join(HERE, "..", "assets", n), f"/usr/share/fonts/opentype/inter/{n}",
                  f"/usr/share/fonts/truetype/dejavu/{n}", f"/Library/Fonts/{n}", os.path.expanduser(f"~/Library/Fonts/{n}")):
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)
REG = lambda s: _font(["Inter-Regular.otf", "Inter-Regular.ttf"], s)
BOLD = lambda s: _font(["Inter-SemiBold.otf", "Inter-SemiBold.ttf"], s)
MONO = lambda s: _font(["IBMPlexMono-Regular.ttf", "DejaVuSansMono.ttf", "Menlo.ttc"], s)

GAP, PAD = 16, 24
AGENT = ["AI"]  # the agent's short name, from app.agent (set in main)

class Canvas:
    def __init__(self, w, h):
        self.im = Image.new("RGB", (w, h), BG); self.d = ImageDraw.Draw(self.im, "RGBA")
    def box(self, x, y, w, h, fill=PANEL, line=LINE, r=8, width=1):
        self.d.rounded_rectangle([x, y, x + w, y + h], r, fill=fill, outline=line, width=width)
    def text(self, x, y, s, f=None, fill=INK, anchor="la"):
        self.d.text((x, y), str(s), font=f or REG(13), fill=fill, anchor=anchor)
    def tw(self, s, f): return self.d.textlength(str(s), font=f)
    def bar(self, x, y, w, h=8, fill=FILL): self.d.rounded_rectangle([x, y, x + w, y + h], h // 2, fill=fill)
    def pill(self, x, y, s, solid=False, f=None):
        f = f or REG(11); w = self.tw(s, f) + 16
        self.d.rounded_rectangle([x, y, x + w, y + 20], 10, fill=DARK if solid else PANEL, outline=DARK if solid else LINE)
        self.text(x + 8, y + 10, s, f, PANEL if solid else DARK, "lm"); return w
    def button(self, x, y, s, primary=False):
        f = BOLD(12); w = self.tw(s, f) + 28
        self.d.rounded_rectangle([x, y, x + w, y + 32], 6, fill=DARK if primary else PANEL, outline=DARK if primary else LINE)
        self.text(x + w / 2, y + 16, s, f, PANEL if primary else INK, "mm"); return w
    def tag(self, x, y, w, h, b):
        s = f"{b.get('id', '')} · {b['type'] if not b.get('component') else b['component']}".strip(" ·")
        f = MONO(9); tw = self.tw(s, f)
        self.d.rectangle([x + w - tw - 12, y + h - 18, x + w - 4, y + h - 4], fill=(255, 255, 255, 230))
        self.text(x + w - 8, y + h - 11, s, f, MUTED, "rm")

def wrap(c, s, f, width):
    words, lines, cur = str(s).split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if c.tw(t, f) <= width: cur = t
        else: lines.append(cur); cur = wd
    return lines + ([cur] if cur else [])

def title(c, x, y, b):
    if b.get("title"): c.text(x + 16, y + 16, b["title"], BOLD(13))
    return 44 if b.get("title") else 16

# ---------- blocks ----------
def b_header(c, x, y, w, h, b):
    if b.get("breadcrumb"): c.text(x, y + 2, " / ".join(b["breadcrumb"]), REG(12), MUTED)
    c.text(x, y + (22 if b.get("breadcrumb") else 6), b["title"], BOLD(22))
    if b.get("subtitle"): c.text(x, y + (52 if b.get("breadcrumb") else 38), b["subtitle"], REG(13), MUTED)
    bx = x + w
    for i, a in enumerate(reversed(b.get("actions", []))):
        f = BOLD(12); bw = c.tw(a, f) + 28; bx -= bw; c.button(bx, y + 8, a, primary=(i == 0)); bx -= 8
def b_filters(c, x, y, w, h, b):
    if b.get("search", True):
        c.box(x, y + 4, 260, 34, PANEL, LINE, 6); c.text(x + 30, y + 21, b.get("search_label", "Search"), REG(12), MUTED, "lm")
        c.d.ellipse([x + 11, y + 15, x + 21, y + 25], outline=MUTED, width=2); fx = x + 272
    else: fx = x
    for chip in b.get("chips", []):
        f = REG(12); cw = c.tw(chip, f) + 34
        c.box(fx, y + 4, cw, 34, PANEL, LINE, 17); c.text(fx + 14, y + 21, chip, f, INK, "lm")
        c.d.polygon([(fx + cw - 16, y + 18), (fx + cw - 10, y + 18), (fx + cw - 13, y + 23)], fill=MUTED); fx += cw + 8
def b_kpi(c, x, y, w, h, b):
    c.box(x, y, w, h); c.text(x + 16, y + 16, b["label"], REG(12), MUTED)
    c.text(x + 16, y + 38, b["value"], BOLD(26))
    if b.get("delta"): c.text(x + 16, y + h - 26, b["delta"], REG(11), MUTED)
    c.d.line([(x + w - 90, y + h - 26), (x + w - 70, y + h - 34), (x + w - 50, y + h - 30), (x + w - 30, y + h - 42), (x + w - 16, y + h - 38)], fill=FILL2, width=2)
def b_chart(c, x, y, w, h, b):
    c.box(x, y, w, h); t = title(c, x, y, b); ix, iy, iw, ih = x + 16, y + t + 4, w - 32, h - t - 40
    c.d.line([(ix, iy), (ix, iy + ih), (ix + iw, iy + ih)], fill=LINE)
    rnd = random.Random(b.get("id", "c")); kind = b.get("kind", "line")
    if kind == "bar":
        n = 8; bw = iw / n * .55
        for i in range(n):
            bh = ih * rnd.uniform(.25, .95); bx = ix + iw / n * i + 10
            c.d.rectangle([bx, iy + ih - bh, bx + bw, iy + ih], fill=FILL2)
    elif kind == "donut":
        r = min(iw, ih) / 2 - 4; cx, cy = ix + iw / 2, iy + ih / 2; a = -90
        for frac, col in ((.55, DARK), (.3, FILL2), (.15, FILL)):
            c.d.pieslice([cx - r, cy - r, cx + r, cy + r], a, a + 360 * frac, fill=col); a += 360 * frac
        c.d.ellipse([cx - r * .6, cy - r * .6, cx + r * .6, cy + r * .6], fill=PANEL)
    else:
        for k, col in ((0, DARK), (1, FILL2)):
            pts = [(ix + iw / 9 * i, iy + ih * rnd.uniform(.15 + .2 * k, .8)) for i in range(10)]
            c.d.line(pts, fill=col, width=2)
    if b.get("caption"): c.text(x + 16, y + h - 20, b["caption"], REG(11), MUTED)
def b_table(c, x, y, w, h, b):
    c.box(x, y, w, h); t = title(c, x, y, b)
    if b.get("bulk"):
        bx = x + w - 16
        for a in reversed(b["bulk"]):
            f = BOLD(12); bw = c.tw(a, f) + 28; bx -= bw; c.button(bx, y + 8, a, a == b["bulk"][-1]); bx -= 8
    cols = b["columns"]; cx0 = x + 16 + (28 if b.get("select") else 0); cw = (w - 32 - (28 if b.get("select") else 0)) / len(cols)
    hy = y + t + 2; c.d.rectangle([x + 1, hy, x + w - 1, hy + 30], fill=FILL)
    for i, col in enumerate(cols): c.text(cx0 + cw * i, hy + 15, col, BOLD(11), DARK, "lm")
    rnd = random.Random(b.get("id", "t")); ry = hy + 30; rh = 36
    statuses = b.get("statuses", ["Critical", "Low", "OK"])
    while ry + rh <= y + h - 8:
        c.d.line([(x + 1, ry + rh), (x + w - 1, ry + rh)], fill=FILL)
        if b.get("select"): c.box(x + 16, ry + 11, 14, 14, PANEL, LINE, 3)
        for i, col in enumerate(cols):
            px = cx0 + cw * i
            if col == b.get("status_col"): c.pill(px, ry + 8, rnd.choice(statuses), solid=False)
            elif col == b.get("action_col"): c.text(px, ry + rh / 2, "Open  ›", REG(12), DARK, "lm")
            else: c.bar(px, ry + 14, min(cw - 20, rnd.uniform(.35, .8) * cw))
        ry += rh
    if b.get("paging", True) and h > 160: c.text(x + w - 16, y + h - 4, "", REG(1))
def b_list(c, x, y, w, h, b):
    c.box(x, y, w, h); t = title(c, x, y, b); iy = y + t
    for it in b.get("items", []):
        if iy + 56 > y + h - 8: break
        c.text(x + 16, iy + 10, it["title"], BOLD(12)); c.text(x + 16, iy + 30, it.get("meta", ""), REG(11), MUTED)
        if it.get("status"):
            f = REG(11); c.pill(x + w - 16 - c.tw(it["status"], f) - 16, iy + 12, it["status"])
        c.d.line([(x + 16, iy + 54), (x + w - 16, iy + 54)], fill=FILL); iy += 58
def b_tabs(c, x, y, w, h, b):
    tx = x
    for i, t in enumerate(b["items"]):
        f = BOLD(13) if i == b.get("active", 0) else REG(13); tw = c.tw(t, f)
        c.text(tx, y + 14, t, f, INK if i == b.get("active", 0) else MUTED)
        if i == b.get("active", 0): c.d.rectangle([tx, y + 36, tx + tw, y + 38], fill=DARK)
        tx += tw + 28
    c.d.line([(x, y + 38), (x + w, y + 38)], fill=LINE)
def b_form(c, x, y, w, h, b):
    c.box(x, y, w, h); iy = y + title(c, x, y, b)
    for fd in b.get("fields", []):
        c.text(x + 16, iy, fd["label"], BOLD(11), DARK); kind = fd.get("kind", "text"); fh = 64 if kind in ("textarea", "photo") else 36
        if kind == "photo":
            c.d.rounded_rectangle([x + 16, iy + 18, x + w - 16, iy + 18 + fh], 6, outline=MUTED, width=2, fill=FILL)
            cx3, cy3 = x + w / 2 - 50, iy + 18 + fh / 2; c.d.rounded_rectangle([cx3 - 12, cy3 - 8, cx3 + 12, cy3 + 9], 3, outline=DARK, width=2); c.d.ellipse([cx3 - 5, cy3 - 4, cx3 + 5, cy3 + 6], outline=DARK, width=2); c.text(cx3 + 22, cy3, "Take photo", BOLD(12), DARK, "lm")
        else:
            c.box(x + 16, iy + 18, w - 32, fh, PANEL, LINE, 6)
            if fd.get("value"): c.text(x + 28, iy + 36, fd["value"], REG(12), INK, "lm")
            else: c.bar(x + 28, iy + 32, (w - 32) * .35)
            if kind == "select": c.d.polygon([(x + w - 38, iy + 32), (x + w - 28, iy + 32), (x + w - 33, iy + 39)], fill=MUTED)
            if kind == "number": c.text(x + w - 30, iy + 36, "−   +", BOLD(13), DARK, "rm")
        iy += fh + 34
    if b.get("submit"):
        if b.get("submit_full"): c.d.rounded_rectangle([x + 16, y + h - 70, x + w - 16, y + h - 26], 8, fill=DARK); c.text(x + w / 2, y + h - 48, b["submit"], BOLD(14), PANEL, "mm")
        else: c.button(x + 16, y + h - 48, b["submit"], True)
def b_card(c, x, y, w, h, b):
    c.box(x, y, w, h); iy = y + title(c, x, y, b)
    for l in b.get("lines", []):
        for ln in wrap(c, l, REG(12), w - 32): c.text(x + 16, iy, ln, REG(12), DARK); iy += 18
        iy += 6
    if b.get("action"): c.button(x + 16, y + h - 48, b["action"], True)
def b_timeline(c, x, y, w, h, b):
    c.box(x, y, w, h); iy = y + title(c, x, y, b)
    for i, it in enumerate(b.get("items", [])):
        if iy + 44 > y + h: break
        c.d.ellipse([x + 18, iy + 4, x + 28, iy + 14], fill=DARK if i == 0 else PANEL, outline=DARK, width=2)
        c.text(x + 40, iy + 2, it, REG(12), INK); c.text(x + 40, iy + 20, "", REG(10)); iy += 40
BLOCKS = dict(header=b_header, filters=b_filters, kpi=b_kpi, chart=b_chart, table=b_table, list=b_list,
              tabs=b_tabs, form=b_form, card=b_card, timeline=b_timeline)
NO_TAG = {"header", "filters", "tabs"}

# ---------- overlays ----------
def o_drawer(c, W, H, top, b):
    c.d.rectangle([0, 0, W, H], fill=(30, 30, 28, 60)); w = b.get("width", 400); x = W - w
    c.d.rectangle([x, top, W, H], fill=PANEL, outline=DARK); c.text(x + 20, top + 22, b["title"], BOLD(15))
    c.d.line([(W - 34, top + 22), (W - 24, top + 32)], fill=MUTED, width=2); c.d.line([(W - 34, top + 32), (W - 24, top + 22)], fill=MUTED, width=2); iy = top + 64
    for m in b.get("messages", []):
        f = REG(12); lines = wrap(c, m["text"], f, w - 90); bh = 18 * len(lines) + 20
        user = m.get("from") == "user"; bw = min(w - 60, max(c.tw(l, f) for l in lines) + 28)
        bx = W - 20 - bw if user else x + 20
        c.box(bx, iy, bw, bh, FILL if user else PANEL, LINE if not user else FILL, 10)
        for i, l in enumerate(lines): c.text(bx + 14, iy + 10 + i * 18, l, f, INK)
        iy += bh + 10
        cx = x + 20
        for ch in m.get("chips", []): cx += c.pill(cx, iy, ch) + 6
        if m.get("chips"): iy += 30
        if m.get("card"):
            c.box(x + 20, iy, w - 40, 76, PANEL, DARK, 8, 2); c.text(x + 34, iy + 14, m["card"], BOLD(12))
            c.button(x + 34, iy + 36, "Approve", True); c.button(x + 140, iy + 36, "Edit"); iy += 88
    c.box(x + 16, H - 64, w - 32, 44, PANEL, LINE, 22); c.text(x + 34, H - 42, b.get("input", "Ask a question…"), REG(12), MUTED, "lm")
    c.tag(x, top, w, H - top - 70, b)
def o_modal(c, W, H, top, b):
    c.d.rectangle([0, 0, W, H], fill=(30, 30, 28, 70)); w, h = b.get("width", 460), b.get("height", 220)
    x, y = (W - w) / 2, (H - h) / 2; c.box(x, y, w, h, PANEL, DARK, 10, 2)
    c.text(x + 24, y + 24, b["title"], BOLD(16)); iy = y + 60
    for ln in wrap(c, b.get("body", ""), REG(13), w - 48): c.text(x + 24, iy, ln, REG(13), DARK); iy += 20
    bx = x + w - 24
    for i, a in enumerate(reversed(b.get("actions", ["Cancel", "Confirm"]))):
        f = BOLD(12); bw = c.tw(a, f) + 28; bx -= bw; c.button(bx, y + h - 56, a, i == 0); bx -= 8
    c.tag(x, y, w, h, b)
OVERLAYS = dict(drawer=o_drawer, modal=o_modal)

# ---------- shells ----------
def shell_desktop(c, W, H, app, page):
    nav_w = 220; c.d.rectangle([0, 0, nav_w, H], fill=PANEL); c.d.line([(nav_w, 0), (nav_w, H)], fill=LINE)
    c.box(20, 18, 28, 28, FILL2, None, 6); c.text(58, 32, app["name"], BOLD(14), INK, "lm")
    for i, item in enumerate(app["nav"]):
        y = 84 + i * 40; active = item == page.get("nav_active")
        if active: c.d.rounded_rectangle([12, y - 4, nav_w - 12, y + 30], 6, fill=FILL)
        c.d.rounded_rectangle([24, y + 5, 40, y + 21], 4, fill=DARK if active else FILL2)
        c.text(52, y + 13, item, BOLD(13) if active else REG(13), INK if active else DARK, "lm")
    c.d.rectangle([nav_w + 1, 0, W, 56], fill=PANEL); c.d.line([(nav_w, 56), (W, 56)], fill=LINE)
    c.box(nav_w + 24, 12, 320, 32, BG, LINE, 6); c.text(nav_w + 40, 28, app.get("search_label", "Search"), REG(12), MUTED, "lm")
    c.d.ellipse([W - 52, 12, W - 20, 44], fill=FILL2); c.d.ellipse([W - 96, 18, W - 76, 38], outline=MUTED, width=2)
    return nav_w + PAD, 56 + PAD, W - nav_w - 2 * PAD, 56
def shell_phone(c, W, H, app, page):
    c.d.rectangle([0, 0, W, 56], fill=PANEL); c.d.line([(0, 56), (W, 56)], fill=LINE)
    c.text(16, 28, "‹", BOLD(20), INK, "lm"); c.text(W / 2, 28, page["title"], BOLD(15), INK, "mm")
    tabs = app.get("phone_tabs", app["nav"][:4]); tw = W / len(tabs)
    c.d.rectangle([0, H - 64, W, H], fill=PANEL); c.d.line([(0, H - 64), (W, H - 64)], fill=LINE)
    for i, t in enumerate(tabs):
        active = t == page.get("nav_active"); cx = tw * i + tw / 2
        c.d.rounded_rectangle([cx - 10, H - 52, cx + 10, H - 32], 5, fill=DARK if active else FILL2)
        c.text(cx, H - 18, t, BOLD(10) if active else REG(10), INK if active else MUTED, "mm")
    return 16, 56 + 16, W - 32, 56


# ---------- more blocks (map-console apps) ----------
def b_label(c, x, y, w, h, b):
    c.text(x, y + h / 2, b["text"].upper(), MONO(11), MUTED, "lm")
def b_insight(c, x, y, w, h, b):
    c.box(x, y, w, h, PANEL, DARK if b.get("active") else LINE, 8, 2 if b.get("active") else 1)
    lx = x + 16
    if b.get("warn"): c.d.polygon([(lx, y + 26), (lx + 6, y + 15), (lx + 12, y + 26)], outline=DARK, width=2); lx += 20
    if b.get("ai"): c.box(lx, y + 13, 16, 16, FILL2, None, 3); c.text(lx + 8, y + 21, AGENT[0][:2].upper(), BOLD(7), INK, "mm"); lx += 22
    for ln in wrap(c, b["label"].upper(), MONO(11), w - (lx - x) - 40)[:2]: c.text(lx, y + 20, ln, MONO(11), DARK, "lm"); y += 15
    y -= 15 * min(2, len(wrap(c, b["label"].upper(), MONO(11), w - (lx - x) - 40)))
    c.text(x + w - 18, y + 20, "↗", BOLD(13), MUTED, "mm")
    nl = len(wrap(c, b["label"].upper(), MONO(11), w - (lx - x) - 40)[:2]); vy = y + 22 + 15 * nl + 8
    vf = BOLD(26); c.text(x + 16, vy, b["value"], vf, INK, "lt")
    if b.get("of"): c.text(x + 22 + c.tw(b["value"], vf), vy + 9, b["of"], REG(14), MUTED, "lt")
    if b.get("badge"): c.pill(x + w - 16 - c.tw(b["badge"], REG(11)) - 16, vy + 5, b["badge"])
    by = vy + 40
    if b.get("progress") is not None:
        c.bar(x + 16, by, w - 32, 4, FILL); c.bar(x + 16, by, max(4, (w - 32) * b["progress"]), 4, DARK); by += 12
    if b.get("sub"): c.text(x + 16, by + 6, b["sub"].upper(), MONO(10), MUTED, "lm")
def b_stat(c, x, y, w, h, b):
    c.box(x, y, w, h); lx = x + 22
    if b.get("warn"): c.d.polygon([(lx, y + 32), (lx + 6, y + 21), (lx + 12, y + 32)], outline=DARK, width=2); lx += 20
    c.text(lx, y + 27, b["label"].upper(), MONO(11), DARK, "lm"); c.d.ellipse([lx + c.tw(b["label"].upper(), MONO(11)) + 8, y + 21, lx + c.tw(b["label"].upper(), MONO(11)) + 20, y + 33], outline=MUTED)
    vf = BOLD(34); c.text(x + 22, y + 52, b["value"], vf, INK, "lt")
    if b.get("unit"): c.text(x + 30 + c.tw(b["value"], vf), y + 66, b["unit"], REG(16), DARK, "lt")
    if b.get("delta"): c.pill(x + w - 22 - c.tw(b["delta"], REG(11)) - 16, y + 18, b["delta"])
def b_segmented(c, x, y, w, h, b):
    f = MONO(11); widths = [c.tw(t.upper(), f) + 28 for t in b["items"]]; tw = sum(widths) + 8
    c.box(x, y, tw, h, FILL, None, h // 2); cx = x + 4
    for i, t in enumerate(b["items"]):
        if i == b.get("active", 0): c.box(cx, y + 4, widths[i], h - 8, PANEL, LINE, (h - 8) // 2)
        c.text(cx + widths[i] / 2, y + h / 2, t.upper(), f, INK if i == b.get("active", 0) else MUTED, "mm"); cx += widths[i]
def b_select(c, x, y, w, h, b):
    if b.get("label"): c.text(x, y + 6, b["label"].upper(), MONO(10), DARK, "lm"); y += 18; h -= 18
    c.box(x, y, w, h, FILL if b.get("filled") else PANEL, None if b.get("filled") else LINE, 6)
    c.text(x + 12, y + h / 2, b["value"], REG(13), INK if b.get("strong", True) else MUTED, "lm")
    if b.get("kind", "select") == "select": c.d.polygon([(x + w - 22, y + h / 2 - 3), (x + w - 12, y + h / 2 - 3), (x + w - 17, y + h / 2 + 3)], fill=DARK)
def b_stepper(c, x, y, w, h, b):
    if b.get("label"): c.text(x, y + 6, b["label"].upper(), MONO(10), DARK, "lm"); y += 18; h -= 18
    c.box(x, y, 144, h, PANEL, LINE, 6); c.text(x + 20, y + h / 2, "−", BOLD(14), DARK, "mm"); c.text(x + 72, y + h / 2, b.get("value", "1"), REG(13), INK, "mm"); c.text(x + 124, y + h / 2, "+", BOLD(14), DARK, "mm")
def b_slider(c, x, y, w, h, b):
    c.text(x, y + 6, b["label"].upper(), MONO(10), DARK, "lm"); c.text(x + w, y + 6, b["value"], BOLD(12), INK, "rm")
    c.bar(x, y + 28, w, 6, FILL2); k = b.get("at", .15); c.bar(x, y + 28, w * k, 6, DARK); c.d.ellipse([x + w * k - 8, y + 23, x + w * k + 8, y + 39], fill=PANEL, outline=DARK, width=2)
def b_text(c, x, y, w, h, b):
    f = BOLD(b.get("size", 13)) if b.get("bold") else REG(b.get("size", 13))
    for ln in wrap(c, b["text"], f, w): c.text(x, y, ln, f, INK if b.get("bold") else DARK); y += b.get("size", 13) + 7
def b_button(c, x, y, w, h, b):
    if b.get("full"):
        c.d.rounded_rectangle([x, y, x + w, y + h], 8, fill=FILL if b.get("disabled") else DARK)
        c.text(x + w / 2, y + h / 2, b["text"], BOLD(13), MUTED if b.get("disabled") else PANEL, "mm")
    else: c.button(x, y, b["text"], b.get("primary", True))
def b_tiles(c, x, y, w, h, b):
    n = len(b["items"]); tw = (w - 8 * (n - 1)) / n
    for i, it in enumerate(b["items"]):
        tx = x + i * (tw + 8); act = i == b.get("active", 0)
        c.box(tx, y, tw, h, PANEL if act else FILL, LINE if act else None, 6)
        lf = REG(10 if n > 3 else 11); lab = it[0]
        while c.tw(lab, lf) > tw - 14 and len(lab) > 3: lab = lab[:-2] + "…"
        c.text(tx + 8, y + 14, lab, lf, DARK); c.text(tx + 8, y + 34, it[1], BOLD(14 if n > 3 else 15), INK)
def b_move(c, x, y, w, h, b):
    c.box(x, y, w, h); c.text(x + 16, y + 20, b.get("kind", "Branch request"), BOLD(12), DARK, "lm")
    c.d.ellipse([x + 16, y + 44, x + 26, y + 54], outline=DARK, width=2); c.d.line([(x + 21, y + 56), (x + 21, y + 80)], fill=MUTED, width=2); c.d.ellipse([x + 16, y + 82, x + 26, y + 92], fill=DARK)
    c.text(x + 36, y + 49, b["from"], BOLD(14), INK, "lm"); c.text(x + 36, y + 68, b.get("miles", ""), REG(11), MUTED, "lm"); c.text(x + 36, y + 87, b["to"], BOLD(14), INK, "lm")
    c.text(x + w - 16, y + 50, b.get("value", ""), BOLD(18), INK, "rm"); c.text(x + w - 16, y + 72, b.get("value_label", ""), REG(11), MUTED, "rm")
    c.text(x + 16, y + 116, b.get("detail", "").upper(), MONO(10), DARK, "lm")
    bw = (w - 44) / 2; c.box(x + 16, y + h - 50, bw, 36, PANEL, LINE, 6); c.text(x + 16 + bw / 2, y + h - 32, "Reject", BOLD(13), INK, "mm")
    c.d.rounded_rectangle([x + 28 + bw, y + h - 50, x + w - 16, y + h - 14], 6, fill=DARK); c.text(x + 28 + bw + bw / 2, y + h - 32, "Approve", BOLD(13), PANEL, "mm")
def b_slot(c, x, y, w, h, b):
    """An empty region that names the component the design system will design for it."""
    c.d.rounded_rectangle([x, y, x + w, y + h], 8, fill="#f7f7f5")
    for (x1, y1, x2, y2) in ((x, y, x + w, y), (x, y + h, x + w, y + h), (x, y, x, y + h), (x + w, y, x + w, y + h)):
        n = int(max(abs(x2 - x1), abs(y2 - y1)) // 10)
        for k in range(0, n, 2):
            a, bb = k / n, min(1, (k + 1) / n)
            c.d.line([(x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * bb, y1 + (y2 - y1) * bb)], fill=MUTED, width=1)
    name = b.get("component", "component") + (f"  ×{b['count']}" if b.get("count") else "")
    lines = [b["note"]] if b.get("note") else []
    if b.get("variants"): lines.append("variants: " + " · ".join(b["variants"]))
    if b.get("states"): lines.append("states: " + " · ".join(b["states"]))
    th = 22 + 18 * sum(len(wrap(c, l, REG(11), w - 32)) for l in lines); ty = y + max(14, (h - th) / 2)
    if b.get("title"): c.text(x + 14, y + 16, b["title"], BOLD(12), DARK); ty = max(ty, y + 34)
    c.text(x + w / 2, ty + 8, name, MONO(13), INK, "mm"); ty += 26
    for l in lines:
        for ln in wrap(c, l, REG(11), w - 32): c.text(x + w / 2, ty, ln, REG(11), MUTED, "mm"); ty += 18
BLOCKS["slot"] = b_slot
BLOCKS.update(label=b_label, insight=b_insight, stat=b_stat, segmented=b_segmented, select=b_select, stepper=b_stepper,
              slider=b_slider, text=b_text, button=b_button, tiles=b_tiles, move=b_move)
NO_TAG.update({"label", "segmented", "select", "stepper", "slider", "text", "button"})

def shell_topbar(c, W, H, app, page):
    tb = page.get("topbar", {}); c.d.rectangle([0, 0, W, 72], fill=PANEL if page.get("layout") != "map" else None)
    c.box(20, 22, 116, 28, FILL2, None, 4); c.text(78, 36, app.get("logo", "LOGO"), BOLD(12), DARK, "mm")
    if tb.get("tabs"): b_segmented(c, W / 2 - 120 if page.get("layout") == "map" else 170, 18, 0, 36, {"items": tb["tabs"], "active": tb.get("active", 0)})
    rx = W - 64; c.d.ellipse([rx, 16, rx + 40, 56], fill=DARK); c.text(rx + 20, 36, "H", BOLD(14), PANEL, "mm"); rx -= 12
    for item in reversed(tb.get("right", [])):
        f = MONO(11) if item.isupper() else REG(13); w = c.tw(item, f) + (52 if not item.isupper() else 50); rx -= w
        c.box(rx, 18, w, 36, PANEL, LINE, 18)
        if item.isupper(): c.box(rx + 12, 28, 16, 16, FILL2, None, 3); c.text(rx + 34, 36, item, f, INK, "lm")
        else: c.text(rx + 16, 36, item, f, INK, "lm"); c.d.polygon([(rx + w - 22, 33), (rx + w - 14, 33), (rx + w - 18, 39)], fill=DARK)
        rx -= 10
    return 36, 72 + 8, W - 72, 72

# ---------- full-screen map pages: the map is the page, panels float over it ----------
def map_ground(c, x, y, w, h, seed):
    c.d.rectangle([x, y, x + w, y + h], fill="#e9e9e5"); rnd = random.Random(seed)
    for _ in range(9):  # coastline-ish land blobs and state lines, so it reads as a country map
        px, py = x + rnd.uniform(.1, .9) * w, y + rnd.uniform(.1, .9) * h
        c.d.line([(px, y + 80), (px + rnd.uniform(-90, 90), y + h - 40)], fill="#dcdcd6", width=2)
        c.d.line([(x + 40, py), (x + w - 40, py + rnd.uniform(-50, 50))], fill="#dcdcd6", width=2)
def ring(c, cx, cy, n, split, r=None):
    r = r or (16 + min(16, n ** .5 * 2.2)); box = [cx - r, cy - r, cx + r, cy + r]
    c.d.ellipse(box, fill=PANEL); a = -90; cols = [DARK, MUTED, "#bdbdb8", FILL2]
    tot = sum(split) or 1; split = [v / tot for v in split]
    for frac, col in zip(split, cols):
        if frac > 0: c.d.arc(box, a, a + 360 * frac, fill=col, width=5); a += 360 * frac
    c.text(cx, cy, str(n), BOLD(13), INK, "mm")
def site_dot(c, x, y, status, halo=True):
    if halo: c.d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=(140, 140, 135, 45))
    if status == 0: c.d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=DARK, outline=PANEL, width=2)
    elif status == 1: c.d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=PANEL, outline=DARK, width=3)
    else: c.d.ellipse([x - 6, y - 6, x + 6, y + 6], fill="#9c9c97", outline=PANEL, width=2)
def legend_mark(c, x, y, kind):
    if kind == "dot0": c.d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=DARK)
    elif kind == "dot1": c.d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=PANEL, outline=DARK, width=2)
    elif kind == "dot2": c.d.ellipse([x - 5, y - 5, x + 5, y + 5], fill="#9c9c97")
    elif kind == "dash":
        for k in range(3): c.d.line([(x - 9 + k * 7, y), (x - 5 + k * 7, y)], fill=DARK, width=2)
    elif kind == "ai": c.d.ellipse([x - 6, y - 6, x + 6, y + 6], outline=DARK, width=1); c.text(x, y, "≈", BOLD(9), DARK, "mm")
def draw_map(c, x, y, w, h, m, avoid_l, avoid_r):
    map_ground(c, x, y, w, h, m.get("id", "m")); rnd = random.Random(m.get("id", "m") + "p")
    lo, hi = x + avoid_l + 40, x + w - avoid_r - 60
    mode = m.get("mode", "dots")
    if mode == "rings":
        for n in m.get("counts", [2, 10, 2, 19, 4, 15, 61, 6, 41, 20, 3, 29, 9]):
            cx, cy = rnd.uniform(lo, hi), rnd.uniform(y + 130, y + h - 150)
            crit = rnd.uniform(.55, .95); watch = rnd.uniform(0, 1 - crit); ring(c, cx, cy, n, [crit, watch, 1 - crit - watch, 0])
    elif mode == "arcs":
        hubs = [(rnd.uniform(lo + 300, hi), rnd.uniform(y + 220, y + h - 200)) for _ in range(m.get("hubs", 5))]
        for _ in range(m.get("routes", 16)):
            sx, sy = x + avoid_l + rnd.uniform(-40, 160), rnd.uniform(y + 250, y + h * .62); tx, ty = rnd.choice(hubs)
            mx, my = (sx + tx) / 2, min(sy, ty) - rnd.uniform(40, 110)
            pts = [((1 - t) ** 2 * sx + 2 * (1 - t) * t * mx + t * t * tx, (1 - t) ** 2 * sy + 2 * (1 - t) * t * my + t * t * ty) for t in [i / 32 for i in range(33)]]
            for i in range(0, 32, 2): c.d.line([pts[i], pts[i + 1]], fill=DARK, width=2)
        for (hx, hy), n in zip(hubs, m.get("counts", [8, 2, 5, 5, 5])):
            s = rnd.uniform(.3, .7); ring(c, hx, hy, n, [s, 0, 0, 0] if False else [s, 0, 1 - s, 0])
    elif mode == "radius":
        cx, cy, r = x + w * .7, y + h * .5, h * .34
        c.d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=DARK, width=2, fill=(120, 120, 115, 18))
        c.pill(cx - 45, cy - r - 10, m.get("radius_label", "50 MI"))
        for _ in range(m.get("n", 26)):
            a, d = rnd.uniform(0, 6.28), r * rnd.uniform(.05, .95) ** .5
            site_dot(c, cx + d * __import__("math").cos(a), cy + d * __import__("math").sin(a), 0)
        site_dot(c, cx, cy, 0); c.d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], outline=DARK, width=3)
    else:
        for _ in range(m.get("n", 140)):
            st = 0 if rnd.random() < m.get("share0", .12) else (1 if rnd.random() < m.get("share1", .05) else 2)
            site_dot(c, rnd.uniform(lo - 200, hi + 60), rnd.uniform(y + 90, y + h - 90), st)
        for lab in m.get("labels", []):  # attention sites carry a label; healthy ones none
            lx, ly = rnd.uniform(lo, hi - 120), rnd.uniform(y + 140, y + h - 160); site_dot(c, lx, ly, 0)
            c.box(lx + 12, ly - 11, c.tw(lab, REG(10)) + 14, 22, PANEL, LINE, 4); c.text(lx + 19, ly, lab, REG(10), INK, "lm")
    if m.get("card"):  # the site card a click opens
        cd = m["card"]; cx, cy = min(x + w * .52, x + w - avoid_r - 290), y + h * .38; site_dot(c, cx, cy, 0)
        cw, ch = 250, 46 + 20 * len(cd["lines"]) + 16; bx, by = cx + 16, cy - 20
        c.box(bx, by, cw, ch, PANEL, DARK, 8, 2); c.text(bx + 14, by + 16, cd["title"], BOLD(13), INK, "lm")
        c.pill(bx + 14, by + 30, cd["status"], True)
        for i, l in enumerate(cd["lines"]): c.text(bx + 14, by + 66 + i * 20, l, REG(11), DARK, "lm")
    # legend pill, bottom centre
    items = m.get("legend", []); f = REG(12)
    lw = sum(c.tw(t, f) + 34 for _, t in items) + 16; lx, ly = x + avoid_l + max(0, (w - avoid_l - avoid_r - lw) / 2), y + h - 58
    c.box(lx, ly, lw, 36, PANEL, LINE, 18); px = lx + 18
    for kind, t in items: legend_mark(c, px, ly + 18, kind); c.text(px + 12, ly + 18, t, f, INK, "lm"); px += c.tw(t, f) + 34
    # zoom + fit, bottom right (left of an open right panel)
    zx = x + w - avoid_r - 66; zy = y + h - 210
    c.box(zx, zy, 42, 126, PANEL, LINE, 8)
    for i, s in enumerate(("+", "−", "⤢")): c.text(zx + 21, zy + 21 + i * 42, s if s != "⤢" else "↗", BOLD(16), DARK, "mm")
    c.text(x + w - 12, y + h - 8, "© OpenStreetMap contributors", REG(9), MUTED, "rb")
    c.tag(x, y, w - 90, h - 6, m)
def stack(c, x, y, w, blocks, gap=12):
    for b in blocks:
        h = b.get("h", 100); BLOCKS[b["type"]](c, x, y, w, h, b)
        if b["type"] not in NO_TAG: c.tag(x, y, w, h, b)
        y += h + b.get("gap", gap)
    return y
def render_map_page(app, page, out):
    W, H = page.get("width", 1280), page.get("height", 800); c = Canvas(W, H)
    left, right = page.get("left", {}), page.get("right")
    lw = left.get("width", 256) + 36 if left else 0; rw = right.get("width", 380) + 36 if right else 0
    draw_map(c, 0, 0, W, H, page["map"], lw, rw)
    x0, y0, cw, top = shell_topbar(c, W, H, app, page)
    if left:
        if left.get("card"):  # a solid panel (search form) rather than floating cards
            c.box(36, 88, left.get("width", 256), H - 120, PANEL, LINE, 10); stack(c, 56, 108, left.get("width", 256) - 40, left["blocks"], 14)
        else: stack(c, 36, 88, left.get("width", 256), left["blocks"])
    if right:
        rx = W - right.get("width", 380) - 24; c.box(rx, 88, right.get("width", 380), H - 112, PANEL, LINE, 12)
        c.d.ellipse([rx + 20, 108, rx + 36, 124], outline=DARK, width=2); c.text(rx + 46, 116, right["title"], BOLD(19), INK, "lm")
        c.d.ellipse([rx + right.get("width", 380) - 48, 100, rx + right.get("width", 380) - 16, 132], fill=FILL)
        c.d.line([(rx + right.get("width", 380) - 37, 111), (rx + right.get("width", 380) - 27, 121)], fill=DARK, width=2); c.d.line([(rx + right.get("width", 380) - 37, 121), (rx + right.get("width", 380) - 27, 111)], fill=DARK, width=2)
        stack(c, rx + 20, 148, right.get("width", 380) - 40, right["blocks"])
        c.tag(rx, 88, right.get("width", 380), H - 112, right)
    # copilot button, bottom right, above everything but overlays
    c.d.ellipse([W - 76, H - 76, W - 20, H - 20], fill=PANEL, outline=DARK, width=2); c.text(W - 48, H - 48, AGENT[0][:2].upper(), BOLD(13), INK, "mm")
    for o in page.get("overlays", []): OVERLAYS[o["type"]](c, W, H, 72, o)
    strip = 40; full = Image.new("RGB", (W, H + strip), "#ffffff"); full.paste(c.im, (0, strip))
    d = ImageDraw.Draw(full); d.text((14, 20), f"{page['id']} · {page['title']} · {page.get('persona', '')} · {W}px", font=MONO(12), fill=DARK, anchor="lm")
    full.save(os.path.join(out, "png", f"{page['id']}.png")); return full

# ---------- page ----------
def row_height(row): return max(b.get("h", 120) for b in row)
def render_page(app, page, out):
    if page.get("layout") == "map": return render_map_page(app, page, out)
    W = page.get("width", 1280); phone = W < 600
    gap = 12 if phone else GAP
    rows = page["rows"]; body_h = sum(row_height(r) for r in rows) + gap * (len(rows) - 1)
    topbar = page.get("shell") == "topbar"
    H = (80 if topbar else 56) + (16 if phone else PAD) * 2 + body_h + (64 if phone else 0)
    c = Canvas(W, H); x0, y0, cw, top = (shell_phone if phone else shell_topbar if topbar else shell_desktop)(c, W, H, app, page)
    if topbar: y0 += 12
    y = y0; col = (cw - gap * 11) / 12
    for row in rows:
        x = x0; rh = row_height(row)
        for b in row:
            span = b.get("span", 12); w = col * span + gap * (span - 1); h = b.get("h", rh)
            BLOCKS[b["type"]](c, x, y, w, h, b)
            if b["type"] not in NO_TAG: c.tag(x, y, w, h, b)
            x += w + gap
        y += rh + gap
    for o in page.get("overlays", []): OVERLAYS[o["type"]](c, W, H, top, o)
    # page label strip (outside the screen), so a reviewer always knows which page this is
    strip = 40; full = Image.new("RGB", (W, H + strip), "#ffffff"); full.paste(c.im, (0, strip))
    d = ImageDraw.Draw(full); d.text((14, 20), f"{page['id']} · {page['title']} · {page.get('persona', '')} · {W}px", font=MONO(12), fill=DARK, anchor="lm")
    full.save(os.path.join(out, "png", f"{page['id']}.png")); return full

def manifest(spec):
    comps = OrderedDict()
    parts = set()
    def add(b, page):
        if not b.get("component"):  # header, filters, tabs, labels, single controls: page parts, not components
            parts.add(b["type"]); return
        name = b["component"]
        e = comps.setdefault(name, {"component": name, "type": b["type"], "pages": [], "blocks": [], "variants": set(), "features": set(), "states": set()})
        if page["id"] not in e["pages"]: e["pages"].append(page["id"])
        if b.get("id"): e["blocks"].append(f"{page['id']}/{b['id']}")
        e["variants"].update(b.get("variants", []))
        if b.get("cmp"): e.setdefault("cmp", []); e["cmp"] += [b["cmp"]] if b["cmp"] not in e["cmp"] else []
        if b.get("note"): e.setdefault("notes", []); e["notes"] += [f"{page['id']}: {b['note']}"]
        for k in ("kind", "select", "bulk", "status_col", "cluster", "popup", "card"):
            if b.get(k): e["features"].add(f"kind:{b[k]}" if k == "kind" else k)
        if b["type"] == "map": e.setdefault("modes", []); e["modes"] += [b["mode"]] if b["mode"] not in e["modes"] else []
        e["states"].update(b.get("states", []))
        if b["type"] == "map" and b.get("data"):
            e.setdefault("data_contract", {})[b.get("mode", "dots")] = b["data"]
        if b["type"] == "map" and b.get("behaviour"):
            e["behaviour"] = b["behaviour"]
    shells = set()
    for p in spec["pages"]:
        shells.add("phone" if p.get("width", 1280) < 600 else "desktop")
        for r in p.get("rows", []):
            for b in r: add(b, p)
        if p.get("map"): add(p["map"], p)
        for b in p.get("left", {}).get("blocks", []): add(b, p)
        if p.get("right"): add(dict({k: v for k, v in p["right"].items() if k != "blocks"}, type=p["right"].get("type", "panel")), p)
        for b in (p.get("right") or {}).get("blocks", []): add(b, p)
        for o in p.get("overlays", []): add(o, p)
    out = {"app": spec["app"]["name"], "client": spec.get("client"), "use_case": spec.get("use_case"),
           "shells": sorted(shells), "pages": [{"id": p["id"], "title": p["title"], "persona": p.get("persona"),
           "width": p.get("width", 1280), "brd_ref": p.get("brd_ref")} for p in spec["pages"]], "components": []}
    for e in comps.values():
        e["variants"] = sorted(e["variants"]); e["features"] = sorted(e["features"]); e["states"] = sorted(e["states"]); out["components"].append(e)
    out["page_parts"] = sorted(parts)
    return out

def validate(spec):
    """Stop on spec errors before drawing anything, with one line per problem."""
    errs, ids = [], set()
    if not spec.get("pages"): sys.exit("spec errors:\n  spec has no pages")
    for p in spec.get("pages", []):
        pid = p.get("id", "?")
        if pid in ids: errs.append(f"{pid}: duplicate page id")
        ids.add(pid)
        for k in ("id", "title", "persona"):
            if not p.get(k): errs.append(f"{pid}: page needs '{k}'")
        blocks = [b for r in p.get("rows", []) for b in r] + p.get("left", {}).get("blocks", []) + (p.get("right") or {}).get("blocks", [])
        if p.get("layout") == "map":
            m = p.get("map") or {}
            if m.get("type") != "map": errs.append(f"{pid}: a map page needs a 'map' block with type 'map'")
            if m.get("mode") not in ("rings", "dots", "arcs", "radius"): errs.append(f"{pid}: map mode must be rings, dots, arcs or radius")
            if not m.get("data"): errs.append(f"{pid}: map block needs its data contract ('data')")
            if not m.get("legend"): errs.append(f"{pid}: map block needs a legend in this screen's own words")
        elif not p.get("rows"): errs.append(f"{pid}: page has no rows")
        for r in p.get("rows", []):
            if sum(b.get("span", 12) for b in r) > 12: errs.append(f"{pid}: a row spans more than 12 columns")
            if any(b.get("type") == "map" for b in r): errs.append(f"{pid}: a map is the page, never a block in a row: use \"layout\": \"map\" (references/map-component.md)")
        for o in p.get("overlays", []):
            if o.get("type") not in OVERLAYS: errs.append(f"{pid}: overlay type must be drawer or modal, not '{o.get('type')}'")
            if not o.get("component"): errs.append(f"{pid}: overlay {o.get('id', '')} needs a 'component' name")
        for b in blocks:
            t = b.get("type")
            if t not in BLOCKS: errs.append(f"{pid}: unknown block type '{t}'" + (" (drawer and modal go in 'overlays')" if t in OVERLAYS else ""))
            if t in BLOCKS and t not in NO_TAG and not b.get("component"):
                errs.append(f"{pid}: block '{t}' {b.get('id', '')} needs a 'component' name")
    if errs: sys.exit("spec errors:\n  " + "\n  ".join(errs))

def main(spec_path, out):
    spec = json.load(open(spec_path)); validate(spec); os.makedirs(os.path.join(out, "png"), exist_ok=True)
    AGENT[0] = spec.get("app", {}).get("agent", "AI")
    imgs = [render_page(spec["app"], p, out) for p in spec["pages"]]
    slug = spec.get("slug", "app")
    # PDF: one page per wireframe, each scaled onto A4 landscape-ish width
    pdf = [im.convert("RGB") for im in imgs]; pdf[0].save(os.path.join(out, f"{slug}-wireframes.pdf"), save_all=True, append_images=pdf[1:], resolution=110)
    json.dump(manifest(spec), open(os.path.join(out, "wireframe-manifest.json"), "w"), indent=2)
    print(f"{len(imgs)} pages → {out}/png, {slug}-wireframes.pdf, wireframe-manifest.json")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
