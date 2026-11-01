---
name: "design-system"
description: "Build a client design system from a scoping document (or BRD), a client name and a website — read the whole document, research the brand and public design references, sample the real brand, harvest the logo into every variant, choose a client-specific expression, skin house Design Language v3.4 onto it preserving luminance, and ship ONE self-contained HTML file that is a true design system: a labelled component kit with variants, a set of distinct layout patterns, signature flows and components drawn in full, and a composition contract that tells the builder how to compose the app's pages itself — not a pre-drawn copy of every screen. Audited in light and dark. Use before any screen is drawn."
---

# Design system for a POC

**Input: a scoping document (or BRD), a client name and a website. Output: a design system the builder
composes an app from.** Everything between is a pipeline you run, not a method you interpret.

**A design system is transformed, then expressed, then composed from.** The **core** is a validated
system moved onto the client's colour without breaking a measurement. The **expression** (shell,
chrome, surface, voice) makes it read as this client's product. The **composition** is the builder's:
this file gives it a kit of components with variants, a set of distinct layout patterns, and the rules
for choosing between them. **The core never varies, the expression always does, and the builder
composes the pages.** This file does not pre-draw every screen; when it did, every app came out the same.

**Run this as Phase 3a — before any screen is drawn, before the first builder prompt.**

> **How this file is layered (read once).** The original pipeline — sample, harvest, transform, audit,
> ship — is unchanged and authoritative. On top of it: **Phase 0** reads the scoping document and
> chooses what the app needs; **research** (next section) confirms the brand; **the expression**
> (Step 2c) finds the client's design concept and makes the system look like this client and no other;
> **the composition model** (REFERENCE) makes every design choice and records it in a build plan, so the
> builder looks answers up instead of choosing; **Step 7** hands all of it over in one file. The version history, and the real runs each change came from, is at the end of the file.
>
> **The output is a design system: deep on components, light on screens.** Every component is
> documented in full (anatomy, variants, every state, micro-interactions, usage, accessibility), the
> foundations show the material properly, every pattern has a blueprint, and every journey is a flow
> diagram. **At most 5 full screens** show the system put together. A sixth screen means a rule is
> being read as "draw every page" — stop and check 0.6.

---

# GETTING OUTSIDE FACTS · call the `research` skill

**Any web search or outside research this skill needs goes through the `research` skill first.** Run
your own searches only when `research` fails (see "Calling `research`" below). `research` searches, rates the sources and returns an answer with sources, dates,
a strength rating and any gaps. It stays inside the question it was sent. This skill decides what to do
with the answer.

**Reading the client's own site comes first, and research confirms it.** Steps 1, 2 and 2b fetch the
swatch, the linked stylesheet, the font files and the logo directly from the client's site. Research
then confirms what was sampled against a second source, and fills in what the site could not give.
Research also covers facts from outside the conversation: the client's business, an industry process,
a regulation, comparable products, design references, and the client's brand guidelines and tone.

## The research plan — mandatory, before Step 1

Research is not optional and not "when needed". Every run writes a research plan at the end of Phase 0
and completes it before Step 3 (the transform). The plan has two parts.

**Part 1 · Questions every run asks**, whatever the BRD says:

| # | Question | Depth |
| --- | --- | --- |
| 1 | What are the client's brand colours? Confirm the hex values on an official source (the live site's CSS, a brand or press page) and a second independent source | Deep |
| 2 | Which typeface does the client use, who licenses it, and which open substitute matches it? | Deep |
| 3 | Where is the client's official logo file published (site, press kit, brand page, Wikimedia Commons)? | Deep |
| 4 | Does the client publish brand guidelines, and what do they say about tone, colour use and logo use? | Quick |
| 5 | What does the client do, for whom, and which words do they use for their own products, customers and processes? (feeds the sample content; the scoping document usually answers most of it) | Quick |
| 6 | **Inspiration.** Which 5 or 6 public products and design references best show this domain and these surface archetypes done well? At least 1 from the client's own industry, 2 best-in-class products for the main archetype (0.2), and 1 for each signature component (0.8). For each: the link, what it does well, and the one idea worth borrowing | Standard |
| 7 | **Journey patterns.** For the signature journeys (0.7), how do the best products handle the same moments: the refused action, the approval, the hand-off, the empty first run, the AI suggestion the user accepts or rejects? Answer from the references found for question 6 where possible | Quick |

**Part 2 · Questions the BRD raises.** Read the build brief and add a question only where the BRD leaves
something the design depends on unsaid or thin. **At most three Part 2 questions, each Quick.** For
example:

- personas or jobs are vague → who does this work in this industry, and what do they read most
- the BRD names countries, regulated data or languages → which privacy, accessibility and language rules
  apply, and how dates, numbers and names are formatted there
- an archetype from 0.2 is in play → 3 to 5 polished references for that archetype and data shape
- the BRD names a third-party product the app mirrors or connects to → how that product presents the
  same data, so the terms and statuses match

**A question is done only when it meets its depth:**

| Depth | Minimum before the question is done |
| --- | --- |
| Quick | 3 searches, the pages behind the answer opened and read |
| Standard | 6 searches, at least one official or primary source |
| Deep | 12 searches, at least one official or primary source, and every key fact confirmed by a second independent source |

**Deep is only for questions 1 to 3** (colours, typeface, logo), because a wrong hue or a redrawn logo
is the most expensive mistake this skill can make. Everything else is Quick or Standard. **Stop a
question as soon as its minimum is met and the answer is clear** — the minimum is a floor to reach,
and also the point to stop.

**Questions 6 and 7 feed the design, not just the record.** Keep it to the 5 or 6 references. Their answers become the **inspiration
board** on the style guide: each reference as a card with its link, what it does well, the idea taken,
and the component or expression choice it informed. Take ideas — layout moves, interaction patterns,
density, how a status or an agent is presented — never colours, logos, artwork or copied markup.
Nothing from a reference adds a colour value, radius or new rule to the core; it informs the
expression (Step 2c), the signature components (0.8) and the flows (0.7). A board of references that
changed nothing in the system is a list, not research.

**Keep a research ledger** and ship it in the port note: one row per question with its depth, the number
of searches run, the pages opened, the sources with dates, the strength of each finding, and the
answer. A row that has not met its minimum is not done. Keep searching (different phrasing, the
client's own subdomains, press releases, investor pages, app-store listings, archived copies, the
browser for pages a fetch cannot read) until it is. Only after the minimum is spent may a fact be
recorded as `[DERIVED]`, and the row then lists what was tried.

## Calling `research`, and what to do with the answer

