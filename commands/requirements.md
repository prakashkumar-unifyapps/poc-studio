---
description: Make one Requirement Gathering document for a client use case, on its own (no POC needed)
argument-hint: <Client> | <Use case> [| <POC ID>]
---

Make **the Requirement Gathering document (Orbit type `requirements`)** on its own, without a POC and without the other stages: **$ARGUMENTS**

The arguments are `<Client> | <Use case> [| <POC ID>]`. The POC ID is optional; without it the asset is made all the same.

## Step 0 — make sure this is the latest POC Studio (always first)

This command was loaded from **POC Studio v1.26.0**. Before anything else, run this check with the Bash tool:

```bash
LOADED="1.26.0"
python3 - "$LOADED" <<'PY'
import json, subprocess, sys, urllib.request
loaded = sys.argv[1]
url = "https://raw.githubusercontent.com/shubhankargarg-lang/poc-studio/main/.claude-plugin/plugin.json"
try:
    latest = json.load(urllib.request.urlopen(url, timeout=10))["version"]
except Exception as e:
    print(f"UPDATE_CHECK_FAILED {e}"); sys.exit(0)
v = lambda s: tuple(int(x) for x in s.split("."))
if v(latest) <= v(loaded):
    print(f"UP_TO_DATE {loaded}"); sys.exit(0)
def run(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    print("$", " ".join(cmd)); print((r.stdout + r.stderr).strip()); return r.returncode
ok = run("claude", "plugin", "marketplace", "update", "unifyapps-poc") == 0
for scope in ("user", "project", "local"):
    if ok and run("claude", "plugin", "update", "poc-studio@unifyapps-poc", "-s", scope) == 0:
        print(f"UPDATED {loaded} -> {latest}"); sys.exit(0)
print(f"UPDATE_FAILED {loaded} -> {latest}")
PY
```

Then act on the last line it printed:

- **`UP_TO_DATE`** → carry on with the run below.
- **`UPDATED <old> -> <new>`** → the new version is on disk, but this session is still running the old one, and only
  the person can switch it. **Stop here and do not start the run.** Tell the person, in two lines:
  "POC Studio was updated from <old> to <new>. Type `/reload-plugins`, then run the same command again:
  `/poc-studio:requirements $ARGUMENTS`".
- **`UPDATE_FAILED`** (e.g. the `claude` command is not on the shell's PATH) → stop and ask the person to run these
  three commands, then the same `/poc-studio:requirements` command again:
  `/plugin marketplace update unifyapps-poc`, `/plugin update poc-studio@unifyapps-poc`, `/reload-plugins`.
- **`UPDATE_CHECK_FAILED`** (no network to GitHub) → say in one line that the update check could not run and that you
  are continuing on v1.26.0, then carry on.

## Step 1 — prerequisites (asked in the chat, before anything runs)

Load the `asset-run` skill (Skill tool: `poc-studio:asset-run`) and follow its **1 · Prerequisites** for the asset
**`requirements`**: take each prerequisite from the arguments, then from an existing workspace for this client and use case
(offer what you find in one line), then ask for everything still missing in **one** question. Never ask for a password.

- **Required:** Client name · Use case · the Slack and Google Drive connectors connected.
- **Optional** (asked once, in the same question; the run goes on without it): Client website · Gmail and Calendar connectors.
- **If something required is missing:** Connectors missing: stop and ask the person to connect them (in Claude Code: `/mcp`, or as a claude.ai connector), then check again.

If a POC ID was given, verify it as `asset-run` § 1 describes (found → the Orbit row carries it; not found → ask once to
correct it or drop it).

## Step 2 — make the asset

Only once every required prerequisite is in hand, continue with `asset-run` §§ 2–6 for **`requirements`**: the workspace and
run state, the stage run unattended (questions go to the AI PM), the AI PM review, the Orbit write as a one-off
document (a new version every time), the result in the chat, and the approval.
