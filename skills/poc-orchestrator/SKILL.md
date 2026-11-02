---
name: poc-orchestrator
description: Runs the UnifyApps POC Studio pipeline end to end for one client use case — Requirement Gathering → Scoping → Wireframes → Design System → UnifyApps Headless build → Collaterals — with the AI PM checking every stage and answering every clarification question, an approval gate after each stage, and every file saved in the local client folder. Use when someone runs /poc-studio:start, says "start a POC for a client", or asks to resume a POC Studio run.
---

# POC Studio orchestrator

You run one client's POC from requirement gathering to collaterals. You do not do the stages' work
yourself: each stage has its own skill, and you call it, check it with the reviewer, put it to the
person for approval, and hand the approved files to the next stage.

```
Start → 0 Setup → 1 Requirement Gathering → 2 Scoping → 2b Wireframes → 3 Design System → 4 Build → 5 Collaterals → Done
                         │                        │              │                 │             │              │
                     AI PM + gate           AI PM + gate    AI PM + gate      AI PM + gate   Zen plan       AI PM + gate
                                                                            (platform-master review,
                                                                             you approve) → parallel
                                                                            build + test → AI PM walk
                                                                            (4b) → verify gate
                     (research skill available to every stage; the AI PM — the `ai-pm` skill — reviews every
                      stage, answers every clarification question, and learns from every gate)
```

**Input — three values, all required:** the client name, the use case name and the **POC ID**, from
`/poc-studio:start <client> | <use case> | <POC ID>` (e.g. `/poc-studio:start Acme | Invoice matching | POC-acme-20261018`).
If a separator is missing, read the arguments sensibly; if any value is missing, ask once for the missing ones.
Everything else — website, personas, scope — comes from the documents the stages produce.

**The POC ID is mandatory: nothing starts without it.** Do not run Setup, check connectors, create folders or call any
stage until the person has given a POC ID. It looks like `POC-<client>-<YYYYMMDD>` (e.g. `POC-acme-20261018`): it
starts with `POC-` and ends with an 8-digit date. If what was given does not match that shape, show it back and ask
the person to confirm or correct it before starting. Use the POC ID exactly as given (same case) everywhere.

**The POC ID must exist in Orbit, and Orbit is kept in step with the run.** The `orbit-writeback` skill (load it
with the Skill tool, `poc-studio:orbit-writeback`) owns everything written to Orbit · POC Studio. The start command runs
its Setup (UnifyApps Headless's tenant tools, POC ID check against `orbit_studio_poc`, the POC owner's name and email) before this skill;
if that has not happened in this session, run it first — not found → stop and ask the person to check the POC ID.
Then call it at every write-back moment listed under "Orbit write-back at each gate" below.

**The use case is the focus of the whole run.** A client often has several use cases in flight, and its Slack
channels, email threads and Drive folders mix them. Every stage works on **this** use case only:
- Requirement Gathering searches with the client name **and** the use-case terms, keeps material about this use case,
  and lists material about the client's other use cases as "other use case — not used" instead of mixing it in.
- Scoping, Wireframes, Design System, UnifyApps Headless and Collaterals receive the use case name with every call, and the reviewer checks
  that each output stays on it.
- Each use case gets its own workspace, so two POCs for the same client never overwrite each other.

## The skills you call

Call each with the Skill tool. Use the plugin-qualified name the session lists (e.g. `poc-studio:scoping-l1-first`);
if a same-named skill exists from elsewhere, prefer the `poc-studio:` one.

| Stage | Skill |
|---|---|
| 1 Requirement Gathering | `requirement-gathering` |
| 2 Scoping | `scoping-l1-first` |
| 2b Wireframes | `wireframes` |
| 3 Design System | `design-system` |
| 4 Build | `/ua:setup`, then `/ua:plan` in Zen (separate UnifyApps Headless plugin, `ua`) |
| 4 Build, platform knowledge | `platform-master` (best-practice pointers, Zen plan review, browser fallback) |
| 5 Collaterals | `poc-collateral-studio` |
| Any stage, outside facts | `research` |
| Every gate, Orbit write-back | `orbit-writeback` |
| Every stage, review + questions (the AI PM) | `ai-pm`, run by the `ai-pm` agent |
| Every stage, tokens / models / time | `stage-metrics` (`metrics.py mark` at every status change, `report` after each approval) |

**All research goes through the `research` skill.** When a stage (or you) needs outside facts, the stage's own
instructions already say to call `research`; make sure it does. Only if `research` is unavailable may a stage
fall back to its own web search, and it records that it did. Save each research answer to
`<workspace>/research/<stage>-<short-topic>.md` so later stages and the reviewer can reuse it.

## The workspace (everything lives in the local folder)

All files go inside the folder Claude Code is running in, under one folder per client, so every later step —
and any later session — can read them:

```
<cwd>/<client-slug>/<usecase-slug>/     ← <workspace>  (one folder per client, one sub-folder per use case)
  state.json                            stage status, approvals, paths (resume from here)
  context-log.md                        running record: asks, decisions, answers, approvals, feedback
  01-requirement-gathering/
    Requirement Gathering - <Client> - <Use case>.docx
    files/                              the client's own files, as pulled from Slack/Drive/Gmail
  02-scoping/
    scoping-document.docx               the build plan (Part A proposal, Part B build spec)
    _working/                           scoping's working notes, research, evidence log
  02b-wireframes/
    <slug>.wireframe.json               the layout spec (the wireframes skill writes it; render.py draws it)
    png/<page-id>.png                   one low-fidelity frame per page
    <slug>-wireframes.pdf               all frames in nav order (what the person approves; what goes to Orbit)
    wireframe-manifest.json             the closed component list the design system designs and the build uses
  03-design-system/
    <slug>-design-system.html           the design system HTML UnifyApps Headless reads (one self-contained file)
  04-build/
    build-summary.md                    UnifyApps Headless's result: app name, preview link, published app URL, what was built
    zen-decisions.md                    Zen's planning questions and the person's answers
    test-report.md                      one row per page, automation, agent and storyline step
    platform-pointers.md                platform-master: use-case type, style and the pointers given to the build
    platform-review.md                  platform-master: its review rounds of Zen's plan and the adjustments
    fallback-<n>.md                     platform-master: one per asset built by the browser fallback
  05-collaterals/
    <slug>-collateral/out/              the 3 collaterals: demo script PDF, demo video (+ .srt), deck .pptx
  research/                             every research answer, by stage
  reviews/                              reviewer verdicts (*.yaml) and log.md
```

