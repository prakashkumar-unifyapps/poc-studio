# AI PM lessons

Rules learned from real reviews. Every review of a stage runs the lessons for that stage and `all`.
Add with `lessons.py add`; never edit an id. Owner profiles (`profiles/<owner>.md`) are not shipped: they are
created at runtime, in the lesson home, the first time an owner's gate feedback is personal. The seed below comes from feedback already written into the stage skills
(scoping §11–12, the design-system defect register, the collateral skill's Pentland notes), so the AI PM starts
with the team's history instead of from zero.

### L-001 · scoping · sizing
- check: The build scope stays within the POV budget per app: 3–6 pages, 8–12 objects, 3–8 workflows, one live copilot. Over budget is a finding even when the document explains it.
- why: Reviewers found Pentland's 19 objects, many personas and many pages too heavy and asked for about 10–12 objects, three personas and three workflows.
- origin: Pentland scoping review (scoping skill §11)
- added: 2026-10-30

### L-002 · scoping · drift
- check: The app's centre is the client's core loop. A supporting check (data quality, IDs, GTIN) that has grown into its own module or the home page is a blocking finding.
- why: A Pentland draft drifted into a product-data and GTIN tool and was rejected.
- origin: Pentland scoping review (scoping skill §11)
- added: 2026-10-30

### L-003 · scoping · prioritisation
- check: Re-test L1 when it is over half the catalogue. The core loop, the agents, the client-asked items and the research must-haves are L1; imports, coaching, monitoring, digests, extra channels and BI export are L2.
- why: The first shelf-compliance draft marked 126 of 175 rows L1 and specified 18 pages, which buried the core flow.
- origin: Brand-compliance scoping run (scoping skill §12)
- added: 2026-10-30

### L-004 · scoping · readability
- check: No table over 10 columns; one place for each list; every count generated, the same in every section; no "Phase 2" outside 5.5 and 10.3; at least five diagrams.
- why: The VTInfo document ran to 130 pages with a 21-column catalogue, three different Phase 1 counts and "Phase 2" 53 times in the specs.
- origin: VTInfo shelf-compliance run (scoping skill §12)
- added: 2026-10-30

### L-005 · scoping · out-of-ask material
- check: When the inputs cover more than the ask, the extra material is absorbed into an in-ask app (a tab, a meeting page) or scoped as later, with a Decision — never a silent third app and never silently dropped.
- why: Pentland's decks spent most pages on demand planning while the ask was PLM and Enrichment.
- origin: Pentland scoping (scoping skill §11)
- added: 2026-10-30

### L-006 · scoping · what builds improvised
- check: Part B specifies the things builds had to improvise: a generic read workflow as the copilot's tool, an activity-log object, reset-demo with date shifting, an object prefix, one validated change-status workflow, gate conditions per stage, computed fields recalculated on save, planted seed defects matching copilot answers, a deep-link route, global filters.
- why: Both Pentland builds had to invent all of these because the build plans missed them.
- origin: Pentland builds (scoping skill §11)
- added: 2026-10-30

### L-007 · design-system · same look
- check: With the logo covered, the main screen must not match a recent client's look (chrome + surface + layout). Compare against recent-looks.md.
- why: Pentland, ClickUp, Vermont and Topcon came out as one product in four hues.
- origin: design-system defect register v5
- added: 2026-10-30

### L-008 · design-system · brand decided outside the skill
- check: The brand hue follows the skill's own source order. A black-led or achromatic brand shipped on a coloured rail, or a hue taken from the site's link colour, is blocking.
- why: Three runs settled a hue with a "standing decision"; Pentland's black-and-lime brand shipped electric blue.
- origin: design-system defect register v5
- added: 2026-10-30

### L-009 · all · agent placement
- check: Every agent opens in the drawer on the platform's live agent component. An agent as a card or full-width block on a page, or an automation that writes answers for a refresh, is blocking.
- why: Pentland's Range Copilot was built as a block on Home fed by an automation.
- origin: design-system defect register v5
- added: 2026-10-30

### L-010 · all · status colours
- check: A chart or list series that encodes a status uses the status palette and a worded legend, never steps of the brand colour.
- why: Vermont's pass-rate chart showed Fail, Needs attention and Pass as three blues.
- origin: design-system defect register v5
- added: 2026-10-30

### L-011 · design-system · must-haves dropped
- check: Every L1 feature ID and CMP ID from the scoping document maps to an inventory row in the design system (with approved wireframes: every manifest component has a component page, design-system 0.0).
- why: Pentland's material compare, detail pane and docked copilot were L1 and were dropped.
- origin: design-system defect register v5
- added: 2026-10-30

### L-012 · all · implementation in copy
- check: No field names, query syntax or rule expressions on screen ("status = open", "interview_count > 0"); ratios shown as percentages, never 0.87.
- why: v5 tiles read "status = open"; the orchestrator's visual acceptance adds the percentage rule.
- origin: design-system defect register v5.1; orchestrator Stage 4 4a
- added: 2026-10-30

### L-013 · all · density
- check: One line per table cell (two in the first column), at most two chips then "+n", cards within four lines, no paragraphs or sub-score breakdowns in cells, no dead space beside header actions.
- why: v5 screenshots showed paragraphs and four-row breakdowns in cells and actions floating in their own row.
- origin: design-system defect register v5.1
- added: 2026-10-30

### L-014 · collaterals · one truth across panels
- check: Every AI summary on a recorded screen agrees with the record it summarises and with every other AI panel (status, sample round, amounts).
- why: Pentland's summary said the fit sample was late while the record showed fit approved and SMS in transit; two AI panels gave £14.52 and £27.17 for the same swap.
- origin: collateral skill Phase 0.5
- added: 2026-10-30

### L-015 · collaterals · domain sense
- check: Would the client's own experts accept every suggestion shown? A suggestion that fails a domain sense-check is fixed in the data or dropped.
- why: A 2-layer fabric was shown "meeting the same brief" as a 3-layer GORE-TEX Pro shell.
- origin: collateral skill Phase 0.5
- added: 2026-10-30

### L-016 · collaterals · told vs shown
- check: Narration claims only what the screen can do ("copies the draft", not "sends it"), and the voice never talks about a screen that has not loaded.
- why: Pentland's narration ran 2–4 s ahead of the screen and claimed actions with no button.
- origin: collateral skill (lint and check.py notes)
- added: 2026-10-30

### L-017 · build · records the person made
- check: Fixes and re-seeding never delete records the person created while verifying the app.
- why: Owner decision in the orchestrator.
- origin: poc-orchestrator Stage 4
- added: 2026-10-30

### L-018 · all · side stripes
- check: No coloured left-side border (side stripe) on cards, rows, bubbles or fields. Reject a `TB` status-stripe variant in the active style set; status is shown with the tag.
- why: Reviewers sent side-striped cards back as decoration; the tag already carries the status.
- origin: owner gate feedback
- added: 2026-10-30
