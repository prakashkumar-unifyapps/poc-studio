---
description: Start (or resume) a UnifyApps POC for a client use case — requirement gathering → scoping → wireframes → design system → UnifyApps Headless build → collaterals
argument-hint: <client name> | <use case name> | <POC ID>
---

Run the POC Studio pipeline for: **$ARGUMENTS**

The arguments are `<client name> | <use case name> | <POC ID>` (e.g. `Acme | Invoice matching | POC-acme-20261018`).
**All three are required. Do not start the run until a POC ID has been given** (format `POC-<client>-<YYYYMMDD>`).

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
  the person can switch it. **Stop here and do not start the pipeline.** Tell the person, in two lines:
  "POC Studio was updated from <old> to <new>. Type `/reload-plugins`, then run the same command again:
  `/poc-studio:start $ARGUMENTS`".
- **`UPDATE_FAILED`** (e.g. the `claude` command is not on the shell's PATH) → stop and ask the person to run these
  three commands, then the same `/poc-studio:start` command again:
  `/plugin marketplace update unifyapps-poc`, `/plugin update poc-studio@unifyapps-poc`, `/reload-plugins`.
- **`UPDATE_CHECK_FAILED`** (no network to GitHub) → say in one line that the update check could not run and that you
  are continuing on v1.26.0, then carry on.

## Step 1 — verify the POC ID in Orbit (after the update check, before anything else)

Only once Step 0 has finished and the POC ID has been given:

1. Load the `orbit-writeback` skill (Skill tool: `poc-studio:orbit-writeback`) and run its **Setup**: load UnifyApps Headless's
   tenant tools, then call `get_records` on the object **`orbit_studio_poc`** on Orbit UAT
   (`https://orbit.uat.unifyapps.com`), **filtered on `poc_id` EQUAL the POC ID given above**.
2. **Found** → keep the record id and the POC owner's name and email (they go in `state.json` → `orbit` once the
   workspace exists), and go on to Step 2.
3. **Not found** → **stop.** Tell the person: "POC ID `<POC ID>` was not found in Orbit (`orbit_studio_poc`). Please
   check the POC ID and send the correct one." Wait for their reply, then run this check again with the new ID.
   Do not start the pipeline until the check finds the record.
4. **The check cannot run** (UnifyApps Headless not installed, not set up in this folder, or Orbit needs a sign-in) → stop and
   tell the person what is needed (install UnifyApps Headless, or run `/ua:setup` here on `orbit.uat.unifyapps.com` and sign in
   themselves — never type a password), then run the check again. Never skip it.

## Step 2 — run the pipeline

Load the `poc-orchestrator` skill from this plugin (Skill tool: `poc-studio:poc-orchestrator`) and follow it exactly,
starting with Setup. If the client name, the use case name or the POC ID is missing above, ask once for the missing
values and **wait**; nothing starts without the POC ID. If a workspace for this client and use case already exists in
the current folder with the same POC ID, resume from its `state.json`.
