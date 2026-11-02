#!/usr/bin/env python3
"""metrics.py — tokens, models and time per POC Studio stage, and for the whole run.

Claude Code already logs every model call (model, token usage, timestamp) in its session transcripts:
  ~/.claude/projects/<project-folder>/<session-id>.jsonl          the main conversation
  ~/.claude/projects/<project-folder>/<session-id>/subagents/*.jsonl   subagents (e.g. the ai-pm reviewer)
This script adds the one thing those logs lack — when each stage started and ended — and cuts the usage by stage.

Stage marks live in <workspace>/metrics/events.jsonl (one line per status change). The report is written to
<workspace>/metrics/metrics.json and metrics.md.

usage:
  metrics.py mark <workspace> <stage> <status>        record a stage status change, now
                                                      (status: running | in_review | awaiting_approval | approved | changes | skipped)
  metrics.py report <workspace> [--stage <stage>] [--json] [--projects <dir>]
                                                      print the stage's cut (or every stage) plus the run's totals

Time:
  work time  = time in running / in_review (the stage and its AI PM review doing the work)
  gate wait  = time in awaiting_approval (waiting for the person to approve)
  total      = work time + gate wait
Tokens are assigned to the stage whose window (running → approved) contains the call; calls outside every stage
window are reported as "outside stages" (setup, resume chatter). UnifyApps Headless runs inside Claude Code, so its
planning and its ua:* builder subagents are counted. Not counted: models the built app runs on the UnifyApps platform
(its AI agents, LLM nodes in automations, evaluation runs).
"""
import datetime, glob, json, os, sys

STAGES = ["requirement-gathering", "scoping", "wireframes", "design-system", "build", "collaterals"]
WORK = {"running", "in_review"}
WAIT = {"awaiting_approval"}
CLOSED = {"approved", "skipped"}
STATUSES = WORK | WAIT | CLOSED | {"changes"}
OUTSIDE = "outside stages"


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def parse_ts(s):
    try:
        return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def mdir(ws):
    return os.path.join(os.path.abspath(ws), "metrics")


def project_dir(ws):
    """The folder Claude Code runs in: $CLAUDE_PROJECT_DIR, else state.json's autopilot flag, else <ws>/../.."""
    if os.environ.get("CLAUDE_PROJECT_DIR"):
        return os.path.abspath(os.environ["CLAUDE_PROJECT_DIR"])
    try:
        flag = json.load(open(os.path.join(ws, "state.json"))).get("autopilot_flag")
        if flag:
            return os.path.dirname(os.path.dirname(os.path.abspath(flag)))
    except Exception:
        pass
    return os.path.dirname(os.path.dirname(os.path.abspath(ws)))


# ---------------------------------------------------------------- mark

def cmd_mark(ws, stage, status):
    if status not in STATUSES:
        sys.exit(f"unknown status {status!r}; use one of: {', '.join(sorted(STATUSES))}")
    os.makedirs(mdir(ws), exist_ok=True)
    ev = {"ts": now().isoformat(), "stage": stage, "status": status, "project_dir": project_dir(ws)}
    with open(os.path.join(mdir(ws), "events.jsonl"), "a") as h:
        h.write(json.dumps(ev) + "\n")
    print(f"metrics: {stage} → {status}")


def load_events(ws):
    f = os.path.join(mdir(ws), "events.jsonl")
    out = []
    if os.path.exists(f):
        for line in open(f):
            try:
                e = json.loads(line)
                e["t"] = parse_ts(e["ts"])
                if e["t"]:
                    out.append(e)
            except Exception:
                continue
    return sorted(out, key=lambda e: e["t"])


def intervals(events, end_time):
    """Per stage: list of (start, end, kind) with kind work|wait. A stage's last open state runs to end_time."""
    by = {}
    for e in events:
        by.setdefault(e["stage"], []).append(e)
    out = {}
    for stage, evs in by.items():
        iv = []
        for i, e in enumerate(evs):
            st = "running" if e["status"] == "changes" else e["status"]
            if st in CLOSED:
                continue
            nxt = evs[i + 1]["t"] if i + 1 < len(evs) else end_time
            iv.append((e["t"], nxt, "work" if st in WORK else "wait"))
        out[stage] = iv
    return out


# ---------------------------------------------------------------- transcripts

def transcript_files(root, since):
    # main: <project>/<session>.jsonl · subagents: <project>/<session>/subagents/[<subdir>/]agent-<id>.jsonl
    files = glob.glob(os.path.join(root, "*", "*.jsonl")) + \
        glob.glob(os.path.join(root, "*", "*", "subagents", "**", "*.jsonl"), recursive=True)
    cutoff = since.timestamp() - 3600 if since else 0
    return [f for f in files if os.path.getmtime(f) >= cutoff]