**Send one decision per question**, with its purpose (internal check, working draft, or something the
client will read), the context (client, industry, country, the build brief so far) and the format you
need. "Research the client" gives `research` nothing to aim at. Depth follows the research plan above:
**state the search budget in every request** (for example "Quick — at least 3 searches, stop once the
answer is clear"). The `research` skill uses the same words Quick, Standard and Deep for larger default
counts, so a request without a stated budget runs longer than this skill needs.
Send related questions together so sources are reused; run unrelated ones in parallel.

**It returns** an answer in two to four sentences, a findings table (finding, source, date, strength),
the gaps, and notes on conflicts. Strength is **Strong** (official or primary, or two reputable sources
agreeing), **Medium** (one reputable secondary source) or **Weak** (marketing, galleries, unverified).

**Using it:**
- Treat it as a draft. Close every gap and Weak finding the build depends on with your own search. If
  nothing turns up once the depth minimum is spent, decide, record it as `[DERIVED]` with what was
  tried, and keep going. A gap is never a stop; the two stops in THE RUN stay the only two.
- Research never replaces sampling. A hex or logo URL it returns is a lead to verify on the live site
  (Steps 1 and 2).
- References inform the expression and the choice of pattern, never the core: no new colour value,
  radius or component comes from a reference.
- Record each question, the strength of each finding used, and every source with its date in the port
  note.

**If `research` fails** (not available, errors, returns only gaps or only Weak findings for something
the build depends on, or falls short of the depth minimum), do the searching yourself with the web
search and fetch tools, to the same standard: open the pages you take facts from, prefer official
sources, confirm client-facing facts with a second source, and log them in the ledger. Never stop the
build because `research` failed.

---

# PHASE 0 · Read the BRD, choose the system

## 0.0 · Approved wireframes (POC Studio) — when given, they set what is built

In POC Studio the Plan phase runs Scoping → **Wireframes** → Design System. When the call includes the approved
wireframes (`wireframe-manifest.json`, the `png/` frames and the PDF), the person has already approved what is on
every page and where. Read all three before 0.1, then:

1. **The manifest is the component inventory.** Write a component page for every component in the manifest and for
   the baseline (2), and no other. On each: the forms the manifest lists under `variants` (the pages need them, so
   they must exist), the states it lists plus the universal state rule, and its `features` (bulk select, a status
   column, a map mode). The style-set alternatives of "Variants and the style set" (rule-1 families only, at most
   three per family counting the manifest's forms) and a signature component's second layout (0.8) are still drawn.
   Nothing else: no `Proposed` views or components, and no view from the reserve the manifest does not name. A component the scoping document names
   but the manifest does not is not built (the wireframes were approved without it); if it is clearly needed, say so
   in the port note for the next wireframe change, and do not add it.
2. **The baseline is always built**, whether or not a frame shows it: the floor in 0.1 (the shell parts the frames
   use, sign-in with forgot and reset password, the four statuses in the domain's words, empty, no-results, loading,
   error and no-access states with wording, a toast with undo, the confirmation modal, every input state, light and
   dark), the agent drawer with its launcher for every agent (0.9), and the kit atoms of "The component inventory" in
   REFERENCE (buttons, inputs, status tags, badges and the rest).
3. **The frames are the layouts.** Each page's pattern, region order and region fillers in `#build-plan` come from its
   frame (same page ID). Where a frame shows a slot, the region filler is that slot's component. A pattern blueprint
   is drawn only for a pattern no frame shows. Never re-decide a layout a frame fixes.
4. **The five full screens are frames at high fidelity:** pick up to five frames (the main personas' first screens,
   the demo storyline's key moments, a map page if there is one) and draw each with its frame's regions in the same
   order, now in the client's brand with real content.
5. **Maps.** A manifest component with a map `data_contract` gets one map component page that follows the wireframes
   skill's `references/map-component.md`: only the modes the manifest lists; ring, dot, label, site card and route or
   radius anatomy with every state; the legend pill; the floating controls; and the tile tint for light and dark as a
   token-driven filter.
6. **Check by script before hand-over:** every manifest `component` has a component page (`data-component` values),
   every frame's page ID (without its letter suffix: `PG-03b` is page `PG-03`) is in `#build-plan`, and no component
   page exists that is neither in the manifest nor in the baseline.

Without wireframes (a run that skipped them, or a design system made without any), 0.1–0.9 work from the scoping
document alone, exactly as written.

**In the automated flow the BRD is a scoping document** — 80 to 130 pages, most of it data model,
workflows, business rules, agent prompts, seed data and sources. Read it as the BRD throughout this
file. Most of it is not visual, and that is exactly why it has to be read whole: the visual facts are
spread through it, and the journeys in it are the richest design input the system gets.

**This runs before THE RUN.** THE RUN (below) skins the system onto the client's brand. Phase 0 decides
*what gets skinned* — which views, which components, at what density — so the build matches the BRD
instead of defaulting to the same glass dashboard every time. If there is no BRD, only a client and a
website, skip to THE RUN and use the use-case dial defaults; Phase 0 is what a real requirement unlocks.

**The discipline is the same as Step 0's:** decide, record the decision, keep going. Phase 0 produces a
short **build brief** that every later step and the hand-over cite. It never asks the user more than the
two stops already allow.

## 0.1 · Parse the BRD into a build brief

**Read the whole BRD, end to end, before deciding anything.** Every section, table, appendix, data
model, automation, agent instruction and prompt, and every stakeholder note. Design facts hide in
unlikely places: a theme line in application settings, a chart tool in an agent's tool list, a status
value in a data model, a route list, an error message in a test case. Do not skim for the screens
alone. Record what you extract, mark anything you inferred `[DERIVED]`, and keep going.

```
DOMAIN          what the app is about (AP invoices, recruitment, churn, logistics…)
PERSONAS        who uses it, and their role (analyst, approver, exec, agent-operator, external user)
JOBS            the handful of things each persona comes to do
SURFACES        which surface archetypes the jobs imply (see 0.2)
SCREENS/ROUTES  every screen, route, overlay and modal the BRD names, including sign-in and recovery
VIEWS           which view-types the data and jobs require (see the View Library in REFERENCE)
DATA SHAPES     records · time series · relationships · stages/process · locations · documents · hierarchy
DATA VOLUMES    how many records, rows, items — decides paging, density and summaries
STATUSES        every status value and state word the BRD or its data model uses, in its own words
EDGE STATES     empty, no-results, loading, error, stale, locked, unset, no-access cases the BRD mentions
AGENT OUTPUTS   every agent and automation, its tools and what it can produce (see 0.3)
INTEGRATIONS    the systems the app reads from or writes to, and their terms
BRAND INPUTS    any colour, logo, typeface, theme, radius, tone or design system the BRD supplies
DEVICES         screen sizes, desktop or phone, light or dark
REGION/LOCALE   LTR/RTL, language, any compliance that touches the UI
CONTRADICTIONS  where the BRD disagrees with itself — each resolved and recorded as a derived decision
UNKNOWNS        what the design needs and the BRD does not say — each becomes a research question
OUT OF SCOPE    what the BRD does NOT ask for — stated explicitly
```

**When the BRD is a scoping document, read these sections for these fields** (section numbers follow
the usual template; find the equivalent if they differ):

| Scoping section | Feeds |
| --- | --- |
| Executive summary, context, pain points (§1–§3) | DOMAIN, the WOW factor, what the demo must prove |
| Scope, asked vs scoped, live vs simulated, decisions (§5) | OUT OF SCOPE, CONTRADICTIONS, what is real and what is staged |
| Research findings and brand cues (§6) | BRAND INPUTS, competitors for research question 6 |
| Personas (§7) | PERSONAS, DEVICES, density and shell per role (0.4) — every persona, not the first three |
| Journeys and workflows (§8) | JOBS and the flows in 0.7 — every journey, every step, every exception |
| Solution overview, global conventions (§9) | SURFACES, the app map, navigation, global elements |
| Feature catalogue and UI pattern coverage (§10, §10.5) | VIEWS; every must-have (L1) feature ID |
| Page specifications (§11) | SCREENS/ROUTES, layout order, key states per page |
| Data model, allowed transitions (§12) | STATUSES in their own words, state machines, UNSET fields |
| Agents (§13) | AGENT OUTPUTS, the agent drawers in 0.9 |
| Workflows, rules and scoring (§14) | refusal messages, gates, thresholds, what turns a status red |
| Roles and permissions (§16) | role shells, read-only states, no-access wording |
| AI trust and governance (§17) | the AI marker states, confidence display, human-in-the-loop moments |
| Non-functional notes, seed data (§18–§19) | DATA VOLUMES, sample content, hero records the specimens use |
| Demo storyline (§20) | which flows and screens carry the demo; the order the style guide follows |
| Hand-off to the design system (§21) | BRAND INPUTS, vibe, custom components, key states, interactions, layouts |
| Component inventory (§23) | signature-component candidates (0.8); every CMP ID gets a specimen (with wireframes: every manifest component; 0.0) |

**Every must-have (L1) feature ID and every CMP ID maps to at least one inventory row (0.6)** (with wireframes, the
manifest is the inventory and its coverage was checked at the wireframe stage: 0.0). Nothing
the document builds now is moved to "future scope" by this skill. Where the document itself marks a
feature future scope, it stays dormant.

**Go beyond the document, inside its fences** (only without wireframes; with them, the approved frames are the
scope and nothing is proposed: 0.0). The scoping document is the floor, not the ceiling.
After the read, ask: what would make each persona's main journey faster, clearer or more convincing
in a demo? Add those as **proposals** — a view, a variant, a state, an interaction — drawn and labelled
`Proposed` on the page, each with the persona and journey it serves. A proposal never contradicts the
out-of-scope list, never adds a live integration, and never replaces what the document specifies.

**Correct the document where it would hurt the app.** Scoping documents are written fast and
sometimes ask for something that breaks a doctrine here — an agent as a full-width card on a page, a
status shown by colour alone, a drag with no keyboard path, a chart that colours a delta by its sign.
Follow the doctrine, draw it correctly, and record the correction in the port note with the line it
replaces. The document's intent wins; its wording does not.

**Where each fact comes from, in order:**

1. **The BRD.** What it states is used as stated. Research never overrides a requirement.
2. **The `research` skill**, for every UNKNOWN and for the seven questions every run asks (see the
   research plan).
3. **Your own web search and fetch**, when `research` fails or falls short, held to the same depth
   minimums and source standards.
4. **A derived decision**, only after 1 to 3 are exhausted, recorded with what was tried.

Brand inputs follow their own order — the brand source order in Step 1 — because a brand can be
current in two places at once (a deck and a website) without either being out of date. Where the BRD's
brand input is **demonstrably retired** (a rebrand dated after it, a logo the client no longer uses),
use the current brand, say so in the port note, and name the BRD line it replaces.

**The out-of-scope line is load-bearing.** It is how the build stays inside the requirement. A BRD for
an approval queue does not get a map, a chart wall or a chat just because the system can produce them.
Scope creep in a POC reads as "they didn't understand what we asked for."

⚠️ **A thin or messy BRD is the normal case, not an error.** Do not stop to interview the user; the two
stops in THE RUN are still the only two stops. Fill the gaps instead:

1. **Every empty field in the build brief becomes a research question** (Part 2 of the research plan),
   at standard depth. For example: no personas → who does this work in this industry and what do they
   read most; no statuses → which states this kind of record moves through in this industry; no
   volumes → typical record counts for a company of this size; no devices → where this kind of user
   works.
2. **Use what comes back to complete the brief**, marked `[DERIVED]` with its source, so the build
   brief has every field filled before Step 1.
3. **Sample content comes from research question 5** (the client's own business and terms), never from
   lorem ipsum or a generic company.
4. **Apply the floor below**, whatever the BRD leaves out.

**The floor — every build carries these, even from a one-paragraph BRD:**

- the app shell: left navigation with the logo, top bar, profile menu
- sign-in, with forgot-password and reset-password
- the main record list with its toolbar, search, filters and paging, and the record's detail view
- one primary form with validation, and every input state
- the four statuses (positive, attention, negative, neutral), named in the domain's own words
- empty, no-results, loading, error and no-access states, each with wording
- a toast with undo, and a confirmation modal for the one irreversible action
- light and dark, both reachable
- every component used, in every state of the universal state rule

The floor is the minimum, not a cap. Add what the brief and research call for; leave dormant what
neither does.

## 0.2 · Map to surfaces

The build brief resolves to one or two **surface archetypes**; each sets the use-case dial row
(REFERENCE) and the layout patterns its pages usually take (REFERENCE, "The composition model"):

- **Dashboard / overview** → P5 metric dashboard · demo-surface row
- **Dense ops console** or **record workspace** → P1 list workspace, P2 split master-detail, P3 focus · dense-internal row
- **Process / workflow** → P4 board, plus flow views · dense-internal row
- **Map / geospatial** → P6 map · demo-surface row
- **Activity / history** → P7 feed · either row
- **Wizard**, **conversational**, **artefact studio**, **portal**, **mobile-first** → the stepper, the
  agent drawer, the studio shell, a lighter shell, a one-column phone shell, inside whichever pattern
  the page's data needs

Everything the brief does not name stays dormant.

## 0.3 · The data-shape → view rule

Read the dominant data shape of each page and reach for the matching view, so a flow is drawn as a
flow and not a table. The pattern-fit table in the composition model turns the same reading into a
page layout.

- **Many records, flat** → table or card list. **One record, deep** → detail / focus view.
- **A value over time** → trend chart or timeline. **Values compared** → comparison chart.
  **Parts of a whole** → part-to-whole chart. **Spread** → distribution chart.
- **Entities and relationships** → graph, tree, ER or dependency view.
- **Steps, branches or stages** → flow diagram, swimlane, board or stepper.
- **Locations** → map. **Durations over time** → Gantt or timeline.
- **An agent's work** → run / trace + approval. **A long text or file** → document, code or preview view.
  **Two things side by side** → compare / diff.

**Read what the agents and automations can output, not only the screens.** Each output type is a view
the system must style, even when no screen in the BRD shows it: a **chart** tool → the chart engine,
drawn inside that agent's drawer; a **file** output → document card and file viewer; a **table** →
the in-chat table; a **proposed action** → the approval card; a **citation** → citation chips and the
evidence hover card. "There is no trend data" is not a reason to leave charts dormant when an agent can
draw one.

## 0.4 · Persona → density, device and shell

Set the information density from the primary persona, then let the use-case dial and the density tokens
(REFERENCE) carry it:

- **Analyst / power user** → compact, keyboard-first, more on screen, fewer labels.
- **Occasional / external user** → spacious, guided, more labels and help.
- **Executive** → summary-first, few actions, headline numbers over raw rows.
- **Field / mobile user** → one column, thumb-reach actions at the bottom, large targets, glanceable
  status, camera and upload first, works in bright light.

**Then do it for every persona, not only the primary one.** Each persona gets a row in the build brief:
density, device and width (phone 375 px, tablet 768 px, laptop 1,280 px, wide 1,440 px), default theme,
and **its own shell** — which navigation it sees, what its first screen is, and how it reaches each
screen it uses. A persona who works on a phone or tablet gets real layouts at that width, with their
own navigation (bottom tabs on a phone, a collapsed rail on a tablet), not a desktop screen shrunk.
An external persona (customer, partner) gets its own lighter shell. **A persona whose screens are not
reachable from a shell has not been designed.**

**Shells are shown through the five screens (0.6), not drawn separately.** Choose the five so the
main personas' shells appear in them, each at its primary device; a phone screen is one of the five
only for a persona who mainly uses a phone. Any persona whose shell is not in the five gets a **shell
blueprint**: its navigation, first screen and regions as a labelled diagram, not a drawn screen.
Responsive behaviour is one line per shell (rail collapses to icons under 1,100 px; bottom tabs under
600 px). Device specimens use `<template class="device">` (Step 0's kit), never a narrowed `<div>`.

## 0.5 · Record the build brief on the page

The build brief ships in the port note (Step 7), alongside the colour decisions: the surfaces chosen,
the views drawn from the reserve, the density, and the out-of-scope line. A reviewer should be able to
see *why these views and not others* without opening the BRD. **The views you did not build, because
the BRD did not ask for them, are part of the record** — they show the scope was a decision, not a
limit.

## 0.6 · The deliverable — a kit and its rules, not a drawn copy of every page

**Write a page inventory, not a page gallery.** One row per page, overlay and screen the brief names
(sign-in and recovery, file viewer, confirmations, and every agent output from 0.3), recording what the
builder needs to **compose** it. Every L1 feature ID and component ID maps to at least one row (with wireframes:
every manifest component and every frame's page; 0.0).

| # | Page | BRD ref | Data shape (0.3) | Persona (0.4) | Fitting patterns | Chosen | Drawn? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Case queue | §8.1 | many records, flat | agent, dense | P1 · P2 | P2 | screen 1 of 5 |
| 2 | Case record | §8.3 | one record, deep | agent, dense | P3 · P2 | P3 | screen 2 of 5 |
| 3 | Hub overview | §8.4 | metrics + map | supervisor | P5 · P6 | P6 | blueprint, composed |

**The page draws five things. Only the fifth is full screens** (with approved wireframes, 0.0 decides which
components, the frames are the layouts, and the five screens are frames at high fidelity):

1. **Component pages** — every component the inventory needs, documented to the component-page spec
   (REFERENCE): anatomy, labelled variants, the full state matrix, micro-interactions, sizes, content
   rules, accessibility, do and don't. Signature components (0.8), modals, drawers and the agent drawer
   are documented here as components. **This is the bulk of the page and where its quality shows.**
2. **Foundations** — colour with measured ratios, type, spacing, **material and elevation** (the glass
   tiers over the ambient field, the solid rung, the edge light, both themes), motion and icons.
3. **Pattern blueprints** — every chosen pattern as a labelled region diagram: regions, grid split,
   which component families fill each region, how it reflows.
4. **Journeys as flow diagrams** (0.7), the demo storyline included, with exact wording.
5. **At most 5 full screens** — the system assembled. Pick them so that together they cover the main
   patterns chosen, the main personas' shells, and the key moments of the demo storyline; show the agent
   drawer open on one of them. Each is real: client content, in its shell, in a device at real width.

**Five screens is a hard limit.** Everything else a reviewer needs is in the component pages and
blueprints. A page unlike every pattern is a signature component (document it) or a sign the brief is
wrong for this system (say so in the inventory).

**The composition contract** (spec in REFERENCE, quoted in Step 7) carries the seed, the chosen
pattern per page, the active variant per family (`#style-sets`), and the rules. Ship the inventory in
the build brief section, each row linking to its screen or blueprint. "Finished" means every needed
component has its full page, every chosen pattern has a blueprint, every journey is a diagram, the
five screens are drawn and the contract is quoted.
Everything drawn meets the specimen bar: client content, real states, in its shell, screens in a
`<template class="device">` at real width.

## 0.7 · Journeys → flow diagrams

**The journeys are where the scoping document already describes the design.** A journey table that
says *"clicks Move stage → refused: 'No approved Fit or SMS sample'"*, *"reject without a reason is
refused"* or *"tile 24 → 23"* is an interaction specification. Earlier runs either never drew the
journey, so the builder invented every refusal, or drew a full app screen for every step, which
redrew the whole app and took most of the run. v8 keeps the information and drops the redraw.

**Every journey becomes a flow diagram on the page**, built with the flow engine (REFERENCE, process
and flow views): one node per step, swimlanes when more than one persona is involved, and the branch
for each exception. Each node carries, as short text on or beside it:

```
STEP       the screen it happens on (page name + pattern, from the 0.6 inventory)
ACTION     what the persona does (click, drag, type, approve, ask the agent)
RESPONSE   what the system shows next: the new state, the toast, the moved card, the changed count
EXCEPTION  the refusal or error, as its own branch, with the document's exact wording in quotes
FEEDBACK   only where it is not the default: an undo, a focus move, a keyboard path, an announcement
DATA       the record and field that changed
```

**Rules:**

- **Exact wording is mandatory.** Every refusal, toast and message the document gives appears on the
  diagram word for word. This is what stops the builder inventing them.
- **Cross-persona hand-offs are drawn as hand-offs** between swimlanes.
- **A diagram fits its column or says it scrolls.** If the steps do not fit the content width, wrap
  them onto a second row, or let the diagram scroll inside its frame with the lane names sticky on the
  left, an edge fade and a "Scroll →" hint. No card may end cut off at the frame edge.
- **Where the document gives the step but not the screen state, derive it** and mark it `[DERIVED]`.
  Where the document gives no journey for a persona, write that persona's first session and mark it
  `Proposed` (with wireframes, draw it from that persona's frames instead).
- **Default interactions are not repeated per node.** Hover and focus on everything clickable, a
  loading state between action and response, an empty first run and an undo after a reversible action
  are stated once, as the rule for every journey, in the composition contract.

**The demo storyline (§20) is a flow diagram too**, drawn first because it is what the client sees
first. Each of its steps names the screen (one of the five, 0.6) or the component page that shows that
moment, so the reviewer can follow the demo through the drawn screens without extra frames.

## 0.8 · Signature components — depth where it matters

**Every domain has two or three components that carry the product.** Shelf compliance has the shelf
photo with evidence boxes. Product creation has the colour-checked image studio and the stage gate.
Recruitment has the ranked shortlist with explained scores. Delivery has the risk grid and the change
approval chain. Generic parts — tiles, tables, tabs — are carried by the kit; signature components are
where the client sees that we understood their work.

**Choose them** from the scoping document's custom-component list (§21), the component inventory
(§23), the WOW factor in the executive summary and the demo storyline. Name each in the build brief
with the reason.

**Specify each one in depth, on the page:**

1. **Anatomy** — every part named, with the token it uses and its measured contrast.
2. **Every state** of the universal state rule, plus its domain states (for a shelf photo: analysing,
   scored, retake needed, low confidence, override pending).
3. **Data variants** — empty, one item, typical, many (the document's real volumes), overflow, very
   long text, missing image, the worst real record in the seed data.
4. **Interactions** — what each click, hover, drag and key does, with the keyboard path and the
   non-drag alternative; what is selected, what is linked (tap a finding ↔ highlight its box).
5. **Responsive** — how it reflows at each persona's device width (0.4).
6. **Motion** — what moves, why, how long; nothing decorative.
7. **AI behaviour** — where the AI marker sits, how confidence shows, how a person accepts, edits or
   rejects, what an AI failure looks like.
8. **Variants** — at least two layouts for different contexts (a full view and a compact card; a
   desktop panel and a phone sheet), so the builder has the right one for each page (with wireframes,
   the forms the manifest lists for it come first; 0.0).

Document each signature component on its own full component page, drawn large, with real seed data, in its states and variants. **A signature
component drawn once, at one size, in its happy state, is a generic component with a new name.**

**Signature components take their form from the design concept** (Step 2c): they are where the
concept is most visible. **They may introduce new composition** — a new layout of existing atoms, a new
overlay on an image, a new arrangement of a grid — but never a new colour value outside the transform,
a new radius, a third elevation or a new type size. That is where the expression of depth lives.

## 0.9 · Agents → the agent drawer

**Every agent the document names gets the agent drawer** (REFERENCE, "The agent component"), with
that agent's name, scope, suggested prompts from the document, a real question from a journey, its
working stages and its answer rendered with its own output types (0.3) — chart, table, file, citation,
proposed action. **The main agent is shown open over one of the five screens.** Every other agent is
documented on the agent-drawer component page as the drawer alone, with its own content, so no extra
screens are drawn.

- **The drawer is the default for every agent, on every page.** If the document puts an agent on a
  page as a card or a full-width block ("Copilot full width on Home"), draw it as the drawer, give
  the page a launcher in the top bar and a floating button, and record the correction (0.1). A
  dashboard may keep an **AI insight card** that summarises; the conversation still opens in the
  drawer.
- **One drawer per agent family**, opened from the top bar on every internal page, with the current
  page's record as context.
- **Specify that it is built on the platform's live agent component** — streamed replies, real
  stages, tool outputs rendered in the thread. Never an automation that writes the answer to an
  object which the page shows after a refresh. The composition contract (Step 7) carries this line.
- **Agents that act** (approve, move, send) show the proposed action inside the drawer as a
  human-in-the-loop card, before and after, with approve and reject; nothing happens without it.

---
## Answering the AI PM (POC Studio, v1.0)

The orchestrator may call this skill again with the AI PM's findings (`<workspace>/reviews/design-system-review-<n>.yaml`)
instead of a fresh task. Then:

1. **Fix only what is listed.** Edit the existing output in place: the named sections and specimens of the one HTML file only, byte-for-byte elsewhere; leave everything else exactly as it was. Do
   not re-run the whole pipeline for a handful of findings.
2. **Answer every finding** in `<workspace>/reviews/design-system-response-<n>.yaml` (same `n` as the review):
   ```yaml
   responses:
     - { finding: F1, status: fixed,    where: "<section / page / specimen / scene>" }
     - { finding: F2, status: disputed, reason: "<the evidence: an E-, S-, A- or D-ID, a stated ask, a human decision>" }
     - { finding: F3, status: deferred, reason: "<non-blocking only>" }
   ```
   Dispute when the finding is wrong for this client, and say why with evidence; a dispute without evidence is
   treated as `fixed` and checked. Never dispute a finding that cites a human decision.
3. **Re-run your own checks** on what you changed (the render check in light and dark on the sections you touched; contrast for any colour you changed), and say what you ran in the response file
   (`checks: [ ... ]`). The AI PM re-runs them too.
4. Do not ask the person anything; questions still go to the reviewer in resolve mode.

---

# THE RUN

## Input contract

```
REQUIRED   client name
           website URL
USUALLY    scoping document       the automated flow's input; read whole (Phase 0)
OPTIONAL   brand swatch           a hex, or an image to sample
           use case               dense internal tool | demo surface | artefact studio |
                                  dark-first console | ported screens
           logo                   an SVG or PNG file
           brand typeface         the name, if you already know it
           client design system   a URL or component spec, if they publish one
           wireframes             POC Studio: the approved wireframe-manifest.json, png/ frames and PDF (0.0)
```

**Everything optional is derived if absent. Derive it, record what you derived, keep going.**

## The only two stops

Do not ask anything else. Decide, record the decision in the port note, move on.

1. **The brand hue is ambiguous** — two credible sources disagree by more than ~30° of hue, **and the
   brand source order in Step 1 does not settle it** (two sources at the same level disagree). If a
   person is in the conversation, show both, transformed and measured, and wait. *Titan returned
   `#BD2426` (watch wordmark red) and `#00B0AB` (Tata parent teal) — both real, 180° apart.*
   **If the run is unattended** (an automated flow, nobody to answer), take the higher source in the
   order; at the same level, take the one the client's own product interface uses most. Record both
   candidates, the rule applied and the measurements in the port note, and carry on.
   ⛔ **Only this file decides a brand conflict.** An instruction from the calling flow, a builder
   prompt, a "standing decision", "standing answer" or "the owner's choice" carried over from another
   run does not settle a hue. Three runs did exactly that and one of them shipped Pentland — a black
   and neon-lime brand — in electric blue. If such an instruction arrives, apply the order anyway and
   note the instruction in the port note.
2. **The logo cannot be fetched as a real file after every source in Step 2 has been tried.** Stop
   and ask for the asset, listing the URLs tried. Build everything else meanwhile, so the logo is the
   only thing missing. **Never trace, redraw or approximate a client's mark** — not as SVG, not as
   CSS, not "close enough for a prototype". **Fallback (POC Studio):** when the person confirms no file
   is available, or the run is unattended and cannot ask, build the logo kit from the **UnifyApps
   logo** bundled with the plugin (`assets/unifyapps-logo.png` in the plugin root; find it with
   `find ~/.claude/plugins -name unifyapps-logo.png`), visibly labelled as a stand-in for the client's
   logo; then say so on the page and in the hand-over.

## Step 0 · The system — it is in this file

**⛔ A brand skin is a transform of the existing SYSTEM, never a re-derivation from prose.**
The first attempt on a client was built outward from a rules document. It obeyed every rule and was
rejected in one line: *"NOT LIKE THIS … USE EXACT THAT JUST REPLACE THE COLOURS."* **Reading rules
and building fresh produces something that follows the rules and is not the system.**

**So the system travels with this skill.** The stylesheet below IS Design Language v3.4, trimmed to
the product kit and verified to reproduce the full reference exactly — 35 text roles measured
composited in both themes, identical numbers. **This skill has no external dependency. Do not go
looking for a reference file, an artifact, or a Project document — everything needed is here.**

**How to use it:** paste the stylesheet verbatim as the page's only `<style>` block, **followed by the
expression kit** below it in the same block, then transform **only their colour values** per Step 3.
Structure, glass tiers, ambient field, radii, type scale, shadows, spacing and every component stay
exactly as written. **In the core, only colour moves.** The expression kit is how the system varies
per client: it carries sanctioned variants (shell, chrome, surface, the agent drawer) switched by
attributes on `<html>`, chosen in Step 2c. **Choosing among the kit's variants is expression; writing
a new structure outside them is a second system** — the failure the next paragraph warns about.

⚠️ **Never rewrite a component from the prose in this file when a class for it exists below.** The
prose states *why* a component behaves as it does; the stylesheet states *what it is*. A second
implementation is how one design system quietly becomes two — it is the most common failure on this
work, and it shows up as mixed radii and two kinds of search field on one screen.

### The class inventory — call these, never write a second set

| Piece | Class |
| --- | --- |
| Glass tiers · padding · nested rung · solid | `.g1` `.g2` `.g3` `.pad` `.pad-s` `.inner` `.solid` |
| Ambient field (3 fixed layers) | `.amb.a` `.amb.b` `.amb.v` |
| Type | `.title` `.micro` (mono eyebrow) |
| Buttons · tags · pips | `.btn` `.btn-p` `.btn-s` `.btn-t` · `.tag` + `.neutral/.attention/.negative/.positive` · `.pip` |
| Table toolbar · search · facet · card · grid | `.toolbar` `.field` `.chipsel` `.tblwrap` `.tbl` |
| Pagination | `.pg` `.pgb` `.rng` |
| AI Insight (scoped, see below) | `.ai:not(.msg)` |
| Tiles · loop strip · empty | `.tile` `.loop` `.empty` |
| Fused tabs | `.tabs` `.tab` `.tabpanel` |
| Forms | `.fld` `.ctl` (+`.focus/.err/.warn/.off`) `.hint` `.seg` `.tog` `.opt` `.box` `.dot` |
| Steppers · progress · reasoning stages | `.sth` `.stv` `.prog` `.stages` |
| Copilot | `.canvas` `.convo` `.msg.me` `.msg.ai` `.chips` |
| Kanban · calendar · agenda · slots | `.kb` `.cal` `.agenda` `.slot` |
| Person card · face stack · avatar | `.pc` `.faces` `.av` |
| Activity feed | `.feed` `.fi` `.fd` |
| Chart frame · sparkline · delta · legend | `.chart` `.spark` `.delta` `.legend` |
| Toast · menu · breadcrumb · note | `.toast` `.menu` `.crumb` `.note` |
| **App shell** (kit) | `.app` (+`.with-agent`, `[data-shell="top"]`) `.app-rail` `.brand` `.nav-i` (+`[aria-current="page"]`) `.prof` `.app-main` `.app-top` (+`.scrolled`) `.app-body` `.app-tabs` |
| **Agent drawer** (kit) | `.agent-launch` `.agent-drawer` (+`[data-open]`, `.wide`, `.docked`) `.ad-hd` `.ad-name` `.ad-tools` `.ad-ctx` `.ad-thread` `.ad-dock` `.ad-composer` `.ad-out` `.ad-action` `.ad-diff` |
| **Expression switches** (kit, on `<html>`) | `data-chrome="brand / ink / light"` · `data-surface="glass / solid / paper"` · `data-density="compact / comfortable"` · `data-style-set="S1/S2/S3"` · `data-theme` · `--font-display` · `--signal` · `--paper` |
| **Overlays** (kit) | `.scrim` · `.modal` (+`.s`, `.l`) · `.drawer` (+`.s`, `.l`) · `.ov-hd` `.ov-t` `.ov-sub` `.ov-x` · `.ov-bd` · `.ov-ft` (+`.lead`) |
| **Spacing and density** (kit) | `--s-1…--s-12` · `--page-pad` `--section-gap` `--card-pad` · `--row-h` `--cell-px` `--cell-py` · `--ov-s/m/l` `--ov-pad` · `--content-max` |
| **Dense data** (kit) | `.cl` `.cl2` (`--col-w`) · `.cell-chips` `.more` · `.tblwrap.freeze` · `.row-x` `.xp` · `.dl` · `.cv` `.cv-tag` |
| **Specimens** (kit) | `<template class="device" data-device="desktop / wide / tablet / phone">` → `.device-wrap` · `.devices` · `.frame` (components only) |

**Not in the kit, by choice** — the artefact studio, command palette, notification tray, diff view,
bulk bar, slider and file drop. They are rare enough that carrying them costs every run. **Build them
from the tokens and the doctrine in the REFERENCE section, never with new colour values**, and if one
recurs across two builds, add it to the kit.

⚠️ **`.ai` vs `.msg.ai`.** The AI Insight card is `.ai:not(.msg)` and agent chat bubbles are
`.msg.ai`. An unscoped `.ai` rule renders **every conversation turn as an AI Insight card** —
invisible in light, obvious in dark. The kit is already scoped; keep it that way.

### The stylesheet

**Paste verbatim. Measured in v5: the core carries 47 distinct hexes, 26 `rgb()`/`rgba()` triples and 9
bare `--aur` triple declarations; the expression kit adds 11 hexes and 7 triples. Inventory them,
transform them, diff the count afterwards.** (Earlier versions printed "54 hexes and 25 triples"; the
trimmed sheet never matched it, and three runs had to re-count. These are the measured numbers.)

```css
:root{--sp-deep:#0033A1;--sp-blue:#0071CE;--sp-cerise:#CC27B0;--sp-pink:#E17FD2;--base:#F1F5FB;--page-top:rgba(0,51,161,.022);--glass-1:rgba(255,255,255,.72);--glass-2:rgba(255,255,255,.82);--glass-3:rgba(255,255,255,.93);--glass-solid:rgba(255,255,255,.965);--inner:rgba(0,51,161,.045);--edge:inset 0 1px 0 rgba(255,255,255,.92);--blur-1:blur(22px) saturate(160%);--blur-2:blur(26px) saturate(170%);--ink:#0B1220;--ink-2:#47566B;--ink-3:#626D84;--ink-mute:#8E9AAE;--hair:rgba(11,18,32,.07);--hair-2:rgba(11,18,32,.12);--st-neutral:#47566B;--st-neutral-t:rgba(71,86,107,.10);--st-attention:#8A5A00;--st-attention-t:rgba(138,90,0,.11);--st-negative:#96302A;--st-negative-t:rgba(150,48,42,.11);--st-positive:#1F6F5B;--st-positive-t:rgba(31,111,91,.11);--c1:#00325C;--c2:#005194;--c3:#0070CC;--c4:#0A90FF;--c5:#47ACFF;--c6:#85C8FF;--r:10px;--r-sm:6px;--r-pill:999px;--lift-1:0 1px 2px rgba(6,22,54,.05),0 12px 32px -18px rgba(6,22,54,.28);--lift-2:0 2px 6px rgba(6,22,54,.07),0 28px 60px -26px rgba(6,22,54,.40);--ease:150ms cubic-bezier(.22,.7,.28,1);--aur-a:0,51,161;--aur-b:0,113,206;--aur-c:204,39,176;--aur-1:.055;--aur-2:.045;--aur-3:.050;--vig:radial-gradient(120% 100% at 50% 40%,transparent 42%,rgba(6,18,46,.10) 100%)} @media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--base:#0B1018;--page-top:rgba(120,165,225,.04);--glass-1:rgba(150,180,230,.05);--glass-2:rgba(150,180,230,.07);--glass-3:rgba(150,180,230,.095);--glass-solid:#151B26;--inner:rgba(160,190,240,.06);--edge:inset 0 1px 0 rgba(214,232,255,.10);--ink:#E7ECF3;--ink-2:#B6C0CF;--ink-3:#9AA6B8;--ink-mute:#6F7B90;--hair:rgba(206,224,255,.08);--hair-2:rgba(206,224,255,.14);--sp-blue:#7DBDF0;--sp-deep:#3A72DE;--sp-cerise:#E884D6;--sp-pink:#F2BCE9;--st-neutral:#B6C0CF;--st-neutral-t:rgba(182,192,207,.12);--st-attention:#E8BC69;--st-attention-t:rgba(232,188,105,.13);--st-negative:#F2A49D;--st-negative-t:rgba(242,164,157,.13);--st-positive:#8FD3BA;--st-positive-t:rgba(143,211,186,.13);--c1:#E6F2FF;--c2:#B9DDFF;--c3:#8CC6F8;--c4:#62ADEC;--c5:#3F90D6;--c6:#3576B0;--lift-1:0 1px 2px rgba(2,6,14,.46),0 14px 34px -18px rgba(2,6,14,.68);--lift-2:0 2px 7px rgba(2,6,14,.52),0 32px 66px -26px rgba(2,6,14,.80);--aur-a:76,127,232;--aur-b:107,179,234;--aur-c:232,132,214;--aur-1:.18;--aur-2:.12;--aur-3:.14;--vig:radial-gradient(120% 100% at 55% 42%,transparent 48%,rgba(2,5,11,.42) 100%)} }:root[data-theme="dark"]{--base:#0B1018;--page-top:rgba(120,165,225,.04);--glass-1:rgba(150,180,230,.05);--glass-2:rgba(150,180,230,.07);--glass-3:rgba(150,180,230,.095);--glass-solid:#151B26;--inner:rgba(160,190,240,.06);--edge:inset 0 1px 0 rgba(214,232,255,.10);--ink:#E7ECF3;--ink-2:#B6C0CF;--ink-3:#9AA6B8;--ink-mute:#6F7B90;--hair:rgba(206,224,255,.08);--hair-2:rgba(206,224,255,.14);--sp-blue:#7DBDF0;--sp-deep:#3A72DE;--sp-cerise:#E884D6;--sp-pink:#F2BCE9;--st-neutral:#B6C0CF;--st-neutral-t:rgba(182,192,207,.12);--st-attention:#E8BC69;--st-attention-t:rgba(232,188,105,.13);--st-negative:#F2A49D;--st-negative-t:rgba(242,164,157,.13);--st-positive:#8FD3BA;--st-positive-t:rgba(143,211,186,.13);--c1:#E6F2FF;--c2:#B9DDFF;--c3:#8CC6F8;--c4:#62ADEC;--c5:#3F90D6;--c6:#3576B0;--lift-1:0 1px 2px rgba(2,6,14,.46),0 14px 34px -18px rgba(2,6,14,.68);--lift-2:0 2px 7px rgba(2,6,14,.52),0 32px 66px -26px rgba(2,6,14,.80);--aur-a:76,127,232;--aur-b:107,179,234;--aur-c:232,132,214;--aur-1:.18;--aur-2:.12;--aur-3:.14;--vig:radial-gradient(120% 100% at 55% 42%,transparent 48%,rgba(2,5,11,.42) 100%)} *{box-sizing:border-box} body{background:var(--base);background-image:linear-gradient(176deg,var(--page-top) 0%,transparent 46%);color:var(--ink);font-family:Archivo,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:15px;line-height:1.6;font-variant-numeric:tabular-nums;letter-spacing:-.003em;-webkit-font-smoothing:antialiased;position:relative} .amb{position:fixed;inset:-10%;pointer-events:none;z-index:0} .amb.a{filter:blur(84px);background:radial-gradient(62% 52% at 12% 4%,rgba(var(--aur-a),var(--aur-1)),transparent 72%),radial-gradient(56% 48% at 90% 20%,rgba(var(--aur-b),var(--aur-3)),transparent 72%),radial-gradient(64% 54% at 28% 82%,rgba(var(--aur-a),var(--aur-1)),transparent 74%)} .amb.b{filter:blur(70px);opacity:.9;background:radial-gradient(50% 42% at 78% 64%,rgba(var(--aur-c),var(--aur-2)),transparent 72%),radial-gradient(44% 38% at 6% 44%,rgba(var(--aur-c),var(--aur-2)),transparent 72%)} .amb.v{background:var(--vig)} .display{font-size:34px;line-height:1.12;font-weight:600;letter-spacing:-.028em;margin:0;text-wrap:balance} .title{font-size:19px;line-height:1.3;font-weight:600;letter-spacing:-.014em;margin:0} p,li,td,th{font-size:15px;line-height:1.6;font-weight:400;margin:0} .micro{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;line-height:1.4;font-weight:600;letter-spacing:.09em;text-transform:uppercase} header.mast{padding-block:76px 30px;display:flex;flex-direction:column;gap:16px} header.mast .micro{color:var(--sp-blue)} header.mast p{color:var(--ink-2);max-width:64ch;font-size:17px;line-height:1.6} h3.sub{font-size:15px;font-weight:600;margin:0;letter-spacing:-.008em} .g1,.g2,.g3{border-radius:var(--r);position:relative} .g1{background:var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .g2{background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:var(--lift-2),var(--edge)} .g3{background:var(--glass-3);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:var(--lift-1),var(--edge)} .pad{padding:22px} .pad-s{padding:16px 18px} .inner{background:var(--inner);border-radius:var(--r-sm);padding:14px 16px} .solid{background:var(--glass-solid);border-radius:var(--r);box-shadow:var(--lift-1),var(--edge)} .grid{display:grid;gap:16px} .g2c{grid-template-columns:repeat(auto-fit,minmax(272px,1fr))} .g3c{grid-template-columns:repeat(auto-fit,minmax(205px,1fr))} .g4c{grid-template-columns:repeat(auto-fit,minmax(158px,1fr))} .stack{display:flex;flex-direction:column;gap:12px} .row{display:flex;gap:10px;align-items:center;flex-wrap:wrap} .sw{border-radius:var(--r);overflow:hidden;background:var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .btn{font-family:inherit;font-size:14px;font-weight:600;border:0;border-radius:var(--r-pill);padding:10px 20px;cursor:pointer;letter-spacing:-.006em;transition:transform var(--ease),box-shadow var(--ease),background var(--ease)} .btn-p{background:linear-gradient(180deg,#0071CE 0%,#005DB4 42%,#0035A6 100%);color:#fff;box-shadow:0 1px 1px rgba(6,22,54,.18),0 10px 22px -12px rgba(0,63,168,.70),inset 0 1px 0 rgba(255,255,255,.28)} .btn-p:hover{transform:translateY(-1px);box-shadow:0 1px 1px rgba(6,22,54,.20),0 16px 30px -14px rgba(0,63,168,.80),inset 0 1px 0 rgba(255,255,255,.32)} .btn-s{background:var(--glass-2);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);color:var(--ink);box-shadow:var(--lift-1),var(--edge)} .btn-t{background:transparent;color:var(--ink-2);padding-inline:12px} .btn-t:hover{background:var(--inner)} .btn:disabled{background:var(--inner);color:var(--ink-mute);box-shadow:none;cursor:not-allowed;transform:none} .btn:focus-visible{outline:2px solid var(--sp-blue);outline-offset:3px} .tag{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;font-weight:600;line-height:1.3;padding:4px 11px;border-radius:var(--r-pill);background:var(--inner);color:var(--ink-2);letter-spacing:.01em} .tag.neutral{background:var(--st-neutral-t);color:var(--st-neutral)} .tag.attention{background:var(--st-attention-t);color:var(--st-attention)} .tag.negative{background:var(--st-negative-t);color:var(--st-negative)} .tag.positive{background:var(--st-positive-t);color:var(--st-positive)} .tag svg{width:12px;height:12px;flex:none} .pips{display:inline-flex;gap:6px;align-items:center} .pip{width:14px;height:14px;border-radius:50%;display:grid;place-items:center} .pip.done{background:linear-gradient(180deg,#2C8A74,#1F6F5B);box-shadow:inset 0 1px 0 rgba(255,255,255,.3)} .pip.draft{background:linear-gradient(180deg,#A87213,#8A5A00);box-shadow:inset 0 1px 0 rgba(255,255,255,.28)} .pip.stale{background:var(--st-attention-t);box-shadow:inset 0 0 0 1.8px var(--st-attention)} .pip.missing{background:transparent;box-shadow:inset 0 0 0 1.5px var(--hair-2)} .pip i{font-style:normal;font-family:"IBM Plex Mono",monospace;font-size:8px;font-weight:600;color:#fff;line-height:1} .pip.stale i{color:var(--st-attention)} .pip.missing i{color:var(--ink-mute)} .tblwrap{overflow-x:auto;border-radius:var(--r);background:var(--glass-solid);box-shadow:var(--lift-1),var(--edge)} .tbl{width:100%;border-collapse:collapse} .tbl thead th{text-align:left;padding:12px 16px;color:var(--ink-3);font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;white-space:nowrap;border-bottom:1px solid var(--hair)} .tbl tbody td{padding:13px 16px;border-top:1px solid var(--hair);vertical-align:middle} .tbl tbody tr:first-child td{border-top:0} .tbl tbody tr{transition:background var(--ease)} .tbl tbody tr:hover{background:var(--inner)} .tbl .n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap} .toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding-bottom:14px} .field{flex:1;min-width:190px;display:flex;align-items:center;gap:9px;background:var(--glass-2);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);border-radius:var(--r-pill);padding:9px 15px;color:var(--ink-3);box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.04)} .field input{border:0;background:transparent;font-family:inherit;font-size:14px;color:var(--ink);width:100%;outline:none} .chipsel{background:var(--glass-2);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);border-radius:var(--r-pill);padding:9px 14px;font-size:13px;font-weight:500;color:var(--ink-2);display:flex;gap:7px;align-items:center;box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.04)} .tabs{display:flex;gap:3px;padding:0 5px} .tab{font-family:inherit;font-size:13.5px;font-weight:600;border:0;background:transparent;color:var(--ink-3);padding:11px 16px;border-radius:var(--r) var(--r) 0 0;cursor:pointer;transition:color var(--ease),background var(--ease)} .tab[aria-selected="true"]{background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);color:var(--ink);box-shadow:var(--edge)} .tabpanel{background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);border-radius:0 var(--r) var(--r) var(--r);box-shadow:var(--lift-1),var(--edge);padding:20px} .ai:not(.msg){border-radius:var(--r);padding:18px 20px;display:flex;flex-direction:column;gap:10px;background:linear-gradient(135deg,rgba(0,51,161,.075) 0%,rgba(0,113,206,.045) 48%,rgba(204,39,176,.065) 100%),var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .ai .hd{display:flex;align-items:center;gap:8px} .ai .hd .micro{color:var(--sp-blue)} .ai p{color:var(--ink)} .ai .ground{font-size:13px;color:var(--ink-3)} .ai .foot{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap} .chev{background:transparent;border:0;color:var(--ink-3);font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;cursor:pointer;padding:0} .tile{border-radius:var(--r);padding:18px 20px;display:flex;flex-direction:column;gap:7px;background:linear-gradient(180deg,rgba(255,255,255,.28),rgba(255,255,255,0)),var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .tile .micro{color:var(--ink-3)} .tile .v{font-size:30px;font-weight:600;line-height:1.08;letter-spacing:-.03em} .tile .sub{font-size:13px;color:var(--ink-3);line-height:1.45} .tile.flag{background:linear-gradient(180deg,rgba(138,90,0,.10),rgba(138,90,0,.04)),var(--glass-1)} .tile.flag .v{color:var(--st-attention)} .loop{display:flex;border-radius:var(--r);overflow:hidden;background:var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .loop div{flex:1;padding:14px 16px;display:flex;flex-direction:column;gap:4px} .loop div + div{border-left:1px solid var(--hair)} .loop .micro{color:var(--ink-3)} .loop b{font-size:19px;font-weight:600;letter-spacing:-.02em} .loop .on{background:linear-gradient(180deg,rgba(0,113,206,.10),rgba(0,113,206,.03))} .loop .on b{color:var(--sp-blue)} .rail-demo{border-radius:var(--r);overflow:hidden;box-shadow:var(--lift-2);display:flex;min-height:230px} .empty{border-radius:var(--r);padding:28px 22px;display:flex;flex-direction:column;gap:12px;align-items:flex-start;background:var(--inner)} .legend{display:flex;gap:16px;flex-wrap:wrap} .legend i{width:10px;height:10px;border-radius:3px;display:inline-block;margin-right:7px} .legend span{font-size:13px;color:var(--ink-2);display:inline-flex;align-items:center} code.inl{font-family:"IBM Plex Mono",monospace;font-size:12.5px;background:var(--inner);padding:2px 6px;border-radius:var(--r-sm);color:var(--ink-2)} .note{border-radius:var(--r);padding:16px 18px;display:flex;flex-direction:column;gap:7px;background:linear-gradient(180deg,rgba(138,90,0,.09),rgba(138,90,0,.03)),var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .note .micro{color:var(--st-attention)} .note p{color:var(--ink)} @media (max-width:640px){.loop{flex-direction:column} .loop div + div{border-left:0;border-top:1px solid var(--hair)} .rail-demo{flex-direction:column} .rail-demo .nav{width:auto} } @media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}} .fld{display:flex;flex-direction:column;gap:6px} .fld > label{font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3)} .ctl{display:flex;align-items:center;gap:9px;background:var(--glass-2);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);border-radius:var(--r);padding:11px 14px;box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.04);transition:box-shadow var(--ease)} .ctl input,.ctl textarea,.ctl select{border:0;background:transparent;font-family:inherit;font-size:15px;color:var(--ink);width:100%;outline:none;letter-spacing:-.003em} .ctl textarea{resize:vertical;min-height:76px;line-height:1.55} .ctl.focus{box-shadow:var(--edge),0 0 0 3px rgba(0,113,206,.18),0 1px 2px rgba(6,22,54,.05)} .ctl.err{box-shadow:var(--edge),0 0 0 3px rgba(150,48,42,.16),0 1px 2px rgba(6,22,54,.05);background:linear-gradient(0deg,var(--st-negative-t),var(--st-negative-t)),var(--glass-2)} .ctl.warn{box-shadow:var(--edge),0 0 0 3px rgba(138,90,0,.15),0 1px 2px rgba(6,22,54,.05);background:linear-gradient(0deg,var(--st-attention-t),var(--st-attention-t)),var(--glass-2)} .ctl.off{background:var(--inner);box-shadow:none} .ctl.off input{color:var(--ink-mute)} .hint{font-size:13px;color:var(--ink-3);line-height:1.45} .hint.e{color:var(--st-negative);display:flex;gap:6px;align-items:flex-start} .hint.w{color:var(--st-attention);display:flex;gap:6px;align-items:flex-start} .hint svg{width:13px;height:13px;flex:none;margin-top:2px} .req{color:var(--st-negative);font-weight:600} .seg{display:inline-flex;gap:2px;padding:3px;border-radius:var(--r-pill);background:var(--inner)} .seg button{font-family:inherit;font-size:13px;font-weight:600;border:0;background:transparent;color:var(--ink-3);padding:7px 16px;border-radius:var(--r-pill);cursor:pointer;letter-spacing:-.004em;transition:color var(--ease),background var(--ease)} .seg button[aria-pressed="true"]{background:var(--glass-3);color:var(--ink);box-shadow:var(--edge),0 1px 3px rgba(6,22,54,.10)} .tog{display:inline-flex;align-items:center;gap:11px;cursor:pointer} .tog .track{width:44px;height:26px;border-radius:var(--r-pill);background:var(--inner);position:relative;transition:background var(--ease);box-shadow:inset 0 1px 2px rgba(6,22,54,.08)} .tog .track .knob{position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(6,22,54,.28),inset 0 1px 0 rgba(255,255,255,.9);transition:transform var(--ease)} .tog.on .track{background:linear-gradient(180deg,#0071CE,#005DB4 60%,#0056B4)} .tog.on .track .knob{transform:translateX(18px)} .tog span{font-size:14px;color:var(--ink-2)} .opt{display:inline-flex;align-items:flex-start;gap:10px;cursor:pointer;font-size:14px;color:var(--ink-2)} .box,.dot{width:19px;height:19px;flex:none;border-radius:var(--r-sm);background:var(--glass-3);box-shadow:var(--edge),inset 0 0 0 1px var(--hair-2);display:grid;place-items:center;margin-top:1px} .dot{border-radius:50%} .opt.on .box,.opt.on .dot{background:linear-gradient(180deg,#0071CE,#005DB4 60%,#0056B4);box-shadow:inset 0 1px 0 rgba(255,255,255,.3),0 1px 3px rgba(0,63,168,.35)} .box svg,.dot svg{width:12px;height:12px;color:#fff;opacity:0} .opt.on .box svg{opacity:1} .opt.on .dot::after{content:"";width:7px;height:7px;border-radius:50%;background:#fff} .sl{display:flex;flex-direction:column;gap:9px} .drop{border-radius:var(--r);padding:26px 20px;background:var(--inner);display:flex;flex-direction:column;align-items:center;gap:9px;text-align:center} .sth{display:flex;align-items:flex-start;gap:0} .sth .nd{flex:1;display:flex;flex-direction:column;gap:8px;position:relative;padding-top:2px} .sth .bar{display:flex;align-items:center;gap:0} .sth .cir{width:26px;height:26px;border-radius:50%;flex:none;display:grid;place-items:center;font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600} .sth .cir.done{background:linear-gradient(180deg,#2C8A74,#1F6F5B);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.3)} .sth .cir.now{background:linear-gradient(180deg,#0071CE,#005DB4 60%,#0035A6);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.3),0 0 0 4px rgba(0,113,206,.14)} .sth .cir.todo{background:var(--glass-3);color:var(--ink-mute);box-shadow:var(--edge),inset 0 0 0 1px var(--hair-2)} .sth .cir.block{background:var(--st-negative-t);color:var(--st-negative);box-shadow:inset 0 0 0 1.5px var(--st-negative)} .sth .ln{flex:1;height:2px;background:var(--hair-2);border-radius:2px} .sth .ln.done{background:linear-gradient(90deg,#1F6F5B,#2C8A74)} .sth .lbl{font-size:13px;font-weight:600;letter-spacing:-.006em;padding-right:12px} .sth .sub{font-size:12.5px;color:var(--ink-3);padding-right:12px;line-height:1.45} .stv{display:flex;flex-direction:column} .stv .nd{display:grid;grid-template-columns:26px minmax(0,1fr);gap:0 14px;position:relative;padding-bottom:16px} .stv .nd:last-child{padding-bottom:0} .stv .nd::before{content:"";position:absolute;left:12.5px;top:26px;bottom:0;width:2px;background:var(--hair-2)} .stv .nd:last-child::before{display:none} .stv .cir{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;z-index:1} .stv .c{display:flex;flex-direction:column;gap:6px;padding-top:2px;min-width:0} .stv .hdr{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap} .stv .hdr b{font-size:14px;font-weight:600;letter-spacing:-.006em} .stv .hdr .when{font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--ink-3);letter-spacing:.05em} .stv .ev{font-size:13.5px;color:var(--ink-2);line-height:1.5} .pad ul,.stack ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px} .pad ul li,.stack ul li{position:relative;padding-left:17px;font-size:14px;line-height:1.6;color:var(--ink-2)} .pad ul li::before{content:"";position:absolute;left:1px;top:8px;width:5px;height:5px;border-radius:50%;background:var(--sp-blue);opacity:.5} .stack ul li::before{content:"";position:absolute;left:1px;top:8px;width:5px;height:5px;border-radius:50%;background:var(--sp-blue);opacity:.5} .pad ul li b,.stack ul li b{color:var(--ink);font-weight:600} .prog{height:6px;border-radius:var(--r-pill);background:var(--inner);overflow:hidden;box-shadow:inset 0 1px 2px rgba(6,22,54,.08)} .prog i{display:block;height:100%;border-radius:var(--r-pill);background:linear-gradient(90deg,#0033A1,#0071CE)} .prog.mini{width:130px;height:4px;flex:none} .stages{display:flex;flex-direction:column;gap:9px} .stages div{display:flex;gap:10px;align-items:center;font-size:13.5px} .stages .tick{width:16px;height:16px;border-radius:50%;flex:none;display:grid;place-items:center} .stages .tick.ok{background:var(--st-positive-t);color:var(--st-positive)} .stages .tick.run{background:var(--inner);box-shadow:inset 0 0 0 1.5px var(--sp-blue)} .stages .tick.wait{background:var(--inner);box-shadow:inset 0 0 0 1.5px var(--hair-2)} .stages .ok + span{color:var(--ink-2)} .stages .run + span{color:var(--ink);font-weight:600} .stages .wait + span{color:var(--ink-mute)} .scene{position:relative;border-radius:var(--r);overflow:hidden;background:var(--glass-3);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:var(--lift-2),var(--edge);min-height:340px} .three{display:grid;grid-template-columns:132px minmax(0,1fr) 250px;gap:1px;border-radius:var(--r);overflow:hidden;background:var(--hair);box-shadow:var(--lift-1),var(--edge);min-height:270px} .toast{display:inline-flex;align-items:center;gap:13px;padding:13px 16px;border-radius:var(--r);background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:var(--lift-2),var(--edge)} .toast .ic{width:22px;height:22px;border-radius:50%;flex:none;display:grid;place-items:center;background:var(--st-positive-t);color:var(--st-positive)} .toast b{font-size:14px;font-weight:600;letter-spacing:-.006em} .toast small{display:block;font-size:12.5px;color:var(--ink-3)} .toast .undo{font-family:inherit;font-size:13px;font-weight:600;color:var(--sp-blue);background:transparent;border:0;cursor:pointer;padding:0 2px} .menu{width:236px;border-radius:var(--r);padding:6px;background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:var(--lift-2),var(--edge);display:flex;flex-direction:column;gap:1px} .menu a{display:flex;justify-content:space-between;gap:12px;align-items:center;padding:9px 12px;border-radius:var(--r-sm);font-size:14px;color:var(--ink-2);text-decoration:none} .menu a:hover{background:var(--inner);color:var(--ink)} .menu a kbd{font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--ink-3)} .menu hr{height:1px;background:var(--hair);border:0;margin:5px 0} .menu a.danger{color:var(--st-negative)} .crumb{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink-3);flex-wrap:wrap} .crumb a{color:var(--ink-2);text-decoration:none} .crumb a:hover{color:var(--ink)} .crumb b{color:var(--ink);font-weight:600} .av{width:30px;height:30px;border-radius:50%;flex:none;display:grid;place-items:center;font-size:11.5px;font-weight:600;color:#fff;background:linear-gradient(150deg,#0058B8,#0033A1);box-shadow:inset 0 1px 0 rgba(255,255,255,.22),0 1px 3px rgba(6,22,54,.20)} .av.c2{background:linear-gradient(150deg,#B93CA5,#8C1E79)} .canvas{border-radius:var(--r);overflow:hidden;box-shadow:var(--lift-2),var(--edge);background:var(--glass-3);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);min-height:420px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:20px;padding:36px 24px;text-align:center;position:relative} .canvas .glowwrap{width:100%;max-width:520px;padding:26px} .canvas .composer{position:relative;display:flex;align-items:center;gap:11px;padding:15px 18px;border-radius:var(--r);background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:var(--edge),0 2px 6px rgba(6,22,54,.07),0 0 34px -6px rgba(0,113,206,.38),0 0 60px -10px rgba(204,39,176,.26)} .canvas .composer input{border:0;background:transparent;font-family:inherit;font-size:16px;color:var(--ink);width:100%;outline:none;letter-spacing:-.006em} .canvas .composer input::placeholder{color:var(--ink-3)} .canvas h3{font-family:inherit;font-size:26px;font-weight:600;letter-spacing:-.024em;margin:0;line-height:1.2} .canvas .sublede{font-size:14.5px;color:var(--ink-3);max-width:46ch;margin:0} .chips{display:flex;gap:9px;flex-wrap:wrap;justify-content:center} .chips button{font-family:inherit;font-size:13px;font-weight:500;color:var(--ink-2);background:var(--glass-2);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);border:0;border-radius:var(--r-pill);padding:8px 15px;cursor:pointer;box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.04)} .chips button:hover{color:var(--ink)} .proactive{width:100%;max-width:560px;display:flex;flex-direction:column;gap:10px;text-align:left} .convo{border-radius:var(--r);overflow:hidden;box-shadow:var(--lift-1),var(--edge);background:var(--glass-3);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);display:flex;flex-direction:column;min-height:420px} .convo .thread{flex:1;padding:18px;display:flex;flex-direction:column;gap:14px} .convo .dock{padding:14px 16px;display:flex;flex-direction:column;gap:10px;background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:inset 0 1px 0 var(--hair)} .convo .dock .composer{display:flex;align-items:center;gap:11px;padding:12px 15px;border-radius:var(--r);background:var(--glass-3);box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.05)} .convo .dock .composer input{border:0;background:transparent;font-family:inherit;font-size:15px;color:var(--ink);width:100%;outline:none} .msg{max-width:78%;display:flex;flex-direction:column;gap:5px} .msg.me{align-self:flex-end;align-items:flex-end} .msg.ai{align-self:flex-start} .msg .who{font-family:"IBM Plex Mono",monospace;font-size:10px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3)} .msg .bub{padding:12px 15px;border-radius:var(--r);font-size:14.5px;line-height:1.55} .msg.me .bub{background:linear-gradient(180deg,#0071CE,#005DB4 62%,#0059B6);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.24),0 6px 16px -10px rgba(0,63,168,.6)} .msg.ai .bub{background:var(--glass-2);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);color:var(--ink);box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.05)} .raildrw{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:1px;border-radius:var(--r);overflow:hidden;background:var(--hair);box-shadow:var(--lift-1),var(--edge);min-height:310px} @media (max-width:760px){.three{grid-template-columns:minmax(0,1fr)} .raildrw{grid-template-columns:minmax(0,1fr)} .sth{flex-direction:column;gap:14px} .sth .ln{display:none} } .scene{min-height:380px} .scope{display:inline-flex;align-items:center;gap:8px;align-self:flex-start;padding:5px 10px 5px 8px;border-radius:var(--r-pill);background:rgba(0,113,206,.10);color:var(--sp-blue);font-size:12px;font-weight:600} .cmdk{width:min(520px,100%);border-radius:var(--r);overflow:hidden;background:var(--glass-2);backdrop-filter:var(--blur-2);-webkit-backdrop-filter:var(--blur-2);box-shadow:var(--lift-2),var(--edge)} @media (max-width:860px){.diff > div{grid-template-columns:minmax(0,1fr)} }:root{--r-shell:28px;--r-canvas:22px;--r-sheet:16px;--r-tile:12px} @media (max-width:900px){.bleed{margin-inline:0}} .studio2{position:relative;border-radius:var(--r-shell);display:grid;grid-template-columns:318px minmax(0,1fr);min-height:600px;overflow:hidden;background:linear-gradient(112deg,rgba(255,255,255,.74) 0%,rgba(255,255,255,.52) 26%,rgba(255,255,255,.28) 52%,rgba(255,255,255,.14) 100%),radial-gradient(60% 80% at 4% 0%,rgba(0,51,161,.10),transparent 70%),radial-gradient(52% 66% at 100% 100%,rgba(204,39,176,.09),transparent 72%);backdrop-filter:blur(30px) saturate(180%);-webkit-backdrop-filter:blur(30px) saturate(180%);box-shadow:var(--lift-2),inset 0 1px 0 rgba(255,255,255,.95)}:root[data-theme="dark"] .studio2,:root:not([data-theme="light"]) .studio2{} @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .studio2{background:linear-gradient(112deg,rgba(150,180,230,.10) 0%,rgba(150,180,230,.07) 30%,rgba(150,180,230,.05) 60%,rgba(150,180,230,.03) 100%),radial-gradient(60% 80% at 4% 0%,rgba(76,127,232,.20),transparent 70%),radial-gradient(52% 66% at 100% 100%,rgba(232,132,214,.14),transparent 72%);box-shadow:var(--lift-2),inset 0 1px 0 rgba(214,232,255,.10)} }:root[data-theme="dark"] .studio2{background:linear-gradient(112deg,rgba(150,180,230,.10) 0%,rgba(150,180,230,.07) 30%,rgba(150,180,230,.05) 60%,rgba(150,180,230,.03) 100%),radial-gradient(60% 80% at 4% 0%,rgba(76,127,232,.20),transparent 70%),radial-gradient(52% 66% at 100% 100%,rgba(232,132,214,.14),transparent 72%);box-shadow:var(--lift-2),inset 0 1px 0 rgba(214,232,255,.10)} .chat2{display:flex;flex-direction:column;padding:22px 6px 18px 22px;min-width:0;position:relative} .t-ai{display:flex;flex-direction:column;gap:5px} @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .chat2 .cmp{background:rgba(150,180,230,.07);box-shadow:inset 0 1px 0 rgba(214,232,255,.10),0 2px 9px -5px rgba(2,6,14,.52)}}:root[data-theme="dark"] .chat2 .cmp{background:rgba(150,180,230,.07);box-shadow:inset 0 1px 0 rgba(214,232,255,.10),0 2px 9px -5px rgba(2,6,14,.52)} .seam{position:absolute;top:0;bottom:0;right:-1px;width:56px;pointer-events:none;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.22))} @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .seam{background:linear-gradient(90deg,rgba(150,180,230,0),rgba(150,180,230,.05))}}:root[data-theme="dark"] .seam{background:linear-gradient(90deg,rgba(150,180,230,0),rgba(150,180,230,.05))} .canv{margin:14px 14px 14px 0;border-radius:var(--r-canvas);display:flex;flex-direction:column;min-width:0;overflow:hidden;background:var(--glass-solid);box-shadow:var(--lift-2),inset 0 1px 0 rgba(255,255,255,.95)} @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .canv{box-shadow:var(--lift-2),inset 0 1px 0 rgba(214,232,255,.10)}}:root[data-theme="dark"] .canv{box-shadow:var(--lift-2),inset 0 1px 0 rgba(214,232,255,.10)} .canv .bar2{padding:13px 18px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;box-shadow:inset 0 -1px 0 var(--hair)} .canv .bar2 .ttl2{font-size:14px;font-weight:600;letter-spacing:-.008em;margin-right:auto} .canv .gen2{display:flex;align-items:center;gap:11px;padding:10px 18px;box-shadow:inset 0 -1px 0 var(--hair);background:linear-gradient(90deg,rgba(0,51,161,.07),rgba(0,113,206,.04) 55%,rgba(204,39,176,.05))} .canv .gen2 span{font-size:12.5px;color:var(--ink-2)} .canv .gen2 .dot3{width:7px;height:7px;border-radius:50%;background:var(--sp-blue);flex:none} .canv .body3{flex:1;display:grid;grid-template-columns:66px minmax(0,1fr) 50px;min-height:0} .thumbs2{padding:16px 9px;display:flex;flex-direction:column;gap:9px;align-items:center;box-shadow:inset -1px 0 0 var(--hair)} .thumbs2 .th2{width:46px;height:32px;border-radius:8px;background:var(--inner);display:grid;place-items:center;cursor:pointer;font-family:"IBM Plex Mono",monospace;font-size:9.5px;font-weight:600;color:var(--ink-3)} .thumbs2 .th2.on{background:rgba(0,113,206,.12);box-shadow:0 0 0 2px var(--sp-blue);color:var(--sp-blue)} .vrail2{padding:16px 7px;display:flex;flex-direction:column;align-items:center;box-shadow:inset 1px 0 0 var(--hair)} .vrail2 .v2{width:30px;padding:7px 0;text-align:center;font-family:"IBM Plex Mono",monospace;font-size:9.5px;font-weight:600;color:var(--ink-3);border-radius:8px;cursor:pointer} .vrail2 .v2.on{background:rgba(0,113,206,.12);color:var(--sp-blue)} .vrail2 .tk{width:1px;height:13px;background:var(--hair-2)} .paper2{padding:26px 22px;display:flex;justify-content:center;align-items:flex-start;min-width:0;overflow:hidden} @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .sheet2{background:linear-gradient(170deg,rgba(76,127,232,.14),rgba(0,0,0,0) 44%),var(--glass-solid);box-shadow:0 1px 2px rgba(2,6,14,.34),0 20px 48px -24px rgba(2,6,14,.62),inset 0 1px 0 rgba(214,232,255,.10)}}:root[data-theme="dark"] .sheet2{background:linear-gradient(170deg,rgba(76,127,232,.14),rgba(0,0,0,0) 44%),var(--glass-solid);box-shadow:0 1px 2px rgba(2,6,14,.34),0 20px 48px -24px rgba(2,6,14,.62),inset 0 1px 0 rgba(214,232,255,.10)} .kpi2.upd{box-shadow:0 0 0 2px rgba(0,113,206,.30);background:rgba(0,113,206,.07);position:relative} .kpi2.upd::after{content:"updated";position:absolute;top:-8px;right:9px;font-family:"IBM Plex Mono",monospace;font-size:8.5px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:#fff;background:var(--sp-blue);padding:2px 6px;border-radius:5px} .assump{border-radius:var(--r-tile);padding:13px 15px;background:var(--inner);font-size:12px;color:var(--ink-3);line-height:1.55} .rscale{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px} .rscale div{background:var(--inner);padding:14px;display:flex;flex-direction:column;gap:5px} .rscale .s1{border-radius:28px} .rscale .s2{border-radius:22px} .rscale .s3{border-radius:16px} .rscale .s4{border-radius:12px} .rscale .s5{border-radius:10px} .rscale b{font-size:13.5px;font-weight:600} .rscale code{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--sp-blue)} .rscale span{font-size:12px;color:var(--ink-3);line-height:1.45} @media (max-width:860px){.studio2{grid-template-columns:minmax(0,1fr);min-height:0;border-radius:var(--r-canvas)} .chat2{padding:18px} .seam{display:none} .canv{margin:0 14px 14px} .canv .body3{grid-template-columns:minmax(0,1fr)} .thumbs2{flex-direction:row;box-shadow:inset 0 -1px 0 var(--hair);overflow-x:auto} .vrail2{flex-direction:row;box-shadow:inset 0 1px 0 var(--hair);overflow-x:auto} .paper2{padding:16px 12px} .sheet2{padding:20px} } @media (max-width:620px){.sheet2 .kpis2{grid-template-columns:minmax(0,1fr)} .kpi2.upd::after{right:auto;left:12px} } @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .convo,:root:not([data-theme="light"]) .scene,:root:not([data-theme="light"]) .canvas,:root:not([data-theme="light"]) .tabpanel,:root:not([data-theme="light"]) .kb .kc{background:var(--glass-solid);backdrop-filter:none;-webkit-backdrop-filter:none} }:root[data-theme="dark"] .convo,:root[data-theme="dark"] .scene,:root[data-theme="dark"] .canvas,:root[data-theme="dark"] .tabpanel,:root[data-theme="dark"] .kb .kc{background:var(--glass-solid);backdrop-filter:none;-webkit-backdrop-filter:none} .themesw{display:flex;align-items:center;gap:10px;flex-wrap:wrap} .kb{display:grid;grid-template-columns:repeat(auto-fit,minmax(218px,1fr));gap:12px} .kb .col{background:var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);border-radius:var(--r);box-shadow:var(--lift-1),var(--edge);padding:12px;display:flex;flex-direction:column;gap:9px} .kb .ch{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:0 2px} .kb .ch .micro{color:var(--ink-3)} .kb .ct{font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;color:var(--ink-3);background:var(--inner);border-radius:var(--r-sm);padding:2px 7px;font-variant-numeric:tabular-nums} .kb .kc{background:var(--glass-3);border-radius:var(--r-sm);padding:11px 12px;display:flex;flex-direction:column;gap:8px;box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.05)} .kb .kc b{font-size:13.5px;font-weight:600;letter-spacing:-.006em;line-height:1.4} .kb .kc .kid{font-family:"IBM Plex Mono",monospace;font-size:10px;color:var(--ink-3);letter-spacing:.06em} .kb .kc .kf{display:flex;align-items:center;justify-content:space-between;gap:8px} .kb .dz{border-radius:var(--r-sm);min-height:54px;background:var(--inner);outline:1.5px dashed var(--hair-2);outline-offset:-2px;display:grid;place-items:center;font-size:12.5px;color:var(--ink-3)} .kb .col.wip .ct{background:var(--st-attention-t);color:var(--st-attention)} .cal{background:var(--glass-solid);border-radius:var(--r);box-shadow:var(--lift-1),var(--edge);padding:16px;display:flex;flex-direction:column;gap:12px} .cal .chd{display:flex;align-items:center;justify-content:space-between;gap:10px} .cal .chd b{font-size:14px;font-weight:600} .cal .grid7{display:grid;grid-template-columns:repeat(7,1fr);gap:3px} .cal .dow{font-family:"IBM Plex Mono",monospace;font-size:9.5px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3);text-align:center;padding:4px 0} .cal .d{aspect-ratio:1;border-radius:var(--r-sm);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:13px;color:var(--ink-2);font-variant-numeric:tabular-nums;cursor:pointer;transition:background var(--ease)} .cal .d:hover{background:var(--inner)} .cal .d.out{color:var(--ink-mute);cursor:default} .cal .d.out:hover{background:transparent} .cal .d.today{box-shadow:inset 0 0 0 1.5px var(--sp-blue);color:var(--ink);font-weight:600} .cal .d.sel{background:linear-gradient(180deg,#0071CE,#005DB4 60%,#0035A6);color:#fff;font-weight:600;box-shadow:inset 0 1px 0 rgba(255,255,255,.26)} .cal .d.sel .evd{background:#fff} .cal .evd{width:4px;height:4px;border-radius:50%;background:var(--sp-blue)} .cal .d.busy .evd{background:var(--st-attention)} .agenda{display:flex;flex-direction:column;gap:1px;border-radius:var(--r);overflow:hidden;background:var(--hair)} .agenda .ar{display:grid;grid-template-columns:76px minmax(0,1fr) auto;gap:12px;align-items:center;background:var(--glass-solid);padding:12px 14px} .agenda .at{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink-3);letter-spacing:.05em;font-variant-numeric:tabular-nums} .agenda .an{display:flex;flex-direction:column;gap:2px;min-width:0} .agenda .an b{font-size:13.5px;font-weight:600;letter-spacing:-.006em} .agenda .an span{font-size:12.5px;color:var(--ink-3)} .slots{display:grid;grid-template-columns:repeat(auto-fit,minmax(92px,1fr));gap:8px} .slot{font-family:inherit;font-size:13px;font-weight:500;border:0;border-radius:var(--r-pill);padding:9px 12px;cursor:pointer;background:var(--glass-2);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);color:var(--ink-2);box-shadow:var(--edge),0 1px 2px rgba(6,22,54,.04);font-variant-numeric:tabular-nums} .slot[aria-pressed="true"]{background:linear-gradient(180deg,#0071CE,#005DB4 60%,#0035A6);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.26)} .slot:disabled{background:var(--inner);color:var(--ink-mute);box-shadow:none;cursor:not-allowed;text-decoration:line-through} .pc{display:flex;gap:13px;align-items:flex-start;padding:15px 16px;border-radius:var(--r);background:var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .pc .av{width:40px;height:40px;font-size:13.5px} .pc .pb{display:flex;flex-direction:column;gap:5px;min-width:0;flex:1} .pc .pn{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap} .pc .pn b{font-size:14.5px;font-weight:600;letter-spacing:-.008em} .pc .pn span{font-size:12.5px;color:var(--ink-3)} .pc .pm{display:flex;flex-direction:column;gap:3px} .pc .pm div{display:flex;gap:8px;align-items:center;font-size:12.5px;color:var(--ink-2)} .pc .pm .k{font-family:"IBM Plex Mono",monospace;font-size:9.5px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3);min-width:56px} .pc .pa{display:flex;gap:7px;flex-wrap:wrap;padding-top:2px} .faces{display:inline-flex;align-items:center} .faces .av{width:26px;height:26px;font-size:10px;box-shadow:inset 0 1px 0 rgba(255,255,255,.22),0 0 0 2px var(--glass-solid)} .faces .av + .av{margin-left:-6px} .faces .more{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;margin-left:-6px;background:var(--inner);color:var(--ink-2);font-family:"IBM Plex Mono",monospace;font-size:9.5px;font-weight:600;box-shadow:0 0 0 2px var(--glass-solid)} .feed{display:flex;flex-direction:column} .feed .fi{display:grid;grid-template-columns:22px minmax(0,1fr);gap:0 13px;position:relative;padding-bottom:15px} .feed .fi:last-child{padding-bottom:0} .feed .fi::before{content:"";position:absolute;left:10.5px;top:22px;bottom:0;width:2px;background:var(--hair-2)} .feed .fi:last-child::before{display:none} .feed .fd{width:22px;height:22px;border-radius:50%;display:grid;place-items:center;z-index:1;background:var(--glass-3);box-shadow:var(--edge),inset 0 0 0 1px var(--hair-2);color:var(--ink-3)} .feed .fd svg{width:11px;height:11px} .feed .fd.pos{background:var(--st-positive-t);color:var(--st-positive);box-shadow:none} .feed .fd.att{background:var(--st-attention-t);color:var(--st-attention);box-shadow:none} .feed .fd.neg{background:var(--st-negative-t);color:var(--st-negative);box-shadow:none} .feed .fb{display:flex;flex-direction:column;gap:4px;padding-top:1px;min-width:0} .feed .fh{display:flex;gap:9px;align-items:baseline;flex-wrap:wrap} .feed .fh b{font-size:13.5px;font-weight:600;letter-spacing:-.006em} .feed .fh span{font-size:13.5px;color:var(--ink-2)} .feed .fw{font-family:"IBM Plex Mono",monospace;font-size:10px;color:var(--ink-3);letter-spacing:.05em;margin-left:auto} .feed .fp{font-size:12.5px;color:var(--ink-3);line-height:1.5} .pg{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-top:13px} .pg .rng{font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-variant-numeric:tabular-nums} .pg .pgs{display:flex;gap:4px;align-items:center} .pgb{font-family:inherit;font-size:13px;font-weight:600;border:0;cursor:pointer;min-width:30px;height:30px;border-radius:var(--r-sm);background:transparent;color:var(--ink-2);font-variant-numeric:tabular-nums;transition:background var(--ease),color var(--ease)} .pgb:hover:not(:disabled){background:var(--inner);color:var(--ink)} .pgb[aria-current="page"]{background:var(--glass-3);color:var(--ink);box-shadow:var(--edge),0 1px 3px rgba(6,22,54,.10)} .pgb:disabled{color:var(--ink-mute);cursor:not-allowed} .pg .gap{color:var(--ink-mute);padding:0 2px;font-size:13px} .chart{border-radius:var(--r);padding:18px 20px 16px;display:flex;flex-direction:column;gap:14px;background:var(--glass-1);backdrop-filter:var(--blur-1);-webkit-backdrop-filter:var(--blur-1);box-shadow:var(--lift-1),var(--edge)} .chart .chh{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;flex-wrap:wrap} .chart .cht{display:flex;flex-direction:column;gap:3px} .chart .cht b{font-size:14px;font-weight:600;letter-spacing:-.008em} .chart .cht .unit{font-family:"IBM Plex Mono",monospace;font-size:9.5px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3)} .chart .plot{position:relative} .chart svg{display:block;width:100%;height:auto;overflow:visible} .chart .ax{font-family:"IBM Plex Mono",monospace;font-size:9.5px;fill:var(--ink-3);letter-spacing:.04em} .chart .gl{stroke:var(--hair);stroke-width:1} .chart .nodata{border-radius:var(--r-sm);background:var(--inner);padding:26px 18px;display:flex;flex-direction:column;gap:6px;align-items:center;text-align:center} .chart .nodata b{font-size:13.5px;font-weight:600} .chart .nodata span{font-size:12.5px;color:var(--ink-3)} .spark{display:inline-block;vertical-align:-2px;width:74px;height:18px} .delta{font-family:"IBM Plex Mono",monospace;font-size:11px;font-weight:600;font-variant-numeric:tabular-nums} .delta.up{color:var(--st-positive)} .delta.dn{color:var(--st-negative)} @media (max-width:640px){.agenda .ar{grid-template-columns:64px minmax(0,1fr)} .agenda .ar >:last-child{grid-column:1/-1} } @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .tile:not(.flag){background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,0)),var(--glass-1)}} :root[data-theme="dark"] .tile:not(.flag){background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,0)),var(--glass-1)} .sheet2{width:100%;max-width:680px;border-radius:var(--r-sheet);padding:28px 30px;display:flex;flex-direction:column;gap:14px;background:var(--glass-solid);box-shadow:var(--lift-1),var(--edge)} .kpis2{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px} .kpi2{border-radius:var(--r-tile);background:var(--inner);padding:12px 14px;display:flex;flex-direction:column;gap:4px;min-width:0} .chat2 .cmp{display:flex;align-items:center;gap:10px;margin-top:auto;padding:12px 14px;border-radius:var(--r-tile);background:rgba(255,255,255,.62);box-shadow:inset 0 1px 0 rgba(255,255,255,.95),0 2px 9px -5px rgba(6,22,54,.18)} .chat2 .cmp input{border:0;background:transparent;font-family:inherit;font-size:14.5px;color:var(--ink);width:100%;min-width:0;outline:none} .grid > *{min-width:0} .field input,.ctl input,.ctl select{min-width:0;text-overflow:ellipsis} img,video{max-width:100%} p,li{overflow-wrap:break-word} .tag,.chipsel,.slot{white-space:nowrap}
```

### The expression kit — paste after the stylesheet, in the same `<style>` block

```css
:root{--s-1:4px;--s-2:8px;--s-3:12px;--s-4:16px;--s-5:20px;--s-6:24px;--s-8:32px;--s-10:40px;--s-12:48px;--page-pad:24px;--section-gap:24px;--card-pad:20px;--ov-s:420px;--ov-m:560px;--ov-l:760px;--ov-pad:24px;--row-h:44px;--cell-px:14px;--cell-py:10px;--content-max:1440px} [data-density="compact"]{--row-h:36px;--cell-px:12px;--cell-py:7px;--card-pad:16px;--section-gap:20px} [data-density="comfortable"]{--row-h:52px;--cell-px:16px;--cell-py:14px;--card-pad:24px} @media (max-width:760px){:root{--page-pad:16px;--section-gap:16px;--card-pad:16px;--ov-pad:16px}} :root{--rail-w:248px;--rail-deep:#0033A1;--rail-deep-2:#00226E;--rail-ground:var(--rail-deep);--rail-bg:linear-gradient(180deg,var(--rail-deep) 0%,var(--rail-deep-2) 100%);--rail-ink:#fff;--rail-ink-2:rgba(255,255,255,.78);--rail-hover:rgba(255,255,255,.08);--rail-active-bg:rgba(255,255,255,.16);--rail-active-ink:#fff;--rail-indicator:transparent;--signal:var(--sp-blue);--on-signal:#fff;--paper:var(--base)} @media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--rail-deep:#1B3576;--rail-deep-2:#0E1D45}} :root[data-theme="dark"]{--rail-deep:#1B3576;--rail-deep-2:#0E1D45} [data-chrome="ink"]{--rail-ground:#0B0C0E;--rail-bg:linear-gradient(180deg,#0B0C0E 0%,#17181C 100%);--rail-ink:#F4F5F7;--rail-ink-2:rgba(244,245,247,.74);--rail-hover:rgba(255,255,255,.06);--rail-active-bg:rgba(255,255,255,.09);--rail-active-ink:#fff;--rail-indicator:var(--signal)} [data-chrome="light"]{--rail-ground:var(--base);--rail-bg:linear-gradient(var(--glass-solid),var(--glass-solid));--rail-ink:var(--ink);--rail-ink-2:var(--ink-2);--rail-hover:var(--inner);--rail-active-bg:var(--inner);--rail-active-ink:var(--ink);--rail-indicator:var(--sp-blue)} [data-surface="solid"],[data-surface="paper"]{--glass-1:var(--glass-solid);--glass-2:var(--glass-solid);--glass-3:var(--glass-solid);--blur-1:none;--blur-2:none} [data-surface="solid"] .amb.a,[data-surface="solid"] .amb.b{opacity:.5} [data-surface="paper"] .amb{display:none} [data-surface="paper"] body{background:var(--paper)} .display,.title{font-family:var(--font-display,inherit)} .app{display:grid;grid-template-columns:var(--rail-w) minmax(0,1fr);min-height:var(--app-h,100vh);position:relative;z-index:1} .app.with-agent{grid-template-columns:var(--rail-w) minmax(0,1fr) var(--ov-s)} .app-rail{position:sticky;top:0;height:var(--app-h,100vh);overflow-y:auto;display:flex;flex-direction:column;gap:4px;padding:20px 14px;background-color:var(--rail-ground);background-image:var(--rail-bg);color:var(--rail-ink);z-index:21} .app-rail .brand{padding:4px 10px 18px} .nav-i{position:relative;display:flex;align-items:center;gap:10px;min-height:38px;padding:8px 12px;border-radius:var(--r);color:var(--rail-ink-2);font-size:14px;font-weight:500;text-decoration:none;transition:background var(--ease),color var(--ease)} .nav-i svg{width:18px;height:18px;flex:none} .nav-i:hover{background:var(--rail-hover);color:var(--rail-active-ink)} .nav-i[aria-current="page"]{background:var(--rail-active-bg);color:var(--rail-active-ink);font-weight:600} .nav-i[aria-current="page"]::before{content:"";position:absolute;left:-14px;top:8px;bottom:8px;width:3px;border-radius:0 3px 3px 0;background:var(--rail-indicator)} .nav-i:focus-visible{outline:2px solid var(--rail-active-ink);outline-offset:2px} .app-rail .prof{margin-top:auto} .app-main{min-width:0;display:flex;flex-direction:column} .app-top{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:12px;min-height:56px;padding:10px 24px;background-color:var(--base);background-image:linear-gradient(var(--glass-solid),var(--glass-solid));box-shadow:inset 0 -1px 0 var(--hair);transition:box-shadow var(--ease)} .app-top.scrolled{box-shadow:inset 0 -1px 0 var(--hair),0 8px 18px -14px rgba(6,22,54,.30)} .app-body{padding:var(--page-pad);display:flex;flex-direction:column;gap:var(--section-gap);min-width:0;width:100%;max-width:var(--content-max)} .app[data-shell="top"]{grid-template-columns:minmax(0,1fr);grid-template-rows:auto 1fr} .app[data-shell="top"] .app-rail{height:auto;flex-direction:row;align-items:center;gap:6px;padding:10px 20px;overflow-x:auto} .app[data-shell="top"] .app-rail .brand{padding:0 14px 0 0} .app[data-shell="top"] .app-rail .prof{margin:0 0 0 auto} .app[data-shell="top"] .nav-i[aria-current="page"]::before{left:12px;right:12px;top:auto;bottom:-10px;width:auto;height:3px;border-radius:3px 3px 0 0} .app[data-shell="top"] .app-top{top:0} .app-tabs{display:none} @media (max-width:1100px){.app:not([data-shell="top"]){--rail-w:72px} .app:not([data-shell="top"]) .app-rail .lbl,.app:not([data-shell="top"]) .app-rail .brand .word{display:none} } @media (max-width:760px){.app,.app.with-agent{grid-template-columns:minmax(0,1fr)} .app .app-rail{display:none} .app-body{padding-bottom:88px} .app .app-tabs{position:fixed;left:0;right:0;bottom:0;z-index:30;display:flex;justify-content:space-around;padding:6px 6px calc(6px + env(safe-area-inset-bottom));background-color:var(--base);background-image:linear-gradient(var(--glass-solid),var(--glass-solid));box-shadow:inset 0 1px 0 var(--hair)} .app .app-tabs a{flex:1;min-height:52px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:11.5px;font-weight:600;color:var(--ink-3);text-decoration:none;border-radius:var(--r)} .app .app-tabs a[aria-current="page"]{color:var(--ink);background:var(--inner)} .agent-launch{right:16px;bottom:calc(76px + env(safe-area-inset-bottom))} } .agent-launch{position:fixed;right:24px;bottom:24px;z-index:40;width:52px;height:52px;border:0;border-radius:50%;display:grid;place-items:center;cursor:pointer;color:#fff;background:linear-gradient(180deg,#0071CE,#005DB4 60%,#0035A6);box-shadow:0 10px 24px -10px rgba(0,63,168,.70),inset 0 1px 0 rgba(255,255,255,.28)} .agent-launch:focus-visible{outline:2px solid var(--sp-blue);outline-offset:3px} .agent-drawer{position:fixed;top:0;right:0;bottom:0;z-index:50;width:min(var(--ov-s),100vw);display:flex;flex-direction:column;background-color:var(--base);background-image:linear-gradient(var(--glass-solid),var(--glass-solid));box-shadow:var(--lift-2),inset 1px 0 0 var(--hair);transform:translateX(100%);visibility:hidden;transition:transform var(--ease),visibility 0s linear 160ms} .agent-drawer[data-open]{transform:none;visibility:visible;transition:transform var(--ease)} .agent-drawer.wide{width:min(var(--ov-l),100vw)} .agent-drawer[data-open] ~ .agent-launch,.app.with-agent .agent-launch{display:none} .agent-drawer.docked{position:sticky;top:0;height:var(--app-h,100vh);width:auto;transform:none;visibility:visible;box-shadow:inset 1px 0 0 var(--hair);z-index:19} .ad-hd{display:flex;align-items:center;gap:10px;padding:14px 16px;box-shadow:inset 0 -1px 0 var(--hair)} .ad-hd .ad-name{font-size:15px;font-weight:600;letter-spacing:-.008em} .ad-hd .ad-tools{margin-left:auto;display:flex;gap:4px} .ad-ctx{display:flex;gap:8px;flex-wrap:wrap;padding:10px 16px 0} .ad-thread{flex:1;min-height:0;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:14px} .ad-thread .msg{max-width:92%} .ad-dock{padding:12px 14px calc(12px + env(safe-area-inset-bottom));display:flex;flex-direction:column;gap:10px;box-shadow:inset 0 1px 0 var(--hair)} .ad-composer{display:flex;align-items:center;gap:11px;padding:12px 15px;border-radius:var(--r);background:var(--base);box-shadow:inset 0 0 0 1px var(--hair-2)} .ad-composer:focus-within{box-shadow:inset 0 0 0 1px var(--hair-2),0 0 0 3px rgba(0,113,206,.18)} .ad-composer input,.ad-composer textarea{border:0;background:transparent;font-family:inherit;font-size:15px;color:var(--ink);width:100%;outline:none;resize:none} .ad-dock .chips{justify-content:flex-start} .ad-dock .chips button{background:var(--inner);box-shadow:none} .ad-out{border-radius:var(--r);background:var(--inner);padding:12px 14px;display:flex;flex-direction:column;gap:10px} .ad-action{border-radius:var(--r);background:var(--inner);padding:14px;display:flex;flex-direction:column;gap:12px} .ad-diff{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:8px} .ad-diff > div{border-radius:var(--r-sm);background:var(--glass-solid);padding:10px 12px;display:flex;flex-direction:column;gap:4px} .ad-diff .was{color:var(--ink-3)} .ad-diff .now b{color:var(--ink)} @media (prefers-reduced-motion:reduce){.agent-drawer{transition:none}}
 .frame{position:relative;transform:translateZ(0);overflow:hidden;height:var(--frame-h,720px);--app-h:var(--frame-h,720px);border-radius:var(--r);background:var(--base);box-shadow:var(--lift-2),var(--edge)} .frame > .frame-scroll{height:100%;overflow:auto;overscroll-behavior:contain} .frame .amb{position:absolute} .device-frame{display:block;border:0;border-radius:var(--r-shell);background:var(--base);box-shadow:var(--lift-2),var(--edge);max-width:100%} .device-frame.phone{width:390px;height:800px} .device-frame.tablet{width:820px;height:1000px} .devices{display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start} .scrim{position:fixed;inset:0;z-index:55;background:rgba(6,14,30,.38)} :root[data-theme="dark"] .scrim{background:rgba(0,0,0,.55)} .modal,.drawer{position:fixed;z-index:60;display:flex;flex-direction:column;background-color:var(--base);background-image:linear-gradient(var(--glass-solid),var(--glass-solid));box-shadow:var(--lift-2),var(--edge)} .modal{left:50%;top:50%;transform:translate(-50%,-50%);width:min(var(--ov-m),calc(100vw - 32px));max-height:calc(100% - 64px);border-radius:var(--r-sheet,16px)} .modal.s{width:min(var(--ov-s),calc(100vw - 32px))} .modal.l{width:min(var(--ov-l),calc(100vw - 32px))} .drawer{top:0;right:0;bottom:0;width:min(var(--ov-m),100vw)} .drawer.s{width:min(var(--ov-s),100vw)} .drawer.l{width:min(var(--ov-l),100vw)} .ov-hd{display:flex;align-items:flex-start;gap:var(--s-3);padding:var(--ov-pad) var(--ov-pad) var(--s-4)} .ov-hd .ov-t{font-size:18px;font-weight:600;letter-spacing:-.01em} .ov-hd .ov-sub{font-size:13.5px;color:var(--ink-3);margin-top:2px} .ov-hd .ov-x{margin-left:auto} .ov-bd{flex:1;min-height:0;overflow-y:auto;padding:0 var(--ov-pad) var(--ov-pad);display:flex;flex-direction:column;gap:var(--s-4)} .ov-ft{display:flex;justify-content:flex-end;gap:var(--s-2);padding:var(--s-4) var(--ov-pad);box-shadow:inset 0 1px 0 var(--hair)} .ov-ft .lead{margin-right:auto} @media (max-width:760px){.modal{left:0;right:0;top:auto;bottom:0;transform:none;width:100vw;max-height:88%;border-radius:var(--r-sheet,16px) var(--r-sheet,16px) 0 0} .drawer,.drawer.s,.drawer.l{width:100vw}} .tbl td,.tbl th{padding:var(--cell-py) var(--cell-px)} .tbl tbody tr{height:var(--row-h)} .tbl .cl{display:block;max-width:var(--col-w,260px);overflow:hidden;text-overflow:ellipsis;white-space:nowrap} .tbl .cl2{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;max-width:var(--col-w,320px)} .tbl .cell-chips{display:flex;gap:var(--s-1);flex-wrap:nowrap;align-items:center;white-space:nowrap} .tbl .more{font-size:12px;font-weight:600;color:var(--ink-3)} .tblwrap.freeze .tbl th:first-child,.tblwrap.freeze .tbl td:first-child{position:sticky;left:0;z-index:1;background-color:var(--base);background-image:linear-gradient(var(--glass-solid),var(--glass-solid))} .row-x td{padding-top:0} .row-x .xp{border-radius:var(--r);background:var(--inner);padding:var(--s-4);display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:var(--s-4)} .dl{display:grid;grid-template-columns:minmax(120px,160px) minmax(0,1fr);gap:var(--s-2) var(--s-6);align-items:baseline} .dl dt{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)} .dl dd{margin:0;min-width:0} .cv{display:flex;flex-direction:column;gap:var(--s-3)} .cv-tag{font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;letter-spacing:.08em;color:var(--ink-3)} .device-wrap{position:relative;width:100%;overflow:hidden;border-radius:var(--r);box-shadow:var(--lift-2),var(--edge);background:var(--base)} .device-wrap > iframe{position:absolute;top:0;left:0;border:0;transform-origin:0 0;background:var(--base)} @media (max-width:1439px){.app.with-agent{grid-template-columns:var(--rail-w) minmax(0,1fr)} .agent-drawer.docked{position:fixed;top:0;right:0;bottom:0;height:auto;width:min(var(--ov-s),100vw);box-shadow:var(--lift-2),inset 1px 0 0 var(--hair);z-index:50}}
```

**What the kit fixes, from the four runs:**

- **The rail runs the full height, always.** `.app-rail` is sticky at `height:100vh` inside a grid, so
  it never stops halfway down a long page (Pentland's rail ended at 750 px).
- **The top bar is opaque.** `.app-top` paints the solid rung over the page ground, so content never
  slides visibly under it and collides with the title (Pentland). Add `.scrolled` once the page has
  scrolled, for the shadow.
- **The agent is a drawer.** `.agent-drawer` slides in from the right over the page (the default),
  widens with `.wide` for charts and tables, or sits in the layout as a third column with `.docked`
  inside `.app.with-agent`. It is opaque, so text on it measures against one ground. On a phone it
  fills the screen.
- **Phone and tablet are part of the shell.** Under 1,100 px the rail collapses to icons (labels in
  `.lbl`, the wordmark in `.brand .word`); under 760 px it is replaced by `.app-tabs`, a bottom tab bar
  with 52 px targets.
- **In dark, the brand rail stays deep.** `--rail-deep` and `--rail-deep-2` are their own tokens in
  both themes (transformed like every other colour), so the rail does not turn pale when the dark theme
  lightens `--sp-deep`. No `color-mix()` anywhere: in a browser without it the rail rendered
  transparent.
- **Every screen that is drawn is drawn at its real width, in a device** (which screens are drawn
  at all is decided by 0.6 and its budget, not by this rule). Media queries answer the window, not a
  box, so a "1,280 px" screen drawn inside a 1,000 px guide column gets the desktop layout at the wrong
  width: the v5 runs squeezed state screens to one word per line and let a docked Copilot eat the page.
  **Every screen specimen** — desktop, wide, tablet, phone — goes in `<template class="device"
  data-device="desktop|wide|tablet|phone">`. The device script below renders it in an `<iframe>` at its
  true width (1,280, 1,440, 820, 390 px) with the page's own stylesheet, **scales it to fit the guide**,
  sizes desktop screens to their content height (`data-height="700"` fixes a height), and keeps the
  theme, chrome, surface, density and style set in sync. `.frame` remains only for a component shown
  without its screen.
- **Overlays share one system.** Modals (`.modal`, sizes `.s` 420 / default 560 / `.l` 760 px), side
  drawers (`.drawer`, same three sizes, always full height) and the agent drawer (420 px, `.wide` 760 px)
  use the same width tokens (`--ov-s/m/l`), the same anatomy (`.ov-hd` title and one line of support,
  `.ov-bd` scrolling body, `.ov-ft` footer with the primary action last on the right) and the same
  padding (`--ov-pad`, 24 px; 16 px on a phone). A modal never exceeds the screen height minus 64 px;
  its body scrolls. On a phone a modal becomes a bottom sheet and a drawer goes full width. `.scrim`
  dims the page under a modal, never under a drawer the person works beside.
- **The docked agent only docks when there is room.** `.app.with-agent` gives the drawer its own
  column at 1,440 px and wider; below that the same drawer becomes an overlay, so the page is never
  squeezed. The launcher hides while any agent drawer is open (place `.agent-launch` after the drawer).
- **Spacing and density are tokens.** `--s-1…--s-12` (4–48 px) is the only spacing scale; page padding
  `--page-pad`, gaps between sections `--section-gap`, card padding `--card-pad`. `data-density=
  "compact|comfortable"` on `<html>` moves row height (36 / 44 / 52 px), cell padding and card padding
  together; nothing else changes.
- **Table helpers for dense data.** `.cl` (one line with ellipsis, width `--col-w`), `.cl2` (two lines),
  `.cell-chips` with `.more` ("+2"), `.tblwrap.freeze` (first column stays while the table scrolls),
  `.row-x .xp` (an expanded row that holds what does not fit a cell). `.dl` is a definition list with a
  label column of 120–160 px. `.cv` and `.cv-tag` frame a chart view and its code.
- **Chrome is a switch, not a rewrite.** `data-chrome="brand"` (the house gradient rail), `"ink"`
  (near-black chrome with the brand's signal colour as the active indicator — for black-led and
  achromatic brands), `"light"` (the rail on the solid rung, the brand only on the active indicator).
- **Surface is a switch.** `data-surface="glass"` (the house look), `"solid"` (opaque cards, no blur,
  a quieter aurora — for dense tools and clients whose own product is flat), `"paper"` (solid cards on
  the client's own page ground `--paper`, no aurora — for print-like, editorial or very calm brands).

**The device script — paste once, inline, at the end of `<body>`:**

```js
(function(){
  var KEYS=['data-theme','data-chrome','data-surface','data-density','data-style-set'];
  var SIZES={phone:[390,800],tablet:[820,1000],desktop:[1280,800],wide:[1440,900]};
  var head=[].map.call(document.querySelectorAll('style,link[rel="stylesheet"]'),function(n){return n.outerHTML}).join('');
  function rootAttrs(){var h=document.documentElement;return KEYS.filter(function(a){return h.hasAttribute(a)}).map(function(a){return a+'="'+h.getAttribute(a)+'"'}).join(' ')}
  var items=[];
  [].forEach.call(document.querySelectorAll('template.device'),function(t){
    var kind=t.getAttribute('data-device')||'desktop', sz=SIZES[kind]||SIZES.desktop;
    var W=+(t.getAttribute('data-width')||sz[0]), hAttr=t.getAttribute('data-height')||((kind==='phone'||kind==='tablet')?String(sz[1]):'auto');
    var wrap=document.createElement('div'); wrap.className='device-wrap '+kind;
    if(kind==='phone'||kind==='tablet'){wrap.style.maxWidth=W+'px';wrap.style.borderRadius='var(--r-shell)'}
    var f=document.createElement('iframe'); f.title=t.getAttribute('data-title')||(kind+' specimen');
    f.style.width=W+'px'; f.style.height=(hAttr==='auto'?sz[1]:+hAttr)+'px';
    f.srcdoc='<!doctype html><html '+rootAttrs()+'><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+head+'</head><body>'+t.innerHTML+'</body></html>';
    wrap.appendChild(f); t.parentNode.insertBefore(wrap,t.nextSibling);
    var it={t:t,wrap:wrap,f:f,W:W,auto:hAttr==='auto'}; items.push(it);
    f.addEventListener('load',function(){sync();fit(it);var d=f.contentDocument;if(d&&d.fonts)d.fonts.ready.then(function(){fit(it)});setTimeout(function(){fit(it)},400)});
  });
  function fit(it){
    var d=it.f.contentDocument;
    if(it.auto&&d&&d.documentElement){it.f.style.height='0px';var h=Math.min(Math.max(d.documentElement.scrollHeight,480),2600);it.f.style.height=h+'px'}
    var s=Math.min(1,it.wrap.clientWidth/it.W);
    it.f.style.transform='scale('+s+')';
    it.wrap.style.height=(parseFloat(it.f.style.height)*s)+'px';
  }
  function sync(){var h=document.documentElement;items.forEach(function(it){var d=it.f.contentDocument;if(!d||!d.documentElement)return;KEYS.forEach(function(a){if(h.hasAttribute(a))d.documentElement.setAttribute(a,h.getAttribute(a));else d.documentElement.removeAttribute(a)})})}
  new MutationObserver(function(){sync();items.forEach(fit)}).observe(document.documentElement,{attributes:true,attributeFilter:KEYS});
  if(window.ResizeObserver){var ro=new ResizeObserver(function(){items.forEach(fit)});items.forEach(function(it){ro.observe(it.wrap)})}
  else window.addEventListener('resize',function(){items.forEach(fit)});
})();
```

**Every colour in the kit is transformed with the core** in Step 3, and its ratios are measured in
Step 6 like everything else. The kit's literal blues follow the brand; the ink chrome's near-blacks are
near-neutral and barely move.

**Fonts as shipped:** Archivo 400/500/600 and IBM Plex Mono 400/500/600, both from Google Fonts and both openly licensed. **Archivo is the DEFAULT body face, not a fixed one — Step 2b decides whether it is replaced by the client's.** IBM Plex Mono stays. **If the mono is not
actually embedded, table headers fall back silently and the whole grid loses its register.**

⚠️ **Two token groups are declared as BARE triples** — `--aur-a` / `--aur-b` / `--aur-c`, consumed
as `rgba(var(--aur-a),a)`. **There is no `rgb(` to match, so a find-and-replace over hexes and
`rgba(...)` will skip them and leave the ambient field on the previous brand.** At 5% opacity that
does not look broken, it just casts the whole page in the wrong hue. Their hex equivalents are
`#0033A1` / `#0071CE` / `#CC27B0` in light and `#4C7FE8` / `#6BB3EA` / `#E884D6` in dark.

## Step 1 · Sample the brand

**The brand source order — highest first.** It decides every colour conflict; nothing else does.

1. **What the client supplied**: a swatch, the client's own deck or brand cues, a named brand system,
   the brand inputs and §21 hand-off of the scoping document when they come from client material.
2. **The client's published brand guidelines** or brand portal (colour pages, brand kit).
3. **The client's live product interface** — their own app or platform, when it is public.
4. **The client's live marketing site** — the CSS custom properties, the computed button and header
   colours.
5. **Third-party sources** (colour sites, logo libraries) — only ever as the confirming second source.

A source higher in the order wins even when a lower one is used more often. A retired source (a rebrand
dated after it) drops out of the order entirely. Record the order applied in the port note.

**Sample the identity, not only the hue.** A hue rotation alone produced four apps that looked the
same. Record each of these from the sources above; together they feed the expression (Step 2c):

- **Light-to-dark balance.** Is the brand light-led (white grounds, colour as accent), dark-led
  (black or near-black grounds, as on Pentland's deck) or colour-led (large fields of brand colour)?
- **The brand's chromatic role.** One hero colour, a pair, a gradient, or achromatic (black, white,
  grey) with a single accent? **An achromatic brand's "brand colour" is its black**, and its accent is
  the signal colour. Do not promote a link blue from the site into the brand.
- **The accent and where the client uses it** — buttons only, highlights, data, illustration.
- **The neutral ramp** — warm, cool or pure grey; the client's page background.
- **Shape and line** — square or rounded, hairlines or shadows, flat or layered, as their own product
  draws them (this informs the expression only; the core radius scale does not move).
- **Imagery** — product photography, people, illustration, data, none; and its treatment.
- **A motif** — a shape, line, angle or pattern in the logo or brand work that can become one quiet
  graphic element (a chevron, an oval, a stripe).
- **Type voice** — the display face and how loud headings are.

* **On the live site, read the CSS custom properties off `:root`** — not a screenshot. *On
  daikincomfort.com they are literally `--daikin_blue`, `--daikin_orange`, `--daikinGradient`.* Take
  the neutral ramp too. **From brand guidelines, take the digital (screen) palette**; a print primary
  (Pantone, CMYK) is not the screen colour the client means, as the next point shows. **The type stack is its own step — see Step 2b.**
* **🔴 A brand book's print primaries are not necessarily the hue the client means by "our colour".**
  Proofpoint's second attempt used H 196 — the hue of their own 5415 Blue — and was still wrong. The
  answer came as a swatch: *"Its more of sea green and bluish…"*, sampled as `#102F2D` off their live
  site. **When a swatch is available, sample it. Do not reason toward it.**
* **If the CSS cannot be fetched** (blocked, empty, or built by JavaScript), open the site in a browser
  (Claude in Chrome or the built-in browser) and read the values from the rendered page: the `:root`
  custom properties, and the computed colours of the primary button, links, header and nav. Do not
  fall back to a third-party colour site as the only source; use it as the second, confirming source
  in research question 1.
* **Inventory before transforming** — v3.4 carries **54 distinct hexes and 25 `rgb()` triples**.
  Count, transform, diff the count.

## Step 2 · Harvest the logo

**Acquisition, in order. Stop at the first that yields a real file:**

1. **Inline `<svg>` in the site header**, or a linked `.svg` (`/logo.svg`, `/assets/logo*.svg`) —
   always preferred; it scales and recolours cleanly.
2. `<link rel="apple-touch-icon">` — usually 180px, square, the mark alone.
3. `<meta property="og:image">` — usually the lockup, often with padding to crop.
4. `/favicon.svg` or `/favicon.ico`.
5. **The rendered page.** If a direct fetch is blocked, empty or JavaScript-rendered, open the site in
   a browser (Claude in Chrome or the built-in browser, whichever the session has) and take the logo
   from the rendered DOM: the header `<svg>` markup, or the `src` of the header `<img>`, then fetch
   that URL.
6. **The client's other official sources:** press, media or brand-kit page (`/press`, `/media`,
   `/brand`, `/newsroom`), the logo on the client's own docs or support site, and the client's
   app-store icon.
7. **Public logo libraries that hold the official file:** Wikimedia Commons (the file the client's
   Wikipedia article uses), Brandfetch, Simple Icons. Use the file as published; record its URL and
   check it matches the mark on the client's live site.
8. **Ask.** See stop 2 — never trace.

**Work through every step before stop 2.** "Could not be downloaded into this workspace" after one
blocked fetch is not a reason to stop. Record every URL tried and what each returned in the port note,
so a reviewer can see the search was complete.

**Then derive the kit. Seven variants, because a navbar and a favicon are not the same problem:**

| Variant | Where it goes | Min size | Ground |
| --- | --- | --- | --- |
| **Primary lockup** | Login, splash, cover slide, document header | 140px wide | Light page only |
| **Horizontal lockup** | Product header, email signature | 110px wide | Light page or tier-1 glass |
| **Stacked lockup** | Narrow columns, print, square crops | 96px wide | Light page only |
| **Mark only** | Collapsed rail, tab strip, compact header | 24px | Any |
| **Reversed mono** | **The nav rail** — the one branded surface | 24px | Brand gradient |
| **One-colour** | Watermark, single-ink print | 24px | Any |
| **App / favicon** | Tab, bookmark, PWA | 16 · 32 · 180 · 512 | Its own |

**Rules, and they are measured like anything else:**

* **Clear space is half the mark's height on all four sides.** Nothing crosses it, including the
  product name.
* **The mark is measured at ≥ 3:1 against its ground.** It is a graphical object, not text — 3:1 is
  the bar, and it still has to be met, in every variant and both themes.
* **Account and org logos are circles** (given on SailPoint: *"the logo used should be circular"*).
  Crop to a circle; never letterbox a rectangle inside one.
* **🔴 The rail is a gradient, so the logo on it is REVERSED MONO** — not the colour version with a
  white plate or glow behind it. A knocked-out mark on the brand gradient is the single most common
  place a prototype stops looking like the client owns it.
* **Never** recolour the mark outside the approved mono and reversed versions · place the
  full-colour logo on the brand fill · stretch, rotate, outline or shadow it · redraw it.
* **Record provenance** — which URL each file came from. Confirm anything uncertain by fetching it
  again or searching for it yourself; nothing ships with an unverified source.

## Step 2b · Type — research the real face, then decide what you may legally ship

**Two separate questions, and conflating them is the mistake.** *What typeface does the client
actually use?* is research. *May we put that file in our prototype?* is licensing, and the answer is
usually no.

### Identify it — in this order

⚠️ **Fetch the linked STYLESHEET, not the page.** A page fetch returns converted text with no
`@font-face` in it — tried on a live client site and it came back with zero font information while
the site plainly loads webfonts. Read the CSS file the page links to, or use the browser.

1. **`<link>` to `fonts.googleapis.com/css2?family=…`** — names the family outright, and tells you it
   is openly licensed. Best case; you are done.
2. **`@font-face` in the stylesheet** — `font-family` plus a `src: url(….woff2)`. The filename
   usually carries the family name.
3. **The loader domain names the foundry:** `use.typekit.net` / `p.typekit.net` → **Adobe Fonts** ·
   `fast.fonts.net` / `*.fontdeck` / Monotype paths → **Monotype** · `cloud.typography.com` →
   **Hoefler&Co**.
4. **Computed `font-family` on `body` and on a heading** — catches the case where the brand face is
   only used for display and the body is a system stack.
5. **Their brand or press page**, which often names the typeface in words.
6. **Ask.** Do not guess from a screenshot; a wrong guess propagates into every screen.

**Record what you found even when you cannot use it.** The style guide names the real face as what
production should license. That sentence is worth having in front of the client.

### 🔴 The licensing rule — identify the real face, ship an open one

**A webfont licence does not travel to us.** This is not caution, it is what the licences say:

* **Adobe Fonts cannot be self-hosted at all** and cannot be used by a third party — *"Adobe doesn't
  offer the ability to host fonts locally"*, and a client's site *"must load Adobe Fonts through
  their own Creative Cloud subscription"*. An agency cannot carry them into its own build.
* **Monotype webfonts are single-domain and metered** — a licence covers *"a single domain"*, runs on
  *"prepaid pageviews"*, and **agencies "may not share a single webfont license across multiple
  websites"**.
* **Google Fonts are open** (SIL OFL / Apache 2.0) — self-hosting, commercial use and redistribution
  are all permitted. This is why they are the fallback.

**So the rule, and it is not negotiable: never download and redistribute a client's licensed webfont
into our prototype.**

| What you found | What to ship |
| --- | --- |
| A Google Font | **Use it.** Link it or self-host it |
| Any other open face (OFL/Apache on GitHub or a foundry's free tier) | **Use it**, after checking the licence text itself |
| A licensed face — Adobe, Monotype, Hoefler, a bespoke foundry cut | **The closest open substitute**, with the real face named in the style guide |
| A display or script face used only in the logo | **Do not use it for UI at all.** It is a logo face; the body face is a separate question |
| Nothing identifiable | **Keep the system's own faces** and say so |

### Choosing the substitute — match the metrics, not the vibe

Two faces that "look similar" at 48px can wreck a 13px table. **Match, in this order:
x-height ratio · advance width · classification (grotesque / neo-grotesque / geometric / humanist) ·
stroke contrast · terminal style · whether it has tabular numerals**, which the system needs on
every number.

Starting points, **each to be verified by overlaying the two at the same size, never accepted from
this table alone**:

| Client's face | Open starting point |
| --- | --- |
| Helvetica / Helvetica Neue / Neue Haas Grotesk / Arial | **Inter** |
| Graphik, Founders Grotesk, Aktiv Grotesk | **Inter** or **Archivo** |
| Proxima Nova, Brandon, Sofia Pro | **Archivo** or **Figtree** |
| Gotham, Montserrat-adjacent geometrics | **Montserrat** |
| Avenir, Museo Sans, Nunito-adjacent humanists | **Nunito Sans** |
| Futura, Avant Garde | **Jost** |
| Circular, Poppins-adjacent geometrics | **Poppins** |
| DIN, Eurostile | **Barlow** or **Archivo Narrow** |
| Frutiger, Myriad, Univers | **Source Sans 3** |
| Tiempos, Georgia, a transitional serif | **Source Serif 4** |
| Garamond, an old-style serif | **EB Garamond** |

### ⚠️ A font swap invalidates the audit — re-measure

Changing the body face changes x-height and advance width, so it moves **apparent size, line length,
vertical rhythm and every fixed-width layout**. After the swap:

* **Re-run the contrast audit in both themes.** Contrast itself does not move, but perceived weight
  does — a lighter face at `--ink-3` can read thinner than the measured ratio suggests.
* **Re-measure fixed-width layouts.** A wider face is exactly what pushes a six-station rail back out
  of its container.
* **Check the numerals are tabular**, or every number in the system loses its alignment.
* **Check the four type sizes still hold their hierarchy** — a large x-height face makes 13px and
  15px look like the same size.

**🔴 Keep IBM Plex Mono regardless.** The mono is structural, not brand — it carries table headers,
eyebrows, KPI labels, timestamps and citation chips, and its 10.5px table header is a measured value.
Clients almost never have a brand mono, and swapping it changes the grid's register for no gain.
**Swap the body face; keep the mono.**

## Step 2c · Choose the expression — so it looks like this client, and only this client

**Four runs, four clients, one look.** With the logo covered, Pentland, ClickUp, Vermont and Topcon
were the same product in a different hue: the same gradient rail, white bar, glass cards and aurora.
The core is right to stay fixed — its measurements are why the apps worked. What was missing is a
decision about **how this client's product should feel**, taken from evidence and recorded.

**Start with the design concept, then set the dials.**

**The design concept — the one idea that makes this system belong to this client.** Find an object,
material or ritual from the client's own world and let it shape the system: Asian Paints' shade card
and paint chip; an airline's departure board and boarding pass; a fashion brand's lookbook and swatch
card; a lab's sample tray; a bank's statement. Choose it from what the scoping document, the client's
site and the research show the client's people actually handle every day, never from a generic
metaphor. Write it on the expression card in one line with its evidence, then let it drive:

- **the signature components (0.8)** — their form borrows from the concept (a dealer score shown as a
  paint chip whose shade fills to the score; a bag case header laid out like a boarding pass);
- **the variants** — each family's variants are designed from the concept, not taken from a house set;
- **the motif, empty states and imagery** — drawn from the concept, used quietly;
- **the chart voice** — how data is marked (chips, departure-board rows, swatches) where it reads
  better than a plain bar;
- **one signature interaction** — a single memorable moment tied to the concept (a score filling like
  paint; a status flipping like a departure-board tile; a card turning like a lookbook page), built
  within the motion rules, used once or twice in the app, never on every control.

**The concept changes form, never the core.** It can shape layout, composition, imagery and motion. It
never adds a colour value outside the transform, a radius outside the scale, a third elevation, a new
type size, or anything a UX law forbids. If the concept fights readability, the concept loses.

**Then set each dial from the concept, the identity sample (Step 1), the personas (0.4) and the
inspiration board (research question 6).** Every dial records its choice and the evidence that chose
it, in an **expression card** on the style guide.

| Dial | Options | Chosen by |
| --- | --- | --- |
| **Chrome** | `brand` gradient rail · `ink` near-black chrome · `light` rail on the solid rung | The brand's light-to-dark balance and chromatic role. Dark-led or achromatic → `ink`. Colour-led → `brand`. Light-led with a restrained accent → `light`. |
| **Shell** | left rail · top navigation (`data-shell="top"`) · rail plus docked agent (`.with-agent`) | Number of top-level destinations (≤ 5 and a wide content area → top navigation works), how the client's own product navigates, the persona's session length. |
| **Surface** | `glass` · `solid` · `paper` | The client's own product (layered or flat), density (dense tools lean `solid`), the vibe line in §21. |
| **Default theme** | light · dark | Dark-led brands and dark-first personas (night shifts, control rooms) → dark; otherwise light. The product ships this default; the other theme stays one attribute away. |
| **Type voice** | display face = body face · a separate display face (`--font-display`) · display weight and size emphasis within the four-size scale | The client's display face (open or substituted, Step 2b) and how loud their headings are. |
| **Imagery** | product photography · people · illustration · data-led (no imagery) | What the client's own work shows and what the records have (styles with photos, shelves, people). Where records have images, every specimen shows them, with a real fallback. |
| **Motif** | none · one graphic element from the logo or brand work | Used once or twice, quietly: an empty-state illustration, the rail's top edge, a section divider, the AI marker. Never behind text, never a new colour. |
| **Chart voice** | bars and lines with gridlines · minimal with direct labels · dense small multiples | The personas (an executive reads big numbers and direct labels; an analyst reads grids) and the references. |
| **Signal** | the transformed accent (default) · the brand's literal accent as `--signal` | When the brand's own accent cannot be a fill under white text (neon lime, yellow, light cyan), keep it literal as `--signal` for indicators, focus glow on dark chrome, a key data series, selection marks — measured per use, never as body text on light. |

**Rules for the dials:**

- **The house default is a choice, not a fallback.** Picking `brand` chrome + left rail + `glass` +
  light needs evidence from the brand, the same as any other combination.
- **The logo-off test.** Cover the logo on the main screen and ask whether a person who knows the
  client would recognise it as theirs. If not, revisit chrome, surface, imagery and motif before going
  on. Record the answer in the expression card.
- **Two consecutive runs for different clients must not land on the same card** unless the evidence
  for both points there; the card states it.
- **What the dials never move:** the radius scale, the no-borders-on-cards rule, the two elevation
  levels, the four type sizes and two weights, spacing, component anatomy, every state, the status
  palette, the contrast floors. Variation lives in composition and colour application, never in
  breaking the measured core.

### Variants and the style set — options for the reviewer, one answer for the builder

Reviewers want choices ("show me another chart header"), and the builder needs one unambiguous answer.
Too many loose variants and the builder mixes them or picks the weakest. So variants are **coded,
capped and bundled**:

1. **Families.** Only these component families may carry variants: page header `PH`, record header
   `RH`, KPI tile `KPI`, chart frame and header `CH`, table row style `TB`, card `CD`, filter bar `FB`,
   empty state `ES`, and the signature components from 0.8 (`SG1`, `SG2`, …). Everything else has one
   form.
2. **At most three variants per family**, coded `<family>-<n>` (`KPI-1`, `KPI-2`, `CH-3`). Each must
   differ in a way a reviewer can see in one second (number above label vs label above number; header
   with inline legend vs legend below), and each passes every rule in this file. No variant is a
   weaker copy kept for contrast.
3. **One style set by default: `S1`.** A style set names exactly **one** variant per family — never
   two. S1 is the set every drawn screen uses, and the only set the builder uses. The other variants
   still appear, labelled, on the component pages, so the reviewer can see the choices without whole
   screens being redrawn. **Draw `S2` (and at most `S3`) only when the user asks for options**, and
   then on **one** hero screen each, side by side.
4. **Every specimen is tagged.** Each component instance carries `data-variant="KPI-1"` (and the screen
   carries `data-style-set="S1"`), and the style guide prints the code beside each variant in the
   component section.
5. **Machine-readable for the builder.** The file carries one JSON block, which the composition contract
   quotes:

```html
<script type="application/json" id="style-sets">
{"active":"S1",
 "sets":{"S1":{"PH":"PH-1","RH":"RH-1","KPI":"KPI-1","CH":"CH-1","TB":"TB-1","CD":"CD-1","FB":"FB-1","ES":"ES-1"}},
 "variants":{"KPI-1":"number over label, delta below, no icon","KPI-2":"label over number, sparkline right"}}
</script>
```

   **The rule for the builder: use only the active set's variant for each family, everywhere, and never
   mix sets.** If the user asks for options and then picks S2, S2 is added to `"sets"` and only
   `"active"` changes.
6. **Variants are designed for this client.** Each family's variants come from the design concept,
   the brand and the references, so two clients' KPI tiles can look nothing alike. Each variant names
   its source (the concept, a reference from research question 6, or brand evidence) in the `variants`
   text, and the **recommended** one (active in S1) says in one line why it fits this client best.

### Chart views — more than one way to see the same data

For every chart the document needs, start from the **question the chart answers** ("which stores
fail most?", "is the pass rate improving?") and draw **chart views**: the recommended view plus one or
two alternatives that answer the same question differently, each coded `CV-<chart>-<a|b|c>` and framed
in `.cv` with its code (`.cv-tag`).

- **Same frame, same data, same units, same status palette** across the views of one chart; only the
  encoding changes (bars ↔ dot plot ↔ line; stacked ↔ small multiples; donut never for more than three
  parts).
- **Mark one view Recommended** and say why in one line. The recommended view goes into the active
  style set's screens; the alternatives appear beside it in the chart section only.
- **Where the persona benefits, the view switch ships in the app**: a `.seg` in the chart header
  (Chart / Table at minimum, for accessibility and export), drawn in its states.
- **Every chart has a table view** available, even if it is not the recommended view.

**Black-led and achromatic brands** (Pentland: black grounds, white type, a neon yellow-green accent):
chrome `ink`, default theme usually dark, surface `solid` or `glass` over a near-black ground, the
accent kept literal as `--signal` for the active nav indicator, focus, selection and the one hero data
series. The primary button becomes a light fill with dark text, or the signal fill with dark text,
whichever measures ≥ 4.5:1 — never the signal under white. **An achromatic brand is never rotated
onto a hue taken from its website's link colour.**

**Brands whose hue is close to the house blue** (Topcon, H 208°): the transform barely moves anything,
so the expression has to carry the identity — chrome, surface, imagery, motif and type voice do the
work the hue cannot.

## Step 3 · Transform, preserving LUMINANCE

**The whole value of porting a validated system is that its measurements survive. They survive only
if you hold the right quantity fixed, and it is not the one in the colour picker.**

Contrast is a function of relative luminance alone. **HSL lightness is not luminance** — green at
L .40 is far brighter than blue at L .40. Measured on the Proofpoint port: holding HSL-L fixed while
rotating 207° → 176° took the primary from **4.54:1 to 3.12:1**, silently, on a token the document
prints a number for.

```python
import colorsys
def _lin(c): c/=255; return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
def Y(rgb): r,g,b=rgb; return .2126*_lin(r)+.7152*_lin(g)+.0722*_lin(b)
def hsl_rgb(h,s,l): return tuple(round(v*255) for v in colorsys.hls_to_rgb(h,l,s))

def reskin(rgb, hue, sat):
    """Saturation is CHOSEN (that is the muting). Lightness is SEARCHED. hue/sat/l in 0..1."""
    target, lo, hi = Y(rgb), 0.0, 1.0
    for _ in range(60):
        mid = (lo+hi)/2
        if Y(hsl_rgb(hue, sat, mid)) < target: lo = mid
        else: hi = mid
    return hsl_rgb(hue, sat, (lo+hi)/2)
```

⚠️ **Do not add a "drop saturation if Y is unreachable" fallback.** In HLS, lightness 1.0 is white at
every saturation, so every `Y` in [0,1] is always reachable; that branch can only fire spuriously,
on a tolerance tighter than integer-RGB rounding, and when it fires it flattens a colour to grey
while keeping its hue. `#86CDB4` came back `#BFBFBF`. **Saturation is chosen; lightness is searched.**

**Assign colour by job and keep the jobs separate:** brand/chrome · status · categorical ·
sequential.

* **The brand colour has exactly three uses** — the one primary action, the active nav item, the
  selected state. Not headings, icons, counts, or links in tables. Everything else greyscale.
* **Reserve the warm end for risk states** so a categorical colour never reads as an alarm. ⚠️ **If
  the brand itself is warm, Step 4 inverts this.**
* **Muting is a saturation cut, never a lightness cut** — a lightness cut moves the quantity you are
  holding. Worked example: blues → H176 at S × 0.70 (cap .62); the cerise family → H152 at S × 0.62
  (cap .44) for the gradient tail; positive → H138 against a green brand; amber → H28; red → H6;
  anything under S .06 left alone.
* **Four statuses, tonal only** — 8–10% tint, text at the 700 step, never a saturated fill.
  **Status always ships as icon + word + colour.**
* **Charts: one hue at several lightness steps.** Fixed hue order, never cycled.
* **🔴 Brand-as-accent and brand-as-fill are two different values.** White on the Proofpoint fill
  measured 4.15 against a claimed 4.94 — **the fill gradient runs one step darker than the accent
  token**, and it governs the primary button, user chat bubble, toggles, checked boxes, the current
  stepper node and the bulk-bar counter. **Check every gradient stop, not just the mid one.** In
  dark, brand-as-text lightens while brand-as-fill does not.

## Step 4 · The warm-brand checks (skip if the brand is cool)

Three things appear on a red or orange brand and on no cool one:

* **Negative status collides with the brand and no contrast figure will warn you.** A red brand and
  a red error measure 1.54 contrast — but contrast is a *lightness* metric and says nothing about
  categorical separation. **Measure ΔE.** At H 350 negative sits 26 ΔE from the brand against 90 ΔE
  in the blue original; **H 344 recovers 32 ΔE** and is about the ceiling before the error reads as a
  brand tint. Icon + word + colour becomes load-bearing rather than belt-and-braces.
* **The chart ramp must leave the brand hue entirely.** A six-step red ramp reads as six alarm
  levels. Send it cool — still one hue at several lightness steps, and it can never read as risk.
* **The accent needs more headroom.** A straight port put Titan's accent at 4.48 on the page, a fail
  where the blue measured 4.54.

## Step 5 · Both themes, and both reachable

**Light and dark are both deliverables. The mode you built in is not the only one that gets
checked.**

* **v3.3 shipped both themes and zero `<script>`**, so it silently followed the reader's OS and the
  reviewer only ever saw dark: *"do we not have light mode."* Two themes measured and argued over
  across a whole section, one of them invisible. **Shipping both is not enough — both must be
  *reachable*.**
* **A theme built by inversion fails on contact.** Light-mode brand hexes in a dark ambient field
  paint shadow instead of light; that is what blotched the first SailPoint dark mode.

**The style guide ships a theme switch** — built from `.seg` (D0), defaulting to the OS, remembered
in `localStorage`. **A screen built from the design system does not**, because a theme toggle in
product chrome is our scaffolding shipped to the client. On a product build, ship the **default theme chosen in
Step 2c, set explicitly as `data-theme` on `<html>`** — a product never follows the reader's OS (the
Topcon app opened dark on a dark-mode laptop while the design was light-first) — and **keep the other
theme's tokens live in the stylesheet**, so the second theme is one attribute away rather than a
rebuild. Users switch theme from the profile menu.

**Dark specifics — rebuilt in v5.** The v4 dark sat on a mid slate (`#192030`) under blue-grey glass at
12–23% and aurora at 19–26%. It read dull and muddy, and measured worse than it looked: composited on
its own tier-3 glass, `--ink-3` fell to 3.06:1 and the status tags to 2.98–3.43:1, which is why every
run lifted tokens by hand. The v5 dark, now in the stylesheet:

| Token | v4 | v5 | Why |
| --- | --- | --- | --- |
| `--base` | `#192030` | `#0B1018` | A deep, faintly brand-tinted ground: depth comes from a dark page, not from grey washes |
| `--glass-1/2/3` | `rgba(120,165,225,.12/.17/.23)` | `rgba(150,180,230,.05/.07/.095)` | Glass in dark is a whisper of light; heavy alpha is what turned it to slate |
| `--glass-solid` | `#2F3D57` | `#151B26` | The opaque rung sits one clear step above the page |
| `--inner` · `--edge` · `--hair` | `.085` · `.17` · `.10/.17` | `.06` · `.10` · `.08/.14` | Quieter separations on a darker ground |
| `--ink` / `-2` / `-3` / `-mute` | `#D8E0EC` `#AAB7CB` `#9FADC3` `#78869F` | `#E7ECF3` `#B6C0CF` `#9AA6B8` `#6F7B90` | Worst composited case now 9.61 / 6.21 / 4.63 (mute is disabled text, exempt) |
| `--sp-blue` (brand as text) | `#6BB3EA` | `#7DBDF0` | 5.65:1 at its worst ground, up from 3.06 |
| Status text | `#AAB7CB` `#E3B45C` `#EC9790` `#86CDB4` | `#B6C0CF` `#E8BC69` `#F2A49D` `#8FD3BA` | Every status tag ≥ 5.0:1 on its tint over the opaque rung (was 2.98–3.43) |
| `--aur-1/2/3` | `.26/.19/.22` | `.18/.12/.14` | The aurora becomes a glow at the edges, not a wash over everything |
| `--vig` | to `rgba(6,11,22,.30)` | to `rgba(2,5,11,.42)` | Corners fall away, which is what makes the glow read |
| `.tile` highlight | white at 28% | white at 4.5% (dark only) | The 28% highlight painted every tile grey |

**Rules for dark, whatever the brand:**

- **Depth is lightness steps, not washes**: page < glass tiers < opaque rung < inner wells < raised
  overlays, each a small, even step lighter.
- **The brand glows; it does not tint everything.** Allowed: the aurora at the page edges, a soft
  brand glow behind the hero area or the agent launcher, the focus ring, the active nav indicator, a
  brand gradient on the primary fill. Not allowed: brand colour behind body text, saturated panels.
- **No fluorescent text.** Brand-as-text in dark is a pastel step of the brand (HSL lightness ≥ 0.70,
  measured); a neon or saturated accent is used for marks, indicators and fills with dark text, never
  for words on dark.
- **Edges catch light upward in dark and downward in light.** One hue carries two categorical steps
  in dark, three in light.
- **A container that HOLDS other glass takes the opaque rung**, or nested glass composites two rungs
  above its intended one and drags every ink token after it.
- **After the transform, re-measure the dark set on the brand's own hue.** A warm or green brand moves
  luminance differently from blue; the v5 numbers are the floor the port must still meet.
- **Look at references first** (research question 6): well-regarded dark products use near-black
  grounds, low-alpha surfaces, a single accent and generous spacing. Take that discipline, not their
  colours.

**Light specifics — it is not dark with the tokens flipped:** near-white brand tint base · **aurora
alphas roughly halved** · tier 1 `rgba(255,255,255,.72)`, tier 2 `.82`, tier 3 brand at 5% · inset
highlight `rgba(255,255,255,.9)` · shadows to the brand's darkest tone at 8–12% · **the accent glow
drops, replaced by a soft focus ring**.
⚠️ **A tinted light background changes the surface a chart was validated against** — Daikin's palette
passes on `#F4F8FC` and a third slot drops below 3:1 by `#EEF4FA`. Cap the tint and re-run the
validator. **Re-measure fixed-width layouts after restyling** — larger radii and padding are what
push a six-station rail back out of its container.

## Step 6 · Audit, composited, both themes

**Walk every text role with alpha composited over its real parent chain, in light and in dark.** The
reference run on v3.4 covered 35 new roles and ended with 3 under AA in each theme, all three
deliberately dimmed states.

**Mechanical checks, all pass/fail:**

* **Rendered and screenshotted in light AND dark.** A theme nobody has looked at is broken.
* `grep -o 'stroke[A-Z]'` → **nothing.** 79 camelCase SVG attributes once shipped in our own design
  language with every icon at browser-default stroke. **JSX takes camelCase; plain HTML takes
  kebab-case — same defect, opposite fix, both silent.**
* `grep -E '\-\-[a-z-]+: ?[0-9]+,[0-9]+,[0-9]+'` → every **bare rgb triple** accounted for. v3.4
  declares its ambient field as `--aur-a:0,51,161`, consumed as `rgba(var(--aur-a),a)`. **There is no
  `rgb(` to match, so a hex-and-rgba replace leaves the ambient field on the previous client's
  brand** — at 5% opacity it does not look broken, it just casts the page in the wrong hue.
* Card `border-width` computes 0 · gradient cards carry no inset ring · `backdrop-filter` computes
  `blur(...) saturate(...)`, not `none` · 1px top edge on every glass surface.
* Radii only {10, 6, pill, circle} outside the studio.
* Table header IBM Plex Mono 10.5px **and the face actually embedded** — if it silently falls back
  the whole grid loses its register.
* **If the body face was swapped (Step 2b): numerals are tabular, the four type sizes still hold
  their hierarchy, and no fixed-width layout has overflowed.**
* Tag font-size < button font-size · status tags ≥ 4.5 composited, both themes · **logo mark ≥ 3:1
  on its ground, every variant**.
* One `<style>`, one `</style>` · no horizontal page scroll · zero JS errors · **one output file**.
* **Theme switch correct under both OS schemes and across a reload.**
* **Narrow a filter until it returns nothing** and look at which empty state appears.
* **Shell, at the deepest scroll:** the rail's bottom equals the viewport's bottom, the top bar's
  computed background is opaque, no content is visible through or under it, and wide tables scroll
  inside their own container (no column clipped, no page-level horizontal scroll).
* **Every agent drawer opens, closes with Esc, returns focus to its launcher**, and is drawn over a
  real screen; no agent appears as a card or block in a page layout.
* **Images:** every record that has an image shows it; every missing image shows the designed
  fallback, never a broken-image icon or an empty card.
* **Status in charts** uses the status palette and a legend with words, never brand-colour steps.
* **Phone and tablet layouts that are drawn** (0.4: only a persona's primary device) render at their
  widths with their own navigation.

**Four traps, each of which produced a false result on a real run:**

1. **Gradient grounds read as transparent.** A walker reading `backgroundColor` finds nothing on a
   `linear-gradient` surface and falls through to the page — it reported **1.03:1** on rail text that
   measures **12.12:1**. Put an explicit `background-color` under every gradient: honest measurement
   plus a real fallback ground.
2. **Alpha ignored.** Composite the tint over its actual parent or every tonal status tag reports
   ~1.2 and you "fix" what was never broken. **Measuring the wrong thing is its own failure mode.**
3. **🔴 Inject CSS before the LAST `</style>`, not the first.** The first may be the host page's own
   skeleton — the rules land outside the stylesheet, are stripped on export, and every component
   renders with browser defaults while the file looks complete and the elements are all present in
   the DOM. **This is written down and it still happened while building v3.4.** Verify a *computed
   value* on a new component — not the source text, not the presence of the element.
4. **A handler audit false-clears if `[data-theme]` is on `<html>`** — `el.closest('[data-theme]')`
   then matches every element. Exclude `document.documentElement`. Same trap in Playwright:
   `page.click('[data-theme]')` clicks `<html>` and your dark screenshot comes back light — select
   `button[data-theme]`.

### Rendering safety — what broke in real output files, and the rule for each

Every one of these produced a file that looked finished in its source and rendered wrong.

| What broke | Rule |
| --- | --- |
| **Words looked run together** (Vermont, "Retakeneeded") | **Fonts are embedded as base64 WOFF2 taken unchanged from Google Fonts' own files** for the subsets the page needs (latin, latin-ext, plus any script the personas read). Never re-subset, rebuild or convert a font. Some faces simply have narrow spaces — Plus Jakarta Sans measures 0.17 em in its official file, Archivo 0.21, Inter 0.28 — so judge the space against the official file, not an absolute floor. For a face with a space under 0.2 em: no negative letter-spacing below 15 px, and `word-spacing:.04em` on text under 14 px. |
| **Fonts silently fell back** when a run's sandbox could not reach Google Fonts, so its own screenshots showed Arial and the audit measured the wrong face | Embedding (above) makes the file truly self-contained. A `<link>` to Google Fonts is allowed only as a backup *in addition* to the embedded faces. `document.fonts` must report every family loaded before screenshots are taken. |
| **Unstyled studio parts** — the v4 stylesheet had no light-theme base rule for `.sheet2`, `.kpis2`, `.kpi2` or the studio composer `.cmp` | Fixed in v5's stylesheet. Any class the page uses must have a base rule; the render check lists classes with no matching rule. |
| **Broken images and empty image tiles** (Pentland's AI views, its material swatches) | Every image is embedded (SVG inline, raster as a data URI of 200 KB or less) — never hot-linked, since client sites block hot-linking and the file must open offline. Every image box has a size or `aspect-ratio`, `alt` text and a designed fallback. Keep the file under 15 MB. |
| **One open drawer covered the whole guide; a 100vh rail ran past its screen** | Screen specimens go in `.frame > .frame-scroll` (the kit). |
| **A phone drawn in a narrow box showed the desktop layout** | Phone and tablet specimens go in `<template class="device">` and render as iframes (the device script). |
| **The launcher sat on the phone's tab bar** | Fixed in the kit: on a phone the launcher sits above `.app-tabs`. |
| **Tags broke onto two lines in narrow tables** ("Off / track") | Fixed in the core: tags, facet chips and slots do not wrap. |
| **Clipped inputs and spilling cards** (ClickUp's search placeholder cut off, a Topcon hover card 149 px outside its column) | Placeholders fit their field at the narrowest width shown. State specimens (hover, lifted, open) sit in a cell sized for that state. The render check flags spills and clips. |
| **A transparent rail in some browsers** (`color-mix()`) | No `color-mix()`, CSS nesting or container queries in the system CSS; layout must not depend on `:has()`. |
| **Icons at browser-default stroke** (camelCase SVG attributes in HTML) | The `stroke[A-Z]` grep above, before every hand-over. |
| **The guide's left navigation showed half-height, overlapping labels** (Fujairah: a fixed-height flex column, links with `overflow:hidden`, so the browser shrank each link to 15 px; worse on shorter screens) | Every child of a flex column that must keep its height gets `flex-shrink:0`; a long navigation scrolls inside itself (`overflow-y:auto`), it never squeezes its items. The render check's `vclipped` count catches it. |
| **State matrices squeezed wide components** (Fujairah: a 360 px pilot card forced into 190 px state columns — eyebrows one word per line, the last card cut at the edge) | A state cell is never narrower than the component's real width. Narrow atoms (buttons, chips, toggles) use the table matrix; a component wider than about 240 px shows its states as a wrapping grid, each tile at the component's real width (`grid-template-columns:repeat(auto-fill,minmax(<real width>,1fr))`). |
| **Wide diagrams looked cut off** (Fujairah's swimlanes ran 1,814 px in an 1,116 px column with no sign they scroll) | A diagram wider than its column either wraps (lanes stack, steps flow to a second row) or scrolls inside a frame with its first column (lane names) sticky and a visible edge fade and "Scroll →" hint. Nothing ends mid-card at the edge. |

**The render check — run it in the browser on the finished file, in light and in dark, at 1,280 px and
375 px, and paste the result into the hand-over.** It also walks every device iframe. Every count must be
zero and every face loaded; `where` names the first offenders. `overlaps` finds siblings that collide
(pills on top of each other, task names running into the next card); `squeezed` finds text wrapping at
one or two words per line (a column or card too narrow for its content); `vclipped` finds text cut off
vertically inside a box that hides overflow (a link or row shrunk below its line height). **Run it at
three viewports: 1,280 × 800, 1,280 × 680 (a short laptop screen, where squeezing shows first) and
375 × 812.**

```js
(() => {
  const res = { hScroll: 0, spills: 0, clipped: 0, vclipped: 0, overlaps: 0, squeezed: 0, brokenImages: 0, fonts: {}, unstyledClasses: [], where: [] };
  const note = (k, el, doc, win = window) => { res[k]++; if (res.where.length < 15) res.where.push(k + ': ' + (win.frameElement ? (win.frameElement.title || 'device') : 'page') + ' › ' + el.tagName.toLowerCase() + '.' + [...el.classList].join('.') + ' "' + (el.textContent || '').trim().slice(0, 40) + '"'); };
  const scan = (doc, win) => {
    const de = doc.documentElement; res.hScroll = Math.max(res.hScroll, de.scrollWidth - de.clientWidth);
    const texts = [];
    const layer = el => { for (let n = el; n && n !== doc.body; n = n.parentElement) { const p = win.getComputedStyle(n).position; if (p === 'fixed' || p === 'absolute' || p === 'sticky') return n; } return doc.body; };
    for (const el of doc.querySelectorAll('body *')) {
      const cs = win.getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
      if (['hidden', 'clip'].includes(cs.overflowX) && el.scrollWidth > el.clientWidth + 2 && el.clientWidth > 40 && cs.textOverflow !== 'ellipsis' && !el.closest('.tblwrap')) note('clipped', el, doc, win);
      if (['hidden', 'clip'].includes(cs.overflowY) && el.clientHeight > 0 && el.scrollHeight > el.clientHeight + 2 && cs.webkitLineClamp === 'none' && !el.closest('.frame, .frame-scroll') && [...el.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim())) note('vclipped', el, doc, win);
      const p = el.parentElement;
      if (p && cs.position !== 'fixed' && cs.position !== 'absolute' && win.getComputedStyle(p).overflowX === 'visible' && r.right > p.getBoundingClientRect().right + 4) note('spills', el, doc, win);
      const own = [...el.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim());
      if (own) {
        if (cs.display !== 'inline' && cs.display !== 'contents') texts.push([el, r, layer(el)]);
        const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.3, lines = Math.round(r.height / lh), words = el.textContent.trim().split(/\s+/).length;
        if (lines >= 3 && words / lines <= 1.6 && words >= 3) note('squeezed', el, doc, win);
      }
    }
    for (const parent of doc.querySelectorAll('body *')) {
      if (parent.matches('.faces')) continue;
      const kids = [...parent.children].filter(k => { const cs = win.getComputedStyle(k); return cs.display !== 'none' && cs.visibility !== 'hidden' && cs.position !== 'absolute' && cs.position !== 'fixed' && k.textContent.trim(); });
      for (let i = 0; i < kids.length; i++) for (let j = i + 1; j < kids.length; j++) {
        const ra = kids[i].getBoundingClientRect(), rb = kids[j].getBoundingClientRect();
        const ix = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left), iy = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
        if (ra.width && rb.width && ix > 3 && iy > 3) note('overlaps', kids[j], doc, win);
      }
    }
    res.brokenImages += [...doc.images].filter(i => i.complete && !i.naturalWidth).length;
    const c = doc.createElement('canvas').getContext('2d');
    doc.fonts.forEach(f => { const fam = f.family.replace(/["']/g, ''); c.font = `16px "${fam}"`; res.fonts[fam] = { status: f.status, spaceEm: +((c.measureText('a b').width - c.measureText('ab').width) / 16).toFixed(2) }; });
    const css = [...doc.styleSheets].flatMap(s => { try { return [...s.cssRules].map(r => r.cssText) } catch (e) { return [] } }).join(' ');
    [...new Set([...doc.querySelectorAll('[class]')].flatMap(e => [...e.classList]))].filter(k => !css.includes('.' + k) && !res.unstyledClasses.includes(k)).forEach(k => res.unstyledClasses.push(k));
  };
  scan(document, window);
  for (const f of document.querySelectorAll('iframe')) { try { if (f.contentDocument) scan(f.contentDocument, f.contentWindow); } catch (e) {} }
  console.table(res); return res;
})()
```

**Every count is a defect in screens, specimens, state matrices, component pages and the guide's own
navigation.** The only allowed exception is a short label in the first column of a documentation table
wrapping onto two lines (for example "Hover a waypoint"); check each one by eye and list it in the
hand-over. Anything else flagged is fixed before hand-over. `unstyledClasses` should list only hooks used
by a script, never a visual component. The v5 runs measured 69–381 squeezed elements and up to 54
clipped ones per file; the reference test page measures zero on every count.

## Step 7 · Ship

**The output is one file: a single self-contained HTML file, and nothing else.** Not a published
artifact, not a separate token file, not a logo folder, not JSON or Markdown alongside it. Save it as
`<client>-design-system.html` in the outputs folder and hand over that path. Everything the deliverables
below describe lives inside that one file as sections of the page — the token block as a copyable code
block, the logo kit as inline SVG (raster variants as data URIs) with a copy button per variant, the
composition contract as a quotable block. If something cannot live inside the file, it is not delivered.

**The file is a design system, not a drawn copy of the app.** It documents every component in full,
shows the foundations and patterns, draws the journeys as diagrams and at most five screens, and hands
over the rules for the rest (0.6).

**Five deliverables, all inside the one file:**

1. **Living style guide** — the page itself, built like a real design-system site: self-contained,
   light and dark with a working switch, a **sticky left navigation** of its sections (full viewport
   height, scrolling inside itself when long; every item `flex-shrink:0`, one line, never squeezed), the client's
   expression applied to the guide itself (chrome, motif, type voice) so it reads as this client's
   system. **Its sections, in order:**
   - **Overview** — the build brief and page inventory (0.6), the expression card, the inspiration board.
   - **Foundations** — colour (every token with its measured ratio), type scale, spacing and density,
     **material and elevation** (glass tiers layered over the ambient field, the solid rung, edge light,
     shadows, in both themes), motion (durations, easing, what moves and why), icons.
   - **Components** — one component page per component (REFERENCE, the component-page spec), grouped
     as the inventory groups them; signature components first, then the agent drawer, overlays,
     navigation, inputs, data display, feedback and states. Every component **rendered, not
     described**, with its live specimen and state matrix.
   - **Patterns** — a blueprint for each chosen pattern; chart views.
   - **Journeys** — the demo storyline and every journey as flow diagrams.
   - **Screens** — at most five, each labelled with its pattern, persona and the storyline steps it shows.
   - **Build** — the composition contract, the token block, the logo kit, the port note and ledger, the
     hand-over. Style sets S2/S3 only if the user asked for options.
2. **Token block** — one `:root`, tokens named by **job** never by colour, **a measured ratio printed
   beside each**, non-text ones marked. A token carrying a number nobody re-measured after a hue
   rotation is a defect.
3. **Logo kit** — the seven variants with the usage matrix, clear space, minimum sizes, misuse list
   and provenance. With `ink` or `light` chrome, the rail takes the variant that measures on it.
4. **Composition contract** — a block written for the builder (UnifyApps Headless), quoted verbatim in the build
   prompt. The builder reads this, not the skill, so every rule it must follow is here:
   - **Look up, don't choose.** Every design decision is already made in `#build-plan` and
     `#style-sets`. For each page: find its route in `build-plan.pages` and use that pattern and those
     region fillers. For a page not listed, take its data shape and persona and use the **first
     matching rule** in `build-plan.rules`. Use the `app` settings (shell, theme, surface, density,
     agent drawer) on every page. Never pick a different pattern or variant because it seems better.
   - **Copy only active specimens.** Build from components marked `data-active="true"`. Anything marked
     `data-active="false"` ("Reference — not in this app") is never used. Nothing exists outside the kit
     and the token block: no new component, colour, radius, elevation, type size or spacing step.
   - **Compose the page; don't clone a screen.** Follow the pattern's blueprint and match the drawn
     screens' look, spacing and finish, with the page's own content. Never copy one screen's content
     onto another page.
   - **Keep the concept.** Where `build-plan.concept` and a signature component apply to a page (the
     shade-card score, the boarding-pass header), use them as drawn; they are what make the app this
     client's.
   - **Journeys run as specified.** Build the pages so each journey follows its flow diagram, using the
     document's exact wording for every refusal and message. Signature components are built as
     their component pages specify.
   - **Every component keeps every state and micro-interaction from its component page:** hover,
     focus-visible, pressed, selected, disabled, loading, error and read-only, with the timings and
     easing given. Every page also gets a loading state between action and response, the empty first
     run, undo after a reversible action, and its empty, filtered-empty, error, no-access and UNSET
     states, from the kit.
   - **Shell:** `.app`, `.app-rail`, `.app-top`, `.app-main`, `.app-body`; rail full height; top bar
     opaque, `.scrolled` on scroll; `data-chrome`, `data-surface`, `data-theme` on `<html>` as the
     expression card says.
   - **Agents:** the chosen `AG` drawer, opened from the top bar and `.agent-launch`, built on the
     platform's **live agent component** (streamed replies, real stages, tool outputs in the thread),
     never an automation that writes an answer for the page to show on refresh.
   - **Data and density:** tables scroll inside `.tblwrap`; one line per cell (two in the first column),
     two chips then "+n", about seven columns at 1,280 px; every image has a fallback; a count shown
     twice comes from one query.
   - **Overlays, spacing, colour:** modals and drawers only in the kit sizes and anatomy; the agent docks
     only at 1,440 px and wider; spacing only from the scale; no colour outside the token block; chart
     status series use the status palette; deltas coloured by good or bad, not by sign.
   - **The UX laws** in "The composition model" bound everything the builder composes.
5. **The build plan** — `#build-plan` (composition model, Layer 4) and `#style-sets`, quoted with the
   contract: the seed, the concept, the app settings, the pattern and region fillers per page with the
   reason, the rules for unlisted pages, and the chart encoding per chart. A reviewer changes the app by
   editing these blocks; the builder follows them.

**And a type note:** the client's real typeface named, what was shipped instead, and why — *"Brand face
 is Gotham (Monotype, single-domain licence); shipped Montserrat as the closest open substitute.
 Production should license Gotham."* **A client reading that learns something; a silent substitution
 looks like we did not notice.**

**Plus a port note on the page itself**, stating the source version, max |ΔY| across all colours, and
every decision the port forced, **the brand source order applied, the expression card, the seed, and
every correction made to the scoping document (0.1)**. **Anchor the one branded surface to the client** —
with `brand` chrome the rail gradient starts at the sampled swatch; with `ink` chrome the signal colour
marks the active item; with `light` chrome the brand marks the active item and the primary action.

**Swap the sample domain, not the doctrine.** Proofpoint: Deal Gate → Quote Builder; gate artefacts
→ product configuration / pricing summary / legal review / order form; identities → seats; Okta IG →
Defender for O365; Stage 20/40 → awaiting approval / approved. **Every measurement stayed.**

⚠️ **Anonymise at extraction: the format travels, the client name does not.** The file is the
hand-over; do not publish it or share it as a link.
**If you fix something in the stylesheet, say so in the hand-over** — an unreported fix means
the next run reintroduces it and the skins quietly diverge.
**No demo or synthetic labels anywhere** — not "demo persona", not "synthetic data", not "used for demo
only". The app and its specimens read as the real product with real content.

---
# REFERENCE

## The composition model — how the builder makes pages from the kit

Components are the words, **patterns** are the sentence shapes, and a **seeded chooser** decides which
sentence each page becomes, so two apps differ and one app stays coherent. **Order of authority: core
→ UX laws → fit → seed.** The seed only ever chooses between options that are already correct.

### Layer 1 · Components with labelled variants

Each family below may carry **up to three variants**, each visibly different, each passing every rule
in this file. A variant rearranges the same atoms; it never adds a colour, radius, elevation, type size
or spacing step. Each component page draws every variant with its code.

| Family | Code | What varies |
| --- | --- | --- |
| Page header / record header | `PH` / `RH` | ID eyebrow vs breadcrumb; actions inline vs in a menu |
| KPI tile | `KPI` | number over label vs label over number; sparkline; mini-bar |
| Chart frame | `CH` | legend inline vs below; with a view switch |
| Table row | `TB` | single line vs name over meta; status stripe |
| Card | `CD` | metric-led vs media-led vs text-led |
| Filter bar | `FB` | pill facets vs dropdowns |
| Empty state | `ES` | icon-led vs illustration-led |
| List item | `LI` | one line vs two lines vs thumbnail |
| Right-rail panel | `RP` | summary vs action list vs mixed |
| Agent drawer | `AG` | right drawer vs docked column vs bottom sheet; thread only vs thread with canvas |
| Signature components | `SG1…` | the two layouts 0.8 requires |

### Layer 2 · The layout patterns

A page is built on **one** pattern. Carrying seven means "a list plus a side rail" is one option, not
the only shape.

| # | Pattern | Built around | Fits |
| --- | --- | --- | --- |
| **P1** | List workspace | one list (table or cards), tabs, toolbar, optional rail | many records, flat |
| **P2** | Split master-detail | a list beside the **live full record** | records worked one at a time |
| **P3** | Focus / canvas | **one hero object**, little chrome, docked actions | one record, a document, a photo, a form-led task |
| **P4** | Board | **columns of cards** that move through stages | stages, a process |
| **P5** | Metric dashboard | a **mixed-width widget grid** (8/4, 6/6, 4/4/4) | aggregates |
| **P6** | Map | **the map is the page**, full bleed; top bar, insight cards, list panel and legend float over it (wireframes `map-component.md`) | locations |
| **P7** | Feed / timeline | **a chronological stream** as hero | activity, history, a schedule |

The agent drawer overlays any pattern; it is never a page body. In the kit, each pattern declares its
regions and grid split, which families fill each region, how it reflows per device, and its own
variants (rail left or right, detail inline or in a drawer). Patterns may nest once (a P2 record pane
holding a P7 feed); never two levels deep.

### Layer 3 · The chooser — run here, never by the builder

**All choosing happens in this run, by this skill.** The builder (UnifyApps Headless) works with no person in the
loop and is good at reproducing what it is given, not at judging which of three options is better; left
to choose, it falls back to the safest default, and every app turns into a list with a rail. So this
skill makes every choice, records it, and hands the builder answers, not options.

**How each choice is made — best fit first, the seed only breaks ties:**

1. **Build the candidate set**: the patterns or variants that fit the data shape and persona and pass
   the UX laws.
2. **Rank by fit to this client**: the data, the persona's job, and the design concept (Step 2c). The
   best fit is the **recommended** choice, and its one-line reason is recorded.
3. **Use the seed only when two candidates fit equally well.** One seed per build, from a hash of the
   client name. This is what makes two clients with similar data land on different, equally good
   answers, without any memory of past builds.

What gets chosen this way: the **pattern per page**; the **active variant per family** (once, for the
whole app); the **chart encoding per chart**. Shell, theme, surface, density, the agent-drawer variant
and the concept are set by the expression and the personas from evidence, not by the seed.

**Coherence overrides everything:** one shell, theme, density and surface per app; one variant per
family; the same data shape gets the same pattern wherever it recurs.

### Layer 4 · The build plan — answers the builder looks up

The choices are handed over as one machine-readable block, `#build-plan`, which the composition
contract quotes. The builder does not choose anything; it looks things up:

```html
<script type="application/json" id="build-plan">
{"seed":"asian-paints-7f3a","concept":"shade card: scores and status as paint chips",
 "app":{"shell":"rail","theme":"light","surface":"glass","density":"comfortable","agent":"AG-1"},
 "variants":"#style-sets active set",
 "pages":[
  {"route":"/today","pattern":"P7","regions":{"stream":"LI-2","rail":"RP-1"},"screen":"1 of 5",
   "why":"a rep's day is a timeline of visits"},
  {"route":"/visit/:id","pattern":"P3","regions":{"hero":"SG1 shade-card scorecard","dock":"action bar"},
   "screen":"2 of 5","why":"one visit, worked in depth"}],
 "rules":[
  {"when":{"shape":"many records, flat","persona":"desk"},"pattern":"P2"},
  {"when":{"shape":"many records, flat"},"pattern":"P1"},
  {"when":{"shape":"aggregates"},"pattern":"P5"},
  {"when":{"shape":"one record, deep"},"pattern":"P3"},
  {"when":{"shape":"stages"},"pattern":"P4"},
  {"when":{"shape":"locations"},"pattern":"P6"},
  {"when":{"shape":"activity or schedule"},"pattern":"P7"}]}
</script>
```

- **`pages`** covers every page in the inventory: its pattern, which variant or component fills each
  region, which of the five screens shows it (if any), and why.
- **`rules`** covers pages the builder creates that the inventory did not list: the builder takes the
  page's data shape and persona and uses the **first rule that matches**. The rules are ordered so
  the first match is the recommended fit for this client.
- **Every drawn specimen is tagged** so the builder copies the right one: `data-component="KPI"`
  `data-variant="KPI-2"` `data-active="true"`. Variants that are not active carry `data-active="false"`
  and a visible label "Reference — not in this app", so a builder that copies from the page never
  copies the wrong one. The five screens and the blueprints use active variants only.

**The reviewer can still change things.** Overriding one page's pattern, or making another variant
active, is an edit to `#build-plan` or `#style-sets`; the builder follows whatever the block says.

### The UX laws — every candidate passes these first

- **Jakob's law** — nav, search, primary action and record sit where users expect, in every pattern.
- **Hick's law** — no region offers more actions than it needs; the rest fold into a menu.
- **Fitts's law** — 24×24 targets at least; primary actions near the hand; destructive actions apart.
- **Miller's law** — chunks of 5–7; a stat row is 3–6 tiles.
- **Proximity / common region** — grouping by spacing and containers, not colour.
- **Consistency** — one look per app; the seed serves this law.
- **Von Restorff** — one thing per screen stands out.
- **Tesler's law** — complexity goes into the system, not onto the user.
- **Aesthetic–usability** — a cramped or mis-spaced candidate fails even if structurally valid.
- **Serial position** — the most useful column or action at the start or end, not buried.

A candidate that fails any law is removed before the seed sees it.

---

## The view library — the reserve the app draws from

**Held, not always built.** Phase 0 picks what a build uses; the rest stay dormant. A view the library
does not carry is a view the app can never produce, so it is wide on purpose. **Charts, graphs, flows
and maps are engines**: build each renderer once with the shared palette, then configure it to the
types listed. `[kit]` = a class already exists, reuse it; everything else is built from tokens and
doctrine when first needed, never with new colour values.

**Data and record** — table / data grid `[kit .tbl]` (always with the toolbar and filtered-empty ≠
empty) · editable grid · tree-table · card gallery `[kit .tile]` · list, one to three lines · key-value
list · grouped list · leaderboard · KPI tiles `[kit .tile .loop]` (colour a delta by good or bad, never
by sign) · detail / inspector · master-detail · compare / diff · pivot · heatmap grid (sequential
palette, never colour alone).

**Charts (chart engine, `.chart` owns frame, title, unit, legend, no-data)**, grouped by the question:
comparison (bar, column, grouped, stacked, bullet, lollipop, radar) · trend (line, area, stacked area,
step, slope, sparkline `[kit]`, candlestick) · part-to-whole (donut for at most three parts, treemap,
sunburst, waffle) · distribution (histogram, box, violin, dot, beeswarm) · relationship (scatter,
bubble, hexbin) · flow (funnel, waterfall, sankey) · single value (gauge, progress ring, big number with
delta) · analytics (cohort, retention, control chart, pareto) · geo (choropleth, bubble map, flow map; a site map is never a dashboard widget: it is a P6 page,
handed to the map engine). A chart without a unit is decoration; the ramp never cycles.

**Graph (graph engine, layouts force / hierarchy / radial)** — network · tree · org chart · mind map ·
ER / schema · dependency / lineage · adjacency matrix · taxonomy explorer. Nodes and edges have full
states.

**Process and flow (flow engine)** — workflow / DAG · flowchart · swimlane · sequence · state machine ·
decision tree · data-flow · journey map / blueprint · approval chain · stage board `[kit .loop]` ·
stepper `[kit .sth .stv]` · kanban `[kit .kb]` (always with a non-drag alternative) · agent run / trace
`[kit .stages]`. Nodes reuse the stepper's pip and status tones.

**Spatial (map engine: layers, markers, heat, routes, clustering, legend, zoom, drill-down)** — map ·
canvas / whiteboard · floorplan · network topology · slot / seat map `[kit .slot]` · mini-map.

**Temporal** — calendar month / week / day / agenda / slots `[kit .cal .agenda .slot]` (today takes a
ring, selection takes the fill, never both) · timeline · Gantt · resource schedule · roadmap · activity
feed `[kit .feed]` (a change carries its reason) · audit log.

**Agentic** — agent drawer `[kit .agent-drawer]`, the home of every agent (see "The agent component") ·
agent page `[kit .canvas]`, only when the agent is the page's whole purpose · agent workbench · AI
insight card `[kit .ai]` · reasoning trace · tool-call inspector · prompt console · suggested prompts
`[kit .chips]` · approval / action diff · citation panel.

**Document and artefact** — document reader · rich-text editor · form `[kit .fld .ctl]` · form builder ·
spreadsheet grid · code / log / JSON viewer · PDF / file preview · media gallery · slide view · redline
/ track changes · artefact studio `[kit .studio2]`.

---

## The component inventory — every atom, every state

The views are built from these atoms. **Reuse the stylesheet class whenever one exists**; a second
implementation is the most common failure on this work (mixed radii, two kinds of search field). A new
atom is built from tokens and the Form / Components doctrine, inside the five-step radius scale.

- **Actions** — buttons `[kit .btn-p .btn-s .btn-t]`, icon button, button group, split button, link, menu button.
- **Inputs** — text and textarea `[kit .ctl]`, search `[kit .field]`, number stepper, tag input, OTP;
  select, combobox, multi-select, checkbox and radio `[kit .opt]`, switch `[kit .tog]`, segmented
  `[kit .seg]`, slider, rating; date, time and range pickers, file upload.
- **Status and display** — badge, count dot, status tag `[kit .tag]`, chip `[kit .chipsel]`, avatar and
  group `[kit .av .faces]`, icon, progress bar `[kit .prog]` and ring, skeleton, spinner.
- **Containment** — glass cards `[kit .g1 .g2 .g3]`, panel, accordion, tabs `[kit .tabs]`, tile, inset `[kit .inner]`.
- **Overlays** — tooltip, popover, menu `[kit .menu]` (add trigger, dismiss and focus behaviour), context
  menu, modal, drawer, bottom sheet (phone only), toast `[kit .toast]`, banner (`.note` is the seed),
  command palette.
- **Navigation** — top bar, rail, breadcrumb `[kit .crumb]`, pagination `[kit .pg]`, tabs, stepper, tree nav.
- **States** — empty `[kit .empty]`, filtered-empty, error, loading, no-access, inline validation
  `[kit .ctl.err .hint.e]`, UNSET.

### The universal state + anatomy rule

```
STATES   default · hover · focus-visible · active/pressed · selected · disabled · loading · error · read-only
DECLARES border width · border colour · radius · background · elevation · the token for each state
```

Every interactive atom ships and is audited across these states, including the engines' parts: a graph
node, an edge, a map marker, a flow step, a timeline event and a kanban card all have hover, selected
and disabled states, from tokens, the radius scale and the two elevations. An atom that looks unfinished
is usually missing its focus ring, its disabled tone or its selected treatment.

---

## The component page — how every component is documented

**This is where the design system's quality is seen.** The five screens show the system assembled;
the component pages are what the builder actually builds from, so each one is complete enough that
nothing about the component has to be guessed.

**Every interactive component and every signature component gets a full page. Display-only atoms
(icon, avatar, badge, divider) get a short page: variants, the states that apply, usage.**

**A full page has ten parts, in this order:**

1. **Header** — name, code (`KPI`, `AG`…), one line on what it is for, when to use it and when not.
2. **Anatomy** — the component drawn large with numbered callouts; each part named with the token it
   uses (surface, border, radius, text, icon) and its measured contrast.
3. **Variants** — up to three, side by side, each with its code, a one-line difference and its source
   (concept, reference or brand). The active one is marked **Recommended — used in this app** with its
   reason and `data-active="true"`; the others carry `data-active="false"` and the label "Reference — not
   in this app".
4. **State matrix (static)** — every state shown at once, without a mouse: **default · hover ·
   focus-visible · pressed · selected · disabled · loading · error · read-only** (only the states that
   apply). **Lay it out by the component's width:** narrow atoms (buttons, chips, toggles, inputs) in a
   table, rows as variants and columns as states; anything wider than about 240 px (cards, panels,
   rows, drawers) as a wrapping grid of labelled tiles, **each tile at the component's real width**. A
   component is never squeezed to fit a column.
5. **Live specimen** — the real component, on its real surface, that responds to hover, focus (Tab),
   press and selection, so the reviewer feels the interaction.
6. **Micro-interactions** — a short table: trigger · what changes · duration · easing · reduced-motion
   behaviour. Durations come from the motion foundation (the kit's 150 ms `--ease`; large surfaces such
   as drawers up to twice that). States change colour, shadow, ring or a transform, **never padding,
   size, alignment or border width**.
7. **Sizes and density** — compact, default and comfortable, where the component has them.
8. **Content rules** — label length, truncation and where the full text goes, number formats, empty
   and overflow cases, with the real worst-case content from the seed data.
9. **Accessibility** — role, keyboard path, target size, focus order, what a screen reader announces,
   the non-drag alternative where it drags.
10. **Do and don't** — one of each, drawn, from a mistake this component is prone to.

**How the state matrix renders without a mouse.** After the expression kit, in the same `<style>`
block, add a **state-hook block**: for every `:hover`, `:focus-visible`, `:active` and selected rule in
the stylesheet and kit, repeat the same declarations under a state class — `.is-hover`, `.is-focus`,
`.is-active`, `.is-selected`, `.is-loading` (for example `.btn-p.is-hover{…}` copying `.btn-p:hover{…}`).
A specimen with `class="btn btn-p is-hover"` then shows the hover look. The stylesheet itself stays
verbatim; this block only mirrors it. The builder uses the real pseudo-classes; the state classes are
for the guide.

**Show components on their real material.** A component is drawn on the surface it lives on (a glass
card over the ambient field, the solid rung, the dark chrome), in both themes through the switch, never
on a flat white box. That is how the material quality shows.

**The finish bar for every component page:** parts aligned on one baseline, padding from the spacing
scale, a visible focus ring, icons at their optical size, no text squeezed or orphaned, and the
client's real content. A component page that would not pass for a page in Material or Carbon's
documentation is not finished.

---

## Foundation additions (so the new views render correctly)

These extend the foundations; they never move a measured value.

- **Semantic token tier.** Colour by job through a semantic alias layer, so the Step 3 reskin is
  near-mechanical and the hardcoded gradients and focus rings (`.btn-p`, `.msg.me`, `.tog.on`, the
  `rgba(0,113,206,…)` rings) stop slipping past the port.
- **Glass fallback.** Under `prefers-reduced-transparency`, Windows forced-colors, or a browser without
  `backdrop-filter`, glass falls back to the solid rung, so the page stays legible.
- **WCAG 2.2.** Targets at least 24×24 (buttons, pips, markers, slots, nodes); a visible, measured focus
  ring; a focused element never hidden by a sticky header, banner or the agent launcher; a non-drag
  alternative for every drag.
- **RTL and other scripts** (when the document names Arabic, Hebrew or CJK readers). CSS logical
  properties so the page mirrors; mirror directional icons only; allow for text growing 25–35%; add
  Arabic or CJK fallback fonts, since Archivo and IBM Plex Mono cover neither.
- **Stacking order.** base < sticky < dropdown < drawer < modal < toast < tooltip.
- **Motion.** Keep 120–160 ms and "nothing else moves"; feedback starts within 100 ms; each motion
  has a reason (orient, confirm, emphasise).
- **One visualization palette for all four engines.** Categorical, sequential, divergent and threshold
  palettes as separate jobs, colour-blind safe, never colour alone, and a table view for every chart.
- **Icons from one open, licensed set**, named in the style guide, plus the node, marker and edge
  glyphs the engines need.

**Parked:** design-token JSON export, multi-brand theming, locale formatting and pseudo-localisation,
product tours, a microcopy system, print and email rendering, executable audit tooling.

---

## Form — the parts people get wrong

* **No borders on cards.** Separation is elevation and tone, never a line. Hairlines *inside* a card
  — row separators, a divider between two regions — are fine; the rule is about the card's outline.
* **A card carrying colour gets exactly one treatment** — gradient wash alone, **or** solid tint plus
  one inset hairline. Never both. A gradient already says "selected"; a ring on top of it is the most
  common violation, and it shows up most on selected options inside a chat input. A solid tint
  without a ring reads as a flat slab, which is why the inverse holds.
* **Corner radius is a fixed five-step scale. Never improvise a value.** **10px** everywhere — cards,
  tiles, containers, inputs, selects, buttons, panes, drawers, modals, table containers · **6px**
  small inner elements — tags, chips, code · **pill** for toolbar search, facets and accent pills ·
  **circle** for avatars and account logos · **studio only** shell 28 / canvas 22 / sheet 16 /
  tile 12, because a 10px corner on an 1,100px object reads as a cut rather than a form. **Never
  8/12/14/16 outside that scale, and never a mix on one page** — mixed radii are the single most
  common reason a build reads as unfinished. ⚠️ A blanket flatten to 10px was tried on the SailPoint
  wireframe 22 Sept 2026 and reverted within the hour. **Do not re-propose it.**
* **Ambient aurora in the brand theme, never flat grey.** Layered low-opacity radial blooms
  distributed down the page so a long document does not go flat below the fold. Percentage-sized
  radials on the body; avoid `background-attachment: fixed`, which bands in full-page captures.
  **Dense internal tool: 3–4% maximum, two or three blooms, page body only** — never behind a table
  or a side pane, which take a solid near-white ground so rows stay legible.
* **Glass in three tiers plus a nested rung**, with a **1px inset top highlight** — that detail is
  what sells it as light catching an edge. Nested `inner` surfaces instead of a second bordered box
  is what stops a UI looking cheap.
* **Two elevation levels, never a third.** Resting and raised. Rows do not lift on hover; they change
  tone.
* **Four type sizes, two weights** (400/600), `tabular-nums` on every number. **The mono face is
  structural, not decorative** — table headers, eyebrows, KPI labels, citation and version chips take
  it; body copy never does. If the mono is not actually embedded the headers fall back silently and
  the whole grid loses its register.
* **One icon weight, two sizes** — 16px in tables and chips, 18px in nav. Stroke 1.6.
* **Motion is 120–160ms ease-out on panes, drawers and tonal hover, and nothing else moves.** No
  count-ups, no card entrance animations, no skeleton shimmer.
* **Tags are quiet and smaller than the smallest button** — 11–11.5px against a 13–14px button,
  tonal, no border, no sentence inside. A tag states a fact; it must never read as pressable.

## Components — the doctrine, not just the class

* **Every table gets a toolbar**: search left, filters right, nothing in the middle, **above and
  outside** the card (the card is the table's **ground**, not its container). The search **reports
  its result beside itself — "4 of 7"**. Three or four facets (D8), drawn from the visible rows so a
  facet can never offer a value returning nothing. Applied filters are removable chips with one
  *Clear all*.
  **⚠️ A filtered-empty table is NOT an empty table and they must never share a state.** *"No rows
  match your search and filters"* with a clear action is a different fact from *"No opportunities at
  Stage 20 yet"* with a create action. **Showing the second when the first is true is the single most
  common table bug and it makes working software look broken.** A static reference matrix — a
  discount-authority table, a legend, a key-value spec block — is not a record list and takes no
  toolbar.
* **Pagination is built once and reused.** The range names the **total** ("1–10 of 47"), reflects the
  filter, disables rather than hides at the ends, and does not appear under ~25 rows.
* **Every AI or system-generated insight goes in a labelled AI Insight card** — subtle brand
  gradient, one CTA inside the same card, overflow behind a chevron, never by growing the card or
  truncating mid-sentence. The user must always be able to tell what the data *says* from what we
  *inferred*. **Reference: Topcon's approval-suggestion step** — a *"Suggestion only — you decide"*
  chip, a grounding line naming the source SOP and precedent set, per-row confidence, a reason per
  row, **and one row deliberately excluded with its reason shown.** Copy that shape.
* **Kanban** is for states a person changes and items that can move *backwards*. Fixed-order work is
  a **stepper**. WIP limits shown in the attention tone. The drop zone is **the one dashed edge we
  allow**, because the dash means something; every other dashed edge is decoration.
* **Calendar has three shapes** — month grid ("when is it free"), agenda ("what is happening"), slot
  picker ("commit to one"). Shipping a month grid when the user must choose a *time* is the common
  version of this mistake. Today takes a ring, selection takes the fill, **never both on one cell**.
  A taken slot is struck through and disabled, **never hidden** — hiding it makes a busy day look
  empty.
* **A person is a record, not a string.** Person card or face stack anywhere a human is named. Cap
  the stack at three faces plus a count; the overflow chip is a count, not an avatar; initials, never
  a generic silhouette.
* **An activity feed is not a stepper** — a stepper's shape is known in advance, a feed's is not.
  Newest first, mono timestamps, actor and object bold but not the verb, automated entries say
  "System", and a change carries its reason. A history that records *what* without *why* gets
  re-litigated in a meeting.
* **Chart frame:** the system owns the card, title, **unit**, legend placement and no-data state; the
  ramp and marks follow the palette rules and the `dataviz` skill. A chart without a stated unit is a
  decoration. **Never colour a delta by its arithmetic sign** — colour it by whether the movement is
  good, and name the comparison period beside it. **A series that encodes a status (pass / fail,
  on track / off track) takes the status palette and a worded legend**, never steps of the brand
  colour — Vermont's pass-rate chart showed Fail, Needs attention and Pass as three blues.
* **Container doctrine:** **modal** only for irreversible or legally significant acts (withdraw,
  reject with mandatory reason, e-signature, stop ship) — blocking is the point, never nested, never
  holding a scrolling table · **right drawer** (~480px, dismissible) for configuration attached to
  the current record · **third pane** (persistent, resizable, pushes rather than overlays) for the
  inspector, whose whole value is surviving a move to the next row · **stepper** where the *order* is
  part of the meaning · **full page** only for objects deserving a shareable URL · **inline expand**
  for hierarchies · **bottom sheet** never, on desktop.
* **A control sits inside the boundary of what it changes** — no divider between an active tab and
  the panel it governs. **Named exception: the table toolbar**, above and outside the card.
* **Header carries identity, navigation context, notifications, profile. Nothing else.** No role or
  persona switcher — a visible `Planner · CSR · Manager · Auditor` control tells the client instantly
  this is a mock, and real RBAC is an attribute of the signed-in user, so role switching lives in the
  profile menu. No theme toggle, no demo-path control. A quiet scope indicator is fine.
* **Left nav: logo → navigation → profile at the bottom**, on the chrome the expression chose
  (`brand` gradient, `ink` or `light`), full height at every scroll position. With a top-navigation
  shell, the same order runs left to right.
* **The top bar is opaque.** Content scrolls under it without showing through it.
* **One composer per surface. One right-hand rail, not two** — assistant and inspector share it as
  two modes; opening the assistant swaps the mode and remembers the inspector's state.
* **The agent component — always a drawer, never a card on the page.** Pentland's Range Copilot was
  built as a full-width block on Home, wired as an automation that wrote answers into an object the
  page showed after a refresh. That is not an agent. The rule:
  - **Where it lives.** A right-side **drawer** (`.agent-drawer`, ~440 px) that slides over the page
    without reflowing it — the default on every internal page. It opens from a **top-bar button**, the
    floating **launcher** (`.agent-launch`) and a keyboard shortcut, and closes with Esc, returning
    focus. Variants, each for a reason: **wide** (720 px) while an answer carries a chart or table;
    **docked** as a third column (`.app.with-agent`) for personas who keep it open all session;
    **full screen** on a phone; **studio region** inside a two-pane artefact studio (interface left,
    conversation right, no card); **full page** only when the agent is the screen's whole purpose.
    One drawer at a time; it shares the right-hand side with the inspector as two modes.
  - **Anatomy, top to bottom.** Header: the agent's name, a scope chip (read-only, or what it can
    act on), expand / dock / close. Context chips: the record or page it is looking at. Thread: agent
    left, person right; the agent speaks first with three suggested prompts from the person's own data.
    Working stages while it thinks (`.stages`), named by what it is really doing. Answers rendered with
    their tool outputs — chart (chart engine, with unit), in-thread table, file card, citation chips
    with the evidence hover card, record links — each marked AI-written. Proposed actions as a
    **human-in-the-loop card** (`.ad-action` with `.ad-diff` before → after, approve and reject with a
    required reason). Dock: suggestion chips **outside** the composer, then the composer.
  - **Every state:** closed (launcher with an unread dot when the agent has something), opening, empty
    first run, thinking (stages), streaming, answered, partial answer with a gap named, refused (out of
    scope, with what to try instead), tool failed (which step, retry), offline, and read-only.
  - **How it is built.** On the platform's **live agent/chat component** — streamed replies, real
    stages from the agent run, tool outputs rendered as they arrive. Never an automation that stores
    the answer in an object for the page to pick up on refresh. The composition contract says so.
  - **AI on a page is not the agent.** A dashboard may carry an **AI insight card** (`.ai:not(.msg)`)
    that summarises and links "Ask about this" into the drawer, and a field may carry an AI-draft
    marker with an inline assist. The conversation itself always opens in the drawer.
  - **Loading is a sequence, not a spinner** — a copilot that shows its stages reads as reasoning, a
    spinner reads as latency. **The agent speaks first.**
* **No stacked sublines under headers, no redundant preview data.** One header, one line of support
  at most, and only if it carries something the header does not. Show data by the priority of the
  flow the user is in on the screen they are on.
* **A fifth data state: UNSET.** Beyond empty / loading / error / populated — **a field belonging to
  a journey the user has not completed shows as visibly unset, never a seeded default dressed as
  their own answer.** On one build this produced a cost one-pager reading $26,250 against an actual
  $55,550 and a visit "booked" for March 2011, while the Next card told her to plan the visit the
  one-pager said was already booked.

## Layout, spacing, density and overlays — the rules the v5 screenshots broke

Every rule below comes from a screenshot of a v5 output. They apply to every screen that is drawn, and the builder applies them to every page it composes.

**Spacing.**
- Only the spacing scale (`--s-1` 4 px to `--s-12` 48 px). Page padding 24 px (16 px on a phone),
  24 px between sections, card padding 20 px (16 compact, 24 comfortable), 8 px between related
  controls, 4 px between a label and its value. No other values.
- **Equal rhythm inside a row of cards**: the same padding, the same order of parts (eyebrow → value →
  support line), top-aligned. A label that wraps to two lines must not push its value below its
  neighbours' (image 1: "Candidates in pools" pushed 77 down) — shorten the label or let the eyebrow
  row reserve two lines across the whole row.

**Filling the space — no dead areas.**
- **A row fills its width.** Tile rows use as many equal columns as tiles (3, 4, 5 or 6) across the
  full content width. Two-panel screens split 8/4 or 7/5 of a 12-column grid. A row that leaves a
  large empty area on the right, or a card with a large empty area below its content, is redesigned:
  move a related panel into the gap, or let the content take the width.
- **Headers carry their actions on the title row.** Page header: title left, primary action right,
  same line. Record header: ID eyebrow, title with status tags, one meta line; actions right-aligned on
  the title row — never floating in their own row with empty space beside them (image 5).
- **Definition lists** (`.dl`) use a label column of 120–160 px, never wider (image 5's 250 px label
  column left a channel of white).
- **Specimen height fits the content.** Device specimens size to their content; a fixed height only
  when the screen scrolls by design.

**Density — what fits in a cell, a card, a column.**
- **Tables: one line per cell by default; at most two in the first column** (name over one muted line).
  Longer text is truncated with an ellipsis and the full value in a tooltip, or moves to an expanded row
  (`.row-x`) or the detail drawer. **No paragraphs in cells** — image 4's reasons paragraph and
  four-row sub-score breakdown belong in the expanded row.
- **At most two chips per cell, then "+n"** (`.cell-chips`, `.more`). One status tag per cell. Nothing
  in a cell overlaps or leaves its cell (image 4: a source pill sat on the "Approved" chip; the status
  tag was cut off at the table edge).
- **Column budget at 1,280 px: about seven columns.** More columns → a column picker, a frozen first
  column (`.tblwrap.freeze`) and horizontal scroll inside the table. Minimum widths: ID 96 px, name
  200 px, status 120 px, number 80 px, date 104 px. Numbers right-aligned in tabular figures.
- **Cards in narrow columns** (kanban, lists): a card is at least 240 px wide and holds at most four
  lines — title, one meta line, one status, one blocking or next-action line. No two-column layout
  inside a card narrower than 320 px. Long status text truncates (image 2: "Feedback 2 days overdue"
  left the card; "No feedback yet" wrapped to three lines).
- **Row heights follow density**: 36 / 44 / 52 px for compact / default / comfortable, set by the
  persona (0.4), never mixed on one screen.

**Copy inside specimens.**
- **Never show field names, query syntax or rule expressions as text** — image 1's tiles read
  "status = open" and "interview_count > 0". Write what the person needs: "of 11 jobs", "3 with
  feedback overdue".
- IDs in mono only where the person really uses them (a requisition number), never as decoration.

**States never move the layout.** Hover, selected, focus and active change colour, shadow or an inset
ring — never padding, size, alignment or border width (image 1: the selected "On hold" tile grew a
thick border and centred its text).

**States are drawn once, in the component pages, not per screen.** Empty, loading, error,
filtered-empty, no-access and UNSET are documented as components, and one of them may appear in context
on one of the five screens. The builder applies them to every
page it composes. **Never several full app shells side by side** (images 3 and 6: three shells in one
row left a 200 px content area and one word per line).

**Overlays — one system** (kit: `.modal`, `.drawer`, `.agent-drawer`, `.ov-hd/.ov-bd/.ov-ft`):

| Overlay | Width | Height | When |
| --- | --- | --- | --- |
| Modal S | 420 px | content, max screen − 64 px | confirm an irreversible act |
| Modal M | 560 px | content, max screen − 64 px | a short form |
| Modal L | 760 px | content, max screen − 64 px | review or compare before committing |
| Drawer S | 420 px | full height | the agent; a quick peek |
| Drawer M | 560 px | full height | record detail, inspector, filters |
| Drawer L | 760 px | full height | the agent with a chart or table; a long form beside the list |
| Agent docked | 420 px column | full height | only at 1,440 px and wider |

Same header (title, one line of support, close), same body padding, same footer (secondary actions
left of primary, primary last on the right, a destructive primary in the negative tone). One overlay
at a time; a drawer never opens a modal on top of itself except to confirm. Image 7's agent filled
most of the screen because it was a docked column at 1,280 px; the kit now forbids it.

## The use-case dial

Same system, same components, both themes. What moves is restraint, ground and radius scale.

| Use case | Ambient | Ground | Radii | Colour |
| --- | --- | --- | --- | --- |
| **Dense internal tool** (PLM, config, ops console) | aurora 3–4%, 2–3 blooms, body only | solid near-white behind tables and side panes | 10 / 6 / pill | brand on primary action, active nav, selected — nothing else |
| **Client-facing demo surface** | full aurora, blur 58–70px, vignette | glass tiers 1–3 | 10 / 6 / pill / circle | brand gradient on the nav rail; one accent pill |
| **Artefact / document studio** | quiet — the canvas is the subject | sheet white on a tinted shell | 28 / 22 / 16 / 12 | greyscale plus one brand accent |
| **Dark-first ops console** | blooms *lighter* than the page | opaque rung for any container holding glass | 10 / 6 / pill | brand-as-text steps up; brand-as-fill holds |
| **Ported screens from another build** | inherit the host | — | **normalised, see below** | inherit |

**Ported code gets one card, imposed from outside.** Screens from a separate build each bring their
own idea of a card — on the Enroll · Belong canvases there were **six paddings, four radii and three
shadows** between them, invisible one screen at a time and obvious the moment a dozen stack in one
column. **Do not edit them one by one.** One normalising block at the end of the ported stylesheet:
one radius, one surface, one shadow · **three padding tokens only** — a card you read into, a row
inside a card, a compact cell · a card holding rows takes **no padding of its own** and its rows
carry the rhythm · **media cropped to one aspect ratio** (`height:auto` on an illustration is how two
cards in a row end up different heights) · **restate the selected and status rings after the
normaliser** or the reset eats them · check the containers too — the agent's note, the stepper and
the action bar must sit in the **same column** as the cards.

## The defect register — re-derived on the system itself

**⛔ A figure asserted about the system from a measurement taken on a PORT of it is not evidence.**
One "defect" was recorded that way — a claim that §14's chart ramp fails its own 2.60 figure — and
had to be **withdrawn**: measured across all twenty triples, the best is exactly 2.60, and the dark
pair is exactly 4.24, both as the document claims. A luminance-preserving port makes this trap
worse, not better, because the port's numbers genuinely are the source's, so a wrong number looks
doubly confirmed. **Check every "the file says" against the file.**

The standing lessons, all derived from defects on the record:

* **White on the brand fill** — check every gradient stop, not just the mid one.
* **`.ai` vs `.msg.ai`** — an unscoped insight-card selector captures every agent chat turn.
* **Nested glass in dark** — a container holding glass takes the opaque rung.
* **A theme with no switch** follows the reader's OS and half your work is invisible.
* **Bare rgb triples** survive any regex port.
* **A wrong number in a document is not a wrong colour.** Correct the number.

**Added in v5, from the Pentland, ClickUp, Vermont and Topcon runs:**

* **Same core, same look** — with the logo covered the four apps were one product. The core stays
  fixed; the expression (Step 2c) must differ, with evidence.
* **An agent on a page** — Pentland's Copilot as a full-width block, fed by an automation and a
  refresh. Agents live in the drawer, on the live agent component.
* **A brand decided outside the file** — three runs settled a hue conflict with a "standing decision"
  from the calling flow; Pentland's black-and-lime brand shipped electric blue. Only the brand source
  order decides.
* **Must-haves moved to future scope** — Pentland's material compare, detail pane and docked Copilot
  were L1 and were dropped. Every L1 ID maps to an inventory row.
* **Journeys never drawn** — refusals, approvals and counters were in the scoping document and nowhere
  on the page. Every journey is a flow (0.7).
* **Status as brand steps** — Vermont's chart showed fail and pass as shades of blue.
* **A rail that stops, a bar you can see through** — layout defects in the build that the kit and the
  composition contract now prevent.
* **Personas without screens** — Vermont's merchandiser had no phone or tablet layout reachable from
  any shell.
* **A dull dark** — mid-slate grounds and heavy glass; failing contrast on its own tiers. Rebuilt.

**Added in v5.1, from the first v5 runs and their review screenshots:**

* **Screens at the wrong width** — "1,280 px" screens drawn in a narrower column took the desktop
  layout at half width: state screens one word per line, a docked Copilot covering the page. Every
  screen is now a device at real width, scaled.
* **Overlays of every size** — modals and drawers improvised per run. One overlay system, three sizes.
* **Dense tables and cards** — paragraphs, four-row breakdowns and stacked pills in cells; two-column
  layouts in 240 px kanban cards. Density rules with hard limits.
* **Dead space** — half-empty rows, actions floating in their own row, a 250 px label column.
* **Implementation leaking into copy** — "status = open" as a tile's support line.
* **Unbounded variants** — options with no codes and no way for the builder to pick one coherently.
  Coded variants, at most three style sets, one active.

## The finished-piece rule — no rework after hand-over

**What this skill hands over is the final piece.** The person receiving it should be able to use it
as it is: open the style guide, take the token block, drop in the logo kit, give the composition
contract to the builder. Never hand over a partial build, a "first pass", or a list of things still to do.

**Build first, review, then check once.** Do not run the full checklist after every fix. Build the
page, then do the design review below, then run the render check (Step 6) and the checklist once, fix
what fails, and re-check only the items that failed.

### The design review — taste, before the checklist

The checklist proves the page is correct; the review decides whether it is **good**. Done once, before
the checklist. If the session can start a separate agent, give it the review with only the finished
file, the expression card and the inspiration board, so the work is not grading itself; otherwise do it
yourself with fresh eyes on the screenshots.

**1 · Hunt the generic tells.** Each of these makes a system look templated. Any that appears is either
justified by the concept on the page, in one line, or replaced:

- the same four stat cards across the top of the dashboard
- a list with a right rail of summary cards as the answer to every page
- purple or rainbow AI sparkles on every AI element
- a gradient hero or banner with no reason from the brand
- empty states with a generic icon and "No data yet"
- every card the same size in a uniform grid
- icons decorating labels that do not need them
- every chart a plain bar or line in the default palette
- the concept named on the expression card but visible nowhere on the page

**2 · Score the page against the inspiration references**, 1 to 5 each: **distinctiveness** (with the
logo covered, is it recognisably this client's?), **hierarchy** (is the one most important thing on each
screen obvious?), **rhythm** (spacing and alignment consistent?), **finish** (states, focus, edges,
type set with care), **concept** (does the idea show where it should, and stay quiet elsewhere?).

**3 · Fix the three weakest points** and record the scores, before and after, in the port note. In POC Studio the AI PM rescores the same five dimensions from its own screenshots and re-runs the render check; a self-score more than one point above its score is a finding, so score honestly. A page
scoring under 4 on distinctiveness or finish is not ready, whatever the checklist says.

**The checklist — ten items:**

1. **Components complete, screens few.** Every component the inventory needs has a full component
   page (anatomy, coded variants, the static state matrix, a live specimen, micro-interactions, sizes,
   content rules, accessibility, do and don't). Every hover, focus and press rule has its state class,
   so the matrix renders without a mouse. Every chosen pattern has a blueprint (with wireframes: only
   patterns no frame shows). **At most five full screens.** Count both with a script. With wireframes,
   the component pages are exactly the manifest's components plus the baseline (0.0, checked by script).
2. **Scope and coverage.** Every L1 feature ID and component ID in the document appears in the
   inventory (checked by script; with wireframes, every manifest component and frame page instead). Nothing the document put out of scope appears; dormant views are listed
   as not built.
3. **Journeys and signature work.** Every journey is a flow diagram with the document's exact wording
   for refusals and messages (count journeys in the document and diagrams on the page; they match). The
   demo storyline's steps each point to a screen or component page. Each signature component shows anatomy, every state, data
   variants, interactions, responsive behaviour and two layouts. The main agent's drawer is open on one
   of the five screens; every other agent is on the agent-drawer component page; no agent sits in a
   page layout.
4. **The builder has answers, not options.** The contract and `#build-plan` cover every inventory page
   (pattern, region fillers, reason) and give rules for unlisted pages; `#style-sets` has one active set;
   every specimen carries `data-component`, `data-variant` and `data-active`, and every non-active
   variant is labelled "Reference — not in this app". The contract quotes the default interactions, the
   live-agent rule and the UX laws, and matches the expression card and kit classes.
5. **Brand and research settled.** Research questions 1 to 3 met Deep; the rest met their depth or are
   recorded as `[DERIVED]` with what was tried; the ledger and every source with its date are in the port
   note. The expression card records the design concept with its evidence, every dial with its evidence, and
   the logo-off answer; the concept is visible in the signature components, the variants and the one
   signature interaction.
6. **Both themes measured.** The contrast audit ran in light and dark; every failure is fixed; the ratios
   in the token block match the rendered page.
7. **Renders clean.** One self-contained HTML file, fonts and images embedded. The render check returns
   zero page scroll, spills, clips, vertical clips, overlaps and squeezed text anywhere on the page —
   screens, component pages, state matrices, diagrams and the guide's navigation — zero broken images,
   every font loaded, no unstyled component class, in light and dark, at 1,280 × 800, 1,280 × 680 and
   375 × 812. The only allowed flags are two-line labels in documentation tables, each checked by eye.
   Also look at a screenshot of the navigation and of one state matrix at 1,280 × 680.
8. **Layout and density hold.** No large dead areas; actions on the header's title row; one line per
   table cell (two in the first column); at most two chips per cell; cards within four lines; no field
   names or query syntax in copy; states do not move the layout; overlays use the kit sizes and anatomy.
9. **No leftovers, no generic tells.** No `TODO`, `TBD`, `lorem`, `placeholder`, empty links or empty
   sections, and no "demo" or "synthetic" labels anywhere. The design review ran, its scores are in the
   port note, distinctiveness and finish are 4 or more, and every generic tell left is justified. The
   theme switch, tabs, links and copy buttons work with no console errors. The one allowed exception is
   the labelled UnifyApps stand-in logo, and only under the conditions in stop 2.
10. **Consistent and handed over.** Token names, port note, build brief and style guide agree on every
    number. The three hand-over answers are written in the page's last section.

**Show the result.** The hand-over reply lists the ten items with pass and one line of evidence each
(for example "1 · pass · 5 patterns, 31 components, 5 drawn screens"). An item that cannot show
evidence has not passed.

**A failure found here is fixed here, not reported as a known issue.** Only something that genuinely
cannot be fixed inside this run (the client's logo file does not exist anywhere) goes into the
hand-over, with the reason.

## Hand it over with these three answers

Write them in the style guide's last section and repeat them in the reply.

> **What is the WOW factor here? Name it in one sentence.**
> **What would the client push back on first?**
> **What is the weakest part, and do you know it?**

**Answering the third honestly is not a confession, it is the deliverable.** A hand-over that names
its own weakest part gets fixed; one that hides it gets found.
---

## Version history — why each layer exists

Read only when a rule seems odd; each line names the run that caused it.

- **v3** — Phase 0 (the selection engine), the view library, the component inventory with the universal
  state rule, foundation additions.
- **v4** — the research plan became mandatory, with depths and a ledger.
- **v5** — after Pentland, ClickUp, Vermont and Topcon came out as one product in four hues: journeys as
  flows (0.7), signature components (0.8), the agent drawer (0.9), the expression (Step 2c), a fixed
  brand source order, a rebuilt dark theme, inspiration research, the build contract, rendering safety.
- **v5.1 / v6** — consistency and density: screens in devices at real width, one overlay system,
  spacing and density tokens, table and card limits, coded variants and style sets, chart views, the
  render check.
- **v7** — after Agthia, Vermont, American Airlines, Asian Paints and Pentland were built and inspected
  live: every app was the same layout grammar, because the file pre-drew every page and the builder
  pasted it. The deliverable became a kit, not a page set (0.6); the composition model (component
  variants, layout patterns, the seeded chooser, the UX laws); a build contract that tells the builder
  to compose.
- **v8** — after the first v7 run (Asian Paints) drew 74 screens and took about 50 minutes: at most
  five full screens, with the depth moved into component pages (anatomy, variants, a static state
  matrix with state classes, a live specimen, micro-interactions, accessibility, do and don't);
  foundations show the material properly; patterns as blueprints; every journey, the demo storyline
  included, as a flow diagram with exact wording; the guide laid out like a design-system site; S1
  only unless options are asked for; research Deep only for colours, typeface and logo; a ten-item
  checklist run once; about 4,000 words of repetition removed. Then, so the builder never has to
  choose and the output stands out: a design concept per client that shapes the signature components,
  variants and one signature interaction; variants designed per client; all choosing done in this run
  (best fit first, the seed only for ties) and handed over as `#build-plan` with lookup rules for
  unlisted pages and `data-active` tags on every specimen; a design review with a list of generic tells
  and scores for distinctiveness and finish.
- **v9.1** — after the first V9 run (Fujairah Ports Authority) rendered with three defects the render
  check did not catch or let pass: the guide's left navigation squeezed to half-height overlapping
  labels; state matrices forced wide components into narrow columns; swimlane diagrams ran past their
  column with no scroll cue. Added the rules for each (Rendering safety), a `vclipped` count to the
  render check, a short-laptop viewport, and made every flag a defect outside two-line table labels.
- **v10 (POC Studio edition)** — v9.1 adopted into the POC Studio plugin, with these edits: the
  UnifyApps stand-in logo when no client logo file exists (stop 2, and the one exception to checklist
  item 9); the builder's block named the composition contract everywhere; the example evidence line
  matches the five-screen limit; every research request states its search budget, because the
  `research` skill reads Quick, Standard and Deep as larger counts; no named reviewers in the
  hand-over questions.
- **v10.1 (POC Studio 1.26)** — approved low-fidelity wireframes come before this skill (0.0): their manifest is the
  component inventory, their frames are the layouts, nothing is proposed, the baseline is always built. Design
  systems had grown an open-ended component list; the frames close it.
