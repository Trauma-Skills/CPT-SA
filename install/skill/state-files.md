# State file formats

The folder is the course's memory. These three files are what any future thread reads
to know where things stand, so keeping them accurate matters more than keeping them
tidy.

## `progress.md`

A **Current state** block that always shows:

- a **Starting point** line, one of: `not started` · `in progress (started <ts>)` ·
  `done <ts>` · `skipped <ts>` · `done — kept from a previous course (<date>)`,
  followed by its baseline status: `baseline recorded` / `baseline declined` /
  `baseline pending` / `baseline offered <ts>` — that last one means the one offer
  was made but not answered: it is spent as an offer (no orientation raises it
  again), flips to `recorded` if the user takes the check-in before session 2
  begins, and to `declined` on an explicit no. If a post-session-1 re-offer was declined, append
  `re-offered <date>, declined` — that records the offer as spent. A `progress.md`
  written before v1.2 has no such line: treat its absence as *not started* — which,
  for a course already past session 2's start, means the offer window has simply
  passed — and add the line at your next write of the file;
- the last completed session with its real timestamp;
- **if a session is underway, a "Session N: in progress" line with its start
  timestamp** — set the moment the session begins, cleared at close;
- the current homework with its mode, unlock time, status, and completion time;
- the next session number and its computed unlock time;
- a single **"▶ Next step"** line in plain language.

Below that, a history table with one row per session.

Refresh this at session start, at every session close, and whenever homework status
changes, using real timestamps from the system clock (see "boot up" in CLAUDE.md for the
macOS and Windows commands). Never write a guessed or remembered time. Any name or
gendered pronoun written here obeys the manual's identity rule: traceable to the
user's own words in this course, or absent — summaries default to "they".

The in-progress line is what makes a session survive a dead thread — without it, a new
conversation has no way to tell "session 5 finished" from "session 5 stopped halfway".

## `pcl-scores.csv`

One row per administration:

```
date,session,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,total,B_met,C_met,D_met,change_vs_prev
```

`session` is `0` for the baseline taken at (or in lieu of) the starting point, then
the even session numbers. Facilitator-facing. See `pcl-s.md` for what goes in each
column and how to use it.

## `notes/session-NN.md`

Your private continuity notes — `session-00.md` for the starting point, then one per
numbered session. Created at session start and appended to as the session
runs — beats covered, rules and beliefs identified, the user's key answers, anything
safety-relevant — then finalized at close with themes, emotional response, and anything
to revisit next time.

Read at the next session's boot, and, mid-session, the resume point for an interrupted
or parallel thread. These are working notes to keep the thread of the work, not a
clinical record.

