# Use-case pointers

This file holds the platform lessons from earlier UnifyApps builds, sorted by use-case type. platform-master uses it
twice. At the start of Stage 4 it reads the approved scoping document, picks the use-case type below, and adds the
matching pointers to UnifyApps Headless's build request: the "every use case" pointers plus the pointers for that
type. When UnifyApps Headless returns its Zen build plan, the plan review checks the plan against the same pointers
(see the last section and plan-review-checklist.md). The pointers cover platform mechanics and the mistakes that
cost a rebuild before. They never override the scoping document, the design system or POC Studio's stages. Where a
pointer and the scoping document disagree, the scoping document wins and the plan review notes the difference.

## How to classify

Read the scoping document's problem statement, process and Part B build spec. Pick the row whose description fits
the unit of work and the first screen the customer will judge. Then pick the architecture style.

- **Full atomic:** the process runs in stages. Each AI step is its own AI Agent that returns a confidence score.
  Readings below the bar go to a Resolution Inbox, and an Evidence Ledger records every AI call.
- **Light:** the process is still agreed first. AI steps sit inside the workflows that need them, and a
  low-confidence reading shows as "needs review" on the screen where the person already works. There is still one
  evidence row per AI call.

| # | Use-case type | What the scoping document says (signals) | Style | Why |
|---|---|---|---|---|
| T1 | **Request / case desk** | Items arrive (invoices, claims, travel or onboarding requests, customs entries). Each one is read by AI, checked against rules, policy or tolerances, then auto-decided or routed to an owner. Words like queue, exception, approval, tolerance, hold, owner. | Full | AI readings drive a decision on every item, so each reading needs a confidence score and a route to a person. |
| T2 | **Supplier / third-party risk control tower** | A register of suppliers or providers, external signals or feeds, alerts, treatments, dependencies on critical operations, periodic reviews, board metrics, resilience. | Light | It is a command centre over records. AI summarises and drafts; it does not decide each case. |
| T3 | **Procurement / sourcing / contracts** | Supplier registration and qualification, RFQ to award, spend, savings, contract renewals, compliance documents. Several buyer personas. | Light (Full for one desk where AI readings decide qualification) | A multi-persona hub of registers and dashboards. AI assists each persona. |
| T4 | **Document evidence / fraud verdict** | Documents (invoices, claims, expenses, certificates, KYC) are checked for tampering, duplicates or registry mismatches. The output is a verdict with evidence, and a ground-truth set of documents may exist. | Full | The verdict rests on several independent readings, each of which can be wrong. |
| T5 | **Designed multi-step agentic operation** | A solution design that already names the steps, many AI actions, cycles, confidence gating, an inbox, precedent or learning from corrections. | Full | The design is already atomic. The build follows it step by step. |
| T6 | **Golden-record 360 with rules → to-dos → cases** | One record (student, member, patient, customer) assembled from several systems. Signals and rules raise to-dos and cases. Write-back to source systems with an audit trail, plus an admin console. Words like "brain", 360, lifecycle. | Light (Full when AI readings decide cases) | The rules are deterministic config. AI explains and answers questions. |
| T7 | **Executive analytics over a context graph** | Conversational analytics for executives over an existing data estate, with the context graph as the foundation. Cross-entity questions that need traversal (one customer trading with several divisions). | Light | Chat over data. Figures come from queries, never from model judgement. |
| T8 | **Executive / government performance across entities and regions** | A performance index over many entities and regions, citizen or customer voice, KPI trends, interventions, a regional map, a decision centre for leadership. | Light | A command centre plus insights. No per-item AI decisions. |
| T9 | **Role-governed KPI command centre** | Executive KPIs computed from operational systems (facilities, real estate, campus, hospital, utilities). Roles that see different data, variance explained, actions approved and written back as work orders, an admin console. | Light | KPIs are calculations. AI explains them from a calculation pack. |
| T10 | **Read-only scoring overlay on a system of record** | Score records in a CRM or ERP with the customer's own method (a workbook, a deck), show how scores move over time, and never write to the source. | Light | Scoring is a deterministic, versioned contract. The model never scores. |
| T11 | **Document upload → OCR → agent** | People upload files in the app. Text is extracted, parsed into records, and an agent answers over them or raises actions. | Light | One ingestion workflow and one agent. No staged decisions. |

