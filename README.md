# CPT-SA

> **Getting started? Go to [trauma-skills.github.io/CPT-SA](https://trauma-skills.github.io/CPT-SA/).**
> The project site is the getting-started guide — the disclaimers, the requirements, and a
> step-by-step screenshot walkthrough of setup. This README covers the same ground in
> reference form, plus the licensing and evidence detail.

A self-paced, AI-guided adaptation of the **CPT-SA Individual Treatment Manual (2012)** —
16 sessions of Cognitive Processing Therapy for survivors of childhood sexual abuse — built as
a **Claude Cowork** course that lives in a folder on your own computer.

Requires the Claude desktop app, Cowork, and a paid Claude plan. See
[Requirements](#requirements).

> **If you are in crisis right now, please stop and reach out.**
> US: call or text **988**, or text **HOME** to **741741**. UK & Ireland: **116 123** (Samaritans).
> Anywhere: [findahelpline.com](https://findahelpline.com).
> US sexual assault: RAINN, **1-800-656-4673**.
> This repository is not an emergency service and cannot help you in a crisis.

---

## Read this before anything else

This is a **faithful but unofficial adaptation of the CPT-SA Individual Treatment Manual**
(Chard, 2012). Faithful is the operative word: the sessions, the sequence, the worksheets and
the handouts follow the published clinical manual. They have been adapted for AI-guided use and reformatted to read well on a
screen — **not rewritten, not reinterpreted, and not editorialised.** Nobody has added their own
theory of your recovery to it. Where it departs from the manual at all, those departures are
listed openly under [Deliberate deviations](#deliberate-deviations-from-the-manual).

It has **not been reviewed, endorsed, validated, or approved** by Kathleen Chard, Patricia
Resick, Candice Monson, or anyone else involved in developing Cognitive Processing Therapy.

It's worth being precise about what that does and doesn't mean, in both directions. **The course
itself rests on well-tested ground.** CPT is one of the best-evidenced treatments for PTSD that
exists; the sexual-abuse version was validated in a randomised controlled trial; and the
sessions, worksheets and handouts here follow that manual closely rather than reinventing it.
**What has never been tested is this way of delivering it** — the whole course facilitated by an
AI instead of a person. Good material, untested delivery. Both halves of that are true at once.

Specifically:

- **This is the real work of therapy, without a therapist.** The work is just as demanding done
  this way, and deserves the same seriousness. Claude can ask, listen, notice what you're
  avoiding, and follow the protocol carefully. What it cannot do is **hold clinical
  responsibility** or **intervene if you are in danger**. There is nobody on the other end who
  can call someone, check on you tomorrow, or be accountable for how this goes.
- **So line up a real person before you start.** A friend, a partner, a family member, a doctor,
  a helpline you would actually ring. Not to do the course with you, and not to be told any of
  the detail unless you want them to be — only so that somebody knows you are doing difficult
  work at the moment and would notice if you went quiet. This is the single most useful thing
  you can put in place, and the one thing the course cannot arrange for you. If there is
  genuinely nobody, weigh that seriously before you reach sessions 4–8.
- **CPT normally begins with a clinical assessment.** This course does adjust and stop — the
  safety protocol halts session content on distress, and the minimum waits between sessions hold
  whether or not you want them to. What's missing is the assessment that decides whether you should be doing
  this protocol at all, and a trained, supervised, accountable judgement behind every decision
  to continue.
- **The part that helps most is also the hardest.** Sessions 4–8 involve writing detailed
  accounts of the abuse and re-reading them daily. This is the stretch that does the work, and
  it can be a demanding few weeks — sleep, mood and steadiness are often unsettled while you're
  in the middle of it, and they usually settle again afterwards. None of that is a consequence
  of doing it this way: it is the same in a therapist's room, and the manual expects it. What
  is different here is who is watching how you are coping with it. Claude checks, and will stop
  the session work if you are struggling — but it only sees what you bring to a session, and
  there is no trained person watching the weeks in between.
- **A trained CPT provider is the better-evidenced option, and worth checking for before you
  settle for this one.** The directory is at [cptforptsd.com](https://cptforptsd.com/). But
  *better in principle* and *available to you now* are different things. Cost, waiting lists,
  distance, a bad experience with a clinician before, or simply not being ready to say any of
  this out loud to another person are all real. This exists for the gap between the two — not
  as a replacement for a therapist you could actually see.
- **Do not use this if** you are in an unsafe living situation, in acute crisis, actively
  suicidal or self-harming, experiencing psychosis, or in the middle of untreated substance
  dependence. Those are the conditions under which the protocol is most likely to hurt and
  least likely to help.

Use it with your eyes open, or don't use it.

---

## What it actually is

The insight the design turns on: **the folder is the memory.**

A 16-session protocol will not fit into a single conversation, and two separate conversations
with Claude share nothing — the second has no idea the first ever happened. So everything that
matters is written down in the folder instead: where you are, what you've written, how your
scores are moving, when the next session opens. Every conversation begins by reading those notes
and ends by updating them. That's what lets you work through 16 sessions across dozens of short,
separate conversations without ever having to remember where you left off.

What that buys you concretely:

| | |
|---|---|
| **Pacing you can't rush** | The next session opens once the homework from the last one is done and at least 72 hours have passed — whichever takes longer. The heaviest sessions add a little extra rest, so you're never pointed at account-writing right before bed. The course keeps track of the timing itself, so the structure carries the pacing rather than your willpower. |
| **Safety before progress** | Distress, dissociation, or any mention of self-harm stops the session content. Claude helps you get steady first and puts the crisis helplines in front of you — only then does it ask whether you want to carry on. A grounding exercise is available whenever you ask. |
| **Your writing is yours** | `my-work/` and `notes/` are never edited, rewritten, or deleted. Even a full reset *archives* them rather than destroying them. Permanent deletion is yours alone to do, and it's easy: the archive is an ordinary folder on your own computer. |
| **Resumable mid-session** | Live notes are written after every beat, so a dropped conversation picks up from the last beat instead of starting the session over. |

## The 16 sessions

It opens with a **starting point** — a single, skippable, intake-style conversation about
what brings you here and what you'd want back, closing with a baseline PCL-S. It stands in
for the referral and intake a therapist-delivered course assumes, never asks for details of
what happened, and adds no waiting time. It is an addition of this adaptation; the manual's
16 sessions begin unchanged at session 1.

Psychoeducation and "rules" (1–2) → the Impact Statement → the thought–feeling link via A-B-C
sheets (3–4) → writing and processing trauma accounts (4–8) → Challenging Questions and
Problematic Thinking Patterns (7–9) → the five belief themes worked through the Challenging
Beliefs Worksheet: Safety, Trust, Power/Control, Esteem, Intimacy, plus Social Support (9–15)
→ a final Impact Statement and future goals (16).

The manual schedules the PCL-S on the even sessions; the starting point adds a baseline before
session 1 (or offers it in lieu when the starting point is skipped).

---

## Getting started

### Requirements

This is built **exclusively for [Claude Cowork](https://claude.ai)**, and won't work properly
anywhere else. Cowork is what lets the course read its own notes at the start of every
conversation, and what opens the handouts and the weekly check-in alongside the chat instead of
burying them in the conversation.

| | |
|---|---|
| **App** | The **Claude desktop app** for macOS or Windows — [download it here](https://claude.ai/download). Cowork runs in the desktop app; the web version will not do, and neither will the iPhone or Android apps. |
| **Plan** | A **paid Claude plan** — Pro, currently $20/month — at minimum. |
| **Model** | **Claude Opus 5** or **Claude Fable 5** — the two it has been tested with. Fable needs a **Claude Max** plan, while Opus is available on the Pro plan. |
| **Anything else** | **Nothing.** There is nothing else to install, download, or set up. If you can open the Claude app, you can run this. |

**Why those two models.** It has to be Claude, because the whole thing is built on Cowork,
which is what gives it a folder to keep your work in, notes it can read back at the start of the
next conversation, and handouts that open beside the chat. Within that, **Opus 5 and Fable 5 are
simply the two it has been built and tested against.**

That matters more than a preference usually would, because the session guides ask a lot of a
facilitator across many turns — staying Socratic, not challenging beliefs before the protocol
says to, tracking safety signals, writing continuity notes without being reminded. Another model
might hold all of that perfectly well. Nobody has checked.

There is nothing for you to download and nothing to configure. You ask Claude to set it up,
and Claude does the rest.

**1. Open the Claude desktop app and start Cowork.** Make sure the model is set to Opus 5
or Fable 5. If an effort level is shown next to the model name, set it to **High** — the
sessions depend on unhurried, careful reasoning.

**2. Create a Claude project for the course, and give it its own empty folder.** Open **Project or
folder**, choose **Create new project**, name it `My CPT Course` or another name, leave the optional goal
blank, then **Use a folder** and make a new, empty folder for it — a new folder in Documents,
or anywhere else in your own user directory. It wants an empty folder of its own: 16 sessions
of writing, notes and state accumulate, and keeping them together makes the course easy to find.

**3. Finish creating the project.** Choose **Always allow** when Claude asks for access to
the folder, leave Instructions blank, confirm visibility is **Local**, then **Create
project**.

**4. Inside the project, set approvals to Automatically approve.** The course reads and
updates its own files constantly; without this, every session stops for confirmation on each
file action.

**5. Paste this into the project's message box:**

```
Start CPT-SA from trauma-skills.github.io/CPT-SA/start
```

Claude sets everything up and welcomes you in — the course opens with a short conversation
about what brings you here. You don't have to do anything else.

**6. From then on, open a new conversation in My CPT Course whenever you want to work.**
Just say "Let's start." It reads the files, works out where you are, and offers exactly one next
thing — begin a session, do the homework, or wait until the next unlock. You never have to
track it.

A screenshot walkthrough of all of the above is on the
[project site](https://trauma-skills.github.io/CPT-SA/#getting-started).

> **Two things to check before you paste that prompt.** It tells Claude to fetch and set up
> files from the internet, which is worth doing deliberately rather than reflexively.
> Confirm the address is exactly `trauma-skills.github.io/CPT-SA/start`, and that you are
> signed into **your own** Claude account (see [Privacy](#privacy)).

### What you can say

| Say this | What happens |
|---|---|
| `setup CPT-SA` | First-time install into the current folder |
| `start next session` | Begin the next session, if it's unlocked |
| `let's do my homework` | Guided walkthrough of the current homework |
| `where am I?` | Orientation — current state and the next step |
| `grounding` | A grounding exercise, available at any time |
| `check for updates` | Look now for a newer version. Tells you what changed and waits; never updates on its own |
| `reset CPT-SA` | Back to a first-run state. Confirms first; **archives** your writing rather than deleting it |

### What ends up in your course folder

Everything is a plain file you can open, read, print, or delete yourself. Nothing is hidden or
locked.

- **Your writing** — a `my-work` folder holding the Impact Statement, your accounts, your
  worksheets. This is yours; nothing ever edits or removes it.
- **Where you are** — a progress file recording which sessions you've done, the current
  homework, and when the next session opens.
- **The sessions** — all sixteen guides and their handouts, so you can read ahead, or not.
- **Crisis resources** — a page of helplines, always there, opened for you whenever things
  get heavy.
- **Session notes** — short continuity notes, so a new conversation picks up where the last
  one stopped.
- **The course itself** — a `CLAUDE.md` file and a `skill` folder holding the instructions
  Claude follows, as readable as everything else. They're installed into this folder rather
  than anywhere global, so the whole thing is self-contained — and deleting the folder really
  does remove all of it, with nothing left behind on your computer.

Your course folder is personal. Keep it somewhere private, and don't put it in a shared drive,
a synced folder, or anywhere that gets backed up publicly.

---

## Privacy

This is the most sensitive category of personal writing there is. The design takes that
seriously, and the claims below are specific rather than reassuring.

**What this repository does:**

- **No analytics. No tracking. No crash reporting.** Nothing about you or your
  use of this is recorded anywhere but your own folder, and nothing is ever sent anywhere.
- **It goes online for exactly one thing.** At most once a fortnight, at the start of a
  conversation and before anything else happens, it looks at
  [`version.json`](https://trauma-skills.github.io/CPT-SA/version.json) on the project site to
  see whether a newer version of the course has come out — then tells you, and waits. **It
  doesn't send anything about you**: not your writing, not your progress, not who you are. It's
  the same as your own browser opening a page here, so whoever hosts the site sees what any
  website sees — that a computer somewhere asked for a file. Nothing is downloaded or changed
  unless you say yes, and *"stop asking about updates"* switches it off for good. With it off,
  the course never goes online at all.
- **No accounts, no servers, no sync, no cloud storage.** Your course folder is a folder on
  your own disk and nothing in this project ever uploads it.
- **The welcome card and the check-in form don't reach out to anyone.** Everything they need is
  inside them — no fonts, pictures or code pulled in from other companies.
- **All of it is just writing, and you can read it.** Every part of this course is a document —
  the sessions, the handouts, the instructions Claude follows. Nothing here is a program,
  nothing is scrambled or hidden, and nothing needs special software to open. If you want to
  know what a session will ask of you before you start it, you can go and read it.
- **Your writing is never modified or deleted by the course.** `my-work/` and `notes/` are yours.
  Even a reset archives rather than deletes. **You** can delete it permanently whenever you like —
  the archive is a normal folder on your own computer, and nothing here keeps a second copy
  anywhere, so deleting it is genuinely the end of it.

**The honest caveat — read this one:**

You are talking to Claude. **What you type during a session is sent to Anthropic** to generate
the response, exactly as with any other Claude conversation, and is handled under Anthropic's
privacy policy and whatever data settings apply to your plan. This repository cannot change
that and does not pretend to. What stays local is your *files*; what you type in the
conversation is not local.

So the exposure is exactly one party: **Anthropic, and nobody else.** No third party receives
anything — not the maintainers of this repository, not any analytics vendor, not any hosting
provider, not any other service. There is no middleman, because there is no server between you
and Claude.

That is an inherent property of using an AI facilitator, not a flaw in this design — but you
should decide whether it's acceptable to you **before** you start, not after.
If it isn't, don't use this.

**Use your own accounts — on Claude, and on the computer.**

There are two separate doors into this material, and both need to be yours.

- **Your Claude account.** Everything runs under whichever account is signed in, and that
  account's history is where the conversations live. A shared household, family, or work
  account means someone else can open the app and read every session you have done.
- **Your login on the computer itself.** This matters just as much, and it's easy to miss: your
  writing is saved as files inside whichever user account you're logged into on that machine. A
  shared computer login — the family laptop everyone uses, a communal desktop, a shared work
  profile — means anyone who sits down and logs in can open and read it, no matter whose Claude
  account created it. Use a login that is yours alone, with a password, and set the screen to
  lock.
- **Not a work or employer-managed account**, on either. Those can be subject to administrator
  access, device management, retention policies, and audit.
- **Keep the folder in your own user directory** — not a shared drive, not a synced folder, not
  anywhere backed up somewhere you wouldn't want it.

If you cannot get sole control of both, this is not safe to use yet — sort that out first. It is
worth the delay.

**Also:** your course folder is personal. Don't put it in a git repository, a shared drive, or
anywhere backed up somewhere you wouldn't want it. This repo's `.gitignore` guards against
committing one here by accident, but it can't help you elsewhere.

---

## Clinical notes

### Why this exists

CPT is one of the best-evidenced treatments for PTSD in existence, and most people who could
benefit from it never get it — because there is no trained provider nearby, because there's a
waiting list, because it's unaffordable, or because the prospect of telling a stranger in a
room is itself the barrier. The manual is obtainable. The protocol is highly structured. That
structure is what makes it unusually amenable to being held by software: it is a sequence of
defined sessions with defined homework and defined worksheets, not free-form clinical
improvisation.

**There is a second reason, and it isn't about access at all.** Some people arrive here having
already tried a therapist and been harmed by one — a confidentiality breach, a boundary crossing,
a dependence that was encouraged and then withdrawn, or simply a clinician out of their depth
with this material. For that group, "find a therapist" is not straightforwardly good advice.

That is the argument *for*. It does not make the result equivalent to treatment, and the
sections below try to be precise about where the evidence stops.

### What the evidence supports

**CPT itself — strong.** CPT is *strongly recommended* for PTSD by the
[APA Clinical Practice Guideline](https://www.apa.org/ptsd-guideline/treatments/cognitive-processing-therapy),
the VA/DoD guideline, and
[ISTSS](https://istss.org/clinical-resources/trauma-treatment/treatment-materials/cognitive-processing-therapy/),
on the basis of a large body of randomised trials.

**CPT-SA specifically — supported.** The sexual-abuse adaptation this repository is built from
was tested in a randomised controlled trial: 71 women with PTSD related to childhood sexual
abuse, randomised to CPT-SA or a minimal-attention waitlist, assessed at post-treatment and at
3-month and 1-year follow-up. CPT-SA substantially outperformed the control condition and
gains held at follow-up.
*Chard, K. M. (2005), Journal of Consulting and Clinical Psychology, 73(5), 965–971.*
([PubMed](https://pubmed.ncbi.nlm.nih.gov/16287396/))

**Remote delivery by video — well supported.** Several non-inferiority randomised trials have
found CPT delivered over video to be non-inferior to CPT delivered in person:

- 126 women with PTSD (veterans and civilians), video-teleconferencing vs. in-person; symptom
  improvement in the video arm was non-inferior, and held at 3- and 6-month follow-up.
  *Morland, Mackintosh, Rosen, Willis, Resick, Chard, & Frueh (2015), Depression and Anxiety,
  32(11), 811–820.* ([PubMed](https://pubmed.ncbi.nlm.nih.gov/26243685/))
- *CPT for PTSD delivered to rural veterans via telemental health: a randomised non-inferiority
  clinical trial*, Journal of Clinical Psychiatry (2014).
  ([PubMed](https://pubmed.ncbi.nlm.nih.gov/24922484/))
- *In-office, in-home, and telehealth CPT for PTSD in veterans: a randomised clinical trial*,
  BMC Psychiatry (2022) — remote arms performed at least as well as in-office.
  ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8763446/))

**Sessions more often than once a week — supported.** The minimum wait between sessions here is
**72 hours**, faster than the weekly rhythm most people picture, so it's fair to ask whether
that is a compromise. It isn't, and the evidence leans mildly the other way.

CPT is written to be delivered **once or twice weekly**, so more often than weekly sits inside
the protocol rather than departing from it. In an ongoing non-inferiority trial of a five-day
massed CPT format, twice-weekly individual CPT over six weeks is the *standard* comparison arm,
not the experimental one.

Across trauma-focused therapy generally, a meta-analysis of 160 randomised trials covering
10,556 patients found **no difference in efficacy** between more-intensive delivery (at least
1.5 sessions a week) and standard delivery, and **significantly lower dropout** from the more
intensive schedule.
*Hoppen, Kip & Morina (2023), Journal of Anxiety Disorders, 95, 102684.*
([PubMed](https://pubmed.ncbi.nlm.nih.gov/36827748/))

The same pattern appears in Prolonged Exposure specifically. A meta-analysis of 35 randomised
trials (1,508 adults) found dropout of **21.0%** where sessions were prescribed at least twice
weekly, against **34.0%** where they were less frequent. And a non-inferiority trial in 134
military personnel and veterans compressed ten PE sessions into two weeks: non-inferior to ten
weekly sessions, with dropout of 4.8% against 16.9%.
*Levinson, Halverson, Wilson & Fu (2022), Journal of Traumatic Stress, 35(4), 1047–1059*
([PubMed](https://pubmed.ncbi.nlm.nih.gov/35278229/));
*Dell and colleagues (2022), Psychological Medicine, 53(9), 4192–4199*
([full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10317798/))

**72 hours is a minimum, not a schedule.** Nothing pushes you towards it and there is no streak to
keep. Weekly is a perfectly good rhythm and is what the manual assumes; slower than weekly is
fine too. The minimum exists to prevent the opposite failure — 16 sessions crammed into a fortnight
because nothing was stopping you. How you actually space them is yours.

**And the pace answers to you rather than to a diary.** In ordinary practice the interval between
sessions is settled between two calendars and a clinic's capacity; the once-a-week model is the
norm in outpatient practice rather than a finding about which interval works best. That is not a
small detail. In a randomised trial of 136 women receiving CPT or PE, **longer average gaps
between sessions predicted significantly smaller symptom reduction** — and so did less consistent
spacing. Sessions that slip through cancellation, leave and rescheduling are not neutral.
*Gutner, Suvak, Sloan & Resick (2016), Journal of Consulting and Clinical Psychology, 84(12),
1108–1115.* ([PubMed](https://pubmed.ncbi.nlm.nih.gov/27213491/))

What none of it licenses: it identifies no ideal interval, nobody has tested 72 hours
specifically, and every study above had a clinician setting the pace and a fixed course length.
That frequent, regular sessions do better is not the same as showing that someone left to
schedule themselves will achieve that.

**Delivery by text, without a live session — promising but early.** Remote CPT is not only a
video-call story, and this strand is the closer precedent for how this course actually works.

**CPT-Text** adapts CPT for *asynchronous message-based delivery* — no live session at all, the
work carried out in writing over time. In an open trial of 28 people, compared against a matched
group receiving ordinary messaging therapy on the same platform, CPT-Text produced substantially
greater symptom improvement in less time, with a 63% completion rate comparable to face-to-face
and video CPT. A much larger randomised trial (300 participants) is under way.
*Wiltsey Stirman and colleagues (2021), "Open Trial of an Adaptation of Cognitive Processing
Therapy for Message-Based Delivery," Technology, Mind, and Behavior, 2(1).*
([Full text](https://tmb.apaopen.org/pub/rhr2svcm))

Separately, **Written Exposure Therapy** — a brief, entirely written trauma treatment — has been
found non-inferior to CPT itself in two randomised trials, with lower dropout. It is a different
protocol, not CPT delivered in writing, but it is good evidence that processing trauma *on the
page* is not a compromise.
*Sloan, Marx, Lee, & Resick (2018), JAMA Psychiatry* ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29801098/));
*Sloan, Marx, Resick et al. (2022), JAMA Network Open* ([Full text](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2787933))

**The caveat that survives all of it:** every study above — video and text alike — had *a trained
human therapist* doing the work. Together they establish that CPT survives losing the room,
losing the face, and even losing the live session. None of them establish what happens when you
remove the therapist.

**Self-guided and internet-delivered — weaker, and mostly *guided*.** The Cochrane review of
internet-based cognitive and behavioural therapies for PTSD found they *may* produce a
clinically important symptom reduction versus waitlist, but rated the certainty of evidence
**very low**, on a small number of trials, with no evidence of benefit at short-term follow-up
and no trials reporting adverse events.
*Lewis, Roberts, Bethell, Robertson, & Bisson (2018), Cochrane Database of Systematic Reviews,
12, CD011710.* ([PubMed](https://pubmed.ncbi.nlm.nih.gov/30550643/))

Where internet-delivered trauma therapy has performed best — for example the Spring programme
in the UK, non-inferior to face-to-face trauma-focused CBT at 16 weeks, though *not* sustained
at 52 weeks — it was **guided self-help**: the participant worked through material alone, but
with scheduled contact from a real therapist throughout. Fully unguided delivery is
consistently the weakest arm in this literature, with markedly higher dropout.

**That distinction is the entire design brief here, and this project is built for the guided
side of it.** It is deliberately not a workbook you open by yourself. Something reads your notes
at the start of every conversation, works out where you are, holds the pacing, asks after the
homework, notices what you are steering around, and stops the session if you are in distress.
Those are the functions that separated the guided arms from the unguided ones. The difference —
and it is not a small one — is that in every trial in that literature, **the guide was a
person.** Whether something that performs the same functions without being a person produces the
same benefit is precisely the untested question, and it is the subject of the next section.

### What the evidence does not support

**There is no evidence base for CPT facilitated by a large language model. None.** No trial,
no pilot, no case series. This repository is not an implementation of an evidence-based
delivery method; it is an untested extrapolation from one.

The known risks of the extrapolation are worth naming:

- Its read on how you're doing is **unvalidated**. It has only what you write, and trauma
  survivors under-report — a clinician also has tone, pace, hesitation and body language that a
  text channel never carries.
- It may miss dissociation, which is common in this population and especially likely during
  account work. It might well notice; nobody has ever measured how reliably.
- It may be inappropriately agreeable where a clinician would push back, press on where a
  clinician would stop, or pause when a clinician would continue.
- Nobody is checking on you if you go quiet mid-protocol.
- Nothing here is accountable to anyone — no licence, no supervisor, no regulator, no duty of
  care.

The safety scaffolding in this repository — the minimum waits between sessions, distress checks,
grounding, crisis resources, the rule that safety overrides progress — is a genuine attempt to
mitigate that. It is a mitigation, not a solution, and it has not been validated either.

### Deliberate deviations from the manual

- **No diagnosis.** The manual assumes a completed clinical assessment and tells the client
  they have PTSD. This adaptation offers psychoeducation and invites you to notice what
  resonates instead. It never asserts you have a disorder.
- **A starting point added.** The manual assumes a referral and intake happened before
  session 1. This adds an optional intake-style conversation in their place — what brings
  you here, what it's costing, whether now is the right time — with a baseline PCL-S at its
  close, restoring the pre-treatment measure the manual takes for granted. It sits before
  the manual-derived material; the 16 sessions start unchanged at session 1.
- **Minimum waits added.** The manual is therapist-paced, at one or two sessions a week. This
  adds a hard 72-hour minimum between sessions plus per-session homework cooldowns, because
  there's no clinician watching for someone doing all 16 sessions in a fortnight. The minimum is
  deliberately not *weekly* — see the pacing evidence above.
- **PCL-S scores are never read back.** The manual has a clinician interpret them. Here they
  stay facilitator-facing, because a rising score with nobody to contextualise it is more
  likely to harm than help.
- **Worksheets are guided, not handed over.** A-B-C sheets, Challenging Questions and the
  Challenging Beliefs Worksheet are worked through conversationally rather than issued as blank
  forms, since there's no session to bring a half-finished form back to.

---

## Attribution and source material

The clinical content in this repository — the session structure, the therapeutic sequence, the
handouts, the worksheets — is **derived directly from** Dr. Kathleen Chard's *CPT-SA Individual
Treatment Manual* (2012), which the developers of CPT publish on their own site —
[read it in full (PDF)](https://cptforptsd.com/wp-content/uploads/2017/01/CPT-SA-IND-Tx-Manual-2012.pdf).

CPT-SA is the version of **Cognitive Processing Therapy** written specifically for survivors of
childhood sexual abuse. CPT itself is a treatment for PTSD developed by **Patricia A. Resick,
Candice M. Monson, and Kathleen M. Chard**; its current comprehensive manual is
[*Cognitive Processing Therapy for PTSD: A Comprehensive Manual* (2nd ed., Guilford Press)](https://www.guilford.com/books/Cognitive-Processing-Therapy-for-PTSD/Resick-Monson-Chard/9781462554270),
and its official home — including provider training and the provider directory — is
[cptforptsd.com](https://cptforptsd.com/).

The handouts in this course are the CPT-SA manual's handouts, reformatted to read well on a
screen. They are included because the course is unusable without them, under a good-faith
reading of personal and educational use.

### Further reading

- [CPT official site](https://cptforptsd.com/) — training, consultation, provider directory
- [VA National Center for PTSD — CPT](https://www.ptsd.va.gov/professional/continuing_ed/CPT_Manual.asp)
- [APA Clinical Practice Guideline — CPT](https://www.apa.org/ptsd-guideline/treatments/cognitive-processing-therapy)
- [ISTSS — CPT treatment materials](https://istss.org/clinical-resources/trauma-treatment/treatment-materials/cognitive-processing-therapy/)
- [CEBC — CPT program profile](https://www.cebc4cw.org/program/cognitive-processing-therapy-cpt/)

---

## Licence

**Split, deliberately.** See [NOTICE.md](NOTICE.md) for the full statement.

- **The scaffolding is free and open source (MIT license).** The operating manual (`install/CLAUDE.md`), `install/skill/` (excluding `bootstrap/sessions/`), and
  the widget HTML — the file-based-memory design, the pacing rules, the install/update/reset
  semantics. That work is original and freely reusable.
- **The clinical content is not licensed by this repository.** Everything under
  `install/skill/bootstrap/sessions/` — session guides, handouts, worksheets — is derived from
  Dr. Chard's manual. No rights to it are granted here, because none are held.

If you want to reuse the *machinery* for a different protocol, the MIT part is what you want,
and it is genuinely reusable — the folder-as-memory pattern, the gating, and the archive-never-
delete guarantees are all protocol-agnostic.

---

*Built with care, published with reservations. If you're using this on yourself: go slowly,
stop when you need to, and tell someone you trust that you're doing it.*
