# POC Studio

A Claude Code plugin that runs a UnifyApps POC end to end for one client:

**Requirement Gathering → Scoping → Wireframes → Design System → UnifyApps Headless build → Collaterals**

with a shared **Research** skill any stage can call, and an **AI PM** that checks every stage's output and
answers every clarification question, so the person is only asked to approve (or redirect) at the end of each stage.

## Install

In Claude Code:

```
/plugin marketplace add shubhankargarg-lang/poc-studio
/plugin install poc-studio@unifyapps-poc
```

On Claude Code 2.1.275 or later, one line also works:

```
/plugin install poc-studio --marketplace shubhankargarg-lang/poc-studio
```

**Staying on the latest version:** every `/poc-studio:start` first checks GitHub for a newer release. If one exists it
updates the plugin and asks you to type `/reload-plugins` and run the same command again, so every POC runs on the
latest version. To also get updates in the background, turn on auto-update once: `/plugin` → **Marketplaces** →
`unifyapps-poc` → **Enable auto-update**. Manual update at any time:
`/plugin marketplace update unifyapps-poc`, `/plugin update poc-studio@unifyapps-poc`, then `/reload-plugins`.

## Releasing a change (maintainers)

The update check compares versions, so **every change pushed to `main` needs a new version number**. Use:

```
scripts/release.sh 1.4.0 "what changed"
```

It bumps the version in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `commands/start.md`,
then commits and pushes to `main`.

Requires the **UnifyApps Headless** plugin for stage 4 (`/ua:setup`) and the **Slack** and **Google Drive** connectors
(Gmail and Google Calendar are optional but improve requirement gathering). Drive also hosts the demo video (always,
whatever its size), so it opens straight from Orbit.

### Collateral tools (Mac)

The first run installs every tool the collaterals need, once per Mac, in the background: about 1 GB into
`~/.local/poc-collateral`, no admin password and no Homebrew. Every later POC reuses it, so the collateral stage
starts in seconds. To check it any time: `bash ~/.local/poc-collateral/doctor.sh` (every line should read `ok`).

### Demo video on Google Drive

Every demo video goes to one company **shared drive, `POC Studio Video Library`**, which everyone at UnifyApps already
belongs to (`allemployees@unifyapps.com`), so every video opens for anyone in the company and you do not create or
share any folder yourself. The video goes through **Google Drive for desktop**: the plugin copies it into the shared
drive's local folder (Finder → Google Drive → Shared drives → POC Studio Video Library), the Drive app uploads it, and
the Drive connector finds it and puts its link in Orbit. Setup checks this at the start and flags it if it will not
work. To pass the check:

1. Install Google Drive for desktop and sign in with your company Google account. It must be running (it sits in the
   menu bar; it does not need a window open). Check that **Shared drives → POC Studio Video Library** shows in Finder.
2. Sign the **Google Drive connector** in Claude in to the **same** account.
3. Approve the two one-time prompts the first time: Claude Code's "write outside this folder" and macOS's "access
   files on Google Drive". To skip Claude Code's prompt in future, add the Drive folder to your Claude Code settings
   (`~/.claude/settings.json`):
   ```json
   { "permissions": { "additionalDirectories": ["~/Library/CloudStorage"] } }
   ```

If the shared drive is not available, the run falls back to your own `My Drive/POC Studio` folder (the old route,
which needs that folder shared with UnifyApps once). If neither works, the run still goes ahead; at the end you are
asked to drop the video into the shared drive.

## Use

Open Claude Code in the folder where the POC files should live, then:

```
/poc-studio:start <Client name> | <Use case name> | <POC ID>
```

For example `/poc-studio:start Acme | Invoice matching | POC-acme-20261018`. **The POC ID is required** (format
`POC-<client>-<YYYYMMDD>`); the run does not start until it is given, and it must exist in Orbit: right after the update check, the run reads
the Orbit object `orbit_studio_poc` (filtered on `poc_id`) and stops, asking you to check the ID, if it is not found. The POC ID is recorded in the progress file,
the documents and the build so everything can be traced to the POC.

**Orbit write-back:** at every gate the run uploads the stage's files to Orbit · POC Studio and writes the Document,
Activity, Iteration and POC rows (skill `orbit-writeback`), so the POC owner, the team and the Slack thread follow the
run. It uses UnifyApps Headless's own tenant tools in the session (the same ones it builds with) on
`orbit.uat.unifyapps.com`, and uploads files as public tenant links, so the folder you run in must be set up with
`/ua:setup` on that tenant.