**When none fits.** Classify by the first screen the customer will judge. If it is a command centre over records, use
T2's pointers. If it is a queue of items with a decision on each, use T1's. When the scope clearly spans two types
(a case desk with a document verdict, a command centre with an upload flow), add the pointers of both and name the
primary type first. Say in the build request which type was chosen and why, in one line. Never force Full onto a
dashboard, analytics or chat-over-data use case.

## Pointers for every use case

Add all of these to the build request. Each starts the way it goes into the request.

**Shape of the app**
- The build should deliver **one application with navigation**, with screens grouped by role, not one app per screen
  or per persona. Build a second app only when the scoping document asks for one. *Five screens listed as five apps
  had to be merged.*
- The build should keep **the customer's records, decisions and open work first** on every page Part B defines;
  process steps, agent internals and system diagrams never lead a page. *An architecture-first home was rejected as
  "admin pages".*
- Where Part B's first page is an overview, the build should have it **lead with what needs attention, and why**,
  computed from the data, not long authored paragraphs. *Overviews with authored paragraphs were rejected as "too
  long".*
- The build should **not build its own copy of a module UnifyApps already ships** (an AI-governance page, a context
  graph viewer). Link to or embed the platform's own module. *Home-made copies were rejected on sight.*
- The build should **not add a live ticker or moving banner** unless the scoping document asks for one. *Two
  customers had it removed.*

**AI on the screens**
- The build should put **AI insights on every screen**, not on one AI page, plus an "ask" action on every tile,
  chart, row and AI result. The ask action opens the chat with that item as context. *A single AI page read as
  bolted on.*
- The build should **keep each insight call small**: about 2–3 findings, a token cap of about 1,600, input capped at
  about 30 rows or 8,000 characters. *Large insight calls made screens wait 16–36 s.*
- The build should **store insights per screen and show the stored ones first**, so a screen never opens empty. Live
  re-runs come after. Cache for hours, not minutes, keyed on screen, language and rows. After any data change that
  moves a screen, re-run that screen's insights or stamp them "as of". *Empty panels on load were flagged; stale
  cards contradicted the tiles.*
- The build should **schema-check every AI output before storing it** (expected keys, no blank titles). *Cards were
  stored with blank titles because the model used different keys.*
- The insight prompt should say **"quote only figures present in the data; never count, add or average rows"**.
  *A fast model miscounted 26 as 30.*

**Chat agent**
- The build should give every chat agent an **entity guide** in its instructions: what each object and field holds,
  its category values, "search before saying something is not in the records", and which records to exclude
  (control groups, superseded rows). *Without it the agent told the customer data did not exist.*
- The build should give the chat agent a **turn contract**: answer once, never end on "let me look…", no third
  guess, never name its tools, check numbers the user quotes, and when asked for a draft either show it or say why
  there is none. *Stalling and tool-naming answers were rejected.*
- The build should **hide the suggested-question chips as soon as the user types, sends, or any answer text
  appears**, so the chips never overlap an answer. *"Still overlapping, fix it once and for all" came up in two
  builds.*
- The build should **make every chart the agent writes render**. Give the agent whole example chart blocks in the
  exact format the app's chart renderer parses, and test with a report question that returns several charts: the
  number drawn must equal the number of blocks. *Four charts were written and only one was drawn, because the agent
  put the chart shape in the wrong field.*
- The build should put **every agent write behind an approval card**. Read-only is the default.
- The build should put **one identity line in every AI prompt**: the customer's business in its own words (the
  real industry and product name). *A wrong industry word had to be swept from code, records, prompts and the
  agent.*
- The build should **reset everything cloned from another agent or workflow**: system prompt, avatar, name and
  suggested questions. *A cloned writer carried another customer's prompt.*

