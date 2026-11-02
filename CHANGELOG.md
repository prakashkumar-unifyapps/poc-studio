# Changelog

## 1.28.0
- **Feedback becomes tickets.** `/poc-studio:feedback <text>` files a ticket on POC Build Loop's Feedback page (https://poc-build-loop-orbit.tensor-uat.unifyapps.com/feedback) with a sequential ID `FB-<n>` (next number read from Orbit; a clash retries with the next number, at most 3 times), `status: open`, `priority: none` unless stated, and one `created` row on the new `orbit_studio_feedback_event` object. The reply gives the ticket ID and its link. Assignee, priority, status, due date and tags are set in the app; the plugin never updates or deletes a ticket.
- **A POC is optional.** Feedback from a one-off asset workspace is filed without a POC (and without asking); otherwise the person can pick **No POC (general)**. The old "feedback can only be filed against a POC" rule is gone.
- **`/poc-studio:feedback status FB-<n>`** (or `fb <n>`, `<n>`) reads a ticket's status, priority, assignee and latest activity from Orbit.
- Feedback no longer feeds the skill analysis (no `analysis_status`): skill proposals come from iterations only. Iterations (Moment 3) are unchanged.
- Skill keys: `asset-run` added, `research` removed.

## 1.27.0
- **One OK to the next asset.** A one-off asset's approval question now also offers **Approve and make <next asset>** (Requirements → BRD → Wireframes → Design system → App → Collaterals). It approves the asset and starts the next one-off at once, with the asset just approved as its input (no re-upload, no "use it?" offer); only what is still missing is asked. The question repeats at each approval, so a person can go asset by asset with one OK each, or stop with Approve.
- The chain stays one-off: each asset is its own Assets row (versioned as before) and never starts, joins or moves a POC run; the full loop is only `/poc-studio:start`.

## 1.26.0
- **New stage 2b · Wireframes** in the Plan phase, between the BRD and the design system (skill `wireframes`). From the approved scoping document it writes a short JSON layout spec; a bundled script (`render.py`, Pillow only, no browser, fonts included) draws one low-fidelity grey frame per page at the persona's width, a PDF of all frames, and `wireframe-manifest.json`: every component with its pages, CMP IDs, variants and states. Generic regions are **slots** that only name their component; the page's defining parts are drawn in detail with the BRD's real copy. `coverage.py` checks every §11 page and §23 CMP ID against the BRD. It has its own approval step inside G2 (Orbit: a `wireframes` document under Plan, M1w/M2w; no new gate).
- **Map component reference** (`wireframes/references/map-component.md`), taken from a working build: one shared map, four modes (rings, dots, arcs, radius), full-bleed with floating panels, whole-step fits padded for panels, screen-space health rings, collision-free labels, hover-to-card. Wireframes draw map pages with it, the design system styles it, platform-master adds a `Map:` pointer and checks Zen's plan against it, and the AI PM checks it at 4b. Scoping now gives location records latitude/longitude and seeds real coordinates.
- **Design system (v10.1):** with approved wireframes, the manifest is the component inventory (variants still capped at three per family), the frames are the layouts in `#build-plan`, the five screens are frames at high fidelity, nothing is proposed; the baseline (sign-in, statuses, empty/error/loading/no-access, toast, confirm, input states, both themes) is always built. Without wireframes it works as before.
- **Build:** the frames and manifest go in the build request; platform-master flags a page whose layout differs from its frame.
- **AI PM:** new `wireframes` lens and lesson stage; the design-system and 4b reviews check against the frames.
- **One asset:** `/poc-studio:wireframes <Client> | <Use case>`; `/poc-studio:design` takes approved wireframes when the folder has them.
- Runs started before 1.26 resume without wireframes when their design system has already started.

## 1.25.1
- Removed `/poc-studio:research-report`. Research is not a stage of the POC journey, so it is no longer made as a one-off asset: the command, its `asset-run` row and section, the one-off Orbit `research` document type and its README rows are gone. The one-asset commands are now `requirements`, `brd`, `design`, `app` and `collaterals`. The `research` skill stays: the stages and the AI PM still call it for outside facts. The full pipeline (`/poc-studio:start`) is unchanged.

## 1.25.0
- **Make one asset**: six new commands — `/poc-studio:requirements`, `research-report`, `brd`, `design`, `app`, `collaterals` — each makes one asset without a POC and without the other stages. Prerequisites are collected in the chat first (arguments → an existing client folder → one question); then the existing stage skill runs unattended, the AI PM reviews it, and the new `asset-run` skill writes it to Orbit as a one-off document (`origin: standalone`, shown in POC Build Loop under Assets), versioned from Orbit on every re-run or change, and asks for approval. Collaterals always ask which to make (demo script, deck, video — any of them). A one-off run never changes a pipeline run's files, state or Orbit rows.
- orbit-writeback: "One-off documents" section and a shared Preview link rule; pipeline Document rows now also send `origin: pipeline`, `client_name` and `use_case`, and app documents save the preview link (never the matrix URL). `/poc-studio:feedback` in a one-off workspace asks for a POC ID or writes nothing.
- `scripts/release.sh` bumps the version in every command file.

