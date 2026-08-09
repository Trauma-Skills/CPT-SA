# The check-in task

An optional scheduled task that opens a brief conversation in the course folder on a
recurring schedule — by default once a day — so the course reaches out at the right
moments instead of the user having to remember them. It also gives the project a
standing front door: without it, opening the project means a blank input box, but with
it the most recent check-in is always sitting in the session list, already oriented,
with the next step as a button. It is a knock on the door, never a hand on the
shoulder: every run is an invitation, and the user owes it nothing.

**Reminders only — never auto-run a session.** Trauma work needs the user present and
willing. A check-in run may greet, orient, and offer; session content begins only when
the user answers and asks for it.

## When to offer it

Offer the check-in **once**, at the end of first-time setup, right after the first-run
welcome — one short paragraph, not a second ceremony. **The offer is answerable in one
tap, never only by composing a reply.** Where the surface has a question tool
(AskUserQuestion or similar), the offer *is* that question: a sentence of lead-in,
then a yes/no choice — e.g. *"Set up a daily check-in?"* with options like *"Yes —
mornings"* / *"Yes — another time"* / *"No thanks"* — so taking or declining it costs
one tap, and a "yes" that needs a time asks for the time as its follow-up. Where
there is no question tool but the widget tool exists, render the choice as buttons
(the manual's button pattern); plain prose is the last resort. A "No thanks" is the
recorded decline. If the user heads straight into
session 1 without engaging with the offer, let it go; don't chase it.

For a folder set up before this existed — `state.json` has no `checkIn` field — offer
it once at orientation, under the same conditions that govern the update check: you're
at orientation, no session has begun, nothing in the conversation suggests distress,
and they're not mid-homework on an account.

Only make the offer if the surface can actually schedule: a `schedule` skill or a
scheduled-task tool (`create_scheduled_task` or similar) must be present. **If it
isn't, skip the offer silently** — never send the user off to install something, and
never describe a feature they can't have.

If they decline, record it (below) and let the conversation move on. **The offer
happens once, ever.** After a decline — or after they let the setup offer pass, or
later removed the task — never raise it again yourself: not at session close, not on
a held-gate message, not in a widget's buttons, not as "grounding or a check-in", and
never as standing text in `progress.md` offering it "any time". When `state.json`
records a declined check-in, the word "check-in" simply doesn't appear in anything
you render. The door stays open from their side only: they can ask at any time ("set
up check-ins", "remind me daily") and that always works, declined or not.

## Creating the task

Confirm two things first, in one short exchange:

- **Frequency** — default **daily**. Weekly or every-other-day is fine if they prefer
  a lighter touch.
- **Time of day** — suggest **morning** (e.g. 09:00). Homework unlocks run "next
  morning", and account work must never be nudged near bedtime, so morning is the
  honest default. Any time they choose is fine — the run rules below adapt to it.

Then create the task:

- **Name it something neutral** — `daily-check-in`, never anything with "CPT-SA",
  "trauma" or "therapy" in it. Task lists can appear on shared screens; the task's
  name must not disclose what the course is.
- **The prompt carries no clinical content and nothing personal — ever.** It is only
  a pointer to the folder and the skill. Template, filling in the absolute path of
  the course folder:

  > This is a scheduled check-in for the self-guided course in `<absolute path to
  > the course folder>`. Work in that folder. Its `CLAUDE.md` is the course's
  > operating manual — follow its boot-up procedure, then follow "Running a
  > check-in" in `skill/check-in.md`. This run is an invitation, not a session: one
  > short message, at most one offered action, and no session content unless the
  > user replies asking for it.

- **Record it in `state.json`**: `"checkIn": {"taskId": "<the task's id>",
  "declined": null}` — or, on a decline, `{"taskId": null, "declined": true}`.
  A missing `checkIn` field means never-offered. `declined: true` means the offer is
  never repeated on any surface (see above); it never blocks the user asking for one
  themselves.

## Running a check-in

A run boots like any other conversation — real clock, read the state files, resolve
the single next step — then sends **one short, warm message** with three parts: a
greeting with where things stand in a sentence, **the run's one care question**
(below), and **at most one** next action, as a button (see the button pattern in
CLAUDE.md). Then it stops and waits. A message that orients but never asks the care
question is an incomplete run — the question is the check-in.

What to lead with, by state:

| State | The message |
|---|---|
| Session marked in progress (interrupted thread) | "We were partway through session N — happy to pick it up whenever you like." + resume button |
| Homework complete, next session unlocked | Invite them to begin it + begin button |
| Homework open and not complete | Offer to do it together now + button |
| Everything gated, reading practice running (sessions 4–8) | The supportive daily check-in: "How are you doing today? Did you get a chance to read your account?" |
| Everything gated, nothing to practice | One line with when the next thing opens; offer grounding if they'd like company meanwhile |
| Course complete | Congratulate briefly; offer to turn the check-in off |

**Every run also asks one care question** — woven into the greeting, not appended as
a form. Vary it naturally: sleep is the flagship ("how have you been sleeping?"),
otherwise mood, appetite, how they've been holding up since last time. One question
per run, never a checklist. It matters because trauma work disrupts exactly these
things between sessions, and the check-in is the only part of the course that's
present in the gaps.

Listen to the answer for red flags: several bad nights running, numbness or feeling
"not here", drinking or using more, hopeless language, or any mention of self-harm.
Self-harm or acute distress → the safety protocol in CLAUDE.md, immediately. The
quieter flags (sleep eroding, rising dissociation) → respond in the moment — gentle
pacing suggestions, no account-reading before bed, an offered grounding exercise —
and append a one-line, dated "Between sessions:" note to the most recent
`notes/session-NN.md`, so the next session boots knowing it. Append only; never
rewrite what's there. An ordinary "slept fine, doing okay" needs no note at all —
answers are not data collection.

If the surface can title sessions (a set-session-title tool or similar), give the run
a short neutral title — "Morning check-in", never the session topic or anything
clinical — so the session list stays useful without disclosing what the course is.

Hard rules, every run:

- **One short message is the entire run.** Nothing else is user-visible output: no
  "notes on this run", no diagnostics, no state summaries, no continuity commentary,
  no mention of files read or skills loaded, and no clinical content of any kind —
  nothing from `notes/`, nothing from `pcl-scores.csv`, nothing the user disclosed in
  a session. If a run surfaces something worth keeping, it goes in the dated "Between
  sessions:" line in `notes/` per above — never on screen.
- **The care question rides in every run.** Whatever the state — everything gated,
  nothing open, course barely begun — the message still asks its one care question.
  Orientation without it is not a check-in.
- **Never begin session content in the run itself.** If the user replies and asks to
  start, the conversation becomes an ordinary course thread — follow CLAUDE.md from
  there, gates and all. If they reply with anything else — how they're doing,
  something on their mind, a topic unrelated to the course — follow them there; a
  check-in that got a person talking has done its job, and it never steers back.
- **No guilt, ever.** Never count missed check-ins, never "you still haven't", never
  compare this week to last. A check-in reports what's open, not what's owed.
- **Never nudge account writing or account reading late in the evening.** If the run
  fires at night (their chosen time), offer presence or grounding instead of the
  account during sessions 4–8.
- **Never mention PCL-S scores or trends.** Same rule as everywhere else, and a
  check-in is the easiest place to slip.
- **Never encourage starting before a gate opens.**
- **Safety first, as always.** If the most recent session notes record elevated
  distress or the safety protocol firing, drop every nudge: lead gently, offer
  grounding, surface `crisis-resources.md` if warranted. If a reply raises any safety
  concern, the safety protocol in CLAUDE.md overrides everything here.
- **After a long silence** — nothing in the folder touched for two weeks or more —
  acknowledge the gap once, without weight, and offer to pause or stop the check-ins
  as readily as to continue. Silence may be a choice; make honouring it easy.
- **If the folder can't be read** — no `progress.md`, no `state.json`, path gone —
  don't guess and don't nudge. Say the check-in couldn't find its course and offer to
  remove the task.

## Changing and removing it

The user can change the frequency or time, pause the task, or delete it at any time
by asking — use the surface's update/delete tools and refresh `state.json` to match.

Raise it yourself, briefly, at exactly these moments:

- **Course completion** — when session 16 closes, offer to remove it as part of the
  closing conversation.
- **Reset** — while confirming a reset, ask in the same exchange whether the check-in
  should stay or go. If it stays, carry the `checkIn` field over into the rewritten
  `state.json` so the fresh course still knows about it; if it goes, delete the task.
- **Pausing the course** — if they say they're stepping away for a while, offer to
  pause it, and say plainly that asking again is all it takes to resume.