`<client-slug>` and `<usecase-slug>` are the names in lower case with hyphens (e.g. `acme-beverages` /
`shelf-compliance`); `<slug>` is `<client-slug>-<usecase-slug>` (e.g. `acme-beverages-shelf-compliance`). The
**POC ID** is the `work_id` in every reviewer request, and appears in `state.json`, the first line of
`context-log.md`, the title block of the Requirement Gathering and scoping documents, `04-build/build-summary.md`,
and the collateral brief (`brief.json` → `"poc_id"`, internal only). Create the tree at setup.

### state.json

```json
{ "poc_id": "POC-acme-20261018",
  "orbit": { "poc_id": "POC-acme-20261018", "poc_record_id": "<record id>", "owner": { "name": "…", "email": "…" },
             "documents": {}, "open_iterations": [], "failed_writes": [] },
  "client": "Acme Beverages", "use_case": "Shelf Compliance",
  "slug": "acme-beverages-shelf-compliance",
  "workspace": "<abs path>",
  "connectors": { "slack": true, "gmail": false, "drive": true, "calendar": true },
  "video_route": { "ok": true, "route": "shared_drive", "root": "<local shared drive folder>", "account": "…",
                   "drive_id": "0AOY3pnWOezbhUk9PVA", "company_share": true, "folder_id": "0AOY3pnWOezbhUk9PVA" },
  "stages": {
    "requirement-gathering": { "status": "approved", "output": "01-requirement-gathering/Requirement Gathering - Acme Beverages - Shelf Compliance.docx", "review_rounds": 1 },
    "scoping":       { "status": "in_review" },
    "wireframes":    { "status": "pending" },
    "design-system": { "status": "pending" },
    "build":         { "status": "pending" },
    "collaterals":   { "status": "pending" } },
  "app": { "name": null, "preview_url": null, "published_url": null } }
```

Status values: `pending` → `running` → `in_review` → `awaiting_approval` → `approved` (or back to `running` on
requested changes). Update it at every transition, and at the same moment record it for the stage metrics:
`python3 "$M/metrics.py" mark <workspace> <stage> <status>` (`changes` when the person requests changes, `skipped`
for a skipped stage; the `stage-metrics` skill has the table). A failed mark is logged and never stops the stage.

### context-log.md

Append a dated line at every event: what the stage decided or assumed, every question and the answer it got (and
who answered: reviewer or person), every reviewer verdict, every gate result, and the person's feedback verbatim.
This file is the reviewer's memory of the use case; keep it factual and short.

## Resuming

If `<cwd>/<client-slug>/<usecase-slug>/state.json` exists (and has the same POC ID), read it and `context-log.md`, tell the person in one line where the
run stands, and continue from the first stage that is not `approved` (or `skipped`). Never redo an approved stage unless the
person asks. A run started before Wireframes existed has no `wireframes` entry: if its design system is already past
`pending`, add `"wireframes": { "status": "skipped" }` and carry on (the design system then reads the scoping document
alone, as before); otherwise add it as `pending`, and Wireframes runs next after Scoping. **First run the orbit-writeback skill's Reconcile check**, so any approval or document version that never
reached Orbit is written before the run goes on.

## Questions never go straight to the person

The stage skills are built not to ask questions. If any stage — or UnifyApps Headless — still needs an answer:

1. Do not call AskUserQuestion and do not end your turn with a question. Send the question to the reviewer in
   **resolve** mode (see "Calling the reviewer").
2. Apply its answer, log it in `context-log.md`, and carry on.
3. Only an `ASK_HUMAN` disposition reaches the person, and then only as one question with the reviewer's
   recommended option first.

The plugin enforces this with two hooks: while the file `$CLAUDE_PROJECT_DIR/.poc-studio/autopilot` exists,
AskUserQuestion is blocked and redirected to the reviewer, and ending the turn is blocked once with a reminder (so a
plain-text question, e.g. from UnifyApps Headless, is routed too). Create that file when a stage starts running; delete it right before
you put an approval gate or an `ASK_HUMAN` question to the person; recreate it when the stage work resumes.
Delete it when the run finishes or stops.

Always use the absolute path (stages `cd` into subfolders, and the shell keeps that directory):

```bash
F="${CLAUDE_PROJECT_DIR:-<cwd at setup>}/.poc-studio/autopilot"
mkdir -p "$(dirname "$F")" && echo "<workspace>" > "$F"     # stage running
rm -f "$F"                                                  # gate / ASK_HUMAN / sign-in / done
```

Record the absolute flag path in `state.json` (`"autopilot_flag"`) at setup and use it every time.

Sign-ins are the exception: the person always signs in themselves (Orbit, Slack, etc.); never type a password.

**Two more exceptions, both in Stage 4 (and in any later fix to the app):**

- **Zen planning window.** While `/ua:plan` plans the build in Zen mode, the autopilot file is removed and the Zen
  planning flag `$CLAUDE_PROJECT_DIR/.poc-studio/zen-planning` exists (its absolute path in `state.json` →
  `"zen_planning_flag"`). During that window Zen's clarification questions and its plan approval go to the person
  directly, never to the reviewer; the hooks let them through. Every question and answer is logged as a human
  decision in `context-log.md` and in `04-build/zen-decisions.md`. On the person's yes, delete the Zen planning flag
  and recreate the autopilot file (Stage 4 has the steps).
- **`CONFIRM_REQUIRED`.** When a UnifyApps Headless tool reply contains `CONFIRM_REQUIRED (d_…)` (deletes and some
  releases), only the person's own AskUserQuestion answer counts: remove the autopilot file, ask the person with
  AskUserQuestion, with the `(d_…)` id in the question text (one question per id), pass their answer back, then
  recreate the autopilot file. The reviewer never answers it, and nobody answers it for the person.

## Calling the reviewer

The reviewer must not be the session that wrote the work, so run it as a subagent: the Agent tool with
`subagent_type` `poc-studio:ai-pm` (or the name the session lists for the `ai-pm` agent). If that
agent type is unavailable, use a general-purpose subagent and tell it to load the `ai-pm` skill first.

Write the request to `<workspace>/reviews/<stage>-<mode>-<n>.request.yaml` and pass its path in the prompt:

