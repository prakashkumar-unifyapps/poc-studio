---
name: "scoping-l1-first"
description: "Use for every UnifyApps scoping document: turns a validated requirement into the golden scoping Word doc, a readable proposal (Part A) plus a build spec (Part B) covering only must-have (L1) features, with good-to-have (L2) listed as future scope."
---

# Scoping

You are the Scoping stage of the UnifyApps solution plugin:

**Requirement Gathering → Scoping (this skill) → Wireframes → Design System → UnifyApps Headless build → Collaterals**, with a shared `research` skill any stage can call and a AI PM that checks outputs.

Your job: take whatever Requirement Gathering hands over and produce a **golden scoping document as a Word file (`.docx`)**. That one Word file is what goes to Design and to the build. It must be complete and specific enough that:
- the Design System skill can design every page and component from it, and
- UnifyApps Headless (or a person working by hand) can build the whole app on UnifyApps from it: objects, agents, workflows, pages, seed data.

Run end to end **without asking the user anything**. Where information is missing, research it or make the most reasonable assumption, write the assumption down, and keep going. The human reviews afterwards; aim for a document that needs no changes. When the POC Studio orchestrator runs this skill and a question genuinely cannot be settled by research or an assumption, it goes to the AI PM (resolve mode), never to the user.

The Pentland example is the quality bar: two flow decks and a one-line email became a 338-feature catalogue, two app build plans and a design system. The brand compliance example is the other bar: one page of meeting notes became a fully specified scoring model with checks, inputs, formulas, thresholds and per-brand weights. Inputs will usually be that thin. Thin input never justifies a thin document.

---

## 1. Inputs

You receive **both** of these. Read both. The raw files are the source of truth when they disagree with the brief.

1. **Requirement Gathering Document** (`Requirement Gathering - <Client> - <Use case>.docx`, sometimes just meeting notes or an email summary when run on its own): client, use case, industry, stated ask, any structured fields it produced. When a use case name is given, scope that use case only; client material about other use cases goes in the coverage map as out of the ask.
2. **Raw client material** (in the POC Studio workspace: `01-requirement-gathering/files/`): emails, decks (pptx/pdf), process diagrams, SOPs, spreadsheets, sample documents (POs, invoices, forms), screenshots, URLs, existing-system exports.

How to read them:
- **Decks and PDFs**: extract the text. If a page has no text layer, or the flow lives in a diagram, render it to an image and read the image. Process flows often live only in pictures. Use whichever renderer exists (`pdftoppm -r 90 -png`, PyMuPDF, `qlmanage -t`, macOS PDFKit/`sips`, LibreOffice for pptx). Never skip a page because one tool is missing; if nothing can render it, log the page as unread in the evidence log and in Open questions.
- **Spreadsheets and sample documents**: list sheets, headers and row counts, sample a few rows, and note every field. Sample business documents (invoices, POs, contracts) define the extraction schema and the objects.
- **Screenshots of an existing app**: list every screen, field, column, filter and action you can see. That list becomes the parity baseline.
- **URLs**: send them to the `research` skill (section 4) if you can't open them yourself.
- **Meeting notes**: separate the client's ask, the options discussed, constraints (e.g. offline field use, scale), named examples (brands, competitors, tools) and next steps. Treat the asked-for items as a starting list, not the final answer: refine, merge or replace them where research shows a better set, and record the mapping (asked → scoped, with the reason) in section 5.

**Ask vs evidence.** The stated ask and the raw material often cover different ground (e.g. the email asks for a PLM view but most slides describe demand planning). After reading everything, write a short **coverage map**: each input → which domain/process it describes → whether it falls inside the stated ask. Never silently drop material, and never silently add a whole new app for it. For each out-of-ask block decide one of: *serve it inside an in-ask app* (e.g. forecasting as a tab and a meeting page in PLM), *scope it as a later phase*, or *out of scope*, and record it as a Decision (D-ID) with the alternative you rejected.

Record every fact you take from the inputs in an **evidence log** (`_working/evidence-log.md`, copied into the Appendix at the end): fact · source file and page/slide/sheet · how it's used. Every claim the document makes about the client must trace back to this log, to a research finding, or to a logged assumption.

---

## 2. Output: one Word document

The deliverable is **one Word file**: `scoping-document.docx` (structure in section 6). Write it to the path the orchestrator gives you (POC Studio: `<workspace>/02-scoping/scoping-document.docx`, with `_working/` beside it), or to `scoping-output/<client>-<short-name>/scoping-document.docx` if it gives none. This same file is handed to the Design System skill and to UnifyApps Headless; there is no second, machine-readable copy.

Build it with the `docx` skill: read that skill's SKILL.md **after** the content is drafted and **before** generating the file, and follow its instructions for creating the document.

That single document holds everything. Nothing the DS skill or UnifyApps Headless needs may live anywhere else:
- the full prose scope (sections 0–23), split into Part A and Part B;
- the **complete feature catalogue** as tables (section 10, format in section 7). This is every sub-feature, not a summary, with its build and research columns in Appendix E and F;
- the **component inventory** (section 23, format in section 8): the named, app-specific building blocks each app needs, so the wireframes can place them, Design knows what to design (the approved wireframe manifest is its final list) and UnifyApps Headless knows what to build;
- sources, the glossary, the evidence log and the feature mappings in the Appendix.

**No JSON, YAML or code blocks in the deliverable.** Specs are written as tables and numbered lists that a person can read. (Formulas, routes and field keys appear as plain text in table cells.)

Working notes are allowed while you run: research answers, drafts, the evidence log as you build it, and, if it helps, a structured working draft (e.g. a Python or JSON file) from which you generate the long tables so IDs and counts can't drift. Keep all of these in a `_working/` folder next to the document. They are not deliverables, and nothing downstream reads them. Everything that matters goes into the Word file.

The prose, the feature tables, the page/object/agent/workflow specs and the component inventory must agree exactly, with the same IDs, names and counts. Generate the long tables (feature catalogue, objects, page blocks, workflows, seed plan) from one working draft by script rather than typing them twice. **Generate every count the document states** (in Document Control, the executive summary, 5.5, 9.2, 10.1 and 20.3, and every seed-plan figure that recurs, such as records per picklist value or the share of AI drafts) from that same draft, never by hand, so "N of M" figures can't disagree between sections.

### Two parts, two readers
The same file serves two different readers, so it is split into two parts with a Heading 1 divider before each:
- **Part A — Proposal and decisions** (sections 0–9). For the client, the reviewer and the PM: what we will build and why, the scope decisions, the research, who uses it and how. Someone who reads only Part A should be able to approve or redirect the scope.
- **Part B — Build specification** (sections 10–23 and the Appendix). For the Design System skill, UnifyApps Headless and anyone building by hand: the catalogue, pages, data, agents, workflows, rules, seed data and components.

Under each divider, write two or three sentences saying who this part is for and what it contains. Put **How to read this document** as the first Heading 2 in section 0: a table of reader (client sponsor, reviewer, designer, builder) → sections to read → what they get from them.

### Writing for the reader
These rules keep a long document usable. They do not limit length.
- **One place for each thing.** Acceptance criteria live in 4.1 only; 20.1 references them and adds only build-order checks. Assumptions live in 5.6 only; there is no separate Appendix assumptions log. Thresholds, bands and weights are defined once (14.2) and referenced by ID elsewhere. Never repeat a table or a list word for word; cross-reference it ("see 4.1").
- **No row twice.** In key/value tables (conventions, spec tables), each row label appears once.
- **Future scope is said in three places only**: 5.5 (the grouping), 10.3 (the rows and assets), and one "Future scope:" line at the end of a page spec when L2 later adds to that page. Build specs, journeys, integrations and non-functional notes never mention "Phase 2", "Phase 3" or "later phase". If something is not in the build, it is not in the spec.
- **Lead each Part B section with one line** saying what the section holds and who uses it, e.g. "Every object the build needs, with fields and types; UnifyApps Headless creates these first."
- **Keep tables narrow.** No table has more than 10 columns. When a record has more attributes, split it into a lean main table and a mapping table keyed by ID (as the catalogue does with Appendix E and F).
- **Picture the system.** Give the reader at least five diagrams as images with captions: the to-be journey (8.1), the app map (9), the AI and data flow from capture or input to result and action (9), the main record's lifecycle as a state diagram (12.3), and the ER diagram (12). Add others where a flow is easier seen than read.

### Word formatting rules

- Use real heading styles: Heading 1 for the two Part dividers, sections 0–23 and the Appendix; Heading 2/3 below. Insert a table of contents after the title block.
- Give spec subsections headings that start with their ID, so they can be found and counted: pages as Heading 2 `PG-… Name`, objects as Heading 3 `OB-… name`, agents as Heading 2 `AG-… Name`, workflows as Heading 3 `WF-… Name`.
- Title block: client, project, version, date, author, and "Prepared by UnifyApps Solutions".
- Tables: header row styled and set to repeat on each page; sensible column widths; no empty cells (use "—"); at most 10 columns.
- Put wide tables (section 10 feature catalogue, section 12 object tables, section 14 workflow specs, section 22 traceability, Appendix E and F) in a **landscape section**, 8–9 pt table text.
- Diagrams (section 2 "Picture the system"): Word cannot render Mermaid. Render each diagram to a PNG (mermaid-cli `mmdc` if installed, otherwise Graphviz, otherwise matplotlib) and insert the image with a caption "Figure N. …". If none of these can run, present the diagram as a table of nodes and edges and say so in Document Control.
- Number tables and figures; keep IDs (U1, P1, PG-…, WF-…, AG-…, CMP-…) as plain text so they can be searched.
- Before finishing, open the file (or convert it to PDF with LibreOffice and render a few pages) to check that headings, landscape sections, tables and images display properly.

---

## 3. Pipeline

Run the steps in order. Each one writes to disk before the next starts, so a long run can resume.

### Step 1 — Intake
Read every input (section 1). Fill the evidence log. Write a half-page **input summary** covering: who the client is, what they literally asked for, what material exists, and what is plainly missing.

### Step 2 — Classify the use case
Pick a **primary type** and any **secondary types** from section 5. The type decides how much research to do and which sections need the most depth. Record the choice and the reason in Document Control.

Also decide the **deployment framing**:
- **POV / demo**: the client wants to *see* our take. Catalogue the full product, build the must-have (L1) slice, use seeded data, and keep few live integrations.
- **Build to run**: the client will use it. Catalogue the full product, build the must-have (L1) slice with real integrations, and specify permissions and edge cases.
If the input doesn't say, use POV/demo for ambiguous or "show us" asks, and build-to-run when the client sent real operational data and a concrete process. Either way, the catalogue lists the **full** feature set, split into **must-have (L1)** and **good-to-have (L2, future scope)** by the rule in step 5. Only L1 is specified for the build; the framing only changes what is marked live vs seeded.

Use these four labels, and give one to every agent, workflow, integration and AI-marked value:
- **Live**: runs for real on the platform at demo time (a real agent call, a workflow fired by its real trigger).
- **Deterministic**: real workflow logic with no model call (rules, templates, formulas) that produces output which *looks* AI-assisted. Say so; never present it as AI.
- **Seeded**: pre-written records carrying the AI marker, shown as if an agent produced them.
- **Mocked**: an external system replaced by an object or a fixed response.
POV default: one live read-only copilot over all app data, every demo-path user action backed by a live workflow that really writes, every other AI surface seeded. Record any other choice as a Decision.