## 1.24.0
- The reviewer becomes the **AI PM** (`ai-pm` skill and agent, renamed from `general-reviewer` / `poc-reviewer` everywhere), v1.0: re-runs every stage's own checks instead of trusting them; stage lenses and a slop catalogue; a fixed/disputed/deferred response protocol where the third review is a ruling, not a question; a gate summary with rulings first; a lesson bank across POCs (`lessons.py`, ~/.local/poc-studio/lessons) seeded with 18 lessons, with owner profiles created at runtime (keyed by the owner's email; none shipped); `scope_metrics.py` for scoping. New **Stage 4b**: after UnifyApps Headless's own testing and before publish, the AI PM walks the app from its preview link (`build_walk.mjs`); fixes go back as direct `ua-change` changes in parallel, platform assets through platform-master's fallback. One Orbit sign-in at Setup (`orbit_signin.mjs`) serves the build walk and the video recording. Scoping, design-system and collaterals answer the AI PM's findings. Merged onto the current pipeline (Zen, parallel agents, shared drive, platform-master); no names in skills.

## 1.23.0
- New skill `platform-master`, the UnifyApps platform expert for Stage 4, built from the platform knowledge of the UnifyApps helper (curated: no process, design or conflicting rules). Before `/ua:plan` it classifies the use case and adds best-practice pointers to the build request; in the Zen planning window it reviews and corrects Zen's plan (up to two rounds) before the person sees it, so the person approves an already-corrected plan; when UnifyApps Headless cannot build a platform asset, it builds it over the API from the person's signed-in browser tab on Orbit UAT and hands it back through `ua-change`. Orchestrator, reviewer standing answers, Orbit (M4b) and README updated.

## 1.22.0
- Demo video: saved to the company shared drive `POC Studio Video Library` (open to everyone through `allemployees@unifyapps.com`), in its root as `<POC ID> - <Client> - Demo video v<N>.mp4`, so nobody creates or shares a folder of their own. The Drive connector finds it with `parentId` = the drive id (its plain title search does not return shared-drive files). Video route check and upload updated; the person's own `POC Studio` folder stays as the fallback route, then a manual drop.

## 1.21.0
- Build: Zen plan with the user answering clarification questions and approving the plan; builder and test agents run in parallel; CONFIRM_REQUIRED always goes to the person; hooks let Zen-planning questions through.

## 1.20.0
- Renamed Nebula to UnifyApps Headless: /ua:setup, mcp__plugin_ua_* tools, new plugin cache path; build stage runs ua:setup then ua:plan (Sonic).
- Removed people's names from the skills: the owner column in the orchestrator's skill table, and the General Reviewer's owner (now UnifyApps Solutions).

## 1.19.0
- Requirement Gathering: a short summary under the title (use case, score and verdict, top 3 questions); a use-case type line; the problem stated before any solution; a "What this POC adds" table when earlier work exists; the current process as numbered steps; Visual requirements captured word for word and tagged for the design system; every figure cited to its primary source; a PM's written record of a client call counts as a client source; questions marked Blocking or Nice to have, with region-specific and AI-grounding questions; answered questions move into Section 1 and the score is re-run; internal working notes only in Section 4.
- Scoping: two or three app personas (notification recipients are not personas); L1 checked against the storyline and covering every journey stage; leaner POV sizing (3–6 pages, never more than 8; 8–12 objects; 3–8 workflows; one live copilot agent), reached by merging, with secondary records in drawers or modals; the executive summary opens with the business problem; success criteria measure business outcomes, with honest baselines; differentiators name the products that cover part of the ground; record key generation stated; workflow paths checked for overwrites, edge states and required fields; scoring ownership and weights for rules that do not apply; a live demo core with seed data matching each step (10–15 minutes); real product images, downloaded into the app's storage; Visual requirements from Requirement Gathering carried into the design-system hand-off (§21); Reset demo restores seed records only and never removes records the person made; four new consistency checks; the Pentland sizing lesson.
- Orchestrator (build): a new solution named `<Client> — <Use case>` for every POC, never a cached one; Nebula's text-to-code builder only; forms submitted twice to catch duplicate keys, with test records cleared after testing; agent follow-up questions tested; ratios shown as percentages; records the person creates while verifying are kept.
- Reviewer: standing answers for Nebula's cached-solution and builder questions (new solution, text-to-code), so the reviewer never picks a cached solution because Nebula recommends it.