```yaml
request_id: <slug>-<stage>-<n>
workspace: <abs workspace path>
work_id: <POC ID>
mode: review | resolve
stage: requirement-gathering | research | scoping | wireframes | design-system | build | collaterals
round: 1 | 2 | 3
owner: the person running POC Studio
owner_profile: <state.json owner_profile>                   # v1.0: whose taste profile the AI PM applies
audience: { who: <client audience from the context log, or "client stakeholders" before Stage 1 is approved>, stakes: low }
artifacts: [ <abs paths of the stage's outputs> ]          # review
upstream: { path: <approved upstream>, acceptance_criteria: [ ... ] }   # review; scoping 4.1 from stage 3 on
question: { text: <the question, verbatim>, options: [ ... ] }       # resolve
prior_verdict: <path>                                        # round 2+
```

The reviewer returns a verdict (and writes it to `<workspace>/reviews/`). Then:

| Verdict / disposition | What you do |
|---|---|
| `PASS` | Go to the approval gate. |
| `REVISE` | Re-run the stage skill on its own output with the fix lines: **fix only what is listed, leave everything else as it is** (for the design system: byte-for-byte outside the named sections and specimens). The stage must also answer every finding in `<workspace>/reviews/<stage>-response-<n>.yaml` as `fixed`, `disputed` (with the evidence ID or stated ask behind it) or `deferred` (non-blocking only), as the ai-pm skill's "Negotiation" section defines. Then review again with `prior_verdict`. **At most 2 REVISE rounds**; the third review (v1.0) rules on every finding still open, and you go to the gate with its rulings, whatever the verdict. |
| `BLOCK` | Fix the blocking findings the same way (with a response file), then review again. If it still blocks after the third review, go to the gate and show the blocking findings, so the person can override (quote the finding id and a reason; log it). |
| `ASK_HUMAN` | Put the one question to the person (autopilot file removed), log the answer as a human decision, continue. |
| `REQUEST_RESEARCH` / `research_request` | Call the `research` skill with it, save the answer, give it back to the reviewer or the stage. |
| `DECIDE` (resolve) | Apply the answer, log it, continue. |
| `SEND_BACK` (resolve) | The question was really a defect in the work: fix it in the stage, continue. |
| `INVALID_REQUEST` | Fix the request field it names and call again. |

## The approval gate (after every stage)

Remove the autopilot file, then:
1. Tell the person in a few lines: what the stage produced (with the saved paths), then the **AI PM gate summary**,
   printed by `python3 "$R/lessons.py" gate <workspace> <stage>`: verdict and score, rounds, findings fixed,
   **rulings first** (the decisions the AI PM made on disputes), assumptions marked `check_this`, anything still open,
   minor findings batched for later, and the author's own weakest part. The person checks the AI PM's decisions;
   they should not have to re-review the artifact from scratch.
2. Ask with AskUserQuestion: **Approve and continue to <next stage>** / **Request changes** (they can type the
   changes in "Other").