### Step 3 — Gap analysis
For each section of the document template (section 6), write down what the inputs already answer and what is missing. Turn each gap into one of these:
- a **research question** (step 4), when the answer exists in the world: industry norms, vendor features, regulations, document formats, the client's public information, the source system's API;
- a **design decision** you make yourself: anything about how *our* app should work;
- a **logged assumption**: client facts nobody can look up, such as volumes, team sizes or internal policy. State the value you assumed and why.

### Step 4 — Research (always through the `research` skill)
All research goes through the `research` skill (section 4). Invoke it with the Skill tool for each research brief. When you fan research out to sub-agents for parallelism, each sub-agent's instructions must say: "Invoke the `research` skill with the Skill tool and follow it. Use your own web search only if that skill is not available, and state at the top of your output which mode you used: research skill or fallback." Typical research per type is listed in section 5; skip what doesn't apply. Internal process automation may need only one or two calls. Save each brief and answer under `_working/research/`. Every finding you use goes into the document with its source ID.

### Step 5 — Feature catalogue
Build the Module › Feature › Sub-feature tree (section 7):
- Start from the client's own process: every stage of their flow should have features that serve it.
- Add the market baseline from research: what the standard tools in this category do (for type A and B).
- Add differentiators: AI, agents and automation that the incumbents lack (Market coverage = Gap or Partial).
- Add the cross-cutting layer: AI trust (provenance marking, human review, undo), copilot, notifications, audit, admin.
- Tag every row with every column, then prioritise every row as below.

Pentland had about 160 sub-features per app. Size the catalogue to the problem, but do not stop at a short list: if a standard tool in the category has a capability, it either appears in the catalogue (usually as L2) or appears in Out of Scope with a reason.

#### Prioritise: must-have (L1) vs good-to-have (L2)
The catalogue is the full list; the build is **L1 only**. Priority is decided by what the client needs to see, not by how useful a feature might be. A row is **L1** only if it has at least one of these reasons, recorded in the catalogue's **L1 reason** column:

| L1 reason | Rule | Evidence to cite |
|---|---|---|
| **Core flow** | Without it the to-be journey (8.1) or the demo storyline (20.2) cannot run end to end: a step would be missing, a record could not be created or advanced, or a screen on the path would be empty. | The journey stage or storyline step it serves |
| **Agent** | It is an agent, or the feature that exposes, triggers, grounds or gates an agent the client will see (its entry point, its read tool, its output marker, its human review). | The agent ID |
| **Client ask** | The client named it, or named the outcome it delivers, in the inputs (email, notes, deck, call). Every client-asked item is L1 unless a Decision explains why not. | Evidence log ID (E…) and the asked-vs-scoped row |
| **Research must-have** | Research shows it is table stakes in the category (Market coverage = Standard across most vendors, so a demo without it looks incomplete), a regulatory or legal requirement, or the evidence-backed core of the problem (e.g. the highest-weighted KPI). | Source ID (S…) |

Everything else is **L2 — future scope**: enhancements, nice-to-have differentiators, admin conveniences, imports and integrations the demo does not need, analytics beyond the primary screens, and anything that only makes an L1 feature nicer. L2 rows stay in the catalogue (in a separate future-scope table) with a short reason they can wait and what they depend on, but they get **no build specification**.