The use case name keeps the whole run focused:
Requirement Gathering searches Slack, Gmail, Drive and Calendar for that use case and sets aside material about the
client's other use cases, and each use case gets its own folder. Run the same command again later to resume:
progress is kept in `<client-slug>/<usecase-slug>/state.json`.

## Make one asset

Any one asset can be made on its own, without a POC and without running the other stages. Each command collects
what that asset needs **in the chat first**, then runs the same stage skill the pipeline uses, unattended, has the
AI PM review it, saves it in the client folder, writes it to Orbit as a **one-off document** (shown in POC Build Loop
under **Assets**), shows you the file and its links, and asks you to approve it. Running the same command again later
(or asking for changes) saves a new version; the older one shows as superseded.

| Command | Makes (Orbit type) | Runs | Assets page |
|---|---|---|---|
| `/poc-studio:requirements <Client> \| <Use case> [\| <POC ID>]` | Requirement Gathering document (`requirements`) | `requirement-gathering` | `/assets/requirements` |
| `/poc-studio:brd <Client> \| <Use case> [\| <POC ID>]` | BRD / scoping document (`brd`) | `scoping-l1-first` | `/assets/brd` |
| `/poc-studio:wireframes <Client> \| <Use case> [\| <POC ID>]` | Low-fidelity wireframes: PNG frames, PDF and component manifest (`wireframes`) | `wireframes` | `/assets/wireframes` |
| `/poc-studio:design <Client> \| <Use case> [\| <POC ID>]` | Design system, HTML (`design_system`) | `design-system` | `/assets/design-system` |
| `/poc-studio:app <Client> \| <Use case> [\| <POC ID>]` | The app, saved as its preview link (`app`) | Stage 4: `ua:setup`, `platform-master`, `ua:plan` (Zen) | `/assets/app` |
| `/poc-studio:collaterals <Client> \| <Use case> \| <App preview link> [\| <POC ID>]` | Demo script, deck, video — you choose any one, two or all three (`demo_script`, `deck`, `video`) | `poc-collateral-studio` | `/assets/demo-script`, `/assets/deck`, `/assets/video` |

Assets pages are at `https://poc-build-loop-orbit.tensor-uat.unifyapps.com/assets/<page>`. The POC ID is optional on
every command: when it is given and found in Orbit, the row shows a POC chip; a one-off asset never moves a POC.

**What each command asks for** (from the arguments, then from an existing client folder, then in one question):