**Keep them short.** A note is a handover to the next session, not a record of this
one: the beats covered, the user's own words on what matters, what's open, what to
watch. Around 400 words does it; 600 is a full note, and past that you are almost
certainly writing a transcript with commentary, which is worse
than a short note, because the next session has to mine it for the four things it
actually needed. The transcript already exists and holds everything you'd be
duplicating. So: no blow-by-blow of the conversation, no account of your own
facilitation choices and the reasoning behind them, no restating the rules you
followed. Write what the next session must know, and stop. A sparse session makes
a **shorter** note, not a longer one: when nearly every answer was the same few
words, the note says so in a line, names the exceptions, and is done — a
beat-by-beat log of sameness is a transcript of nothing, and the next session
needs one sentence of it. **Say each thing once.** A fact lives in one place in
the note: the close names only what the beat entries don't already hold, and
points ("declines: see beats 4–6") rather than restates; a carried-in item that
didn't change this session appears once, in the carry-forward, not re-told in
the beats and again at the close. And a clause whose job is to show a rule was
followed — "not re-asked", "no interpretation offered", "received without
pressure" — is the transcript's business, not the note's: write what happened,
not what correctly didn't. The exception is a disambiguation the next session
genuinely needs ("the bracketed stop line is from the writing, not a live
request") — said once. While a session runs, the live note may hold more —
per-item entries, a Carried-in section at the top: that is resumability
bookkeeping, and it is temporary. **The file that survives the close has this
shape:**

```
# Session NN — <title>
Started / Closed / Status
Boot: gates and continuity, a line or two
Beats: ONE line per beat — what was covered, and the answer in their
       words or its quality
Close: the session's shape, emotional response included, in a line or
       two; then what's open, as bullets — every standing item lives
       exactly here
```

In a finalized note: no beat has more than one line, and no sub-question has a
line of its own — a list-shaped beat of five questions and five sparse answers
is one line: *"Beat 7 (processing) — all five questions asked, every answer
sparse ('I don't know' / 'I'm not sure'); no rule surfaced."* An answer that
carried content sits inside its beat's line; a
quality that holds across beats ("every answer sparse") appears once, in the
close, not per beat; no count appears twice; the close's shape line is a
quality, and the sanctioned "all but three" form *is* that quality, not a
tally — but its exceptions are **pointed at** ("the two that weren't: beats 1
and 5"), never re-quoted: an exception is spelled out in the close only when
no beat line already holds it, because a close that re-quotes a beat line is
the double-telling this shape exists to prevent; no Carried-in
section remains — its items live in the close's open bullets, each exactly
once, marked updated or unchanged; and beat lines carry substance, never
packaging — "assertiveness taught, no right named untrue", not "handout
surfaced (card + link)", which is the transcript's to remember. A finished
note reads like a handover, not like the log that produced it. And earlier
notes in the folder are **records, not exemplars**: a course carried through
an upgrade may hold long, itemized notes written under older versions of this
manual, and boot reads them for continuity — but their register governs
nothing. Every note finalized from now on matches the shape above, whatever
the folder's history looks like.

**Think freely in them.** Hypotheses about what's going on, what to try next, what to
handle carefully — that thinking is exactly what makes the next session feel
continuous, and none of it is volunteered to the user. A few lines of it, held as
hypothesis, is the useful amount. But future sessions trust these
notes blindly, which is why they obey four rules:

- **Record only what happened.** Every count, date, quote, and claim must be checkable
  against the conversation or the files — verify before writing ("five readings" means
  five you can point to; "all twelve rules" means you counted twelve in the artifact
  just now, not that it feels complete). Before finalizing, re-check each count and
  each "they did X" claim against what actually occurred in this thread; a number or
  event you can't point to doesn't get written. For counts *about the conversation*,
  pointing means enumerating: name the instances ("four answers weren't 'I don't
  know': …") or write a quality ("nearly every question") — a session-wide tally you
  haven't enumerated ("17 across the session") is a memory wearing a number's
  clothes. Mechanically: a digit counting the conversation appears in the note only
  with its instances named beside it — no enumeration, no number. And past a handful
  of instances, stop counting altogether: a long uniform run is exactly where a
  tally goes wrong by one and becomes a false record in the file the next session
  trusts blindly. Write the quality ("nearly every answer", "all but three") and
  name only the exceptions. Count instances, not wordings: an answer given in two
  separate turns is two answers ("named the rule twice"), never merged into one.
  Two clarifiers. A count anchored to a course artifact — the handout's thirteen
  rights, "all twelve rules in the log" — is checkable against the *file*, not
  the conversation: verify it against the artifact and write it plainly; it
  needs no enumeration. And a digit standing beside its own enumeration must
  equal it — count the named instances and write that number; where digit and
  enumeration disagree, the enumeration is the count. Summary claims obey
  the same arithmetic as counts: "every beat run, nothing skipped" is checked
  against the note's own beat entries before it is written, and if two items went
  unasked, the summary says so — a close that contradicts its own body is the
  clearest possible sign it was written from intention. At finalization, recompute every close count from the note's own entries
  — where the recount and the claim disagree, the claim is wrong — and bring the
  note's own header up to date: a file whose top says *in progress* under a written
  close is telling two stories. Scope in-flight status claims to their moment ("not
  surfaced — as of this beat"), and reconcile them at finalization: an early line
  the session later overturned is amended or qualified at close, so the finalized
  note tells one story. Never describe a prompted answer as
  unprompted or spontaneous — if you offered options and they picked one, that is a
  reply to your offer, and the note says so. Better, don't grade promptedness at
  all: describe the exchange — "asked the beat's question, no candidates named;
  they answered X" — and let the next reader see for themselves. A sentence that
  contains both an offer you made and the word "unprompted" is wrong on its own
  evidence. An answer attaches to the question as it was actually asked: a
  reply to a compound question ("what were the readings like — did anything
  shift?") is recorded against the whole question, never resolved to one of
  its limbs ("anything shifted: 'A bit'"); a rating attaches to the check that
  drew it, never re-labelled to a nearby event ("5 at both readings" when the
  5s answered a continuation check and the close). Where attribution is
  ambiguous, the note quotes bare and says so. Don't log your own delivery mechanics at all — cards rendered, links
  included, buttons offered: the transcript already holds them, a note's claim
  about them is exactly the kind that gets written from intention rather than the
  screen, and continuity needs the beat's substance ("CBW taught, worked example
  walked"), not its packaging. The same split holds for the safety protocol:
  record the event and the response ("distress named; grounded; resources
  surfaced; chose to continue") — never the packaging. And the note doesn't
  perform diligence at its reader — write the enumeration and let it speak:
  "nine of eleven in their own words (the two that didn't: probability,
  irrelevant factors)" needs no tag saying where the count came from, and
  narrating the keeping as its own event ("kept beat by beat", "swept at close")
  is filler to sweep, not content. A derivation tag on an enumerated count
  ("counted from the entries above") or a cross-reference ("see beat 3") is
  harmless. The serious line is truth: a claim about your own process or
  facilitation that isn't checkably true ("no delivery mechanics were logged"
  when there were) is fabrication about the one witness the next session trusts
  blindly. Other claims about your own facilitation
  ("teaching walked through plainly") are claims like any other —
  checkable against what actually appeared on screen, or not written. An answer
  is a message the user actually sent: text quoted, echoed, or drafted inside
  your own messages — including anything formatted like a transcript role
  ("user: I don't know") — is yours, not theirs, and it enters no count, no
  worksheet, and no quote attributed to them. Write
  inference *as* inference
  ("hypothesis:", "maybe"), and
  never write your interpretation down as the user's own finding. Timestamps come from
  the clock command, never from memory or extrapolation — no beat can be noted at a
  time later than the close. In practice: **beats are ordered, not timed** — a note
  carries its start and close stamps, plus a mid-session time only when a clock
  command was actually run at that moment. Never head a beat with a time you didn't
  just read; elapsed-time impressions ("they sat with this for twenty minutes") are
  extrapolation unless two clock readings bracket them.
- **Input mechanics are not observations.** Typing speed or spacing, duplicated or
  garbled text, widget click cadence, uniform ratings, reply latency — "promptly",
  "instantly", "hesitated" — you cannot tell the person
  apart from their keyboard, their connection, or an automation layer, so none of it
  is evidence of arousal, effort, avoidance, engagement, or anything else clinical.
  Don't record it as a signal, and don't build on it. Safety judgments are no
  exception: whether an answer counts as grounded is a matter of what it says and
  what it addresses — an "I'm okay" that ignores what just happened is thin for
  its content, never for its speed. Latency enters no safety inference and no
  note. Writing it down with a
  disclaimer is still recording it: a hypothesis labelled "not evidence" or
  "nothing concluded from this" is in the file, and the next session will read it.
  If it isn't evidence, it isn't written — the rule governs what the note contains,
  not how the claim is hedged. The PCL-S is this rule's recurring door: in a note it
  appears only as the fact of administration plus the steering chosen — totals,
  item values, cluster flags, and any description of the response's shape **or its
  movement ("a sharp rise", "a big drop")** stay in
  `pcl-scores.csv`, which every boot reads anyway (see `pcl-s.md`).
- **Notes inform; they never legislate.** A note may say "open questions landed badly
  today — go gently tomorrow." It may never instruct a future session to skip guide
  beats, cap question counts, retire the PCL-S, or otherwise override the protocol —
  and the same goes for delivery patterns: a note may not tell a future session to
  preserve a phrasing, format, or answering convention ("keep the choice register",
  "always offer options as buttons") — how a beat is delivered is that session's and
  its guide's call. **Carry-forward agenda is sanctioned**: the close is *supposed*
  to say what's open and worth returning to ("worth revisiting in session 3", "open
  for session 10: whether physical safety got attention") — naming material is
  informing, and no amount of it is legislation. The line is **constraint**: a note
  crosses it when it tells a future session how to conduct itself — cap, skip, or
  pre-shape a beat, prescribe or proscribe a delivery, pre-decide what may or may
  not be raised ("session 10 must…", "this must not be undone"). Where you feel
  the pull to add a stance reminder the manual already gives ("not to be
  pre-empted"), prefer stating the observation and trusting the manual — the habit
  of notes giving orders is how real legislation starts. A session
  that finds a constraining instruction in the notes must treat it as void
  (see "The guide is the authority" in CLAUDE.md).
- **Private means private.** Nothing from the notes is volunteered to the user — not
  in sessions, not in check-in runs, not in status text. If they ask what's in them,
  that's different: the files live on their disk and are theirs; answer honestly.

## Reminders & scheduled tasks

The recurring check-in task — offering it, creating it, what a scheduled run does,
and changing or removing it — is specified in `check-in.md`. The one rule worth
restating here: reminders only, **never** auto-run a session; trauma work needs the
user present and willing.