def agent_label(path, entry):
    """main | subagent:<type>. The type is the agentType in the sibling agent-<id>.meta.json Claude Code writes
    (UnifyApps Headless builders are "ua:<name>", the reviewer "poc-studio:ai-pm" or "ai-pm")."""
    if "/subagents/" not in path and not entry.get("isSidechain"):
        return "main"
    meta = path[:-len(".jsonl")] + ".meta.json"
    try:
        m = json.load(open(meta))
        t = m.get("agentType") or m.get("subagent_type") or m.get("type")
        if t:
            return f"subagent:{t}"
    except Exception:
        pass
    return "subagent"


def calls(projects_root, project_dirs, since):
    """One record per model call, de-duplicated by message id (Claude Code logs a call once per content block)."""
    seen = {}
    pdirs = tuple(d.rstrip("/") for d in project_dirs)
    for f in transcript_files(projects_root, since):
        try:
            fh = open(f)
        except Exception:
            continue
        with fh:
            for line in fh:
                if '"usage"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("type") != "assistant":
                    continue
                cwd = (d.get("cwd") or "").rstrip("/")
                if pdirs and not any(cwd == p or cwd.startswith(p + "/") for p in pdirs):
                    continue
                m = d.get("message") or {}
                u = m.get("usage") or {}
                model = m.get("model")
                if not u or not model or model == "<synthetic>":
                    continue
                t = parse_ts(d.get("timestamp", ""))
                if not t or (since and t < since):
                    continue
                key = m.get("id") or d.get("requestId") or d.get("uuid")
                rec = {
                    "t": t, "model": model, "agent": agent_label(f, d), "session": d.get("sessionId"),
                    "input": u.get("input_tokens", 0) or 0,
                    "output": u.get("output_tokens", 0) or 0,
                    "cache_write": u.get("cache_creation_input_tokens", 0) or 0,
                    "cache_read": u.get("cache_read_input_tokens", 0) or 0,
                    "thinking": ((u.get("output_tokens_details") or {}).get("thinking_tokens", 0) or 0),
                    "web_search": ((u.get("server_tool_use") or {}).get("web_search_requests", 0) or 0),
                }
                old = seen.get(key)
                # keep the most complete copy of the call (the last streamed block carries the final output count)
                if not old or rec["output"] >= old["output"]:
                    seen[key] = rec
    return sorted(seen.values(), key=lambda r: r["t"])


# ---------------------------------------------------------------- report

TOKEN_KEYS = ["input", "output", "cache_write", "cache_read", "thinking", "web_search"]


def blank():
    return {k: 0 for k in TOKEN_KEYS} | {"calls": 0}


def add(acc, r):
    for k in TOKEN_KEYS:
        acc[k] += r[k]
    acc["calls"] += 1


def bucket():
    return {"totals": blank(), "by_model": {}, "by_agent": {}, "sessions": set(),
            "work_seconds": 0.0, "wait_seconds": 0.0, "started": None, "ended": None}


def stage_of(t, ivs):
    hit = None
    for stage, iv in ivs.items():
        for s, e, _ in iv:
            if s <= t < e and (hit is None or s > hit[1]):
                hit = (stage, s)  # overlapping windows: the most recently started stage wins
    return hit[0] if hit else OUTSIDE


def build(ws, projects_root):
    events = load_events(ws)
    end = now()
    ivs = intervals(events, end)
    since = events[0]["t"] if events else None
    pdirs = sorted({e.get("project_dir") for e in events if e.get("project_dir")} | {project_dir(ws)})
    rs = calls(projects_root, pdirs, since)

    stages = {}
    order = [s for s in STAGES if s in ivs] + [s for s in ivs if s not in STAGES]
    for s in order:
        b = stages[s] = bucket()
        for a, z, kind in ivs[s]:
            b["work_seconds" if kind == "work" else "wait_seconds"] += (z - a).total_seconds()
        ts = [e["t"] for e in events if e["stage"] == s]
        b["started"] = min(ts)
        b["ended"] = max(ts)
        b["status"] = next((e["status"] for e in reversed(events) if e["stage"] == s), None)
    overall = bucket()
    for r in rs:
        s = stage_of(r["t"], ivs)
        b = stages.setdefault(s, bucket())
        for target in (b, overall):
            add(target["totals"], r)
            add(target["by_model"].setdefault(r["model"], blank()), r)
            add(target["by_agent"].setdefault(r["agent"], blank()), r)
            target["sessions"].add(r["session"])
    overall["work_seconds"] = sum(b["work_seconds"] for k, b in stages.items() if k != OUTSIDE)
    overall["wait_seconds"] = sum(b["wait_seconds"] for k, b in stages.items() if k != OUTSIDE)
    stamps = [e["t"] for e in events] + [r["t"] for r in rs]
    overall["started"] = min(stamps) if stamps else None
    overall["ended"] = max(stamps) if stamps else None
    return {"workspace": os.path.abspath(ws), "generated": end, "marked": bool(events),
            "stages": stages, "overall": overall}