| Command | Required | Optional |
|---|---|---|
| requirements | Client · Use case · Slack and Google Drive connectors | Client website · Gmail and Calendar connectors |
| brd | Client · Use case · At least one input: an RG document, meeting notes, an email, client files, or a Slack or Drive link | Client website |
| wireframes | Client · Use case · A BRD or scoping document | — |
| design | Client · Use case · A BRD or scoping document · Client website ("derive it" is fine) | Wireframes (from this folder) · Client logo · Brand guidelines |
| app | Client · Use case · A BRD or scoping document · UnifyApps Headless installed and this folder set up (`/ua:setup`) · The collateral tools (for the browser check before publish) and an Orbit sign-in · Not a folder whose setup belongs to a running POC (else it asks first) | A design system HTML (else UnifyApps Headless's default look) |
| collaterals | Client · Use case · Which collaterals (always asked, unless the command already says which, e.g. `deck only`) · The app's **preview link** · Orbit sign-in · The collateral tools | A BRD or scoping document (recommended) · An RG document · The audience |

Only preview links are accepted for an app (`…/agent-api/preview/b/<app id>/main` or `…/p/0/interfaces/<app id>/preview`
on `orbit.uat.unifyapps.com`); a published or builder link is turned into the preview link from its app id. You never
type a password: sign-ins happen in the browser window the command opens. The Orbit write needs UnifyApps Headless
set up in the folder (`/ua:setup` on `orbit.uat.unifyapps.com`); without it the asset is still made, and the write is
retried on the next one-asset run.

## Feedback

```
/poc-studio:feedback <what went well or wrong, what should change>
```

Records one piece of POC-level feedback in Orbit (`orbit_studio_feedback`) for the current POC, for the next skill
analysis. It does not move the POC or post to Slack. (Plain `/feedback` is Claude Code's own bug-report command, so use
the `poc-studio:` prefix.)

## What happens

| # | Stage | Skill | Output (in `<client-slug>/<usecase-slug>/`) |
|---|---|---|---|
| 0 | Setup: connector check (Slack and Google Drive required), installs the tools later stages need, workspace | `poc-orchestrator` | `state.json`, `context-log.md` |
| 1 | Requirement Gathering | `requirement-gathering` | `01-requirement-gathering/Requirement Gathering - <Client> - <Use case>.docx`, `files/` |
| 2 | Scoping (build plan) | `scoping-l1-first` | `02-scoping/scoping-document.docx` |
| 2b | Wireframes (Plan phase, between the BRD and the design system): one low-fidelity frame per page, generic regions as named component slots, map pages per the map reference; the manifest is the design system's component list | `wireframes` | `02b-wireframes/<slug>-wireframes.pdf`, `png/`, `wireframe-manifest.json` |
| 3 | Design System (only the wireframes' components, plus the baseline: sign-in, empty/error/loading states, toast, confirm) | `design-system` | `03-design-system/<client-slug>-<usecase-slug>-design-system.html` |
| 4 | Build in UnifyApps Headless on Orbit: planned in Zen mode with you answering its questions; `platform-master` adds best-practice pointers for the use case and reviews and corrects the plan before you approve it; built and tested by parallel builder agents, fixed, then walked in a browser by the AI PM (Stage 4b) before it is published. An asset UnifyApps Headless cannot build is built by `platform-master` over the API in the browser (you sign in) | `/ua:setup`, `platform-master`, `/ua:plan` (Zen) | the app on https://orbit.uat.unifyapps.com/, `04-build/build-summary.md`, `zen-decisions.md`, `test-report.md` |
| 5 | Collaterals (UnifyApps template) | `poc-collateral-studio` | `05-collaterals/<slug>-collateral/out/`: demo script, demo video, deck (PPT) |

After each stage: the **AI PM** (the `ai-pm` agent, an independent subagent) re-runs the stage's own checks, reviews
the output, and negotiates its findings with the stage (fixed / disputed / deferred; a third round is a ruling, not a
question). Then you **approve or request changes**, starting from its gate summary: verdict, rulings first,
assumptions to check. In Stage 4 it also walks the built app in a browser (Stage 4b) before publish. Your gate
feedback becomes a lesson it checks on every later POC (`python3 <ai-pm>/scripts/lessons.py stats` shows first-try
approvals per stage). Questions raised during a stage — including
UnifyApps Headless's (e.g. which model to use) — go to the reviewer, not to you; a hook enforces this while a stage runs.
Two exceptions in Stage 4 come to you: during the **Zen planning window** (while `.poc-studio/zen-planning` exists)
you answer Zen's clarification questions and approve its plan, and every `CONFIRM_REQUIRED (d_…)` (deletes and some
releases) is yours to answer. The hooks let both through, and the POC owner is nudged in Slack while they wait.
Research answers are saved in `research/`, reviewer verdicts in `reviews/`.

## Contents

```
.claude-plugin/plugin.json, marketplace.json
commands/start.md                  /poc-studio:start
commands/feedback.md               /poc-studio:feedback
commands/requirements.md, brd.md, wireframes.md, design.md, app.md, collaterals.md
                                   /poc-studio:<asset> — make one asset on its own
agents/ai-pm.md                    the AI PM, run as an independent subagent
hooks/                             route questions to the reviewer while a stage runs
scripts/release.sh                 bump the version everywhere, commit, push
skills/poc-orchestrator/           the pipeline
skills/requirement-gathering/
skills/research/                   (+ references/calling-research.md, source-guide.md)
skills/orbit-writeback/            Orbit · POC Studio write-back at each gate (+ orbit-spec.md)
skills/scoping-l1-first/
skills/wireframes/                 low-fidelity wireframes from the BRD: render.py (PNG + PDF + manifest, no browser),
                                   coverage.py (against the BRD), references/: spec format, example, map component
skills/design-system/              v10 (component kit + composition contract, max 5 screens; UnifyApps stand-in logo)
skills/asset-run/                  one asset end to end: prerequisites, stage, AI PM, one-off Orbit row, approval
skills/platform-master/            UnifyApps platform expert for Stage 4: pointers, Zen plan review, browser fallback
                                   (+ references/: use-case pointers, plan-review checklist, API, connectors, graph, governance)
skills/ai-pm/                      the AI PM: reviews every stage, re-runs its checks, Stage 4b build walk, lessons
                                   (+ references/: stage lenses, slop catalogue; scripts/: build walk, scope metrics,
                                    render check, lessons, Orbit sign-in)
lessons/lessons.md                 the AI PM's seed lessons (copied once per machine to ~/.local/poc-studio/lessons)
skills/poc-collateral-studio/      (+ assets/UnifyApps_template.pptx)
assets/unifyapps-logo.png          fallback logo when a client logo cannot be found
```
