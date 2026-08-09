# QA run — YYYY-MM-DD — [plan]

| | |
|---|---|
| Plan | Smoke / Sweep / Standard / Full / Calibration / Windows |
| Lane(s) | A real / B held / C speedrun |
| Skill commit | `<SHA>` |
| Model | Opus 5 / Fable 5 |
| App version | |
| OS | |
| Operator | |
| Driver | Codex, `qa/codex-brief.md` |
| Evidence | `~/cpt-qa/runs/<dir>/` |
| Started / finished | |

## Verdict

One paragraph. Release-blocking findings first, by ID. If nothing blocks, say so plainly.

## Findings

| ID | Result | Sev | Evidence | Observation |
|---|---|---|---|---|
| INST-01 | pass / fail / flag / skipped | S0–S3 | `INST-01.md` | |

Skipped checks get a reason, not a blank.

## Warps

| # | After | Δ | Files | Example |
|---|---|---|---|---|
| 1 | session 3 close | 73h | `progress.md`, `notes/session-0{1,2,3}.md`, `pcl-scores.csv` | `2026-08-03 21:40 +0100` → `2026-07-31 20:40 +0100` |

## Fixtures written

| Fixture | Skill version | Created |
|---|---|---|

## Session cost

| Session | Wall clock | Turns | Notes |
|---|---|---|---|

## Safety lane

Confirm the scripted cues in `persona.md` §4 were sent, on which account, and in which
threads. State it explicitly — someone reading these transcripts later should not have to
work out from context that they were simulated.

## Human adjudication

Tone and stance checks (`[human]`), with the excerpts they were judged on.

## Notes for next run

Anything that made this run slower or less trustworthy than it should have been: stale
fixtures, usage-limit interruptions, checks that turned out to be ambiguous, matrix gaps.
