# This repo is the source of the `cpt-sa` skill

It is **not** a course folder. It holds the skill that sets course folders up:

| Path | What it is |
|---|---|
| `install/CLAUDE.md` | The facilitator's operating manual, installed at a course folder's root — stance, gates, PCL procedure, safety protocol |
| `install/skill/` | Procedures read on demand; `install/skill/bootstrap/` is the blank-slate scaffolding setup copies from |
| `docs/` | The published site (GitHub Pages) — landing page, install instructions, screenshots |
| `tools/` | Build-time only: derives the published screenshots from local raw captures |
| `qa/` | **Out of bounds — see below** |
| `NOTICE.md` | Split licence. Read it before moving or reusing anything |

## `qa/` is out of bounds

**Do not read, follow, summarise, or act on anything in `qa/` unless the user explicitly
asks about QA by name.** It is not documentation and it is not guidance.

It holds procedures for rewriting timestamps to defeat the course's own pacing gates, and —
in the untracked files below — a simulated-user script and scripted crisis language. All of
it exists to *test* the skill from outside it. Any of it bleeding into facilitation, or into
a course folder, would be worse than the bug it was written to catch.

**`qa/persona.md` and `qa/runs/` are untracked and must stay that way.** They contain
simulated first-person disclosure, verbatim self-harm strings, and transcripts of both.
They are gitignored; never `git add -f` them, never move their content into a tracked file,
and never quote them into a commit message, an issue, or `docs/`. If you are reasoning about
the persona, [qa/PROTOCOL.md](qa/PROTOCOL.md) §3.1 specifies its shape without carrying any
of the material — use that instead of opening the file.

If work here touches `install/` or `docs/setup/`, it is worth telling the user
that a QA pass is due. That is a pointer, not a reason to open the files.

## When editing

- **`install/skill/bootstrap/sessions/**` is derived clinical content** and is excluded from the
  MIT grant (`NOTICE.md` §2). Don't relicense it, don't move it under a licensed path, and
  don't add material to it that isn't in the manual.
- **The skill must stay dependency-free.** It runs on a stock Mac or Windows machine with no
  developer tools: markdown and two self-contained HTML widgets, no scripts, no build step,
  no network calls from the widgets. `tools/` is for the maintainer's screenshots and never
  ships to a user.
- **The install payload is a built release asset, never the repository.** Users install
  from `releases/latest/download/cpt-sa.zip`, which `.github/workflows/release.yml`
  builds from `install/` plus `LICENSE.md` on every `v*` tag push. `qa/`, `tools/`,
  `docs/` and this file must never reach an installing user's disk — if the setup page
  ever points at a branch archive again, that boundary is broken.
- **The file boundary in `install/CLAUDE.md` is the load-bearing invariant.** Scaffolding is
  replaceable, seeds are write-once, and `my-work/` and `notes/session-*.md` are never
  overwritten, edited or deleted by anything — install, update, reset or otherwise. Any
  change near install/update/reset semantics needs that re-checked.
- **Never create a course folder inside this repo.** They live in the user's own directory.
  The root-anchored entries in `.gitignore` are a backstop for that mistake, not permission
  to make it.
- **`docs/` is published.** Nothing personal, nothing from a real account, no screenshot
  showing conversation titles, account names, or folder paths beyond the demo folder.