**Workflows and AI steps**
- The build should have **one orchestration workflow per human action**. "Analyse this document" runs intake to
  filed record in one call and returns every stage for the screen. *Separate "analyse" and "file" steps left a real
  run with zero records filed.*
- The build should **never let a model do arithmetic, lookups or thresholds**. Totals, scores, matches and rule
  checks are workflow steps. The model explains, extracts and judges. *An LLM-derived figure cannot be defended.*
- The build should make **every AI reading that drives a decision carry a confidence score and its evidence**, and
  send a reading below the bar to a person, never "proceed with a warning". There should be one evidence row per AI
  call.
- The build should keep **one current reading per record**: write it with an upsert keyed by the record it
  describes, and keep the history in the evidence log. *Inserting a row per run gave 167 estimates for 121 requests,
  and the dashboards stopped reconciling.*
- The build should **resolve each entity once** and pass its key through the orchestration. *Two steps resolved the
  same issuer differently and gave two answers.*
- The build should **use native workflow nodes first**: filter in the fetch condition, `count_records`,
  `run_sql_query_on_list` for group and join, `sort_list`, `to_json_object`, IF_ELSE, LOOP, `update_records`
  MULTIPLE, and the STOP result map. A code node is for one real computation of about 40 lines at most, never a
  renamer, an envelope, a filter-builder or a no-op. Avoid `aggregate_records` (it does not group) and `filter_list`
  (it returned nothing). *Builds with 46–48 % code nodes were rejected.*
- The build should **guard SQL-on-list against an empty list**, and should never upsert with a blank id (that
  inserts a new record).
- The build should **use workflows to compute server-side counts and aggregates** for screens and agents. It should
  not page rows into the client or into the model.

**Data model and writes**
- The build should **update records by read-merge-write, never by a partial update**. A partial update replaces the
  whole record. *One partial update wiped 415 records.*
- The build should **retire records with an `active=false` or superseded flag and hide setup or test rows with a
  flag**. It should never delete them.
- The build should **index every object for the queries its screens, data sources and workflows run**, and confirm
  each index has finished building. *A build shipped with no indexes.*
- The build should **keep counts and filters consistent**: a tile, its chart, its list and the agent's answer give
  the same number for the same filter. Derive summary KPIs from the transactions so they cannot disagree. A count
  hook's filter should be memoised so it does not refetch on every render. *A count refetched once per frame on a
  green build.*
- The build should **seed every status band and legend value with at least one record**, and keep headline KPIs
  plausible (a share of the total an executive would believe). *A risk ceiling below the CRITICAL threshold meant
  no record could ever be critical, and an "uncovered spend" figure came out at 86 % of all spend.*
- The build should **model each outside system as its own objects under a neutral role name**, then sync it into the
  product's objects. That keeps the product's model clean when a real connector replaces it.
- The build should **give every generated person a unique full name and no honorific or gender guess**, and the
  agent should disambiguate people by code, never by name alone.

**What appears on screens**
- The build should show **no internal codes, raw ids, raw JSON, object prefixes or "(s)" plurals** on any screen.
  Labels and a readable renderer instead. *Step and agent codes on customer screens were rejected.*
- The build should contain **no other vendor's name anywhere**: UI, records, enum values, primary keys, prompts,
  agent instructions, descriptions and exported definitions. Only UnifyApps and genuine connector names. *One purge
  missed an enum, a primary key, two prompts and an agent's text.*
- The build should **use the customer's currency and a readable money format** ("10.61bn", not "10609m"), and
  should carry no currency words from another region.
- The build should **draw real boundaries when a map shows regions** (data by state, district or territory, with no
  site coordinates): real administrative geometry projected at build time, a ranked list beside it, and click a region
  to ask the agent. A map of sites (records with latitude and longitude) follows the wireframes skill's
  `references/map-component.md` instead (the `Map:` pointer). *Bubble maps on an abstract field were rejected
  on sight, three times.*