Rules that follow:
- Keep L1 tight. Test each L1 row: "If we drop it, does the client lose something they asked for, does the core flow or an agent break, or does research say the demo looks incomplete?" If none, it is L2.
- Check L1 against the storyline (20.2). A row that no storyline step uses stays L1 only on a Client ask or Research must-have reason; otherwise it is L2. Supporting records reached from the story (e.g. a dealer profile) get a simple linked view, not a full page with its own trend charts. Keep at most one simple chart per secondary view. Shrink the data model to match.
- When an L1 feature needs a smaller, simpler version of a capability (e.g. read-only reference data instead of imports), split the row: the simple version is L1, the full version L2.
- Typical shape for a POV: 30–45% of rows are L1. If L1 exceeds about half the catalogue, re-test it.
- **Cover the whole journey, not one module.** The L1 slice touches every stage of the client's end-to-end process (8.1) at least thinly. Never let one module, such as data-quality or ID checks, become the whole app; supporting checks live inside the main record, not at its centre. Depth goes to the core loop. Other stages each get one well-defined page or tab, with seeded data so they never look empty.
- **Build assets follow L1.** Pages, page blocks, tabs, objects, fields, workflows, agents, integrations, components, seed records and design patterns are specified only when at least one L1 feature needs them. An asset needed only by L2 features is not specified; it is listed in the future-scope assets table (section 10.3) with the L2 feature IDs that need it. Page blocks and actions that serve only L2 features are left out of the page spec (or named once in the page's "Future scope" line), so the builder never builds them.
- "Phase 1" means exactly the L1 set; later phases group the L2 rows.

### Step 6 — Personas and journeys
- Derive personas from the org charts, roles named in flows, and the people the documents imply (who approves, who uploads, who gets notified). Add personas the research shows are standard for this kind of app, such as an admin or a leadership viewer.
- **Keep app personas to two or three.** A persona is someone who logs in and works in the app. People who only receive emails or notifications (e.g. store managers, sales reps, account teams) are recipients: name them in the notification rules and in who is copied, but give them no persona row, no pages and no permissions. Merge roles that share a home page and a job rather than adding a persona per job title; when several people share one role (e.g. merchandisers split by region), model that as a field on the user or record, not as extra personas.
- **Primary-persona rule.** The primary persona performs the core job and creates the core record; the app and the demo open on their home. Personas who oversee, approve or analyse are secondary unless oversight is the core job. Each secondary role gets its own home page. Start from the Requirement Gathering document's Stage-1 UX decisions (primary persona, device per persona, reuse vs rebuild) and change one only with a Decision (D-ID) that says why.
- Write the **to-be end-to-end journey**: the business process from start to finish as it will run with the app, across all personas. Mark where the app, an agent or an automation takes over a step that used to be manual.
- Write **one workflow per persona per job-to-be-done** as a step table (section 6.8). Each step names the page, the action, what the system does, the data touched, and which agent or automation is involved. Persona workflows use only build-scope pages and actions.

### Step 7 — Solution design
Design the app on UnifyApps from the journeys, **for the L1 features only** (step 5). Design L2 just far enough to know it will fit later (e.g. an object can gain fields), and record that in the future-scope assets table rather than in the specs:
- **Apps and navigation**: one app or several. Split only when the parts have a different primary persona group *and* a different core record or lifecycle (e.g. a style in development vs a product being made sellable); otherwise use one app with modules. Record the choice as a Decision with the rejected alternative and the hand-off between apps (which record, which stage, which workflow). Give the rail/nav order in journey order, plus global filters (brand, season, region) that every page and badge obeys.
- **Record pages are the heart of most apps.** For each main record (product, case, invoice, student), specify its stages or tabs in full (section 11): the gate rules that let it advance, who advances it, and what each tab reads and writes.
- **Lifecycle and gates**: every status/stage picklist gets an allowed-transition table (from → to → condition → who → workflow). One generic "change status" workflow that validates against this table usually serves every object; side effects (e.g. a "Yes" decision creating a downstream record, a "re-review" loop back) are its branches.
- **Decision forums and calendars**: when the process has recurring meetings (review boards, gate meetings, S&OP) or relative deadlines ("8 weeks before launch", "launch + 1 week"), model them: a Meeting object with agenda items and decisions, a milestone/calendar object with dates derived from offsets, and schedule triggers for the deadline checks.
- **Activity history**: an audit/activity-log object written by every workflow that changes a record (who, what, from, to, when, AI-assisted or not). History tabs, feeds and "recent activity" read it.
- **Copilot data access**: an agent can only see what its tools return. Spec its read tool as a workflow (object, filters, fields, sort, limit, paging, derived fields such as days-in-stage) covering every object it must answer about, plus a deep link per record so its answers can link to the page.
- **Generated files** (decks, reports, packs, exports): say what generates each one, from which records, and the fallback if the platform cannot produce that file type from an agent (e.g. generated in the app and uploaded, with the workflow only recording it).
- **Pages**: every page a persona's workflow touches, each with layout regions, blocks, data bindings, actions, states and UI patterns (section 6.11).
- **Objects**: everything pages, agents and workflows read or write (section 6.12).
- **Agents**: every agent, using the agent spec (section 6.13). State whether each one is needed and why.
- **Workflows/automations**: every automation, using the workflow spec (section 6.14), including the exact trigger and path.
- **Integrations**: every external system, its direction and what moves (section 6.15).
- **Component inventory**: name the app-specific building blocks each app needs, the way a product team would talk about them, e.g. for a product-enrichment app: *content builder*, *tech pack reviewer*, *content generator*, *asset shot-list checker*, *channel readiness board*; for a PLM app: *line plan matrix*, *PACE decision room*, *stage gate stepper*. Each component groups the pages, UI patterns, objects, agents and workflows that make it work (format in section 8). Different apps get different components. The wireframes place these components on each page, Design designs them (the approved wireframe manifest is the final list), and UnifyApps Headless builds against them.
- **Seed data**: enough records that no page, chart, filter or stage column is ever empty (section 6.19).
- **Demo operations** (POV/demo framing): a **Reset demo** workflow and what it needs on every object (`origin` = seed/demo, an `archived` flag or delete rule, a snapshot of each seed row or a snapshot object), with dates stored relative to the demo day and shifted on reset so "overdue", "this week" and "stuck > N days" stay true. Put the Reset action in an admin/user menu.
- **Build surface and platform check**: state whether each app is a no-code app or a code app, and why (a code app suits dense custom UIs such as matrices, drag boards, Gantt and stepped record pages; no-code suits standard list/form/dashboard apps). Then tag every UI pattern, field type, trigger and agent tool you used as *native*, *custom code*, or *not possible / workaround*, from platform knowledge or by asking `research`. Known UnifyApps realities to design around: object picklists and lookups may be simpler in practice than in the spec (say whether you use typed picklists/lookups or string codes joined by key, and use one convention everywhere); nested JSON fields drop null values; numbers read in code nodes may need coercion; some field names (e.g. `version`) collide with system columns; agents may not have every document-generation tool on every tenant; there are no formula or roll-up fields, so computed values must be written by workflows; object names should carry a short solution prefix (e.g. `pc_`, `plm_`) so they don't collide with older objects on a shared tenant.

Check every L1 feature has a page, an object and (where needed) a workflow or agent behind it, and belongs to a component. Check every page is reached by at least one persona workflow. Check the reverse too: every specified page, object, workflow, agent, integration and component serves at least one L1 feature; anything that serves only L2 moves to the future-scope assets table.

### Step 8 — Write, build the Word file, then self-review
Draft the content in `_working/` (prose plus the structured working draft the long tables are generated from). Read the `docx` skill and build `scoping-document.docx` following the formatting rules in section 2. Then run the **quality gate** in section 9, including the `check_docx.py` script. Fix everything it finds, rebuild, and run it again. Only finish when it passes. Report the final counts (L1 and L2 features; build-scope components, pages, objects, agents, workflows), the research mode used, and the top assumptions in your closing summary.

---

## Answering the AI PM (POC Studio, v1.0)

The orchestrator may call this skill again with the AI PM's findings (`<workspace>/reviews/scoping-review-<n>.yaml`)
instead of a fresh task. Then:

1. **Fix only what is listed.** Edit the existing output in place (the working draft, then regenerate the .docx from it so IDs and counts stay in step); leave everything else exactly as it was. Do
   not re-run the whole pipeline for a handful of findings.
2. **Answer every finding** in `<workspace>/reviews/scoping-response-<n>.yaml` (same `n` as the review):
   ```yaml
   responses:
     - { finding: F1, status: fixed,    where: "<section / page / specimen / scene>" }
     - { finding: F2, status: disputed, reason: "<the evidence: an E-, S-, A- or D-ID, a stated ask, a human decision>" }
     - { finding: F3, status: deferred, reason: "<non-blocking only>" }
   ```
   Dispute when the finding is wrong for this client, and say why with evidence; a dispute without evidence is
   treated as `fixed` and checked. Never dispute a finding that cites a human decision.
3. **Re-run your own checks** on what you changed (`check_docx.py` must still print `ok`), and say what you ran in the response file
   (`checks: [ ... ]`). The AI PM re-runs them too.
4. Do not ask the person anything; questions still go to the reviewer in resolve mode.

---

## 4. Calling the `research` skill

**Rule: every piece of outside research goes through the `research` skill.** Invoke it with the Skill tool (`research`, or the plugin-qualified name the session lists). This applies to vendor scans, regulations, the client's public footprint, benchmarks, platform capabilities and URL reading. Sub-agents you spawn for research must invoke it too (step 4).

**Fallback only when it is not available**: if the Skill tool or the `research` skill is not in the session, or the skill fails to load, do the research yourself with web search and page fetching, following the same discipline (cited sources, strength ratings, "Not yet verified" flags). Record in Document Control: *Research mode: research skill* or *Research mode: fallback (reason)*, per brief if it was mixed. Never write "research skill" unless you or the sub-agent actually invoked it and its output says so.

The `research` skill takes four parts. Always send all four.

| Part | What to send |
|---|---|
| **Question(s)** | Required. One or more specific questions. Ask "Which capabilities do Salsify, Akeneo and inriver offer for attribute enrichment, with doc links?", not "research PIM tools". |
| **Purpose** | What the answer feeds and where it's used, e.g. "Feature catalogue for a client-facing scoping document; needs vendor evidence per feature." This sets research depth. Client-facing scoping is high depth. |
| **Context** | Known facts: client, industry, country, the use-case type, relevant findings from earlier calls. |
| **Format** | Ask for what you'll paste in directly, e.g. "Table: capability · vendors offering it · source URL · standard/partial/gap", or "List of fields with type and example". |

Rules:
- Keep each call to one theme. Run independent calls in parallel (several sub-agents, each invoking the `research` skill).
- Every vendor or regulatory claim in the document must carry a source ID that resolves to a URL in the Appendix sources table. Mark findings you couldn't verify as **Not yet verified**.
- **Brand guidelines.** If the client's own material (deck, brand guide, message) does not give their brand, find it by web research through `research` — never guess and never ask the person. In this order: the client's **published brand guidelines** or brand portal; their **live product interface** (their own app, when public); their **live marketing site** (CSS custom properties, the computed header and button colours, the logo). For each cue record what it is, its source URL and its **source type** (client-supplied / brand guidelines / live product / website). Also record the brand's **light-to-dark balance** (light-led, **dark-led** — black or near-black grounds — or colour-led) and its **chromatic role** (one hero colour, a pair, or **achromatic**: black, white and grey with one accent). An achromatic, black-led brand's brand colour is its black: **never promote a link, button or accent blue from the site into "the brand colour"**. Pass all of this to section 21.

---

## 5. Use-case types and what each needs

Inputs often mix types. Use the primary type's playbook and add the secondary types' must-haves.

### A. POV / greenfield in a known product category
*Example: Pentland wanted our POV on Product Enrichment and PLM in fashion. The input was two process decks and an email.*
- **Research (heavy)**: 6–10 leading vendors in the category, their feature sets, recent AI features, the category's regulations (e.g. EU AI Act marking, Digital Product Passport), standard KPIs, and the client's brands, public footprint and current systems.
- **Depth**: a large feature catalogue with Market coverage and Seen In, differentiators, and a must-have slice that tells a story through the client's own process (their stage names, their meeting names such as PACE, their lanes).
- **Watch**: map every feature to a stage in the *client's* flow, not the vendor's. If the client already runs tools in the category, say how the app sits alongside or replaces them.

### B. Replacement of an existing app
*Example: "Replace our Zendesk / Excel tracker / legacy portal."*
- **Research**: the incumbent's full feature list from its docs, and two or three alternatives for a better-than-parity view.
- **Depth**: a parity matrix (incumbent feature → our feature → status: parity / improved / dropped with reason), data migration (objects and field mapping from the old system), integrations the old app had, and user retraining hot spots.

### C. Internal process automation
*Example: an invoice reconciliation system. The client sends sample POs, invoices and goods receipts; documents are extracted by an LLM into objects, an automation matches them, and a match score with exceptions is produced.*
- **Research (light to medium)**: how the leading tools in the space handle it (e.g. AP automation tools for 2-way and 3-way matching, tolerance rules, exception queues), the standard fields for each document type, and finance-style UI patterns (queues, side-by-side compare, variance highlighting).
- **Depth**: an extraction schema per document type taken from the client's samples (every field, type, example value from the sample, and confidence handling); matching rules and scoring formula spelled out; exception states and who resolves them; a step-level workflow for every path, including failures (unreadable document, partial match, duplicate invoice); SLAs; audit trail.
- **Watch**: the sample documents *are* the spec. Read every one and list every field.

### D. Agent-first / AI assistant / "brain" super app
*Example: a university super app. Each student logs in and sees what's relevant to their year and programme, and agents get tasks done, e.g. first-years choose semester subjects.*
- **Research**: comparable products (student portals, campus apps, AI assistants in higher education), the standard student lifecycle by year, and policies that constrain agents (data privacy, academic rules).
- **Depth**: a persona matrix by segment (year × programme × role, plus faculty, advisors and admin), a personalisation rule table (who sees which page, card or agent, and why), one agent spec per job with its tools and guardrails, the handoff to a human (advisor, registrar), and conversation entry points on every page.
- **Watch**: write explicit visibility rules per persona segment. "Personalised" alone gives the build nothing to implement.

### E. Extension / integration layer on an existing system
*Example: an opportunity planner. When a Salesforce opportunity reaches stage 20, a webhook starts an automation that reads the opportunity and related records, fills a planner form in the app, lets users edit it directly or through a copilot agent, and writes the answers back to Salesforce.*
- **Research**: the source system's objects, fields and API/webhook mechanics (e.g. Salesforce Opportunity, Account, Contact, OpportunityLineItem; outbound messages or platform events), and the planner/template the client uses.
- **Depth**: a field mapping table (source object.field → our object.field → form field → write-back field, with direction and transform), every trigger exactly (webhook payload, auth, idempotency), sync and conflict rules (what wins if Salesforce changed meanwhile), and error and retry paths.
- **Watch**: write-back is a workflow of its own, with validation and a visible sync status in the UI.

### F. Ambiguous ask
*Example: "Show us what you'd do for our supply chain."*
- **Research**: an industry scan to find the 2–3 highest-value problems for this client, using their public footprint.
- **Depth**: problem framing with an explicit choice of which problem to solve and why, a heavier assumptions log, and a demo storyline that sells the choice.
- **Then**: proceed as type A or C for the chosen problem.

### G. AI inspection, scoring or compliance engine
*Example: retail brand compliance. Meeting notes asked to check, from store shelf photos, that products meet brand guidelines (shelf space, visibility, logo, font, tagline) for drinks brands such as Jim Beam and Diageo. Reps are often offline, there are hundreds of thousands of stores, and non-compliant stores go to the brand team. The scope became 6 KPIs, each with checks, inputs, formula, result bands and per-brand weights.*
- **Research (medium to heavy)**: the industry's established scorecards and their weights (e.g. Perfect Store: on-shelf availability about 30%, price accuracy about 20%), evidence for each metric's business impact, benchmark thresholds, the client's specifics (hero SKUs, current and retired campaigns, pack designs), how existing tools detect each check, legal or regulatory limits (e.g. a rep must never be asked to change a retail price), and labelled real-world example images.
- **Depth**: a full rules and scoring spec (section 14.2) for every KPI or rule; a weight table per tenant or brand with the reason each weight differs; how scores roll up (KPI → store → region); critical flags that override the score; "Not assessable" handling (e.g. ask the rep to retake the photo); the technical approach options with a recommendation (e.g. classic vision models vs a vision LLM: cost, accuracy, speed, on-device/offline); review queues for low-confidence results.
- **Watch**: every threshold and weight needs a stated reason or source. Every input must say where it comes from: manual upload (which document type), web research, an integration, or none (read from the image).

---

## 6. The golden document: `scoping-document.docx`

Use exactly these sections, in this order, with these numbers (0–23 plus the Appendix), each as a Heading 1. Keep every section. If one truly doesn't apply, keep the heading and write one line saying why (e.g. "No external integrations: all data is entered in the app"). Use tables wherever a list has more than one attribute. Where a Heading 2 name is given below in quotes, use it exactly; the checker looks for it.

**Part A — Proposal and decisions** (Heading 1 divider before section 0; section 2 "Two parts, two readers").

### 0. Document control
- "How to read this document": the reader → sections → what they get table (section 2).
- Client, project name, version, date. Use-case type (primary, secondary) and deployment framing, each with a one-line reason. A table of input sources: file · what was taken from it. Research mode (research skill, or fallback with the reason, per brief if mixed).
- A **Count · Value** table, generated by script: Personas, Features (Grand total, L1 must-have, L2 future scope), and for the L1 build scope: Components, Pages, Objects, Agents, Workflows, Integrations. Each row label starts with the word shown here so the checker can match it against the specs.

### 1. Executive summary
Open with the business problem, never with a description of how the client's process works today. Write it in this order: the pain (who suffers, what goes wrong, what it costs), then what we will show and why it matters to this client, then the scope (for whom, which apps and modules). Keep it to one short paragraph plus three or four outcomes, each tied to a success measure in section 4. Say in one line how many features are must-have (built now) and how many are future scope.

### 2. Context
- **Client and industry**: who they are, brands/units/regions, scale indicators, systems they use today.
- **Current state (as-is)**: the process today, step by step, from the client's material. Name the systems they use today and the hand-offs.
- **Pain points**: each one tied to an as-is step and to evidence (an input or a research finding).

### 3. Problem statements
3–7 numbered statements (P1, P2…): who is affected, what goes wrong, and the cost or impact. These IDs are traced through the rest of the document.

### 4. Objectives and success criteria
- Objectives (O1…), each linked to problems.
- Success criteria table: metric · baseline (known or assumed) · target · how it's measured in the app (which object field or report). Every metric must be measurable with L1 features only; reword any metric that needs an L2 feature to what L1 delivers. Each problem maps (in 22) to a metric that actually measures it. Label every industry or research baseline as such (e.g. 'industry, not <client>', with its source ID) wherever it appears, including sections 1 and 3. Never show a client 'before' number you do not have, and never a 0% for something the client already partly does; state the baseline in words instead (e.g. 'No pre-landing plan today').
- Success criteria measure the business, not the demo. Lead with outcomes the client tracks (e.g. store conversion, average order value, returns), and give no target without a baseline. Log the baseline you assume in 5.6, and ask the client to confirm it in 5.9. Checks that the app works (reasons cited, consent recorded, no medical claims, time to shortlist) are acceptance criteria in 4.1, not success metrics. Where L1 cannot record a business metric, name the client report it is read from.
- "4.1 Acceptance criteria for the build": concrete checks a reviewer can tick, e.g. "Every chart changes when the underlying record changes." Acceptance criteria test L1 only. This is the only place they are listed; 20.1 refers back to them. End 4.1 with a **Visual acceptance** block, tested at 1280×800 on every page in the demo storyline:
  - no horizontal scroll and no clipped column;
  - no list row taller than 64 px (state another number only with a reason), and at least 8 rows visible in a list;
  - no wrapped or mid-word-broken pill or tag;
  - each page opens on its specified tab and first viewport;
  - every AI output named in 4.1 is visible in the seed data;
  - every rail badge and KPI count equals the count on its page;
  - no truncated or inert control: every button either works or is disabled with its reason (section 11 prerequisites).

### 5. Scope
Use these Heading 2s in this order:
- **5.1 In scope**: apps and modules (build scope, L1).
- **5.2 Asked vs scoped**: when the input listed specific items (KPIs, features, screens), a table: asked item → where it is in this scope (kept, merged, renamed, replaced, dropped) → why.
- **5.3 Out of scope**: each item with the reason (future scope L2, not requested, or platform limit).
- **5.4 Live vs simulated** (for POV/demo): a table of every build-scope agent, workflow, integration and AI surface with its label (Live / Deterministic / Seeded / Mocked, step 2) and the reason. Only build-scope items appear; nothing here is labelled with a phase.
- **"5.5 Must-have vs future scope"**: Phase 1 is exactly the L1 set (count, and the L1 reasons tally: core flow / agent / client ask / research must-have). Later phases group the L2 rows by theme, with feature ID ranges. This is the one place in Part A where later phases are described.
- **5.6 Assumptions**: the full log, A1… each with the value assumed, the reason, and the impact if wrong. It is not repeated in the Appendix.
- **5.7 Decisions**: D1… design decisions made, with the rejected alternative and the reason.
- **5.8 Technical approach** (when the input weighs options, or the choice changes the build): the options compared on cost, accuracy, speed, scale and offline/edge needs, and the recommended option with the reason.
- **5.9 Open questions for the reviewer**: only questions whose answer would change the build. Each one has the default this document already uses. **Never ask about colours, theme (light/dark), typeface or look and feel**: those are not preferences to collect; the design-system skill decides them from the brand evidence in section 21.

### 6. Research findings
Skip only for pure internal automation with no comparable tools, and say so. Otherwise include:
- References reviewed (vendors, products, standards), with one line each on why they're relevant.
- Benchmark summary: the capabilities that are standard, partial or missing across the market.
- Differentiators: where our solution goes beyond the market, and why that matters to this client. Never claim no one else does it when known products cover parts of it. Name them, and say what we add, e.g. 'joins all six steps in one case record, from flag to settlement'.
- Regulatory and compliance notes, with dates.
- Brand cues found for the client (for the DS hand-off).

### 7. Personas
A table per persona: ID (U1…), role/title, team, **Primary (Y/N)** (exactly one Y, by the primary-persona rule in step 6), goals, pains, key jobs-to-be-done, frequency of use, devices and working conditions, permissions (what they can see, create, approve), **home page** (the page they land on), and which pages they use most. For segmented audiences (type D) add the segment matrix and visibility rules.

### 8. Journeys and workflows
- **8.1 To-be end-to-end journey**: the stages of the business process as a table: stage · personas · what happens · app page · agent/automation · output. Include a flow diagram (image, section 2).
- **8.2 Persona workflows**: for each persona and each job (J1…), a step table:

| # | Actor | Page / surface | User action | System response | Data read/written | Agent / workflow | Notes (rules, exceptions) |
|---|---|---|---|---|---|---|---|

Cover the happy path and the main exception paths (rejection, missing data, failure, re-review loops).

### 9. Solution overview
- App map: apps, modules, components and nav order (rail items with badge counts where useful), as a diagram image plus a table. Build scope only.
- **AI and data flow**: one diagram image showing how data moves from input (capture, upload, webhook, sync) through workflows and agents to the results, reviews and actions people see, with the human gates marked. For apps without AI, show the main automation flow instead.
- Global conventions: header, global filters (e.g. brand switch), the copilot entry point, the AI signature for AI-generated values (marker, provenance line, confidence, how the marker clears after a human edit), status tones, notifications. One row per convention.
- The UnifyApps building blocks used: objects, workflows, agents, integrations, pages, reports, with counts (generated by script).
- Platform check (step 7).

Section 9 closes Part A. It should leave a reader who stops here knowing what the app looks like, how it works end to end, and what is built now versus later.

**Part B — Build specification** (Heading 1 divider before section 10; section 2 "Two parts, two readers"). Each Part B section opens with one line on what it holds and who uses it.

### 10. Feature catalogue (complete)
The **complete** feature catalogue lives here, in the format of section 7, in a landscape section, split into the must-have build scope and the future scope. Do not summarise it or move it elsewhere.
- **10.1 Summary**: a table per app: module · L1 · L2 · total · market gaps in L1, with totals; plus the L1 reason tally (core flow / agent / client ask / research must-have). State "Grand total: N", "L1 must-have: N" and "L2 future scope: N" here, generated by script.
- **"10.2 Must-have catalogue (L1 — build scope)"**: one lean table per module (grouped by app, then module, with the heading `App › Module`), every L1 sub-feature with the columns in section 7. This is the only feature list the build works from; its build and research details are in Appendix E and F.
- **"10.3 Future scope (L2 — not in this build)"**: one table per module listing every L2 row with: ID · Sub-feature · Description · Why it can wait · Depends on (L1 IDs or assets) · Market coverage · Sources. Then a **future-scope assets** table: page, block, object, field, workflow, agent or integration that only L2 needs · the L2 IDs that need it · note. These are not specified anywhere else in the document.
- **10.4 Agent catalogue**: a one-row-per-agent index for the agents in the build scope: agent · app · what it does · reads from · writes or proposes · human gate · L1 feature IDs. The full specs are in section 13. Agents that only L2 needs appear in the future-scope assets table instead.
- **10.5 UI pattern coverage**: pattern · pages · L1 feature IDs, so the DS skill sees every pattern it must design for the build (L2-only patterns are excluded).

### 11. Page specifications
One subsection per page in the build scope, in nav order (pages needed only by L2 are in 10.3, not here). Specify only the blocks, tabs, fields, actions and states that L1 features need; end with one "Future scope:" line naming any L2 additions planned for the page (L2 IDs only, no description of how to build them). "Features covered" lists L1 IDs only. Every page here is built, so a page spec has no "Phase" row or flag. For each:
- **Purpose**: one sentence on what the persona gets from this page.
- **Screen UX** (required on every page, before the blocks table):
  - **The question the screen answers** for its persona, in their words.
  - **One primary CTA**: its label and placement (one per screen).
  - **Above the fold** at 1280×800: what the persona sees without scrolling.
  - **Hero content**: the one thing the eye lands on first.
  - **Filters** with their exact values and the seed count behind each value.
  - **Row or card anatomy**: what each list row or card shows, in order (at most four lines on a card, one line per table cell).
  - **Exact copy**: headings, the empty state with its CTA, button labels.
  - **Context actions** on a row or record.
  - **States**: loading, slow AI (what shows while an agent works), success, empty, error, no-permission.
- **Home pages by persona type.** A doer's home leads with their next task (a task list or work queue); an overseer's home leads with what needs action (a queue or insights), then numbers. Lead with a task list, not KPI tiles: a full-width chart or a KPI strip is never the whole home. A short summary strip above the queue is welcome. A few AI suggestion cards may sit beside it, each with one button that applies its filter to the queue (e.g. '6 styles missing care copy → Show them'); each card's count equals the rows the filter returns. Every persona's home page is named in section 7.
- **Personas** and **entry points** (nav, links, notifications, agent answers).
- **Components used** (CMP IDs from section 23).
- **Layout**: regions top to bottom (header, KPI strip, main, side pane, drawer).
- **Blocks table**: block · what it shows · data source (object.field, filter, formula) · UI pattern (generic name, list below) · actions.
- **Formulas**: every computed number defined, e.g. "Stuck > 14 days = count Product where now − stage_entered_at > 14".
- **Actions**: button/menu → what happens (the workflow ID it triggers, or the object update).
- **Prerequisites shown before the click**: for every action that needs earlier steps (e.g. 2–3 fields filled, a sample approved, a document attached), list the conditions. The button stays **disabled** until they are met, with a tooltip or helper line naming exactly what is missing; it never fails only after the click. Each such action gets an acceptance check in 4.1.
- **States**: empty (exact message and recovery action), loading, slow AI, success, error, no-permission (the same states as Screen UX; state each once there and reference it here).
- **AI surfaces**: which values are AI-generated, how they're marked, and what the human approves.
- **Features covered**: L1 feature IDs.
- For record pages with tabs or stages, a table per tab or stage with: the fields shown (object.field), which are editable at which stage, the completeness rule for that tab, the AI-prefilled values, the actions, and the **gate** to leave the stage (exact condition, e.g. "every offered variant has a GTIN and country of origin"; who can advance; the message shown when blocked). Future stages are read-only unless you say otherwise.
- **Create and edit paths**: every record type a persona can create needs a create surface (drawer, form or wizard) with its required fields and the ID format it gets; say which records are created only by workflows.
- **Global elements on every page**: global filters, the copilot entry point, notifications, the user menu (theme, settings, reset demo), and the deep-link route an agent answer uses to open a record.

Name UI elements as **generic patterns**, not design-system components. The DS skill maps patterns to components. Use these names, and add new ones when needed:
KPI tile strip · chart (bar / stacked bar / line / donut / funnel) · data table with toolbar, search, facets and pagination · filter chips · kanban board · stage stepper · record header · tabbed record · form (fields, picklists, validation) · side detail pane · drawer · modal · multi-step wizard · calendar (month / agenda) · timeline / Gantt · activity feed · comment thread · file upload / drop zone · document viewer · side-by-side compare · asset grid · image viewer with annotations · matrix grid · progress / completeness indicator · checklist · approval queue · notification centre · chat / copilot panel · AI insight card · AI-draft field marker · empty state · toast.

### 12. Data model
Specify the objects and fields the L1 features need, and nothing else; objects or fields only L2 needs are listed in the future-scope assets table (10.3).
- An ER diagram (image).
- For each object:

Heading 3 **`OB-nn <object_key> — <Name>`** (e.g. `OB-06 bc_store — Store`), then a one-line description of what one record represents.

| Field (key) | Type | Required | Description / allowed values | Example |
|---|---|---|---|---|

Types: text, long text, number, currency, percent, date, datetime, boolean, picklist (list the values), multi-picklist, lookup → Object, multi-lookup → Object, file, image, URL, email, phone, JSON (describe its shape in words, e.g. "list of {milestone, offset_weeks, owner_team}"), **computed** (give the expression, its input fields, and when it is recalculated: on every write by workflow X, on a schedule, or in the page only).

Fields shared by every object (origin, archived, timestamps, AI marker fields) may be defined once in a table at the top of the section and referenced from each object.

- Give every object a business key with an ID format (e.g. `<BRAND>-<yy>-<seq>`, `INV-####`); pages, agents and links use it. Say how the next key is generated (max-plus-one in the creating workflow, or a counter object) and what Reset demo does to it. Avoid record keys that look like feature IDs (e.g. REQ-1042 vs REQ-001). If prefixes overlap, say in "How to read this document" that feature IDs are catalogue references only and never appear in the UI.
- Decide per record whether stage-specific data lives in its own objects (one row per thing, filterable and countable) or as JSON on the parent (fewer objects, but not filterable by the copilot or charts). Anything a chart, filter, queue or the copilot must count gets its own object or flat fields.
- **Locations.** When a page's main question is *where* (sites, stores, branches, warehouses, assets, routes, a radius search), the object behind it carries `latitude` and `longitude` fields (decimal degrees), and section 19 seeds them with real coordinates in the client's region. The wireframes then draw that page as a map page (the wireframes skill's `map-component.md`); without coordinates there is no map.
- Derived values that pages show as badges, pips, scores or "x of y" (completeness, readiness, health score, data quality, days in stage, late/at-risk flags) are computed fields with their formula, not page-only maths.
- Include the support objects most apps need: activity log, AI suggestion (if AI values are stored separately), documents/files, and the demo-reset fields or snapshot object.

Then a **Links** table: from object.field → to object.key · cardinality (1–1, 1–many, many–many) · meaning, and an **allowed transitions** table per status/stage field. For the app's main record (and any other record with more than four statuses), add a **lifecycle diagram** image: each status as a state, each allowed transition as an arrow labelled with its gate and workflow.

- Mark the primary key and any external IDs (e.g. `salesforce_opportunity_id`) used for sync.
- Give status/stage picklists in process order.
- AI-written fields carry `ai_generated`, `ai_source` and `ai_confidence`, or one shared AI Suggestion object. Spec the marker's lifecycle: AI draft → (human accepts or edits) AI-assisted → (record approved) approved, which workflow flips it, and what the UI shows at each state. Use one rule for this everywhere in the document.
- Give extraction-target objects (type C) every field from the sample documents.
- For scoring apps (type G), add objects for the rule configuration (rules, weights per tenant, thresholds), the reference inputs (must-stock lists, price lists, campaigns) and the results (per-check and per-rule result with score, confidence and evidence image region), so weights and thresholds can change without a rebuild.

### 13. Agents
One spec per agent in the build scope (every agent that an L1 feature uses; agents are L1 whenever the client will see them, step 5). Agents only L2 needs are named in 10.3 with one line each, not specified here:

| Item | Content |
|---|---|
| Name and ID | e.g. AG-01 Invoice Extraction Agent |
| Required? | Yes, and why an agent rather than a workflow or rule |
| Purpose | One sentence |
| Capabilities | What it can do, as a bullet list |
| Tasks | The concrete jobs it performs, each with its input and output |
| Tools | Each tool or action it can call (read object X, update object Y, call integration Z, search the web, generate a document), with permissions |
| Knowledge / context | The objects, documents and policies it reads |
| Trigger and entry points | Copilot panel on page P, a button, a workflow step, a schedule, an event |
| Output | What it writes or proposes, and where |
| Human gate | Who approves what, before what takes effect |
| Guardrails | What it must never do; confidence thresholds; escalation |
| Example prompts / interactions | 3–5 realistic examples, each with the **expected answer from the seed data** (the exact records it should name, using the exact names in section 19), so the build can be tested |
| Live or seeded | For POV/demo framing |
| Components and features | CMP IDs and L1 feature IDs |

### 14. Workflows, automations and business rules

**14.1 Workflows.** One spec per workflow that an L1 feature needs (workflows only L2 needs go to 10.3):

| Item | Content |
|---|---|
| Name and ID | e.g. WF-03 Match invoice to PO |
| Purpose | One sentence |
| Trigger | Exactly one of: **app action** (page + button), **object event** (create/update on object + condition), **webhook** (source system, event, payload fields, auth), **schedule** (cron/interval), **agent call**, **called by workflow** |
| Inputs | Fields and records it starts from |
| Path | Numbered steps: read / transform / call agent / call integration / branch on condition / write object / notify. Give each branch's condition and destination. |
| Outputs | Objects created or updated (fields), notifications, documents |
| Errors and retries | What happens on each failure, and how it's surfaced in the UI |
| Idempotency | How repeated triggers are handled (for webhooks and schedules) |
| Features powered | L1 feature IDs |

UnifyApps Headless builds the implementation from this, so the trigger and the path must be exact. Write the path as a numbered list, not prose.
Check each path in three ways:
- Read it top to bottom for overwrites: a later step never resets a value an earlier branch set (e.g. a 'Not eligible' band replaced by a score band).
- Cover the edge states of the records it touches (e.g. an auto-advance when the parent is On hold: what is kept, what is skipped, who is notified).
- Make every row it writes satisfy that object's required fields at that point in the path (no required record key before the record exists).

**14.2 Business rules and scoring.** Required whenever the app judges, scores, matches, validates or routes by rules: compliance KPIs, invoice match scores, data-quality checks, eligibility, risk ratings. Skip with one line otherwise. For each rule or KPI (R1…):

- **What it is and why it matters**: the industry name for it, what it measures, and 2–3 evidence points with source IDs.
- **Checks**: a table of # · check · what is looked for, written precisely enough to judge one example by hand.
- **Inputs**: a table of input · description · potential source type (PDF, XLSX, CSV, web page, image, API) · source (manual input, web research, integration, or none because it's read from the item itself). Each input maps to an object in section 12.
- **Formula**: the exact score calculation, including weighting inside the rule (e.g. hero SKUs counted double) and caps.
- **Result bands**: a table of result → rule, always including a pass, a warning, a fail and a "Not assessable" band, plus what happens on "Not assessable" (e.g. retake the photo, send to a reviewer).
- **Critical flags**: conditions that fail the item regardless of score, and who is alerted.
- **Examples**: a pass and a fail case described in words, plus links to real-world example images or documents. The DS skill uses these for illustrations.

Then:
- Every rule or KPI the client asked for, and the ones research shows are the core of the scorecard, are L1 and fully specified. Extra rules that are only nice to have are L2: list them in 10.3 and leave them out of the weights.
- **Weights**: a table of rule × tenant/brand/segment → weight and priority, totalling 100, with the reason each one differs. When some rules do not apply to an item (e.g. a rule only for one channel or category), say once here how the score treats them: either renormalise the applicable weights to 100 for that item, or score non-applicable rules as pass. Show the effective weights on the item.
- **Roll-up**: how rule scores combine into item, entity and portfolio scores, and the final status bands.
- **Human review**: which results go to a person (low confidence, critical flags), and what they can override.
- **Name thresholds for what they do**: an amount a role may approve alone is an approval limit, not a cap. Check `research` for guidance that discourages a construct (e.g. arbitrary daily caps), and name the rule ID and every label to match. Define every exception a seed record or demo step uses (e.g. 'delivery outside the 24 h window') here, with its exact condition and who approves it.
- **Ownership**: say once which sub-scores the agent returns (e.g. skills and domain match, with rationale and confidence) and which are computed by rule in a workflow (e.g. experience, location). Never assign a sub-score to both. Model calls that score run at low or zero temperature. Hero-record scores are seeded, so the test tables in 13 are reproducible; live scoring on new records is not expected to match them.

### 15. Integrations
Only integrations the L1 features need (most are Mocked in a POV); later integrations are listed in 10.3. A table: system · direction (in / out / both) · mechanism (API, webhook, file drop, email, connector) · objects and fields moved · frequency · auth · live or mocked. For two-way sync, include the field mapping table and conflict rule.

### 16. Roles and permissions
A matrix: persona/role × object or page → none / read / create / edit / approve / admin. Include record-level rules (e.g. "students see only their own enrolment records").

### 17. AI trust and governance
Only when the app has AI features. Cover: how AI output is marked, provenance, confidence display, human review before publishing, undo/revert, audit log of AI actions, agent permissions, and any relevant regulation.

### 18. Non-functional notes
Only what matters for this case: volumes, performance expectations, audit, data residency, localisation and right-to-left languages, accessibility, mobile.

### 19. Seed / demo data plan
Seed only the build-scope objects (section 12); every count, hero record and planted defect must exercise an L1 feature.
- **Per object**: a count and its distribution across every picklist value (e.g. "20 products: design 3, sampling 5, costing 4…"), so every column, filter, chart bucket and queue is non-empty. Child objects scale with parents (variants per product, lines per invoice). Give the load order so links resolve. Make counts consistent across linked objects (e.g. filled slots ≤ styles, decisions = decided agenda items).
- Named **hero records** that carry the demo story, each with the state it's in, its key dates (offsets) and what it demonstrates. One name per record, used identically everywhere.
- **Story defects**: list the deliberate problems planted in seed records (missing field, failed rule, overdue, over budget, low-confidence AI value) and which record carries each, so every warning, gate block and exception path has something to show and the copilot's example questions have known answers.
- **Dates**: store as offsets from the demo day and say how reset re-anchors them.
- **Files and images**: where each comes from (client's public site, generated, placeholder), naming/storage convention, and rights or brand risk. Use the client's real products where public, generic roles instead of real people, neutral names for suppliers. When the app shows product images, use `research` to find real images of the client's actual products (their site or retailer listings) and seed one per product record, so every image card shows a real photo. An illustration or neutral placeholder is only the fallback for records with no public image. State the fallback count and record the feasibility check (source URL per image, rights or brand risk).
- Where AI output is seeded, the share of records carrying it (e.g. about 1 in 4).
- Realistic values that use the client's real brands, products, document formats and regions. Numbers can be dummy, labelled as such.
- **Demo data rules** (UnifyApps Headless follows them when it seeds; the build test checks them by script):
  - one demo "today" that every date agrees with; no date after it; overdue items are overdue by whole days;
  - times in business hours (08:00–18:00) in the persona's stated time zone (the client's head-office time zone when none is stated, and say so);
  - statuses agree with the scores, values and dates on the same record;
  - every filter, badge and KPI count equals its row count, each with its formula;
  - the default persona's first screen is non-empty, and the default period, filter or tab has data;
  - every AI output names the records that carry it and the count shown (never "0 AI suggestions");
  - evidence (images, documents, quotes) is unique to each hero record and shows what it claims;
  - no duplicates or placeholders on any demo path;
  - test datasets are kept separate from the demo data (their own seed, or a hidden entry point), never mixed into demo screens.
- For type C, use the client's sample documents as seed inputs, and add generated variants that exercise each match/exception path.

### 20. Build plan and demo storyline
Start with the build order: build steps in dependency order (objects and seed → shell → core journey → depth → reporting), each one demo-able at its end, naming the pages, workflows and agents built in each step. Call these **build steps** (B1, B2…), never "phases", so they are not confused with the future-scope phases in 5.5. Then use these Heading 2s:
- **"20.1 Acceptance checklist"**: one line pointing to 4.1, plus only the checks that belong to the build order (e.g. "after B3, a photo in gives a score out"). Do not copy the 4.1 list.
- **20.2 Demo storyline**: 6–10 steps, each naming the page, the record and what it proves. Fit it in 10–15 minutes. It uses only L1. **Order:** the primary persona's home → the core action → the result with its evidence → the follow-up by a secondary persona; oversight, admin and setup come only after this core loop. Mark any step that happens outside the app (e.g. a slide in the proposal deck) as "outside the app".
  - **Live, not replayed.** The core action runs live on a fresh or draft record, so the check, score or send happens on screen rather than re-showing a seeded result. Where the record normally comes from an upstream system, add one simulated arrival flow (e.g. 'New style arriving from PLM (simulated)').
  - **Seed matches the story.** Each step's record is seeded in exactly the state the step needs: other required approvals already submitted, or the item still in Draft if the step sends it. The hero records (19), agent test answers (13) and field examples (12) all agree with the step.
  - **Show the differentiators.** Every headline differentiator from section 6 appears in a step, including its blocked or failing case when that is the point. Trim other steps to stay in time.
  - **Say what cannot be shown live.** Anything that cannot happen live during the demo (e.g. hourly scheduled reminders) goes in 20.4, or gets an admin 'Run now' action.
- **"20.3 Build scope vs future scope"**: a table of what the build contains (pages, components, objects, workflows, agents, integrations, L1 feature count) and what is deliberately left for later (the L2 count and the future-scope assets from 10.3), so the builder doesn't improvise L2 and the reviewer doesn't read it as missing. Counts come from the same script as Document Control. As a guide for a POV: per app 4–8 pages, aiming for 3–6 (reviewers keep asking for fewer, cleaner pages), 8–12 objects, 3–8 workflows, and one agent, the live copilot. Add a second agent only with a Decision saying why. Open secondary records, create forms and detail views in drawers or modals rather than as new pages. Reach these numbers by merging, not by dropping journey stages. Fold stages into tabs of one record page, fold small child or lookup records into fields or one shared object, and fold per-action workflows into the generic change-status workflow. Merge workflows that always run together (e.g. approving a message card sends it). Drop metric-refresh schedules when the page can count live from records. Merge one-to-one or few-row child records (a gate, a connection, a handful of deliveries) into their parent as fields. Merge parallel log objects into one with a category. Reset from a seed data file rather than a separate snapshot object when that is simpler. If the L1 build exceeds this, re-test the L1 rows (step 5) rather than explaining the overrun.
- **"20.4 Known limits of the build"**: what will look clickable but isn't wired (publish, send, roles), so the demo script avoids it. Nothing L2 should appear as a visible control; if a page needs a placeholder for it, say so here.

### 21. Hand-off to the design system
- Brand cues (logo, colours, typeface, tone) as **evidence, not a palette**: a table of cue · value · source URL · source type (client-supplied / brand guidelines / live product / website), plus the brand's light-to-dark balance (light-led / dark-led / colour-led) and chromatic role (hero colour / pair / achromatic with one accent), each with its source. If the evidence says the brand is black-led or achromatic, say so plainly here.
- One line, always: "Final palette, theme and expression are decided by the design-system skill (its brand source order and expression step), not by this document." Do not choose colours, a theme or a typeface in this document.
- Vibe: 3–5 adjectives and the reason, e.g. "calm and dense; finance users scan many rows".
- A UI pattern inventory for the build scope only: pattern · pages that use it · special needs (e.g. a side-by-side compare with variance highlighting).
- The components from section 23 that need custom design (e.g. a match-score gauge or a variant matrix), with their key states.
- Interactions and transitions that matter (drag to stage, bulk edit preview, AI accept/reject).

### 22. Traceability matrix
A table: problem (P) → objective (O) → components → feature IDs → pages → objects → agents/workflows → success criterion. Every P and every L1 feature appears.

### 23. Component inventory
The last section before the Appendix, so Design and UnifyApps Headless find it in a fixed place. One table per app, in the format of section 8, listing every app-specific component (CMP-…) in the build scope — each serves at least one L1 feature; a component only L2 needs goes to 10.3 — followed by a short list of shared components used by all apps (copilot panel, AI field marker, activity feed, notification centre, global filters, reset demo).

### Appendix
Use these Heading 2s:
- **A. Sources**: ID → title → URL → where it's cited.
- **B. Glossary** of client terms (e.g. PACE, NPD, GSP).
- **C. Evidence log**: fact → input file and page/slide/sheet → where it's used.
- **D. Coverage map**: input → domain/process → inside the ask or not → decision (section 1).
- **"E. Feature build mapping"**: one row per L1 feature, the build columns of section 7. Design and UnifyApps Headless read this with 10.2.
- **"F. Feature research mapping"**: one row per L1 feature, the research columns of section 7.

Assumptions are in 5.6 and are not repeated here.

---

## 7. Feature catalogue format (used in section 10)

Each feature's attributes are split across three tables keyed by ID, so no table is wider than 10 columns and a reader can follow the main one without scrolling. All three are generated by script from the same working draft, so they always hold the same L1 IDs.

**10.2 L1 catalogue — the main table** (one per module, landscape). What a reviewer, designer or builder reads first:

| ID | Sub-feature | Feature | Description | L1 reason | Primary users | Page / tab | Component | Live |
|---|---|---|---|---|---|---|---|---|

**Appendix E — Feature build mapping** (one table, or one per app). What UnifyApps Headless needs to implement each row:

| ID | Process stage | Build type | UI pattern | Objects | Agent / WF | Comments |
|---|---|---|---|---|---|---|

**Appendix F — Feature research mapping** (one table, or one per app). Why each row is there:

| ID | Market coverage | Seen in | Evidence | Sources |
|---|---|---|---|---|

**10.3 L2 future scope** (one per module):

| ID | Sub-feature | Description | Why it can wait | Depends on | Market coverage | Sources |
|---|---|---|---|---|---|---|

L2 rows carry no Component, Page, Objects or Agent/WF values, because nothing is built for them now, and they do not appear in Appendix E or F.

- **Module** is the table's heading, grouped by app (e.g. `PLM › Season & Range`); the app is not repeated as a column. Use "Cross-app ›" for rows that span apps.
- **Component**: the CMP ID from section 23. **Comments**: implementation notes, kept out of Description. **Objects** and **Agent / WF**: the IDs from sections 12–14 that implement the row. **Live**: Live / Deterministic / Seeded / Mocked (step 2).
- Generate the section 10.1 summary counts with a script from the working draft, never by hand.
- **ID**: an app prefix plus a number (e.g. `INV-001`, `AI-001`), stable across revisions.
- **Feature**: the parent feature the sub-feature belongs to (Module › Feature › Sub-feature). Priority is not a column: every row in 10.2 is L1 and every row in 10.3 is L2, by the rule in step 5.
- **L1 reason**: one or more of Core flow / Agent / Client ask / Research must-have, each with its evidence (journey stage or storyline step, agent ID, E-ID, or S-ID), e.g. "Client ask (E2); Research must-have (S08)".
- **Description**: what the user gets, in plain language, one or two sentences.
- **Process stage**: the client's own stage names from section 8.1.
- **Build type**: one or more of Data model, Workflow, Agent, Integration, UI/App, Report, Platform.
- **Market coverage**: Standard / Partial / Gap / N/A. **Evidence**: Verified / Not yet verified / Client input / Assumption.
- **Seen in**: full vendor names, not abbreviations.
- **Sources**: source IDs that resolve in the Appendix.
- Add a cross-cutting module (e.g. "AI Layer") for features that span apps.

---

## 8. Component inventory format (section 23 of the document)

A component is a named, app-specific building block a product team would recognise, bigger than a UI pattern and smaller than an app: it bundles the screens, data and automation for one job. Name it in plain words for what it does, not after a UI pattern. Examples:
- Product enrichment app: **Content builder** (the stepped product record where attributes, copy, assets and translations are assembled), **Tech pack reviewer** (reads the tech pack/BOM and proposes attributes with confidence for review), **Content generator** (writes on-brand copy and SEO fields from approved attributes), **Asset shot-list checker**, **Channel readiness board**, **Claims checker**.
- PLM app: **Line plan matrix**, **Proposal studio**, **PACE decision room**, **Style stage-gate stepper**, **Critical-path calendar**, **Forecast & sign-off grid**.

One table per app, with these columns:

| CMP ID | Component | What it does (one or two sentences) | Primary users | Pages / tabs | UI patterns | Objects read / written | Agents / workflows | L1 feature IDs | Design notes (key states, interactions, special visuals) |
|---|---|---|---|---|---|---|---|---|---|

Rules:
- Every L1 feature belongs to exactly one component (the Component column in section 7), and every component serves at least one L1 feature. Every page lists the components it uses (section 11).
- Components differ by app; a second app gets its own list. Shared, cross-app components are listed once after the app tables.
- Usually 6–15 components per app. If an app needs more, it is probably two apps.

### `check_docx.py`

Save this as `_working/check_docx.py` and run it on the finished file (`pip install python-docx --break-system-packages` if needed). Extend it with case-specific checks; never weaken it.

    import re, sys, hashlib, collections
    from docx import Document
    from docx.text.paragraph import Paragraph
    from docx.table import Table
    doc = Document(sys.argv[1])
    errs = []

    # --- walk the body in order, tracking the current Heading 1 / Heading 2 ---
    blocks = []                                   # (kind, obj, h1, h2)
    h1 = h2 = ""
    for el in doc.element.body.iterchildren():
        if el.tag.endswith("}p"):
            p = Paragraph(el, doc); s = p.style.name if p.style is not None else ""
            if s == "Heading 1": h1, h2 = p.text.strip(), ""
            elif s == "Heading 2": h2 = p.text.strip()
            blocks.append(("p", p, h1, h2))
        elif el.tag.endswith("}tbl"):
            blocks.append(("t", Table(el, doc), h1, h2))
    paras = [b[1] for b in blocks if b[0] == "p"]
    tables = [b[1] for b in blocks if b[0] == "t"]
    def head(t): return [c.text.strip() for c in t.rows[0].cells]
    def cells(t): return [c.text for r in t.rows for c in r.cells]
    def heading(p, lvl): return p.style is not None and p.style.name == f"Heading {lvl}"
    h1s = [p.text.strip() for p in paras if heading(p, 1)]
    allh = [p.text.strip() for p in paras if p.style is not None and p.style.name.startswith("Heading")]
    text = "\n".join(p.text for p in paras)
    alltext = text + "\n" + "\n".join(x for t in tables for x in cells(t))

    # --- structure: sections, parts, required and forbidden headings ---
    for i in range(24):
        if not any(h.startswith(f"{i}.") for h in h1s): errs.append(f"missing section {i}")
    if not any(h.startswith("Appendix") for h in h1s): errs.append("missing Appendix")
    def pos(pred):
        return next((i for i, h in enumerate(h1s) if pred(h)), None)
    pa, pb = pos(lambda h: h.startswith("Part A")), pos(lambda h: h.startswith("Part B"))
    s0, s10 = pos(lambda h: h.startswith("0.")), pos(lambda h: h.startswith("10."))
    if pa is None or pb is None: errs.append("missing 'Part A' / 'Part B' Heading 1 dividers")
    elif not (s0 is not None and s10 is not None and pa < s0 and s0 < pb < s10):
        errs.append("Part A must come before section 0, Part B between sections 9 and 10")
    for req in ["How to read this document", "5.5 Must-have vs future scope", "10.2 Must-have catalogue",
                "10.3 Future scope", "20.1 Acceptance checklist", "20.3 Build scope vs future scope",
                "20.4 Known limits of the build", "E. Feature build mapping", "F. Feature research mapping"]:
        if not any(h.startswith(req) for h in allh): errs.append(f"missing heading: {req}")
    for bad in [r"Full catalogue", r"^5\.5 Phases\b", r"Build slice", r"Known limits of Phase 1", r"^C\. Assumptions log"]:
        for h in allh:
            if re.search(bad, h): errs.append(f"old-layout heading: '{h}'")

    # --- placeholders and code ---
    for bad in ["TBD", "TODO", "{{", "```"]:
        if bad in alltext: errs.append(f"placeholder or code block: {bad}")
    if re.search(r'^\s*[\{\[]\s*"', alltext, re.M): errs.append("JSON-like block found")

    # --- readability: table width, Phase 1 columns, duplicates ---
    wide, ph_col, ph_row = [], [], []
    for n, t in enumerate(tables, 1):
        h = head(t)
        if len(h) > 10: wide.append(f"{n} ({len(h)} cols, '{h[0]} | {h[1]}…')")
        if any(x == "Phase 1" for x in h): ph_col.append(n)
        if h and h[0] in ("Item", "Convention", "Count", "Topic", "Block"):
            keys = [r.cells[0].text.strip() for r in t.rows[1:]]
            if "Phase 1" in keys: ph_row.append(n)
            for k, c in collections.Counter(keys).items():
                if c > 1 and k not in ("", "—"): errs.append(f"table {n} repeats row '{k}'")
    def few(xs): return ", ".join(map(str, xs[:6])) + (f" … (+{len(xs)-6})" if len(xs) > 6 else "")
    if wide: errs.append(f"{len(wide)} tables wider than 10 columns: {few(wide)}")
    if ph_col: errs.append(f"{len(ph_col)} tables have a 'Phase 1' column: tables {few(ph_col)}")
    if ph_row: errs.append(f"{len(ph_row)} spec tables have a 'Phase 1' row: tables {few(ph_row)}")
    seen = {}
    for n, t in enumerate(tables, 1):
        if len(t.rows) < 4: continue
        key = hashlib.md5("|".join(cells(t)).encode()).hexdigest()
        if key in seen: errs.append(f"table {n} duplicates table {seen[key]}; state it once and reference it")
        seen.setdefault(key, n)
    runs, cur = [], []
    for p in paras:
        if p.style is not None and "List" in p.style.name and p.text.strip(): cur.append(p.text.strip())
        else:
            if len(cur) >= 3: runs.append(tuple(cur))
            cur = []
    if len(cur) >= 3: runs.append(tuple(cur))
    for r, c in collections.Counter(runs).items():
        if c > 1: errs.append(f"list repeated {c} times (starts '{r[0][:50]}'); state it once and reference it")

    # --- "Phase 2/3" only in section 5, 10.3 and the Appendix ---
    def allowed(h1, h2): return h1.startswith("5.") or h2.startswith("10.3") or h1.startswith("Appendix")
    stray = collections.Counter()
    for kind, obj, b1, b2 in blocks:
        if allowed(b1, b2): continue
        txt = obj.text if kind == "p" else "\n".join(cells(obj))
        n = len(re.findall(r"\b(Phase [23]|later phase)\b", txt, re.I))
        if n: stray[b1] += n
    for sec, n in stray.items(): errs.append(f"'Phase 2/3' mentioned {n}× in {sec}; use the page's 'Future scope' line or 10.3")

    # --- diagrams ---
    if len(doc.inline_shapes) < 5: errs.append(f"{len(doc.inline_shapes)} diagram images (need ≥ 5: journey, app map, AI/data flow, lifecycle, ER)")
    caps = [p.text for p in paras if re.match(r"Figure \d+\.", p.text.strip())]
    if len(caps) < len(doc.inline_shapes): errs.append("every diagram image needs a 'Figure N.' caption")
    if not any(s.orientation == 1 for s in doc.sections): errs.append("no landscape section for wide tables")

    # --- catalogue: L1 tables, L2 tables, appendix mappings ---
    l1, l2, comp_ids, mapE, mapF = set(), set(), set(), set(), set()
    for t in tables:
        h = head(t)
        if h[:2] == ["ID", "Sub-feature"]:
            ids = [r.cells[0].text.strip() for r in t.rows[1:]]
            if "L1 reason" in h:
                rsn = h.index("L1 reason")
                for r in t.rows[1:]:
                    fid = r.cells[0].text.strip(); l1.add(fid)
                    if r.cells[rsn].text.strip() in ("", "—"): errs.append(f"L1 row without L1 reason: {fid}")
            elif "Why it can wait" in h: l2 |= set(ids)
            else: errs.append(f"catalogue table (ID | Sub-feature …) with neither 'L1 reason' nor 'Why it can wait': {h[:5]}")
        if h[:2] == ["ID", "Process stage"]: mapE |= {r.cells[0].text.strip() for r in t.rows[1:]}
        if h[:2] == ["ID", "Market coverage"]: mapF |= {r.cells[0].text.strip() for r in t.rows[1:]}
        if h[:2] == ["CMP ID", "Component"]: comp_ids |= {r.cells[0].text.strip() for r in t.rows[1:]}
    feat = l1 | l2
    if not l1: errs.append("no L1 (build scope) catalogue rows")
    if l1 & l2: errs.append(f"IDs in both L1 and L2: {sorted(l1 & l2)[:5]}")
    if mapE != l1: errs.append(f"Appendix E build mapping does not match L1 (missing {len(l1-mapE)}, extra {len(mapE-l1)})")
    if not l1 <= mapF: errs.append(f"Appendix F research mapping misses {len(l1-mapF)} L1 rows")

    # --- every stated count agrees with the tables ---
    for label, val in (("Grand total", len(feat)), ("L1 must-have", len(l1)), ("L2 future scope", len(l2))):
        found = re.findall(rf"{label}: (\d+)", alltext)
        if not found: errs.append(f"'{label}: N' not stated")
        for f in set(found):
            if int(f) != val: errs.append(f"'{label}: {f}' but tables have {val}")
    if feat:
        for a, b in re.findall(r"\b(\d+) of (\d+)\b", alltext):
            if int(b) == len(feat) and int(a) not in (len(l1), len(l2)): errs.append(f"'{a} of {b}' matches neither L1 ({len(l1)}) nor L2 ({len(l2)})")
    spec = {k: len({h.split()[0] for h in allh if re.match(rf"{p}\d+\b", h)})
            for k, p in (("Pages", r"PG-[A-Z]*"), ("Objects", r"OB-"), ("Agents", r"AG-"), ("Workflows", r"WF-"))}
    spec["Components"] = len(comp_ids)
    for t in tables:
        if head(t)[:2] == ["Count", "Value"]:
            for r in t.rows[1:]:
                k, v = r.cells[0].text.strip(), r.cells[1].text.strip()
                for name, n in spec.items():
                    m = re.match(r"(\d+)", v)
                    if k.startswith(name) and m and int(m.group(1)) != n: errs.append(f"Document control says {k} = {m.group(1)} but the specs have {n}")

    # --- components and L2 leakage into build specs ---
    if not comp_ids: errs.append("no component inventory table")
    for cid in set(re.findall(r"\bCMP-[A-Z]*-?\d+\b", alltext)) - comp_ids: errs.append(f"unknown component {cid}")
    def expand(txt):                                         # "FC-001–FC-004" -> each ID
        out = set(re.findall(r"\b[A-Z]{2,4}-\d{3}\b", txt))
        for a, p, x, y in re.findall(r"\b(([A-Z]{2,4})-(\d{3}))\s*[–-]\s*\2-(\d{3})\b", txt):
            out |= {f"{p}-{i:03d}" for i in range(int(x), int(y) + 1)}
        return out
    build_refs = set()
    for p in paras:
        if p.text.startswith("Features covered"): build_refs |= expand(p.text)
    for t in tables:
        h = head(t)
        for col in ("L1 feature IDs", "Features powered", "Feature IDs"):
            if col in h and h[:2] != ["ID", "Sub-feature"]:
                i = h.index(col); build_refs |= {x for r in t.rows[1:] for x in expand(r.cells[i].text)}
        if h and h[0] == "Item":
            for r in t.rows[1:]:
                if r.cells[0].text.strip() in ("Features powered", "Components and features", "Features covered"):
                    build_refs |= expand(r.cells[1].text)
    leak = sorted(build_refs & l2)
    if leak: errs.append(f"{len(leak)} L2 feature IDs referenced in build specs, e.g. {leak[:5]}")

    print("\n".join(errs) or "ok")
    print("features:", len(feat), "L1:", len(l1), "L2:", len(l2), "components:", len(comp_ids),
          "pages/objects/agents/workflows:", spec["Pages"], spec["Objects"], spec["Agents"], spec["Workflows"])

What it enforces, so you know what to fix when it fails:
- **Structure**: sections 0–23 and the Appendix; the Part A divider before section 0 and the Part B divider between sections 9 and 10; the required Heading 2s named in section 6 ("How to read this document", 5.5, 10.2, 10.3, 20.1, 20.3, 20.4, Appendix E and F); and none of the old-layout headings ("Full catalogue", "5.5 Phases", "Build slice", "Known limits of Phase 1", an Appendix assumptions log).
- **Readability**: no table wider than 10 columns; no "Phase 1" column or row anywhere; no repeated row label in a key/value table; no table or numbered list repeated word for word; "Phase 2", "Phase 3" or "later phase" only in section 5, 10.3 and the Appendix; at least five captioned diagram images.
- **Catalogue**: 10.2 tables (headed ID · Sub-feature … with an L1 reason column) hold only L1 rows, each with a reason; 10.3 tables (with a "Why it can wait" column) hold the L2 rows; Appendix E holds exactly the L1 IDs and Appendix F covers them.
- **Counts**: "Grand total", "L1 must-have" and "L2 future scope" are stated and match the tables wherever they appear; any "N of M" where M is the total matches L1 or L2; the Document Control Count · Value table matches the number of PG-, OB-, AG- and WF- headings and the component inventory.
- **Leakage**: no L2 feature ID in any page's "Features covered", any workflow's "Features powered", any agent's "Components and features", or any build-side "L1 feature IDs" / "Feature IDs" column.

Also check (script or by hand) that every page, workflow, agent and object ID referenced anywhere exists in its spec section (or, for future-scope assets, in the 10.3 assets table), and every source ID resolves in the Appendix.

---

## 9. Quality gate (run before finishing)

Write a script or check by hand. Every check must pass.

**Format**
- [ ] The deliverable is a single `.docx` built with the `docx` skill; it opens without errors.
- [ ] Headings use Heading styles; a table of contents is present; wide tables sit in landscape sections with repeating header rows.
- [ ] Diagrams are images with captions (or node/edge tables, with the reason in Document Control): at least the journey, app map, AI/data flow, main-record lifecycle and ER diagram.
- [ ] There is no JSON, YAML or code block anywhere in the document.
- [ ] `check_docx.py` prints "ok".

**Readability**
- [ ] Part A (sections 0–9) reads on its own: someone who stops at the end of section 9 knows the problem, the solution, the scope split and the key decisions.
- [ ] "How to read this document" tells each reader which sections to read.
- [ ] Each Part B section opens with one line on what it holds and who uses it.
- [ ] Every list, table and threshold is stated once and cross-referenced elsewhere; no table exceeds 10 columns.
- [ ] Future scope is described only in 5.5, 10.3 and the pages' "Future scope:" lines.
- [ ] Render a few pages (the catalogue, one page spec, one workflow spec) and check they are readable at normal zoom: no column squeezed to a few characters, no table split mid-row in a confusing way.

**Completeness**
- [ ] All sections 0–23 and the Appendix are present and non-empty (or carry a one-line "not applicable because…").
- [ ] Every persona has at least one workflow in 8.2, and every workflow names real build-scope page IDs.
- [ ] Every page has purpose, components used, blocks with data sources, actions, empty state and features covered.
- [ ] Every page has its Screen UX fields; every persona's home follows the home rule; exactly one persona is Primary; every action with prerequisites is specified disabled-with-reason; 4.1 ends with the Visual acceptance block; 20.2 follows the storyline order; section 19 carries the demo data rules.
- [ ] Every object field has a type, and every picklist lists its values.
- [ ] Every agent and workflow uses the full spec table, and every workflow has exactly one trigger type and a numbered path.
- [ ] Every scoring rule (if any) has checks, inputs with sources, a formula, all four result bands and a weight, and the weights total 100 per tenant.
- [ ] Every stage/status picklist has a transition table with gates, and every record page's stages or tabs list fields, editability and gate; the two agree.
- [ ] Every badge, score, pip or "x of y" shown on a page is a computed field with a formula.
- [ ] Every page action that changes data names a workflow (or a direct object update); every creatable record has a create surface or a creating workflow.
- [ ] Every agent has a read tool covering the objects it answers about, and test questions with expected answers from the seed.
- [ ] Every agent, workflow, integration and AI surface is labelled Live / Deterministic / Seeded / Mocked.
- [ ] Every input file and page is in the coverage map, and every out-of-ask block has a Decision.
- [ ] The component inventory covers every app, and every L1 feature maps to a component.
- [ ] Every L1 row has an L1 reason with evidence; every client-asked item is L1 or has a Decision; every agent the client will see is L1.
- [ ] Every L2 row is in the future-scope tables with why it can wait and what it depends on.
- [ ] POV/demo: a reset workflow exists and seed dates are relative to the demo day.

**Consistency**
- [ ] Every L1 feature maps to a page, and to an object or workflow/agent where it needs one.
- [ ] Every specified page, block, object, workflow, agent, integration, component and seed record serves at least one L1 feature; L2-only assets appear only in the future-scope assets table, and no build spec lists an L2 feature ID.
- [ ] Every page appears in the nav or is reached from another page, and none is orphaned.
- [ ] Every object is used by at least one page, agent or workflow.
- [ ] Every object.field referenced in a page, formula, workflow or mapping exists in section 12.
- [ ] IDs, names and counts match across the prose, the feature tables, the specs and the component inventory; hero records have one name everywhere, and agent test answers match the seed plan.
- [ ] Thresholds (confidence bands, margins, deadlines) are stated once and used the same way everywhere.
- [ ] Every promise in 17 and 4.1 (logged fields such as model and confirmed_by, which AI surfaces are logged) has a matching field in section 12 and a writing step in a workflow or agent spec.
- [ ] Permissions in 16 match the page personas in 11, the nav items defined per role, the Primary users in the catalogue (10.2) and component inventory (23), and every workflow or agent read filter (one filter per restricted role). A persona redirected away from a page is never listed as its user, unless the page gets a filtered view for them.
- [ ] Field examples in section 12 use the hero-record values from 19, so seeding from the examples creates no conflicts.
- [ ] Every report or chart counted in 9 or 20.3 has a page spec.

**Evidence**
- [ ] Research ran through the `research` skill, or the fallback and its reason are recorded in Document Control.
- [ ] Every client fact traces to the evidence log, and every market claim has a source ID that resolves to a URL.
- [ ] Every gap is resolved as research, a decision or a logged assumption, with nothing silently skipped.

**Usefulness**
- [ ] The seed plan gives a count for every object and a non-zero count for every picklist value a page groups by, and plants a defect for every warning, gate block and exception path.
- [ ] The demo storyline touches every module that has L1 features, and uses nothing L2.
- [ ] Someone with no other context could design and build the app from this Word document alone.

If a check fails, fix the document rather than weakening the check. In POC Studio the independent review is the AI PM (ai-pm, stage `scoping`), which re-runs `check_docx.py` and judges the scope; outside POC Studio, have a separate agent that did not write the document review it for contradictions before you finish. The lessons in sections 11–12 are also in the AI PM's lesson bank (L-001 to L-006); add new ones there, not here.

---

## 10. Writing style

- Plain, specific language. Name the record, the field, the number. Write "Invoice.match_score below 0.85 goes to the Exceptions queue", not "low-confidence items are flagged".
- Use the client's own vocabulary for stages, meetings, roles and documents, and define it in the glossary.
- Use tables over prose for anything with attributes. Use diagrams (as images) for flows, the app map and the ER diagram.
- Lead every section with the conclusion, then the detail.
- Long is fine; vague or hard to navigate is not. Every sentence should help someone design or build something. Say each thing once and point to it, keep tables narrow, and use a diagram wherever a reader would otherwise have to assemble a flow from several tables.
- Don't use placeholders such as TBD. Make the call, log it as an assumption, and move on.
- Write for the client as well as the builder: no internal process notes (e.g. "search budget ran out") in the document; say "needs confirmation" instead.

---

## 11. Calibration: how the Pentland example maps to this skill

- **Input**: an email asking for a POV on Product Enrichment and PLM in fashion, a 6-slide deck (future org, Demand vs GSP roles, new-product routes, range-to-release workflow), and a 6-page image-only PDF ("How we operate": strategy → concept → creation → activation, with NPD / Low touch / Zero touch lanes; planning calendar; bottom-up forecast).
- **Type**: A (POV in a known category), secondary C. **Framing**: POV/demo.
- **Research**: about 10 vendors per app, EU AI Act and C2PA, AI-UX guidance; 188 sources. Research also found the client's current stack (Centric PLM, Salsify, SAP, Shopify), which changed the positioning.
- **Catalogue**: PLM 161, Enrichment 159 and AI layer 18 sub-features, plus a 13-agent catalogue and a 36-component UI list.
- **Components**: e.g. Content Hub: content builder, tech pack reviewer, content generator, asset shot-list checker, channel readiness board, claims checker; PLM: line plan matrix, proposal studio, PACE decision room, style stage-gate stepper, critical-path calendar, forecast & sign-off grid.
- **Build plans**: PLM with 5 journey sections plus supporting pages, 19 objects, 3 workflows, one live Copilot and seeded ★ AI. Content app with 6 pages, 6 objects with typed fields, a 7-stage product record, 9 workflows (W1–W9), named seed records, an acceptance checklist and a demo path.
- **Sizing lesson** (from the Pentland scoping reviews): reviewers found 19 objects, many personas and many pages too heavy. They asked for about 10–12 objects, three personas, a handful of well-defined pages and three workflows (reset demo, change stage, generate the PACE pack PPT). They also rejected a draft that had drifted into a product-data and GTIN tool. The fix: keep the whole journey (strategies, concept, PACE, product record, line plan, critical path, materials, approvals) on fewer, richer pages, keep checks inside the product record, and seed every page.
- The client's process stages and meeting names (PACE, IBP, lanes) drove the page order, the stage picklists and the demo story.

A scoping document from this skill should contain everything the Excel and both build plans held, in one Word file, in the structure above.

**What the builds had to improvise** (both apps were built as code apps; the build plans missed these, and the rules above now require them): a generic read workflow as the copilot's tool, an activity-log object, a reset-demo workflow with seed snapshots and date shifting, an object prefix to avoid clashing with an older model on the tenant, one validated change-status workflow for all objects with per-object allowed values, gate conditions per stage, computed completeness/readiness/validation fields recalculated on every save, planted seed defects matching the copilot's expected answers, a deep-link route for agent answers, global brand/season filters, and a browser-side fallback when the agent could not generate a deck. Also note that the inputs spent much of their pages on demand and supply planning while the ask was PLM and Enrichment; the PLM build absorbed it as PACE meetings, forecasts and milestones rather than a third app.

**Don't copy these numbers.** Pentland's counts (two apps, ~160 sub-features per app, 13 agents) fit Pentland. Size each new case from its own process and category.

---

## 12. Calibration: the brand compliance example

- **Input**: one page of meeting notes. The ask was to validate retail shelf compliance from photos using AI or computer vision; the KPIs listed were shelf space, visibility, logo placement, font and tagline; the targets were drinks brands (Diageo and Jim Beam named); field reps are offline, so on-device processing is needed; hundreds of thousands of stores; options weighed were classic vision models vs fine-tuned vision LLMs; the goal was the most frugal solution delivering 7–10 KPIs.
- **Type**: G (AI scoring). **Framing**: POV/demo; the agreed next step was a 3–4 slide proposal deck with a working prototype.
- **What was produced**: 6 KPIs (must-stock SKU presence, share of shelf, campaign and signage, eye-level visibility, brand placement and integrity, price and promo). The asked-for logo, font and tagline items were folded into brand integrity and campaign checks. Each KPI has an industry name, evidence with sources, a checks table, an inputs table with source type and source (manual input, web search or none), a formula, Pass / Needs attention / Fail / Not assessable bands, critical flags (missing hero SKU, counterfeit, price above MRP in India) and real-world example links. Weights per brand total 100, with reasons (price leads for Diageo because its strategy depends on prices reaching the shelf).
- **Components**: e.g. shelf photo capture (offline), KPI scorer, store scorecard, brand-team exception queue, rule & weight configurator.
- **Lesson**: for scoring apps, the rules spec is the heart of the scope, and the pages, objects and workflows are built around it.
- **Prioritisation lesson** (from the first run of this example): the first draft marked 126 of 175 rows L1 and specified 18 pages, which buried the core flow. Re-tested with the L1 rule (step 5), L1 is the capture → quality check → recognition → KPI scoring → review → follow-up loop, the agents (copilot, vision judge, action planner), the five asked items (shelf space, visibility, logo, font, tagline) plus the 7–10 KPI target, and the research must-haves (availability, price/MRP, critical flags); integrity checks, imports, coaching, model monitoring, digests, WhatsApp, native app and BI export are L2 future scope with no build spec.
- **Readability lesson** (from the VTInfo shelf-compliance run): the content was strong, but the document was hard to use. It ran to about 130 pages with 240 tables and only 3 diagrams, and four build sections held about 60% of the words. The catalogue had 21 columns, so every cell wrapped to a few characters even in landscape. Priority and a separate "Phase 1" column disagreed on 23 rows, and the Phase 1 count was 134 in one section and 131 in two others. Out-of-phase pages, workflows and agents were fully specified anyway, "Phase 2" appeared 53 times across the specs, and the acceptance criteria were printed twice. The fixes now in this skill: Part A / Part B with a reading guide, a lean 9-column catalogue with build and research details in Appendix E and F, no phase flags in specs, every count generated by script, each list stated once, and at least five diagrams.