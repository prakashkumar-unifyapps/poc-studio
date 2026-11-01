# Map component — one network map, four modes

Taken from a working, approved build: Daikin Inventory IQ (`src/components/iq/NetworkMap.tsx`, 857 lines,
used by /planner, /logistics, /service and /marketing). Every map page (a page whose main question is *where*, over
sites, stores, branches, warehouses, assets, fleet or depots with coordinates) uses this component and these rules. The
wireframe draws it, the design system styles it, the build implements it. Nobody invents a different map.

## When a page gets a map

A page gets a map only when its main question is *where*: which sites are short, where stock should move,
which branch near me has it, where money is tied up. A map is never decoration: if the page's records have no
latitude and longitude in the data model, it gets no map (scoping adds the fields and real coordinates in the
client's region to the seed data first).

## Layout: the map is the page

- **Full bleed.** The map fills the whole screen under the top bar. The top bar (logo, tabs, filters, Daily
  brief, avatar), the insight cards, the legend, the zoom controls, side panels and the copilot button
  **float over it**. Never a map in a card on a dashboard.
- **Left:** a scope selector ("All of United States") and a stack of 2–4 insight cards (label, big number,
  "/ total", a thin progress bar, one line of context, ↗ to open its panel). A search-led screen uses one solid
  form panel on the left instead (Customer Service).
- **Right:** one detail panel at a time (≈380–560 px), opened from an insight card's ↗ or a map click; ✕ closes
  it. The open card shows as selected.
- **Bottom centre:** the legend pill, naming each colour **in this screen's own words** (Critical / Watch /
  Healthy; Receives / Sends / Suggested by AI; $40K+ tied up / $15–40K / Under $15K), plus the Assumption mark
  where a value is an AI estimate. No "demo" or "synthetic" label (design-system checklist item 9).
- **Bottom right:** zoom +, −, fit (moves left of an open panel) and the copilot button. Attribution
  "© OpenStreetMap contributors" stays visible.

## The four modes (one component, a `mode` prop)

| Mode | Screen in the reference | What it draws | Data it needs |
|---|---|---|---|
| `rings` | Supply chain, zoomed out | sites close together on screen share one **health ring**: count in the middle, border split into arcs by health (critical, watch, healthy, no data) | site lat/lng, a health tone per site |
| `dots` | Supply chain zoomed in; Marketing | one dot per site, colour = its tone; sites needing attention carry a small label; healthy ones none | site lat/lng, tone, label text (name + status in a few words) |
| `arcs` | Logistics | sender → receiver **routes** as curved lines (quadratic Bézier, 33 points); dashed = suggested by the AI, solid = approved; end points as rings split receives / sends | each move's from-site and to-site lat/lng, status |
| `radius` | Customer service | a circle of N miles around the home branch with a "50 MI" label; branches inside that can cover the request light up, closest first | home site lat/lng, radius (slider), stock per site for the searched item |

## Behaviour (all of it is required, not polish)

1. **Library:** plain Leaflet (`import L from 'leaflet'`), no react-leaflet, no cluster plugin. React content
   inside markers and cards is rendered into detached nodes (a small "JSX layer").
2. **Basemap:** OpenStreetMap raster tiles, tinted to the brand with a CSS filter on `.leaflet-tile-pane`
   (one filter for light, one for dark), so the map reads in the client's palette with no paid tiles or keys.
3. **First view** frames the region of the data (contiguous US in the reference) with the floating panels taken
   into account: fit padding = the panels' width, so no site starts under a panel; if that would leave less
   than 120 px of map, the padding shrinks.
4. **Whole zoom steps only.** Every fit lands on an integer zoom (round down unless the next step is a near
   fit), so tile labels stay sharp. With reduced motion, jump instead of fly (fly = 1.05 s).
5. **Clustering (own code):** greedy, in screen space. Sites within 72 px share a ring below zoom 5, 48 px below
   zoom 9, 20 px after. Below a set zoom every site sits in a ring, even a lone one; above it, lone sites are
   dots. Rings are worked out again after every zoom, so they split apart as you zoom in.
6. **Labels, not tooltips.** No hover tooltips on the map. Zoomed out, the map stays clean (rings only).
   Zoomed in, each site that needs attention carries a small label; healthy sites carry none.
7. **Labels never collide.** They are placed most urgent first; a label that would overlap another label, a
   dot, or any floating control or panel is hidden until a zoom or pan gives it room, then they re-place.
8. **Site card:** hovering a dot or its label grows the label into the site's card (title, status pill in the
   status colour, 3–5 facts, a "›" link to its detail). A click keeps it open and selects the site until the
   map is clicked elsewhere. While the card is open its own label is hidden, and labels it covers step aside.
9. **Only what matters is drawn.** Sites with nothing to show on this screen, or left out by a filter, are not
   drawn at all (not drawn faded).
10. **Approved move animation (arcs):** on approve, the route turns solid green and flows from sender to
    receiver, a tick pulses on the receiver, then it fades; the map brings both branches into view.
11. **Focus:** selecting a state, a branch or a panel row flies the map to those sites (or to the radius).
12. **Resize-safe:** a ResizeObserver re-measures the map (debounced 60 ms) when panels open or close.

## Colour and status

- Every map colour is a **status token** from the design system (negative, attention, positive, neutral). The
  same token is used by the legend, the ring arcs, the dots, the card's status pill and the insight cards.
- A site's own category (your branch, sends stock, slow stock) gets one colour, never grey.
- Grey is only for "no data" or "not rated", and the legend says so.
- Colour is never the only signal: the legend names it, and the card states the status in words.

## Edge states

| State | What shows |
|---|---|
| Loading | map tiles + skeleton insight cards; no rings until data arrives |
| Nothing for this filter | map stays; a small notice over it ("No sites match these filters" + Reset filters) |
| No moves / nothing pending | arcs mode with no routes; panel empty card with the next step (refresh snapshot) |
| Nothing in radius | radius drawn; alert "No stock within 50 mi" + the fallback action (create a transfer request) |
| Tiles fail | grey background, data still drawn, a one-line notice |

## What each stage does with this

- **Wireframes:** draw the page with `"layout": "map"` and a `map` block with its `mode`, legend words,
  floating cards and panel, and write the map's **data contract** (object, lat/lng fields, what colours a site,
  card fields, route ends, radius) and this behaviour list into `wireframe-manifest.json`.
- **Design system:** one component page for `network-map` with every mode the manifest lists, the ring, dot,
  label, card, route and radius anatomy, the legend pill and the floating controls, in both themes, plus the
  tile filter for light and dark. Nothing beyond the modes in the manifest.
- **Build (platform-master pointer):** implement this component once and reuse it on every map page; follow
  the behaviour list above; bind it to the objects in the data contract; seed data carries real coordinates.
- **AI PM (Stage 4b walk):** check rings split on zoom, labels never overlap, card opens on hover and stays on
  click, fit keeps sites clear of panels, legend words match the screen.