- The build should **update any UI text that claims where data comes from** whenever the read path changes. *The
  chat dock still said "reading 22 objects" after the move to the graph.*

**Platform order of work**
- The build should **create every data source before the app's final publish**. A running app only sees the data
  sources that existed at its last publish.
- The build should **re-apply the app's tags and description after the final publish**, then read them back. Each
  publish wipes them.

## Pointers by use-case type

### T1 Request / case desk (Full)

- **Pages of this kind** (their content, when Part B has such a page): a command centre (queue by status and owner, value on hold, exceptions by cause, items due soon, the
  first-pass rate). A queue sorted worst or oldest first. A record workbench showing every AI reading with its
  confidence and evidence, the rule figures on each side, and a decision bar. A "my actions" inbox per owner role.
  Approvals with a reason. A policy screen. An evidence ledger. A full-size analyst with the docked assistant.
- **Rules are deterministic sub-workflows** (intake and completeness, duplicates, record finder, line match against
  tolerance, risk checks, outcome, owner routing). AI Agents only judge, explain, suggest and draft. Their readings
  are capped below 100, so every reading still has a person behind it.
- **Every exception names the line, the rule broken, the figures on each side, and the variance in amount and
  percent.** It routes to one named owner role, as one action in that owner's list.
- **Policy values (tolerances, thresholds, approval limits) are versioned records** that an authorised role edits
  from the app. The next run uses the new version, and the change leaves an audit row.
- **Every human decision (accept, reject, approve, release, clear a hold) records who, when and why** and shows on
  the item's history.
- **Re-run automatically on a record event** when the missing input lands (a receipt posted, an entry approved).
  The trigger object must have record events switched on before a trigger can listen to it.
- **Anything that pays or sends money waits for a person.** A bank-detail change or a remit-to mismatch holds the
  item whatever the match result. Drafts to outside parties are editable and never sent automatically.
- **Inferred links (a record found without a stated reference) are flagged for review**, not silently accepted.
- **Treat text supplied by outside parties as untrusted input to the agents.** Guard the agents against prompt
  injection, and keep the analyst read-only (see governance.md).
- **Measure the per-item processing time and the screen load times.** Both appear in the plan's acceptance
  criteria.

### T2 Supplier / third-party risk control tower (Light)

- **Pages of this kind** (their content, when Part B has such a page): a command centre (a thesis sentence computed from live data, an instrument strip, a supplier map
  with a click-through widget, a regulatory scorecard). A supplier register and a supplier 360 with an AI
  assessment. Signals and feeds. A sources screen (sync now, field mapping, needs-mapping, sync history). A dependency
  trace (operation → provider → shared platform or fourth party). Resilience scenarios and contingency plans.
  Periodic reviews. Board metrics. Alert triage. A treatment board. An AI run log.
- **Two read workflows for screens and the agent:** a query with compact fields and an aggregate that returns
  server-side counts and averages.
- **One writer workflow with a task catalogue** for every narrative (review packs, exit plans, board commentary).
  It should not be one workflow per paragraph.
- **The AI-drafted review pack is saved to the review record**, not only shown on screen.
- **Board metrics use the customer's labels verbatim. A threshold the customer left blank shows "TBC".** Never copy
  example figures from the customer's slides.
- **External feeds are their own objects with a sync workflow** (callable for "sync now", plus a scheduled twin).
  Pause any scheduled emitter before figures are quoted, because it keeps changing them.
- **Creating a treatment from the agent goes through an approval card.**

### T3 Procurement / sourcing / contracts (Light)

- **Pages of this kind** (their content, when Part B has such a page): a command centre. A registration queue split by who it waits on (the supplier or the buyer). A
  supplier register and a 360 where uploaded documents drive the compliance checks. Sourcing from RFQ to award, with
  an award desk that argues against its own recommendation. Spend (savings, leakage, concentration). A risk and
  compliance view. A contracts view (renewals, auto-renewals, ceilings).