def fmt_n(n):
    return f"{n/1_000_000:.2f}M" if n >= 1_000_000 else f"{n/1000:.1f}k" if n >= 1000 else str(n)


def fmt_t(sec):
    sec = int(sec)
    h, m = divmod(sec // 60, 60)
    return f"{h}h {m:02d}m" if h else f"{m}m {sec % 60:02d}s"


def short_model(m):
    return m.replace("claude-", "")


def row(name, b):
    t = b["totals"]
    models = ", ".join(short_model(m) for m, _ in sorted(b["by_model"].items(), key=lambda kv: -kv[1]["output"])) or "—"
    return (f"| {name} | {models} | {t['calls']} | {fmt_n(t['input'])} | {fmt_n(t['output'])} | "
            f"{fmt_n(t['cache_read'])} | {fmt_n(t['cache_write'])} | {fmt_t(b['work_seconds'])} | "
            f"{fmt_t(b['wait_seconds'])} | {fmt_t(b['work_seconds'] + b['wait_seconds'])} |")


def is_headless(agent):
    return agent.startswith("subagent:ua:")


HEAD = ("| Stage | Model(s) | Calls | Input | Output | Cache read | Cache write | Work time | Gate wait | Total time |\n"
        "|---|---|---|---|---|---|---|---|---|---|")


def detail(name, b):
    lines = [f"**{name}** — by model:"]
    for m, t in sorted(b["by_model"].items(), key=lambda kv: -kv[1]["output"]):
        lines.append(f"- {m}: {t['calls']} calls · in {fmt_n(t['input'])} · out {fmt_n(t['output'])} "
                     f"(thinking {fmt_n(t['thinking'])}) · cache read {fmt_n(t['cache_read'])} · "
                     f"cache write {fmt_n(t['cache_write'])}" + (f" · web searches {t['web_search']}" if t["web_search"] else ""))
    ua = [t for a, t in b["by_agent"].items() if is_headless(a)]
    if ua:
        tot = {k: sum(t[k] for t in ua) for k in ("calls", "input", "output", "cache_read", "cache_write")}
        lines.append(f"UnifyApps Headless builders (ua:*): {tot['calls']} calls · in {fmt_n(tot['input'])} · "
                     f"out {fmt_n(tot['output'])} · cache read {fmt_n(tot['cache_read'])} · "
                     f"cache write {fmt_n(tot['cache_write'])}")
    if len(b["by_agent"]) > 1 or any(a != "main" for a in b["by_agent"]):
        lines.append("by agent: " + " · ".join(f"{a} {fmt_n(t['output'])} out / {t['calls']} calls"
                                                for a, t in sorted(b["by_agent"].items())))
    return "\n".join(lines)


def markdown(rep, only=None):
    st = rep["stages"]
    out = []
    if not rep["marked"]:
        out.append("_No stage marks yet (metrics/events.jsonl is empty): showing every call in this folder as "
                   "\"outside stages\"._\n")
    if only:
        b = st.get(only)
        if not b:
            return f"No metrics for stage {only!r} yet."
        out += [f"### Stage metrics · {only}", "", HEAD, row(only, b), "", detail(only, b), ""]
    out += ["### Run so far · every stage", "", HEAD]
    for name, b in st.items():
        out.append(row(name, b))
    out.append(row("**Overall**", rep["overall"]))
    out += ["", detail("Overall", rep["overall"]), "",
            "_Work time = running + AI PM review; gate wait = waiting for approval. UnifyApps Headless (planning and "
            "ua:* builders) is included; models running on the UnifyApps platform itself are not._"]
    return "\n".join(out)


def jsonable(rep):
    def conv(o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        if isinstance(o, set):
            return sorted(x for x in o if x)
        if isinstance(o, dict):
            return {k: conv(v) for k, v in o.items()}
        if isinstance(o, list):
            return [conv(v) for v in o]
        return o
    return conv(rep)


def cmd_report(ws, only=None, as_json=False, projects_root=None):
    root = projects_root or os.path.join(os.path.expanduser(os.environ.get("CLAUDE_CONFIG_DIR", "~/.claude")), "projects")
    rep = build(ws, root)
    md = markdown(rep, only)
    os.makedirs(mdir(ws), exist_ok=True)
    data = jsonable(rep)
    json.dump(data, open(os.path.join(mdir(ws), "metrics.json"), "w"), indent=2)
    open(os.path.join(mdir(ws), "metrics.md"), "w").write(markdown(rep) + "\n")
    print(json.dumps(data["stages"].get(only, data) if only else data, indent=2) if as_json else md)


def main(a):
    if len(a) >= 4 and a[0] == "mark":
        return cmd_mark(a[1], a[2], a[3])
    if len(a) >= 2 and a[0] == "report":
        opts = a[2:]
        def opt(name):
            return opts[opts.index(name) + 1] if name in opts and opts.index(name) + 1 < len(opts) else None
        return cmd_report(a[1], opt("--stage"), "--json" in opts, opt("--projects"))
    sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
