---
description: Make the demo collaterals for a built app — demo script, deck, video, or any of them — on their own (no POC needed)
argument-hint: <Client> | <Use case> | <App preview link> [| <POC ID>]
---

Make **the collaterals the person chooses (Orbit types `demo_script`, `deck`, `video`; one row each)** on its own, without a POC and without the other stages: **$ARGUMENTS**

The arguments are `<Client> | <Use case> | <App preview link> [| <POC ID>]`. The POC ID is optional; without it the asset is made all the same.

## Step 0 — make sure this is the latest POC Studio (always first)

This command was loaded from **POC Studio v1.25.1**. Before anything else, run this check with the Bash tool:

```bash
LOADED="1.25.1"
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
  `/poc-studio:collaterals $ARGUMENTS`".
- **`UPDATE_FAILED`** (e.g. the `claude` command is not on the shell's PATH) → stop and ask the person to run these
  three commands, then the same `/poc-studio:collaterals` command again:
  `/plugin marketplace update unifyapps-poc`, `/plugin update poc-studio@unifyapps-poc`, `/reload-plugins`.
- **`UPDATE_CHECK_FAILED`** (no network to GitHub) → say in one line that the update check could not run and that you
  are continuing on v1.25.1, then carry on.

## Step 1 — prerequisites (asked in the chat, before anything runs)

Load the `asset-run` skill (Skill tool: `poc-studio:asset-run`) and follow its **1 · Prerequisites** for the asset
**`collaterals`**: take each prerequisite from the arguments, then from an existing workspace for this client and use case
(offer what you find in one line), then ask for everything still missing in **one** question. Never ask for a password.

- **Required:** Client name · Use case · which collaterals (always asked — demo script, deck, video: any one, two or all three — unless the command already says which, e.g. `deck only` after the preview link) · the app's preview link (a published or builder link is turned into the preview link) · a valid Orbit sign-in · the collateral tools for the ones chosen.
- **Optional** (asked once, in the same question; the run goes on without it): A BRD or scoping document (strongly recommended: it drives the story and personas) · a Requirement Gathering document · the audience (business, technical or mixed).
- **If something required is missing:** Ask for what is missing; the person signs in to Orbit themselves in the window that opens.

If a POC ID was given, verify it as `asset-run` § 1 describes (found → the Orbit row carries it; not found → ask once to
correct it or drop it).

## Step 2 — make the asset

Only once every required prerequisite is in hand, continue with `asset-run` §§ 2–6 for **`collaterals`**: the workspace and
run state, the stage run unattended (questions go to the AI PM), the AI PM review, the Orbit write as a one-off
document (a new version every time), the result in the chat, and the approval.