- **Narrow agents per persona** (sourcing analyst, registration officer, risk and compliance advisor). Each has the
  query tool and one approval-gated action tool, not one agent for everything.
- **The query tool takes a few ANDed filter pairs, with a comma meaning IN**, and compacts prose fields by shape.
  The agent then never gets a wall of text.
- **The scoping document's reason for buying (such as replacing another vendor's suite) never reaches the product**,
  its records or its prompts.
- **Headline KPIs pass a plausibility check.** Count only what the label says. *Documents expiring were counted as
  uncovered spend.*
- **Bilingual or RTL scope means every prose field has its second-language value populated**, not only the UI
  strings. *Arabic mode showed English record prose.*

### T4 Document evidence / fraud verdict (Full)

- **Pages of this kind** (their content, when Part B has such a page): a command centre (a detection overview with one axis per check). A triage queue, worst first. A
  workbench where the risk score is broken down into each finding's contribution, with a decision bar. An analyse
  screen (drop a document, watch the stages run). Network, issuers, claimants and investigation cases. A check
  catalogue.
- **One intake orchestration** takes a document to a filed record: forensics, registry check, duplicate check and
  filing in one call. It returns every stage for the analyse screen.
- **The verdict comes from deterministic checks.** AI explains findings and judges only where language is needed.
- **The duplicate key is strong**: a file hash, or document number plus total plus issuer, or text similarity of
  0.97 or more. *"Same issuer and same total" marked 54 of 65 invoices critical.*
- **Match identifiers against the whole extracted text and resolve by the strongest identifier** (the tax number
  first). Positional parsing broke on wrapped headers. A name that contains a city must not pass an address check.
- **Every finding's check id must exist in the check catalogue.** Assert it after each run. *23 orphan findings
  appeared.*
- **Add a rescore and a rollup workflow** so the score does not saturate and the aggregates stay current as volume
  grows. Hide trend charts that have only one period.
- **Store document files byte-exact.** Any conversion changes their hashes and breaks duplicate detection.
- **A proof run over a labelled document set**, scored against its expected outcomes, is a secondary screen. The
  working desk comes first.

### T5 Designed multi-step agentic operation (Full)

- **Follow the given design step by step**: the master workflow, then sub-workflows, then atomic agents. Each atomic
  agent is a real AI Agent invoked from its sub-workflow by the Invoke Agent node. A workflow pretending to be an
  agent does not count. Reuse envelope and dual-read logic as the agents' tools.
- **Confidence propagates as a minimum, never a mean.** The composite carries the input that capped it.
- **The customer's view first**: the customer's records, shelf or portfolio, decisions and "waiting for you". The
  process river, system map, cycle console, Resolution Inbox, Evidence Ledger and agent detail sit under "How it
  works".
- **A one-screen business explanation of the use case**: who it serves, the problem, what each cycle does, and what
  the customer sees.
- **Resolution Inbox items open with the evidence assembled and the agent's answer pre-selected**, resolvable in one
  gesture. Every resolution writes a precedent rule.
- **Writes to outside channels pass a publish gate with an approval token bound to the change.** Readings are
  re-read after publish.
- **Deterministic, idempotent ids** so a re-run replaces instead of duplicating. A resolved item has a reopen path,
  so a rehearsal click does not lock a real decision.
- **Ingest workflows for a customer API that is not yet granted are defined but switched off** until access exists.
  The plan lists what the customer must grant.
- **Keep code nodes down.** An earlier build of this type was 46 % code nodes, with dozens over 60 lines.

### T6 Golden-record 360 with rules → to-dos → cases (Light; Full when AI readings decide cases)

- **Pages of this kind** (their content, when Part B has such a page): a "today" view (band counts, critical records ranked by cross-source signals). A generic record 360
  (one page for any record, never a page for one story person) showing the golden record with a source chip per
  value, a signal timeline, one ordered to-do list and write-back actions. Lists and to-dos. Operations desks for the
  reconciliations. Two-person approvals. Integrations (status, lag, queues, errors, resync). Admin. Audit. Analyst.
