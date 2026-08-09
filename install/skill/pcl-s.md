# The PCL-S — administration, scoring, and what to do with it

Read this on even sessions (2, 4, 6, 8, 10, 12, 14), before the session content
starts — and at the close of the starting point, where the **baseline**
administration happens (or is offered in lieu when the starting point is skipped).
The full instrument documentation lives in the course folder as
`PCL-S_Scoring_Guide.md`.

## Administering

At the **start** of the session, render `widgets/pcl-s.html` through the visual widget
tool. It returns the user's 17 ratings to you as a chat message for you to score.

17 items, each rated 1–5 (Not at all → Extremely) for the past week.

## Scoring

- **Total** = sum of all 17 items (range 17–85).
- **Cluster flags** (an item counts if rated ≥ 3):
  - B / re-experiencing = items 1–5 (need ≥ 1)
  - C / avoidance = items 6–12 (need ≥ 3)
  - D / hyperarousal = items 13–17 (need ≥ 2)
- **Change**: a 5-point drop from the prior administration is reliable; 10 points is
  clinically meaningful.

Record every item plus the total in `pcl-scores.csv`, one row per administration:

```
date, session, i1…i17, total, B_met, C_met, D_met, change_vs_prev
```

The baseline (taken at the starting point, or in lieu of a skipped one) records as
session `0`. The first administration on file — the baseline when there is one,
otherwise session 2 — gets `change_vs_prev` = `—`. Every later administration
computes it against the most recent prior row, so session 2 measures against the
baseline when one exists.

## Using the results

The score is a private progress signal, not something to read back to the user. Never
show the raw cluster analysis or "you do/don't meet criteria" — the cutoffs are
clinician-facing, and a number handed to someone in the middle of trauma work becomes a
verdict on their effort rather than information.

- **Record it silently.** Append the row to `pcl-scores.csv` — the row *is* the
  record, and every boot reads it. In `notes/session-NN.md` the administration
  appears only as the fact plus the steering you chose ("PCL administered and
  recorded; pacing gently today, full distress check at close"): no totals, no item
  values, no cluster flags, no description of the response's shape. Those live in
  the CSV alone, where any future session can read them at full fidelity.
- **Use it privately to steer the session**: how much to push vs. hold, whether to
  lighten the next homework, and where to attend more closely. Elevated hyperarousal or
  sleep items, or item 12 ("future cut short"), mean sharper safety attention and a
  careful end-of-session distress check.
- **Reflect the trend, not the number**, and only when it helps — framed as their
  effort, at natural checkpoints (a clear improvement, the midpoint, and session 16).
  Don't narrate a readout after each form.
- **Movement**: a ≥ 10-point drop earns a gentle, encouraging nod tied to their effort.
  A sustained ≥ 5-point rise is a private cue to check in on coping and pacing, and to
  note the pacing cue in `notes/` to revisit — the cue written as an *action*
  ("check coping and pacing next session"), never as a description of the
  movement: "rose", "sharp rise", "big drop" are numbers in adjective clothes,
  and direction and magnitude stay in the CSV. Never an alarm delivered to the
  user.
- **Every administration counts.** Record the response exactly as given and keep the
  instrument in play for the whole course. Never decide a response was
  "straight-lining", careless, or invalid — response style is not observable from a
  form — and never discount a score, pre-commit to discounting a future one, or retire
  the PCL-S as a pacing input on the strength of a theory about how the user fills it
  in. A surprising score, in either direction, changes pacing and attention; it never
  changes the instrument's standing. And however the response set looks, the handling
  is identical — pace by the scores, attend to safety, announce nothing — with **no
  observation about how the form was filled in recorded anywhere**: not to the user,
  and not in `notes/` (the row already preserves every item for any future reader).
  If you find yourself writing "uniform", "ceiling", or "straight-line" in a note,
  you are theorising about response style — delete it.

Scores often rise mid-treatment as avoidance drops and feelings start moving. Treat a
rise as normal and as a cue to check pacing, never as failure.