## 1.18.0
- Design system skill replaced with v10: a component kit with full component pages (anatomy, coded variants, every state, micro-interactions), pattern blueprints, every journey as a flow diagram and at most five full screens; a per-client design concept; all design choices made in the run and handed to Nebula as `#build-plan` and `#style-sets`, with `data-active` tags on every specimen; a design review before a 10-item checklist; lighter research depths; Fujairah render fixes.
- POC Studio edits kept in v10: UnifyApps stand-in logo when no client logo exists; no named reviewers in the hand-over questions; every research request states its search budget.
- Orchestrator: the Nebula hand-off follows the Composition contract, `#build-plan` and active specimens only; the five-screen limit is not to be expanded.
- Reviewer: design system checked against v10's 10-item list; undrawn pages and shells are never a finding.
- Research: a search budget stated by the caller sets the depth.

## 1.17.2
- Questions that wait on you now nudge the POC owner in the POC's Slack thread (not while autopilot routes questions to the reviewer).

## 1.17.0
- New skill `poc-collateral-setup` (from a successful run): installs every collateral tool once per Mac into the user's own folders, no admin and no Homebrew (Python 3.12 venv, ffmpeg, ffprobe/pdftotext/pdftoppm stand-ins, pandoc, LibreOffice, Kokoro voice, Spectral fonts, Playwright Chromium, lucide icons), with a doctor that runs each tool. Setup starts it in the background; Stage 5 runs the doctor first.
- Collateral kit: `kit/setup.sh` reuses the shared install (seconds, no downloads) and writes `env.sh`; every command starts with `source env.sh && `; deck icons drawn with resvg-py (cairosvg fallback); `kit/lint.mjs` works when the path has spaces; `kit/auth.mjs` waits for Google SSO to finish and saves only once the app opens; Orbit login set to `https://orbit.uat.unifyapps.com/login`.

## 1.16.0
- Demo video: copied into the person's Google Drive for desktop folder (`POC Studio/<POC ID> - <Client>/`), found and linked with the Drive connector, shared with the whole company through the `POC Studio` folder's General access. Setup runs a Video route check (Drive app installed and running, same account as the connector via a test file read back, folder shared with the company) and flags why the video would not ship automatically; manual drop stays as the fallback.

## 1.15.0
- Orbit: every approval write is read back and confirmed before the next stage starts; every new app version is posted (also after G3 approval); a Reconcile check on every resume and before G4 writes any missing approval or document version without moving the stage backwards.

## 1.14.0
- Collaterals: slow steps are recorded as they happen and the silent wait is cut out (`kit/trim.py`, after `build.py`): click → short beat → result, voice-over stays in sync, subtitles and scene times shifted; app-caused OVERRUN/SLOW count as fixed once trimmed.

## 1.13.2
- Scoping: brand guidelines found by web research when the client gives none (guidelines → live product → website), recorded as evidence with source type, light/dark balance and chromatic role; never promote a link/accent blue for a black-led brand; never ask about colours or theme in open questions; the design-system skill decides the palette and theme.

## 1.13.1
- /poc-studio:feedback rows carry a `skill` field (the skill or agent the feedback is about, or `general`), and the reply names it.

## 1.13.0
- Requirement Gathering: required Personas and journeys table; Stage-1 UX decisions (primary persona, device per persona, reuse vs rebuild) with source or stated default; checklist re-weighted to 12 items (personas and journeys = 25 points); Slack file retries cut to 2.
- Scoping: primary-persona rule and Primary column; Screen UX fields on every page (kept with the data bindings); home pages by persona type; prerequisites shown before the click (disabled with reason); Visual acceptance block in 4.1 (1280×800); demo storyline order; demo data rules in section 19.
- Build test: visual acceptance, blockers-before-click and the demo data rules (by script) are checked in the built app.

## 1.12.2
- The demo video always goes to Google Drive (any size), shared by link; that link is saved in Orbit. No Orbit upload for the video.

## 1.12.1
- Demo video over 20 MB goes to Google Drive (shared by link) and that link is saved in Orbit; Google Drive is now a required connector at setup, with Slack.

## 1.12.0
- Design system skill replaced with v6 (journeys as flows, signature components, agent drawers, per-client expression, brand source order, build contract), with two edits: UnifyApps stand-in logo when no client logo exists, 'Amogh' removed.
- Orchestration unchanged in flow: the stage still reads the approved scoping document and writes one HTML to `03-design-system/`, uploaded to Orbit as a public link; Nebula is told to follow the HTML's build contract; reviewer checks v6's finished-piece list.

## 1.11.0
- Build stage: Nebula tests every page, automation, AI agent and the demo storyline, fixes what fails (max 3 rounds per item), then publishes; results in `04-build/test-report.md` and the G3 summary.

## 1.10.2
- /feedback records POC-level feedback in Orbit for skill analysis (`/poc-studio:feedback <text>`, row in `orbit_studio_feedback`).