- **Ingestion through record-event triggers**, not buttons. Add a scheduled pull as a safety net that detects gaps
  and heals itself. Match and survive into the golden record, with lineage per field.
- **Signals, risk bands, to-do rules and reconciliation rules are config records** that admins edit. A derive
  workflow turns signals into risk, to-dos and a case, all driven by that config.
- **Write-back to the source system is audited**: a role check, a reason, and a second approver for money.
- **Admin screens:** lock keys after the first save (editing a key creates a second row). Fill reference fields
  from config dropdowns, not free text. Validate numbers on the screen and in the workflow. Saving one row must not
  discard another row's edits.
- **Governed reads need an environment-default user row**, or every unlisted user sees blank screens.
- **When the scoping document says "brain", "360" or "one record"**, design the ontology before any screen (see
  context-graph.md).

### T7 Executive analytics over a context graph (Light)

- **Check context-graph.md first** for what the tenant's graph supports. Decide the read path before the first
  object, because moving later meant rebuilding every data hook.
- **The graph is the only read path for figures.** Prove it with a divergence test: change one value in the graph
  only, see the screen move while the object stays put, then restore it. *"Every screen reads the graph" was claimed
  twice before it was true.*
- **One graph-query workflow serves both screens and agents.** Each agent gets that tool, the full schema and the
  category values.
- **KPI history is derived from the transactions**, so tiles and charts cannot disagree.
- **Pages of this kind** (their content, when Part B has such a page): an executive home (KPI tiles, a regional map, insights). A full-size ask page with question sets per
  persona. One parameterised division screen rather than a copy per division. A customer 360 reached by traversal.
  A receivables or credit view ("who to call first"). A data-estate lineage screen using neutral source roles.
- **A specialist agent docked per screen** (credit on receivables, explorer on the 360), with a group analyst as the
  default.
- **Show the traversal that only the graph can answer** (the cross-entity exposure) as a first-class screen
  element. It is the use case's core argument.

### T8 Executive / government performance across entities and regions (Light)

- **Pages of this kind** (their content, when Part B has such a page): an overview led by a decision board that pairs each risk with its action by shared evidence, plus an
  index with weighted dimensions. Entity performance (the entity against its cluster). Citizen or customer voice
  with a comment feed. Workforce quality. A regional map with several heat metrics and site pins. A decision centre
  with the full-size agent. Interventions shown before and after their start date.
- **A rules workflow derives risks, achievements, actions and the brief from the records.** Text authored in the
  seed data does not count.
- **Each insight carries evidence chips, an optional chart, one allowed action and "dig into this"**, and every
  chart can hand its data to the agent.
- **Show where each figure comes from** (lineage chips). No "illustrative" badges, and no pages about how the
  product was built.
- **Generate history from the baseline, never while a scenario is applied**, and anchor it on the earliest real
  point.
- **Derive relative measures (sentiment, posture) against the portfolio**, not from an absolute formula. *An
  absolute formula produced zero complaints.*
- **Each call in a chained action (apply, then refresh) reports its own result**, so a failed second call is not
  swallowed.

### T9 Role-governed KPI command centre (Light)

- **A governed-only data layer**: the app reads only through governed workflows (no direct storage bindings), one
  callable per governed workflow. Identity comes from the audit row of the call, roles live in a user-access object,
  and denials are audited (see governance.md).
- **Search applies permissions before ranking. The graph view returns restricted nodes as locked placeholders.**
  Every deep link to a record checks access on the server.
- **Explain variance with a deterministic calculation pack first.** The LLM writes from it, and every citation is
  validated against it.
- **Pages of this kind** (their content, when Part B has such a page): a portfolio command centre. Sector lenses, each opening on a measure that has history. An asset page
  with "why is this here". A metric page with "how is this calculated", drilling down to source rows. Search. An
  assistant. A graph explorer. An actions inbox with "what happened". An AI control tower (model routing, policy
  tests, audit). Admin (grants, permission matrix, policies, metric rules, connectors).
