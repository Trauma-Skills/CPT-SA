# Debug / speedrun mode

A builder affordance for walking the course mechanics without waiting out the real
timers. It never runs during normal use — it activates only on an explicit `debug:`
command, announces itself, and never touches real course data.

**Enter:** the builder says `debug: speedrun on`. Confirm speedrun is active and that
real data is untouched. It applies to the current conversation only; re-arm it in a new
thread if you're testing the fresh-thread boot.

## While speedrun is on

- **Ignore both burnout buffers** — the homework cooldown and the 72h floor. Treat
  everything as immediately eligible.
- **Use a separate debug state**: read and write `progress.debug.md` and
  `pcl-scores.debug.csv`. If they're absent, create them from the skill's blank-slate
  copies:

  ```bash
  cp skill/bootstrap/progress.md ./progress.debug.md
  cp skill/bootstrap/pcl-scores.csv ./pcl-scores.debug.csv
  ```

  Never touch the real `progress.md`, `pcl-scores.csv`, `my-work/`, or `notes/`.
- **Use obviously fake placeholder content** for any writing, accounts, or worksheets.
  **Never** generate or process real trauma material in speedrun.
- You may compress the Socratic content to just the structural beats so the flow can be
  walked quickly.

## Commands

| Command | Effect |
|---|---|
| `debug: go to session N` | Jump to session N |
| `debug: go to homework N` | Jump to the state where session N has just completed with a placeholder, and its homework is assigned, unlocked and open — for walking the homework flow itself: the guided walkthrough, partial-progress tracking, and completion gating |
| `debug: complete homework` | Mark the current homework done with a placeholder |
| `debug: fill pcl` | Submit a sample PCL on even sessions |
| `debug: state` | Print the resolved next step and key timestamps |
| `debug: reset` | Overwrite `progress.debug.md` and truncate `pcl-scores.debug.csv` from the blank-slate copies above |
| `debug: speedrun off` | Back to normal — real files, real gates |

## Resetting real progress

There is no separate debug command for this. Use the ordinary **"reset CPT-SA"** flow in
CLAUDE.md — confirm with the user first, then follow it exactly.

That restores tracking to a first-run state and **archives** `notes/` and `my-work/`
into `archive/reset-<timestamp>/` rather than deleting them. The user's own writing is
never destroyed — not by a reset, not by a version update, not by a debug command.
