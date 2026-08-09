# NOTICE — licensing and attribution

This repository is **split-licensed**. Read this before reusing anything from it.

## 1. Original work — MIT licensed

The following is original work and is released under the MIT Licence, in [LICENSE.md](LICENSE.md):

```
install/CLAUDE.md
install/skill/debug-mode.md
install/skill/pcl-s.md            (the scoring/administration procedure and thresholds
                               are standard published PCL-S material; the guidance on
                               how this skill uses them is original)
install/skill/state-files.md
install/skill/bootstrap/widgets/**
install/skill/bootstrap/progress.md
install/skill/bootstrap/pcl-scores.csv
install/skill/bootstrap/crisis-resources.md
install/skill/bootstrap/**/README.md
install/skill/bootstrap/.claude/**
README.md
```

This is the machinery: the folder-as-memory design, the pacing and gating rules, the
install/update/reset semantics with their archive-never-delete guarantees, the safety
scaffolding, and the widgets. It is protocol-agnostic and genuinely reusable — if you want to
build something similar for a different structured protocol, this is the part you want.

## 2. Derived clinical content — NOT licensed by this repository

The following is **excluded from the MIT grant**:

```
install/skill/bootstrap/sessions/**
```

That covers every session guide, handout, and worksheet.

This material is **derived directly from**:

> **Chard, K. M. (2012).** *Cognitive Processing Therapy — Sexual Abuse (CPT-SA): Individual
> Treatment Manual.* Copyright © Kathleen M. Chard, Ph.D.
> [Read it in full (PDF)](https://cptforptsd.com/wp-content/uploads/2017/01/CPT-SA-IND-Tx-Manual-2012.pdf), published by
> the developers of CPT on their own site.

Cognitive Processing Therapy was developed by Patricia A. Resick, Candice M. Monson, and
Kathleen M. Chard. The official home of the protocol is <https://cptforptsd.com/>.

**No rights to this material are granted by this repository, because none are held.** The
maintainers of this repository claim no ownership of, and assert no licence over, the
CPT or CPT-SA protocols or any content derived from Dr. Chard's manual. The MIT Licence in
`LICENSE.md` does not extend to it, and no permission to redistribute it is given or implied.

The source manual itself is **not** included in this repository and will not be. Its title page
states *"Do not cite without permission from the author."* It is, however, published free by the
developers of CPT on their own site:
[CPT-SA Individual Treatment Manual (PDF)](https://cptforptsd.com/wp-content/uploads/2017/01/CPT-SA-IND-Tx-Manual-2012.pdf),
via [cptforptsd.com](https://cptforptsd.com/).

The derived handouts are present here because the course is unusable without them, under a
good-faith reading of personal and educational use. This is a statement of intent, not a legal
conclusion, and it has not been reviewed by counsel.

## 3. No endorsement

This adaptation has not been reviewed, endorsed, validated, or approved by Kathleen Chard,
Patricia Resick, Candice Monson, Guilford Press, or any organisation associated with Cognitive
Processing Therapy. Any errors, deviations, or harms arising from this adaptation are the
responsibility of this repository's maintainers alone, and must not be attributed to the
developers of CPT.

## 4. Not medical advice

This repository does not provide medical or psychological advice, diagnosis, or treatment, and
does not create a clinician–patient relationship. It is not a substitute for care from a
qualified professional. See the disclaimers in [README.md](README.md).
