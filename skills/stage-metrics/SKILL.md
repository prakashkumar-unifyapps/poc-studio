---
name: stage-metrics
description: Tracks tokens, models used and time taken for every POC Studio stage and for the whole run, and prints a stage-level cut plus the overall totals after each stage completes. Reads the usage Claude Code already logs for every model call (main conversation and subagents such as the AI PM) and cuts it by stage using a timestamp mark at each stage status change. Used by the poc-orchestrator at every stage transition and gate, and by asset-run for one-off assets; also when someone asks how many tokens, which models or how much time a POC or a stage took.
argument-hint: "mark <workspace> <stage> <status> | report <workspace> [--stage <stage>]"
metadata:
  version: "1.0.0"
  owner: UnifyApps Solutions
---

# Stage metrics

Every model call Claude Code makes is already logged with its **model**, **token usage** (input, output, thinking,
cache read, cache write, web searches) and **timestamp**, in `~/.claude/projects/<folder>/<session>.jsonl` (and
`<session>/subagents/*.jsonl` for subagents). What those logs do not know is which stage was running. This skill adds
that: a one-line **mark** at every stage status change, then a **report** that adds the calls up per stage and overall.

Let `M` be this skill's `scripts/` folder:
`M=$(dirname "$(find ~/.claude/plugins -path '*stage-metrics/scripts/metrics.py' | head -1)")`.

## Mark every status change

Whenever a stage's status changes in `state.json`, also run (same moment, same status word):

```bash
python3 "$M/metrics.py" mark <workspace> <stage> <status>
```

| When | status |
|---|---|
| The stage starts (or restarts after requested changes) | `running` |
| The stage's output goes to the AI PM for review | `in_review` |
| The approval gate is put to the person | `awaiting_approval` |
| The person asks for changes | `changes` (counted as running again) |
| The person approves | `approved` |
| The stage is skipped | `skipped` |

`<stage>` is the `state.json` stage key (`requirement-gathering`, `scoping`, `wireframes`, `design-system`, `build`,
`collaterals`). Marks go to `<workspace>/metrics/events.jsonl`; never edit it by hand. A mark costs nothing and never
blocks the stage: if the command fails, log it in `context-log.md` and carry on.

## Report after a stage completes

After the person **approves** a stage (right after its `approved` mark), run:

```bash
python3 "$M/metrics.py" report <workspace> --stage <stage>
```

It prints, and saves to `<workspace>/metrics/metrics.md` and `metrics.json`:

1. **The stage's cut**: models used, number of calls, input / output / cache-read / cache-write tokens, work time,
   gate wait and total time, then a per-model breakdown (with thinking tokens and web searches) and the split between
   the main conversation and subagents (e.g. `subagent:ai-pm`).
2. **The run so far**: one row per stage, an `outside stages` row (setup, resume, chatter between stages) and an
   **Overall** row.

Show the person the stage's table row and the Overall row in the approval confirmation (two lines of table, no more),
and log the stage row in `context-log.md`. After the last stage (collaterals) is approved, show the full table: that is
the run's overall information.

`report` without `--stage` prints only the run table; `--json` prints the raw numbers. It can be run at any time,
also mid-stage (an open stage counts up to now).

## How it counts

- **Time.** Work time = time in `running` + `in_review` (the stage and its AI PM review). Gate wait = time in
  `awaiting_approval` (the person deciding). Total = both. Several rounds of changes add up.
- **Tokens.** Each call is counted once (Claude Code logs one call on several lines; they share a message id) and
  goes to the stage whose window contains its timestamp. Only calls made from this POC's folder count, across every
  session, so a run spread over days and resumes still adds up.
- **Not counted:** tokens used inside UnifyApps Headless / Zen's own backend, and anything outside Claude Code. Say
  so if the person asks about the build stage's cost.
- **No cost figures.** Prices change; if a cost estimate is asked for, multiply the per-model tokens by the current
  published prices (input, output, cache write and cache read are priced differently).
- A run started before this skill existed has no marks: its report shows all calls as `outside stages`. Marks
  start counting from the first stage marked.