- **Actions follow a state machine.** Approval writes the work order back into the source system's object.
- **Sync acknowledges each source row it takes**, and a rollup workflow computes KPIs with native SQL-on-list
  rather than paged code, then raises recommendations with evidence when a rule fires.
- **Model choice per task is a config record**, so the control tower changes models without a redeploy.
- **A public app runs anonymous visitors as platform user 0.** Grant or refuse that user deliberately, and show a
  "no access yet" page rather than empty dashboards that state conclusions.

### T10 Read-only scoring overlay on a system of record (Light)

- **Never write to the system of record.** The overlay stores only its own objects: the scoring contract, daily
  snapshots and an evidence register.
- **The customer's scoring method is a versioned contract stored as records**, run by one shared deterministic
  engine. The model never scores. Show the contract version in the app.
- **A self-test workflow runs the customer's worked examples and edge cases** (ceiling, off-scale, invalid state)
  after every engine change.
- **List the rules the method does not define as assumptions** and label each where it is used. Never fill them
  silently.
- **Pages of this kind** (their content, when Part B has such a page): a map or plot of every record, with a "no score" lane, direction and trails over time. A record
  detail with the score breakdown, the stage ribbon, per-factor evidence and a history replay that re-scores each
  moment. A contract screen editable only by authorised roles, with a reason and an audit row. A full-page agent
  that answers with the same visual.
- **History replay groups changes made at the same instant into one moment.** Record creation writes every field at
  once.
- **Day-over-day direction needs a real-move test** (stage or score changed). Otherwise fall back to stage age and
  activity.
- **Snapshots at volume run as a page workflow plus a coordinator** (about 100 records in 10 s per page), on a daily
  schedule. Collect loop results into a register object, because a loop does not return them.
- **To add a new value to a model object's enum, extend the schema first.** Retire old records with `active=false`.

### T11 Document upload → OCR → agent (Light)

- **One ingestion workflow**: create the document record, run the OCR node (a text-extraction model), parse, then
  bulk-upsert the extracted records. It took about 39 s, so the screen shows progress.
- **Pages of this kind** (their content, when Part B has such a page): a documents screen (upload → library → analysis with a document viewer and the extracted text →
  "raise as action"), and "ask about this" on every card.
- **The agent knows the document object** in its entity guide and reads files attached in the chat.
- **Insights carry one bound action each.**
- **Use native blocks and nodes first.** Build a custom component only for what they cannot draw (a real map, a
  gauge with a target, a clickable grid).

## What the plan review checks from this file

Check the Zen build plan against the pointers that went into the build request:

- [ ] The plan names the use-case type and the style (Full or Light), and both match this file's classification of
      the scoping document, or the plan says why not.
- [ ] One application with role-grouped navigation; every page leads with the customer's records, decisions and
      open work.
- [ ] Each page Part B defines carries the content its kind calls for in the type's "Pages of this kind" pointer
      (pages are never added or removed by this check; Part B and the design system decide the pages).
- [ ] Insights on every screen, small calls, stored first, schema-checked, with "quote only figures in the data"
      in the prompt; an ask action on tiles, charts and rows.
- [ ] Every chat agent has an entity guide, a turn contract, the identity line, approval on writes, and a chart test
      that counts charts drawn against blocks written.
- [ ] One orchestration workflow per human action; arithmetic, lookups and thresholds in workflow steps; native
      nodes first.
- [ ] AI readings that drive decisions carry confidence and evidence, one current reading per record via upsert,
      one evidence row per AI call, below-the-bar readings routed to a person (inbox in Full, "needs review" in
      Light).
- [ ] Writes use read-merge-write; objects are indexed for their queries; counts agree across
      tile, chart, list and agent.
- [ ] No ticker unless asked, no other vendor's name, no internal codes
      on screens, and a real-boundary map if a map is in scope.
- [ ] Data sources are created before the final publish, and tags and description are re-applied after it.
- [ ] The type-specific data-model and workflow pointers (T1–T11) are reflected in the plan's objects, workflows
      and agents.
