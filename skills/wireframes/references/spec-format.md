# The wireframe spec — format and block library

One JSON file per run: `<workspace>/02b-wireframes/<slug>.wireframe.json`. `scripts/render.py` draws it. Every field
below is read by the renderer or written to the manifest; nothing else is.

```json
{
  "client": "Acme Retail", "use_case": "Inventory IQ", "slug": "acme-retail-inventory-iq",
  "app": { "name": "Inventory IQ", "logo": "ACME", "nav": ["Overview", "Sites", "Reorders"], "phone_tabs": ["Tasks", "Scan"],
           "search_label": "Search stores, SKUs, orders", "agent": "Copilot" },
  "pages": [ { …page… } ]
}
```

## Page

| Field | Meaning |
|---|---|
| `id` | the scoping document's page ID (`PG-03`). A second frame of the same page (a state, an open panel, an overlay) adds a letter: `PG-03b` |
| `title` | the page name from scoping §11 (and what the frame shows, for a second frame) |
| `brd_ref` | the scoping section or route (`§11.3`, `/planner`) |
| `persona` | the page's primary persona (scoping §11 "Personas") |
| `width` | the persona's device width: 1280 desktop, 375 phone (scoping §7 / 0.4 of the design system) |
| `nav_active` | the nav item lit for this page |
| `shell` | omit for the left-nav shell; `"topbar"` for a top-bar app (logo, tabs, filters, avatar); a phone width gets the phone shell |
| `topbar` | for `topbar` and map pages: `{"tabs": [...], "active": 0, "right": ["All states", "DAILY BRIEF"]}` (an UPPER-CASE item draws as a button with an icon) |
| `rows` | the page body: a list of rows, each a list of blocks on a 12-column grid (`span` per block, `h` in px) |
| `layout` | `"map"` for a full-screen map page (see below); then `map`, `left`, `right` replace `rows` |
| `overlays` | a `drawer` or `modal` drawn over the page (one per frame) |

## Blocks — every block has `type`, `span`, `h`; every component block has `id` (scoping block ID) and `component`

Optional on any component block: `cmp` (the scoping §23 CMP ID it belongs to), `states` (from: loading, empty,
no-results, error, no-access, offline, thinking, …), `variants` (the forms the pages need, e.g. "compact",
"horizontal"; at most three per component across all pages), `note` (one line for the design system).

`app.search_label` is the top bar's search placeholder (the document's own words); `app.agent` is the agent's short
name on its button and badges (default "AI"). Blocks without a `component` (`header`, `filters`, `tabs`, `label` and
the single controls) are page parts, not components: they go to the manifest's `page_parts`, never to `components`.

**The manifest** (`wireframe-manifest.json`), per component: `pages`, `blocks`, `cmp`, `variants` (only what the spec
lists), `features` (what the drawing shows it must do: `select`, `bulk`, `status_col`, `card`, `cluster`, `popup`,
`kind:<x>`), `states`, `notes`, and for a map `modes` plus the `data_contract` per mode and any `behaviour` lines.

| type | Draws | Fields |
|---|---|---|
| **`slot`** | **an empty dashed region naming the component** — the default for anything generic | `component`, `count` (×N), `title`, `note`, `variants`, `states` |
| `header` | page title, subtitle, breadcrumb, actions (last = primary) | `title`, `subtitle`, `breadcrumb`, `actions` |
| `filters` | search box + filter chips with their values | `chips`, `search`, `search_label` |
| `tabs` | tab row | `items`, `active` |
| `label` | a small section label | `text` |
| `kpi` | metric tile with a trend line | `label`, `value`, `delta` |
| `stat` | big-number tile (label, info, value, unit, delta pill) | `label`, `value`, `unit`, `warn`, `delta` |
| `insight` | floating insight card (map pages): label, value, "/ total", progress, one line, ↗ | `label`, `value`, `of`, `sub`, `progress`, `warn`, `ai`, `badge`, `active` |
| `table` | table with header, rows, status pills | `title`, `columns`, `status_col`, `statuses`, `action_col`, `select`, `bulk` |
| `list` | one-to-two-line list with status pills | `title`, `items: [{title, meta, status}]` |
| `card` | text card with an optional button | `title`, `lines`, `action` |
| `chart` | chart placeholder | `title`, `kind` (line, bar, donut), `caption` |
| `form` | labelled fields and submit | `title`, `fields: [{label, kind (text, select, number, textarea, photo), value}]`, `submit`, `submit_full` |
| `select`, `stepper`, `slider`, `text`, `button` | single form controls and text inside panels | `label`, `value`, `kind`, `filled` / `text`, `bold`, `size` / `full`, `disabled` |
| `tiles` | a row of 2–4 count tiles at the top of a panel | `items: [[label, value], …]`, `active` |
| `move` | a from → to card with value and Reject / Approve | `from`, `to`, `miles`, `value`, `value_label`, `detail`, `kind` |
| `timeline` | a short event list | `title`, `items` |

**Detail vs slot.** Draw in detail (with real wording) only what makes this app this app: the hero of each page, the
work queue, the record's main card, the map, the agent's answer. Everything generic — a KPI row, a standard chart, a
settings form, a secondary table — is a `slot` with its component name, count, the variants it needs and its states.
The design system designs the component; the wireframe only fixes where it goes and what it must cover.

## Overlays

| type | Fields |
|---|---|
| `drawer` | `id`, `component`, `title`, `width`, `messages: [{from: user|agent, text, chips, card}]`, `input`, `states` — the agent drawer is always a drawer, never a card on the page |
| `modal` | `id`, `component`, `title`, `body`, `actions` (last = primary), `width`, `height` |

## Map pages (`"layout": "map"`) — read `map-component.md` first

```json
{ "id": "PG-03", "layout": "map", "width": 1280, "height": 800, "topbar": {…},
  "map":   { "type": "map", "id": "B-31", "component": "network-map", "mode": "rings | dots | arcs | radius",
             "legend": [["dot0", "Critical"], ["dot1", "Watch"], ["dot2", "Healthy"], ["ai", "Assumption"]],
             "data": { "object": "…", "lat": "…", "lng": "…", "tone_by": "…", "card_fields": [ … ] },
             "behaviour": [ "…only lines that differ from map-component.md…" ],
             "card": { "title": "…", "status": "…", "lines": [ … ] }, "labels": [ "…" ], "states": [ … ] },
  "left":  { "width": 256, "blocks": [ scope select, label, insight cards… ] }  // or "card": true for one form panel
  "right": { "id": "B-36", "component": "detail-panel", "title": "…", "width": 380, "blocks": [ … ] } }
```

Legend marks: `dot0` (filled, most urgent), `dot1` (ring), `dot2` (grey dot), `dash` (dashed route), `ai`
(an AI estimate). No "demo" or "synthetic" mark. Mode extras: `rings` → `counts`; `dots` → `n`, `share0`, `share1`, `labels`;
`arcs` → `routes`, `hubs`, `counts`; `radius` → `radius_label`, `n`.

A map is never a block in a row: the renderer stops with an error if one is.

## What the renderer checks before drawing (it stops with one line per problem)

Duplicate page ids; a page without `id`, `title` or `persona`; a row wider than 12 columns; an unknown block type; a
component block without `component`; a map in a row; a map page without `mode`, `data` or `legend`.