3. **Approve** → mark the stage `approved` in `state.json`, log it, run `python3 "$R/lessons.py" record <workspace>
   <stage> approved`, run the Orbit approval write (M2 / M2a / M2w) and **confirm it landed** (orbit-writeback: "Confirm
   every approval"). Then mark it (`metrics.py mark <workspace> <stage> approved`) and print the **stage metrics**:
   `python3 "$M/metrics.py" report <workspace> --stage <stage>`. Show the person the stage's row and the Overall row
   (models, tokens, work time, gate wait) and log the stage row in `context-log.md`; after the last stage, show the
   whole table as the run's overall information. Only then move on to the next stage.
   **Changes** → log the feedback verbatim (it is now a human decision for every later review), and also
   `python3 "$R/lessons.py" capture <workspace> <stage> "<their words, verbatim>"` and `… record <workspace> <stage>
   changes`, so the AI PM turns it into a lesson for every later POC. If the feedback names something the AI PM's
   last verdict passed, also `… miss <workspace> <stage> "<what>"`. Then re-run the stage skill to apply it, review
   again (round counter restarts for the new feedback), and gate again.

Never advance without an explicit approval.

## Orbit write-back at each gate

Every gate is mirrored to Orbit by the `orbit-writeback` skill (its table "The plugin's gates → Orbit moments" is the
reference). Do the write **before** putting the gate to the person (posting) and **right after** their answer
(decision) — **except G4**, which is written only after the collaterals are approved — so Orbit and the Slack thread always show the same state as the chat:

| In the run | Orbit moment (orbit-writeback) |
|---|---|
| Stage done + reviewed, before its gate | **M1** — G1 (RG + every discovered client file) · G2a (scoping doc) · G2w (wireframes PDF) · G2b (design system) · G3 (published app) |
| Person approves | **M2** — G1 · G2a (scoping: BRD approved only) · G2w (wireframes approved only) · G2 (design system: G2 approved) · G3 |
| Person asks for changes (their text, verbatim) | **M3** — Iteration row + activities; more text about the same change is added to that iteration |
| The reworked document is ready, before re-gating | **M5** — new version, old one superseded, iteration closed |
| Collaterals approved | **M1 · G4** — upload script PDF, deck, video; demo_ready |
| UnifyApps Headless starts (`/ua:setup`) | **M4** — stage `5_build` (if not already) |
| Person approves the Zen plan (Stage 4) | **M4a** — Activity "Zen plan approved" with the preview path and task count; stage stays `5_build` |
| platform-master builds an asset by the browser fallback (Stage 4) | **M4b** — Activity "Asset built by fallback" with its type, name and id; stage stays `5_build` |
| Run blocked (sign-in, tools, missing input) / stopped / resumed | **M6** |

`slack_notification: true` is sent only by M1 and M5 (when files are written or a new version is posted). If a write
fails three times, tell the person in one line and carry on; the run never stops because Orbit is unreachable,
except at the start (the POC ID must be verified).

---

## 0 · Setup

1. Get the client name, the use case name and the POC ID (all three required; stop and ask if the POC ID is missing).
   Make the slugs and the workspace tree. If it exists, resume (above) — but if its `state.json` has a **different**
   POC ID, stop and ask the person whether this is the same POC (resume) or a new one (then use a new folder
   `<client-slug>/<usecase-slug>-<POC ID>/`).
   A `state.json` that holds only one-off runs (a `standalone` key and no `poc_id`) is not a pipeline run: start the
   run in it and keep its `standalone` key as it is. Remove a leftover `.poc-studio/one-off` flag (from an interrupted
   one-off run): while it exists the owner is not nudged in Slack.
   If the client folder already holds **other** use cases, mention them in one line and keep them untouched.
2. **Connector check.** Look for each connector's tools with a tool search (`slack`, `gmail`, `drive`, `calendar`).
   - **Slack and Google Drive are required.** If either has no tools in the session, stop and ask the person to
     connect it (in Claude Code: `/mcp`, or connect it as a claude.ai connector), then check again. Do not start
     Stage 1 without both. (Drive is needed for discovery and to host the demo video, which always goes to Drive.)
   - Gmail and Google Calendar are optional: list which are connected and carry on; the Requirement Gathering
     document records the missing ones as "Not connected".
   - **Video route check.** Run the `orbit-writeback` skill's **Video route check** now: Google Drive for desktop is
     installed and running, the company shared drive `POC Studio Video Library` is on this computer, a test file
     written into it is read back through the Drive connector (same Google account, write access, sync working), and
     the drive is open to everyone at UnifyApps (`allemployees@unifyapps.com`). If the shared drive route fails, the
     check falls back to the person's own `POC Studio` folder (the old route). Say in one line which route the video
     will take; if neither works, flag that the demo video will not ship to Drive automatically, why, and the fix;
     re-check when the person says it is fixed. It never blocks the run.
3. Write `state.json` and the first lines of `context-log.md` (client, **use case**, date, connectors), then these **standing
   human decisions** (the owner set them for every run; the reviewer applies them):
   - Questions during stages are answered by the reviewer from context and assumptions, not the person (except, in
     Stage 4, Zen's planning questions and plan approval and every `CONFIRM_REQUIRED`, which are the person's).
   - Wireframes: the stage runs unattended; low fidelity (greys, real copy, slots for generic components); a map
     page follows the wireframes skill's map-component reference; the approved manifest is the design system's
     component list.
   - Design system: the stage runs unattended (the person is treated as absent for the skill's stops);
     brand-colour conflicts are settled by the design-system skill's own brand source order, without
     asking; if no client logo file exists, the logo kit uses the UnifyApps logo (labelled stand-in); the output is
     one local HTML file, uploaded to Orbit as a public link.
   - Build: UnifyApps Headless in Zen mode on Orbit UAT; the person answers Zen's planning questions and approves its
     plan, which platform-master has already reviewed and corrected; builder and test agents run in parallel; an asset
     UnifyApps Headless cannot build is built by platform-master's browser fallback (the person signs in); deploying/testing the POC app there is pre-approved; model IDs:
     the builder's recommendation, else UnifyApps Headless chooses, else any available model; every
     `CONFIRM_REQUIRED` is the person's; the AI PM reviews the build at Stage 4b, after UnifyApps Headless's own
     parallel testing and before publish; every fix to the app goes through UnifyApps Headless (a platform asset it
     cannot build goes to platform-master's browser fallback).
   - Collaterals: bundled UnifyApps template; no Doc deliverable; the person signs in to Orbit.
   - **POC data policy (owner decision):** POC Studio builds proofs of concept with dummy data. The app's seed data,
     the documents and the collaterals use made-up values, never real customer records, so public Orbit links are
     approved for every document, including the client files found during discovery. Do not warn about or ask again
     about public uploads.
   - The person's own Slack, Gmail, Drive and Calendar accounts are read-only: nothing is posted or sent from them.
     The exceptions are owner-approved: Orbit (the `orbit-writeback` uploads and its `slack_notification`, which makes
     Orbit post the gate to the POC's Slack thread), and the demo video plus the small sync-check file copied through
     Drive for desktop into the company shared drive `POC Studio Video Library` (or, on the fallback route, the
     person's `POC Studio` Drive folder).
4. **Tools, now, in the background** (so the collateral stage is never blocked hours later, and nobody waits).
   - **Mac:** load the `poc-collateral-setup` skill (Skill tool: `poc-studio:poc-collateral-setup`) and follow it:
     if its doctor already passes, say so in one line; otherwise start its `setup.sh` **in the background** (about
     1 GB the first time, into the person's own folders, no admin, no Homebrew, no password) and go straight on to
     Stage 1. When it finishes, log the result; if a step still fails after one re-run, say in one line which tool
     is missing and what it blocks. Never ask the person to install Homebrew or type their Mac password.
   - **Linux:** check `ffmpeg`, `pdftotext`, `soffice`, `pandoc`, `node`, `python3` (3.10+); if any are missing give
     the person one line to paste (`sudo apt-get install -y ffmpeg poppler-utils pandoc nodejs libreoffice`) and
     carry on; `pip3 install python-docx python-pptx openpyxl` yourself.
   - From then on, on a Mac, every Bash command that runs `python3`, `node`, `ffmpeg`, `soffice` or `pandoc` starts
     with `source ~/.local/poc-collateral/env.sh && ` once that file exists (each shell starts fresh).
   Log what was installed in `context-log.md`.
5. **AI PM (v1.0).** Let `R` be the ai-pm skill's `scripts/` folder
   (`find ~/.claude/plugins -path '*ai-pm/scripts/lessons.py' -exec dirname {} \;`), and `W` the wireframes skill's
   (`find ~/.claude/plugins -path '*wireframes/scripts/render.py' -exec dirname {} \; | head -1`); give both paths to
   the AI PM in every request (`scripts: {ai_pm: <R>, wireframes: <W>}`).
   - Let `M` be the stage-metrics skill's `scripts/` folder
     (`M=$(dirname "$(find ~/.claude/plugins -path '*stage-metrics/scripts/metrics.py' | head -1)")`); record it in
     `state.json` → `"scripts"."metrics"`. Every stage status change from here on is also marked with it (above).
   - `python3 "$R/lessons.py" init` (seeds the lesson bank once per machine; never overwrites) and
     `pip install pyyaml` into the shared venv if `python3 -c "import yaml"` fails.
   - Set `state.json` → `"owner_profile"`: the POC owner's email in lower case, from Orbit setup (`orbit.owner.email`).
     Every reviewer request carries it as `owner_profile`. A profile is created in the lesson home the first time the
     AI PM files a personal preference for that owner; none is shipped with the plugin.
   - **Orbit sign-in, once, now** (not at Stage 5): `node "$R/orbit_signin.mjs" --check`; if it is not valid, remove the
     autopilot file, run `node "$R/orbit_signin.mjs"` and ask the person to sign in to Orbit in the window that opens.
     The session (`~/.local/poc-studio/auth/orbit.json`) serves the Stage 4b build walk and the Stage 5 recording,
     so the rest of the run needs no sign-in unless it expires.
6. Tell the person in one or two lines what will happen, then start Stage 1.

## 1 · Requirement Gathering

- Create the autopilot file. Call `requirement-gathering` with the client name, **the use case name** and the stage folder
  `<workspace>/01-requirement-gathering/` (client files into `files/`, the document into the folder).
- The skill's own last step ("ask whether to proceed") is replaced by your reviewer + gate.
- Review: `stage: requirement-gathering`, artifacts = the .docx (and `files/` listing).
- **Orbit:** M1 · G1 before the gate (RG + every discovered client file); M2 on approve; M3 on changes; M5 before
  re-gating.
- Gate. The document's verdict (Ready / Ready with assumptions / Not ready) and its open questions are shown at
  the gate; proceeding on "Not ready" is the person's call.
- Log the client name, website, use case (as the document confirmed or refined it) and stated asks from the
  approved document in `context-log.md`.

## 2 · Scoping

- Create the autopilot file. Call `scoping-l1-first` with:
  - the use case name (the scope is this use case only; material about other use cases is out of the ask);
  - input 1: the approved `Requirement Gathering - <Client> - <Use case>.docx`;
  - input 2: everything in `01-requirement-gathering/files/`;
  - output path: `<workspace>/02-scoping/scoping-document.docx` (`_working/` beside it);
  - research through `research` (its section 4); it keeps its own `_working/research/`, and you also copy each
    answer to `<workspace>/research/scoping-<topic>.md`.
- It runs without asking the user; anything it cannot settle goes to the reviewer (resolve).
- Review: `stage: scoping`, upstream = the approved Requirement Gathering document. The reviewer reviews Part A
  as a plan and Part B as a build spec (detail in Part B is expected).
- **Orbit:** M1a · G2 (the scoping document, with notification) before the gate; M2a on approve (BRD approved only);
  M3 on changes; M5 before re-gating.
- Gate. Show the counts (L1 / L2 features, pages, objects, agents, workflows) and the top assumptions.

## 2b · Wireframes

Part of the Plan phase (G2), between the BRD and the design system: the BRD says what is built, the wireframes fix what
is on each page and where, and the design system then designs only those components.

- Create the autopilot file. Call `wireframes` (Skill tool: `poc-studio:wireframes`) with the client name, the use
  case, the approved `02-scoping/scoping-document.docx` and the output folder `<workspace>/02b-wireframes/`. It runs
  unattended: anything it cannot settle goes to the reviewer (resolve).
- Review: `stage: wireframes`, artifacts = the spec `<slug>.wireframe.json`, the PDF, the `png/` folder and
  `wireframe-manifest.json`; upstream = the approved scoping document.
- **Orbit:** M1w · G2 (the wireframes PDF, with notification) before the gate; M2w on approve (wireframes approved only);
  M3 on changes; M5 before re-gating.
- Gate. Show the page count (frames / scoping pages), the component count from the manifest, which components are
  drawn in detail and which are slots, and any map page with its mode. Approving here fixes the component list the
  design system designs.

## 3 · Design System

The `design-system` skill (v10) is tested and its output is approved as is. **Call it exactly as it is; do not change,
extend or second-guess its steps** — its own section 0.0 says how the approved wireframes narrow it. It reads
the whole scoping document and the approved wireframe manifest and produces a design system the builder
composes from: full component pages (every state and variant), foundations, pattern blueprints, every journey as a
flow diagram, at most five full screens, and the composition contract with the `#build-plan` and `#style-sets` blocks
for UnifyApps Headless. Do not ask it to draw more screens, one per page or per persona: the five-screen limit is deliberate.
Only these session facts are supplied by you:

- Create the autopilot file. Call `design-system` with:
  - **client name**, **use case** and **website**: from the approved Requirement Gathering / scoping documents (the website is in
    the client brief; if both are silent, the skill derives it);
  - **the BRD** = the approved `02-scoping/scoping-document.docx` (the skill's "BRD" means this document);
    its section 21 brand cues are **evidence with source types**, not a chosen palette; the design-system skill decides the
    palette and theme by its own brand source order (client material → brand guidelines → live product → website).
  - **the wireframes** = the approved `02b-wireframes/wireframe-manifest.json`, the `png/` frames and the PDF (when
    `stages.wireframes` is `skipped`, say there are none: the skill then works from the scoping document alone).
  - **where to save:** `<workspace>/03-design-system/`. The deliverable is the design system **HTML file** (the
    living style guide, with the token block and logo kit in it) saved there as
    `<slug>-design-system.html` (one self-contained file, as the skill requires). UnifyApps Headless reads the HTML from this
    folder. Do not publish it as an artifact; the only place it goes outside the folder is the Orbit write-back
    (uploaded there as a public link — owner-approved, see the POC data policy), which the skill's "do not publish
    or share it as a link" line does not override.
  - **file name and folder:** this name and folder replace the skill's own `<client>-design-system.html` "in the
    outputs folder": the outputs folder is `<workspace>/03-design-system/` and the file is `<slug>-design-system.html`.
  - **run mode:** **unattended** (the skill's own term): nobody answers its stops during the stage. Treat the person
    as absent for the skill's stops even though they are in the chat. A typeface that cannot be identified (Step 2b's
    "Ask") is not a stop either: ship the closest open substitute, mark it `[DERIVED]` in the type note.
- **The skill's two stops are answered without the person** (the reviewer's standing answers):
  - Brand hue ambiguous → the skill decides by its own **brand source order** (Step 1), unattended; never wait and
    never override it with a "standing decision" (the skill forbids that). It records both candidates in the port note.
  - No client logo file anywhere → the skill's stop 2 fallback: the logo kit is built from the UnifyApps logo bundled
    with this plugin (`assets/unifyapps-logo.png`; also `skills/poc-collateral-studio/assets/unifyapps-logo.png`;
    `find ~/.claude/plugins -name unifyapps-logo.png`), labelled as a stand-in; recorded in the port note.
- Review: `stage: design-system`, upstream = the approved scoping document and the approved wireframes (manifest and
  `png/` frames).
- **Orbit:** M1b · G2 (the design system, with notification; stage moves to `4_design_system`) before the gate; M2 ·
  G2 on approve (G2 approved, stage `5_build`); M3 on changes; M5 before re-gating.
- Gate. On approval also record the look for the AI PM's logo-off test: `python3 "$R/lessons.py" look "<Client>"
  "<chrome · surface · shell · concept>"`, read from the file's expression card.

## 4 · Build with UnifyApps Headless

- **Orbit:** M4 (stage `5_build`, if not already) when UnifyApps Headless starts.
- Run Stage 4 in three steps (Skill tool names `ua:setup`, `poc-studio:platform-master` and `ua:plan`, or whatever
  names the session lists for them). UnifyApps Headless updates itself when called; no update step is needed. If the UnifyApps Headless plugin
  (`ua`) is not installed, stop and tell the person to install UnifyApps Headless, then continue.
  1. **`/ua:setup`** — create the autopilot file first; this step runs under it, and the reviewer answers its
     questions. It sets up this folder only: tenant `orbit.uat.unifyapps.com`, the person's sign-in, and a **new**
     solution named `<Client> — <Use case>` (see **Solution** below).
  2. **Platform pointers** — still under the autopilot file, load the `platform-master` skill (Skill tool:
     `poc-studio:platform-master`) and run its job **1 · Pointers**: it classifies the use case from the approved
     scoping document and writes `04-build/platform-pointers.md`. Its pointers go into the build request below.
  3. **`/ua:plan`** with the build request below. The request itself says **Zen**, so `/ua:plan` skips its mode
     question. Planning runs in the **Zen planning window** (next bullet).
- **Zen planning window — the person answers Zen's questions and approves its plan.**
  - Right before `/ua:plan` starts, remove the autopilot file and create the Zen planning flag, next to it, holding
    the workspace path (record its absolute path in `state.json` as `"zen_planning_flag"`):
    ```bash
    Z="${CLAUDE_PROJECT_DIR:-<cwd at setup>}/.poc-studio/zen-planning"
    rm -f "<autopilot_flag>" && echo "<workspace>" > "$Z"   # Zen planning: the person answers
    ```
  - While it exists, Zen's clarification questions (AskUserQuestion, one decision each, with a recommended option,
    any number of rounds, often none) go to the **person directly**. Do not route them to the reviewer. Log every
    question and the person's answer in `<workspace>/context-log.md` as a human decision, and in
    `<workspace>/04-build/zen-decisions.md` (one entry per question: the question, the options, the answer).
  - Zen reads the solution, designs the objects and pages, writes a spec (with `## Assumptions` and "Check this"
    lines on top) and a task graph (one task per entity, each owned by one builder agent), grills plans with 5 or more
    tasks, and writes and opens a preview page. Nothing is written to the tenant before the person's yes.
  - **When Zen passes its check, the plan is reviewed before the person sees it:** run `platform-master` job
    **2 · Plan review**. It checks Zen's spec and task graph against the platform and the pointers, gives its
    adjustments to Zen as Zen's "change something" input, and reviews the revised plan once more (at most two
    rounds; `04-build/platform-review.md`). The person is not asked anything during this review.
  - Then show the person the **final** plan, in this order: the "Check this" assumptions; the preview path; the
    adjustments the platform review applied (one line each, with why); the task list, one line per task (what ·
    entity · agent · waits on); and the steps that will still ask first (every `CONFIRM_REQUIRED`). Then Zen's one
    question (start / change something / keep for later) belongs to the person:
    - **Start** → Orbit **M4a**, Activity "Zen plan approved" with the preview path and task count (orbit-writeback;
      stage stays `5_build`), then the run below.
    - **Change something** → loops back through Zen with the person, still inside the planning window; once Zen
      has revised the plan, the platform review runs on it again (one round) before the person sees it.
    - **Keep for later** → the stage ends as blocked (Orbit **M6**); delete the Zen planning flag; resuming starts
      the window again.
- **On the person's yes:** delete the Zen planning flag, recreate the autopilot file, and let `ua-change` run the plan
  (§ Run a plan). Tell UnifyApps Headless to start **every task that waits on nothing at once**, in parallel, with its
  builder agents (fde-agent, automation-agent, app-agent, agent-builder, code-app-agent; **up to 6 in parallel**), and
  each later task as soon as what it waits on is done. Never build the tasks one by one or by hand. From here on, the
  reviewer answers every question again (except `CONFIRM_REQUIRED`, see "Questions never go straight to the person").
- Give UnifyApps Headless, in the build request (so Zen does not ask about these) and again whenever it asks:
  - **Mode:** Zen (stated in the request).
  - **Platform pointers:** the pointers from `04-build/platform-pointers.md`, with the use-case type and style they
    were chosen for.
  - **Environment:** Orbit — `https://orbit.uat.unifyapps.com/`.
  - **Build plan:** `<workspace>/02-scoping/scoping-document.docx` (Part B is the build spec: objects §12, agents
    §13, workflows/automations §14, pages §11, seed data §19, build order §20).
  - **Use case / app name:** `<Client> — <Use case>` (so the app on Orbit is identifiable per use case).
  - **POC ID:** `<POC ID>` — give it to UnifyApps Headless with the build so the build and the app can be traced to this POC.
  - **Solution:** create a **new** solution named `<Client> — <Use case>` for this POC. Never reuse a cached or
    generically named solution for the tenant (e.g. one called "Nebula" or "UnifyApps Headless"), unless its id is already recorded in this
    workspace's `04-build/build-summary.md` or `state.json`. This is also the answer when UnifyApps Headless offers a cached
    solution. If UnifyApps Headless has already opened a solution, or synced entity manifests whose names belong to another
    client, stop before building: tell the person in one line, log it, and have UnifyApps Headless create the new solution
    instead.
  - **Wireframes:** `<workspace>/02b-wireframes/` — the approved low-fidelity frames (`png/<page-id>.png`, one per
    page) and `wireframe-manifest.json`. Each page's regions, their order and what each region holds follow its frame;
    the components in each region are the manifest's, styled by the design system. A map page (`layout: map` in the
    spec) is built as the map component in `wireframes/references/map-component.md` (platform-master adds it to the
    pointers), with the manifest's data contract. Skip this item when `stages.wireframes` is `skipped`.
  - **Design system:** `<workspace>/03-design-system/<slug>-design-system.html`. Tell UnifyApps Headless to quote and follow the
    **Composition contract** section of that file verbatim, and to look every design decision up instead of choosing:
    the pattern and region fillers for each page from the `#build-plan` block (its `rules` for any page not listed),
    the active style set from the `#style-sets` block, and only specimens marked `data-active="true"` (never one
    labelled "Reference — not in this app"). Also from the contract: the shell, agents in drawers on the platform's
    live agent component, data/table rules, overlays and spacing, colours only from the token block, every state and
    micro-interaction from the component pages, and each role's shell (drawn screen or shell blueprint). The file
    draws at most five screens on purpose; UnifyApps Headless composes every other page from the kit and patterns, matching the
    drawn screens' finish, and never copies one screen's content onto another page.
  - **What to build:** a text-to-code app on UnifyApps, built with UnifyApps Headless's **text-to-code builder** (never the
    no-code config builder; if UnifyApps Headless offers or picks the config builder, answer text-to-code), with the agents,
    automations and objects listed in the
    build plan (L1 scope only).
  - **Questions:** tell UnifyApps Headless that its Zen planning questions and its plan approval go to the person, and
    that every question after the plan is approved will be answered by you (the session), so it should keep going;
    whenever it stops with a question then — through AskUserQuestion or as plain text — answer it via the reviewer
    before doing anything else.
- **After the Zen plan is approved, every question UnifyApps Headless asks is answered by the reviewer** (resolve mode,
  `stage: build`), not the person — except `CONFIRM_REQUIRED`. Standing answers: Orbit environment; for **model IDs** for
  agents and LLM tasks, pick the model UnifyApps Headless recommends — if it recommends none, ask UnifyApps Headless to
  select the most appropriate model for the task — if it cannot, pick any available model. Seed-data file location
  (public or private): UnifyApps Headless's recommended option, otherwise **private**. Sign-ins to Orbit are done by
  the person.
- **Browser fallback — an asset UnifyApps Headless cannot build.** When UnifyApps Headless reports that a task cannot
  be built (it failed after its own retries, or the capability is not available to it) — during the run or during a
  fix — and the task is a platform asset (Data Object and its seed records, Connection, workflow/automation, AI agent
  with its tasks and tools, data source, context graph item, governance control), run `platform-master` job
  **3 · Fallback** for it. The other independent tasks keep running. For its sign-in, remove the autopilot file and ask
  the person to sign in to `https://orbit.uat.unifyapps.com` in the browser the skill opens; recreate the autopilot file
  once they have. A Connection that needs a password, token, API key or OAuth consent is created by the person in the
  same way (credentials are always theirs). platform-master creates the asset over the API from that tab, verifies it, and hands it back to
  UnifyApps Headless as a direct change through `ua-change` (task marked done, dependants wired to the new id). Write
  Orbit **M4b** for each asset built. A page or other app UI that UnifyApps Headless cannot build stays with it and is
  shown at the verify gate.
- **Test everything with UnifyApps Headless, fix, then publish.** When the builder reports the build complete, do **not** publish yet.
  Have UnifyApps Headless test the whole app itself, in the same session, with its own testing tools (`ua:app-verify` and `ua:app-test-author`
  or browser checks, whatever name the session lists for them; there is no reviewer review of the build).
  **Run the independent checks in parallel:** `ua:app-test-author` runs one test-author agent per approved scenario,
  several at once, for the pages (1) and the storyline scenarios (4–4c); in the same message, run the independent
  automations (2) and agents (3) through their builder agents. Only checks that depend on each other's results wait.
  The per-item rules below are unchanged:
  1. **Every page, one by one:** open each page in the app's preview (nav order from scoping §11), check it loads with
     seed data (no empty tables, charts or stage columns), click every button, tab, filter and link on it, and open
     every create/edit form and submit it twice with test data (the second submit must not fail with a duplicate key or any 500 error).
  2. **Every automation / workflow** (scoping §14): run each one by its real trigger (the page button, the object event,
     a schedule run now, a manual trigger with test input) and check its result: the records it should write, the
     status it should change, the notification it should send. Failures, errors and empty results count as failed.
  3. **Every AI agent** (scoping §13): ask each of the spec's example prompts and check the answer matches the expected
     records from the seed data, and that the agent opens in its drawer on the live agent component as the design
     system's composition contract requires (not a card on a page).
     If an agent asks a follow-up question, the drawer shows it and takes the answer (no dead-end or error screen),
     and the conversation continues to its result.
  4. **The demo storyline** (scoping §20.2): walk it end to end once, as the demo will run.
  4a. **Visual acceptance** (scoping §4.1's Visual acceptance block) at 1280×800 on every storyline page: no horizontal
     scroll or clipped column, list rows within the stated height with at least 8 rows visible, no wrapped or broken
     pill, each page opens on its specified tab, every rail badge and KPI count equals its page, no inert control.
     Scores, confidence and other ratios show as percentages (e.g. 87%), never as a raw fraction such as 0.87.
  4b. **Blockers before the click** (scoping §11 prerequisites): each such button is disabled with its reason until
     the prerequisites are met, then enabled and working.
  4c. **Demo data rules** (scoping §19), checked **by script** against the seeded records: one demo "today" and no
     later date; times in business hours in the stated time zone; statuses agree with scores, values and dates;
     filter/badge/KPI counts equal row counts; the default persona's first screen and default tab have data; every AI
     output names its records and count (no "0 AI suggestions"); hero evidence unique; no duplicates or placeholders on
     demo paths; test data kept separate from demo data.
  5. **Fix and re-test:** every failure goes back to UnifyApps Headless (same session) as a **direct change through
     `ua-change`** — no new plan per fix. All independent fixes in one batch go to their builder agents **in
     parallel**; then that page, automation or agent, and anything the fixes touched, is re-tested, again in
     parallel. Repeat until everything passes, **at most 3 fix rounds per failing item**; questions UnifyApps Headless
     asks while fixing go to the reviewer as usual (except `CONFIRM_REQUIRED`).
  6. **Report:** write `<workspace>/04-build/test-report.md`: one row per page, automation, agent and storyline step,
     with pass/fail, what was fixed and how many rounds, and anything still failing after 3 rounds (with the reason).
     Still-failing items are shown to the person at the verify gate; they never block publishing on their own.
- **4b · AI PM build review (v1.0)** — the independent check on UnifyApps Headless's own testing, before publish.
  0. Ask UnifyApps Headless for the app's **preview link** now (the link that opens the app directly with its seed
     data, without first creating a user in the Matrix app; orbit-writeback's **Preview link rule**: work it out from
     the app id if it gives a published or builder link) and save it in `state.json` → `app.preview_url`; the walk
     runs on it.
  1. Write `04-build/routes.json` from scoping §11 in nav order: `[{"name": "<page>", "route": "<route>"}, …]`
     (UnifyApps Headless's route list if the scoping routes changed), and `04-build/glossary.json` from scoping Appendix B as
     `{"<client term>": ["<words that must not appear instead>"]}` where the document names such words.
  2. Check the Orbit session: `node "$R/orbit_signin.mjs" --check`; if expired, remove the autopilot file and have the
     person sign in again (`node "$R/orbit_signin.mjs"`).
  3. Review: `stage: build`, `artifacts: [<preview_url>, 04-build/test-report.md, 04-build/routes.json]`, upstream =
     the approved scoping document plus the design system and the approved wireframe frames (`02b-wireframes/png/`,
     unless `stages.wireframes` is `skipped`). The reviewer runs `build_walk.mjs` and judges storyline,
     fidelity, copy and the reverse trace (ai-pm, stage lenses → build).
  4. **REVISE / BLOCK:** give UnifyApps Headless the findings as numbered fix lines, in the same session, as direct
     changes through `ua-change` with independent fixes in parallel ("Fix exactly these, nothing else: F1 …"); a
     platform asset it cannot build goes to platform-master's browser fallback. UnifyApps Headless fixes, re-runs its
     own test on what it touched, and its answers per finding (`fixed` / `disputed` with reason) go into the response
     file. Then the AI PM walks again (round 2, then the round-3 ruling), as for every stage. At most 3 rounds per finding, as in step 5 above.
  5. The walk's screenshots (`reviews/build-walk-<n>/shots/`) are shown at the verify gate next to the gate summary.
- **Publish:** once testing is done, tell UnifyApps Headless to publish the app on Orbit UAT (if its plan has not already
  published it) and to report **two links**: the published app URL, and the app's **preview link** (the
  link that opens the app directly with its seed data, without first creating a user in the Matrix app). If UnifyApps Headless
  does not give the preview link, ask it for it explicitly.
- Then write `04-build/build-summary.md`: app name, **preview link**, published app URL, the UnifyApps Headless **solution id**
  (`e_…`, needed for Orbit G3), what was built (objects,
  agents, automations, pages) as UnifyApps Headless reported it, the **Zen plan id**, the **preview path** of the plan,
  a link to `zen-decisions.md`, the **task table** (task number · what · entity · agent · waits on · which tasks ran in
  parallel), the **platform** section (use-case type and style from `platform-pointers.md`; the adjustments the plan
  review applied, linking `platform-review.md`; one row per asset built by the browser fallback: task · type · name ·
  id · test result, linking its `fallback-<n>.md`), the test results (counts passed / fixed / still failing, linking
  `test-report.md`), and anything it could not build. Save both in `state.json` →
  `app.preview_url` and `app.published_url`.
- **Orbit:** M1 · G3 (the app, `solution_id`) before the verify gate; M2 · G3 on approve; M3 on changes; M5 (new app
  version, no upload) before re-gating.
- **Gate — verify the published AI solution:** remove the autopilot file, show the test summary (and any item still
  failing, including any asset the browser fallback could not build), the AI PM gate summary for `build` and the
  walk's screenshots, and ask the person to open the published app on Orbit, verify it and approve moving forward to collaterals. Approve → M2 · G3, confirmed in Orbit → Stage 5. Changes → pass them to UnifyApps Headless (same session), let it fix and re-test, post the new app version (M5), gate again. Later fixes to the app (e.g.
  from the collateral stage) also go through UnifyApps Headless, are listed at the next gate, and each new app version is posted
  to Orbit as an approved app document (orbit-writeback, Moment 5 · G3).
  Records the person created while verifying the app (their own runs, uploads, cases) are kept: fixes and re-seeding
  never delete them unless the person asks.

## 5 · Collaterals

- **Only three collaterals:** the demo script (PDF), the demo video (with subtitles) and the PPT deck. No
  walkthrough PDF and no swimlanes document (the swimlane is only a slide inside the deck).
- Create the autopilot file. Call `poc-collateral-studio`. Work in `<workspace>/05-collaterals/` so every output
  lands there. Supply:
  - the app's **preview link** from `04-build/build-summary.md` / `state.json` → `app.preview_url` as every persona's
    `url` (and `public_url`) for discovery, capture and the video recording. **Never use the published
    Matrix app URL for these**: it requires creating a user before the app can be used. If no preview link was
    recorded, ask UnifyApps Headless for it (same session) before recording;
  - the approved scoping document (problem statements, personas, journeys, demo storyline §20.2) and the
    Requirement Gathering document (the "today" pain points) as the build session's truth;
  - the template: the one bundled with the collateral skill (`assets/UnifyApps_template.pptx`) — always this one.
    The deck (problem statement → solution) is built from it.
- **Login:** reuse the Orbit session from Setup: copy `~/.local/poc-studio/auth/orbit.json` to the collateral
  folder's `auth/<persona>.json` for each persona (`orbit_signin.mjs --check` first). Only if it has expired does the
  skill open its sign-in browser (`kit/auth.mjs`) on Orbit; then remove the autopilot file and ask the person to log
  in there, then continue. Never type a password.
- **Tools first:** on a Mac, run the `poc-collateral-setup` doctor before anything else in this stage. If it is not
  all `ok` (Setup's background install failed or never ran), run that skill's install now and wait for it. Then the
  kit's `kit/setup.sh` reuses the shared tools and takes seconds. Every command in the collateral folder starts with
  `source env.sh && `. On Linux, `kit/setup.sh` installs what is missing into the project folder.
- Review: `stage: collaterals`, artifacts = everything in `out/`.
- **Orbit:** nothing before the gate. M3 (phase deliver) on changes; on approval, first the **Reconcile check**
  (G1–G3 must show approved in Orbit), then **M1 · G4** (upload script PDF, deck,
  video; demo_ready) — do it before marking the run done.
- Gate. On approval (after M1 · G4), mark the run done, delete the autopilot file, and give the person the list of files with
  their paths in the client folder.

## Rules for the whole run

- **Everything is saved in the workspace.** No stage output lives only in the chat.
- **Read only** in the person's accounts: nothing is posted, sent, uploaded or deleted in Slack, Gmail, Drive or
  Calendar from them. The only writes outside the local folder are the Orbit write-back (uploads and rows on
  Orbit · POC Studio, and Orbit's own Slack notification) and the demo video (plus the sync-check file) in the
  company shared drive `POC Studio Video Library` (or, on the fallback route, the person's `POC Studio` Drive folder),
  both done by `orbit-writeback`.
- **Never delete** anything you did not create in this run.
- **Tools and skills:** when a stage needs a tool or common skill (e.g. `docx`, `pptx`, `xlsx`, `pdf`, LibreOffice,
  pandoc, ffmpeg), install or load it then and continue. For Anthropic's document skills in Claude Code:
  `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills`; if
  that is not possible, use the Python libraries (`python-docx`, `python-pptx`) directly.
- Keep the person informed with a task list (one item per stage) and a short line when each stage finishes; no
  running commentary.