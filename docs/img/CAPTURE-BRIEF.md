# Screenshot capture brief

Eight screenshots drive the install walkthrough on the CPT-SA landing page. They are shown
as a carousel at the top of **Getting started**; a screen whose image is
missing drops itself out of the carousel rather than showing a broken image.

## How the three sets relate

| Set | Path | Tracked? | What it is |
|---|---|---|---|
| Raw | `docs/img/raw/` | **No** — gitignored | Native full-window captures, straight from the machine |
| Cropped | `docs/img/` | Yes | Cropped to the action, downscaled to ≤1600px wide |
| Marked | `docs/img/focus/` | Yes | The same crop, with the control that matters ringed in plum |

Both committed sets are used together: the carousel stacks the marked copy over the plain one
and cross-fades it, which reads as the ring gently pulsing. The ring is baked into the PNG rather
than drawn in CSS so that Markdown — `README.md`, GitHub, anything without a stylesheet — shows
it too. Both files therefore need to exist, at identical dimensions, for every screen.

**Only the raw set is captured by hand.** The other two are derived:

```bash
python3 tools/make-shots.py
```

The crop boxes and focus rectangles live in `SHOTS` at the top of that script, in raw pixel
coordinates. If a shot is retaken at a different window size, its numbers need redoing —
`python3 tools/make-shots.py --grid` writes ruled copies of the raws to `docs/img/.grid/`
to make that quick.

The raws stay out of the public repo but should be kept locally: they are what lets a crop
be reframed without recapturing anything.

Numbering starts at `02`. There was once an `01-cowork.png`; it turned out to be the same
frame as `02`, which already shows the Cowork toggle and the model, so the two steps share
one screen. The remaining names are left alone so they still line up with the script.

---

## Prompt for recapturing

Claude cannot capture these itself — it is not permitted to be granted control of its own
application window. Paste the prompt below into Codex, or any agent that can drive the
Claude desktop app.

> I need eight screenshots of the Claude desktop app on macOS, for the install guide of an
> open-source project. They will be published on a **public website**, so the privacy rules
> below are hard requirements, not preferences.
>
> **Save them to:** `~/Code/projects/cpt-sa/docs/img/raw/`
> **Filenames, exactly:** `02-project-or-folder.png`, `03-create-new-project.png`,
> `04-create-project.png`, `05-folder.png`, `06-folder-permissions.png`,
> `07-project-details.png`, `08-automatic-approve.png`, `09-paste.png`
> **Format:** Full, uncropped window captures at native Retina resolution. Do not crop, and
> do not enlarge a low-resolution or JPEG preview — cropping is done afterwards by a script.
> Keep the window at the same size for every shot.
>
> **Before capturing anything — privacy setup. Do all of these:**
> 1. Sign into a **throwaway or clean Claude account** if one is available. If not, tell me
>    and stop rather than capturing a personal account.
> 2. **Clear or collapse the conversation sidebar.** No conversation titles or history may
>    appear in any shot.
> 3. Make sure **no account name, email address, avatar, or profile initial** is visible.
> 4. Make sure **no other folder names, file paths, or project names** are visible beyond
>    the demo folder created for this.
> 5. Hide the macOS menu bar clock, notifications, and any other app windows. Nothing from
>    outside the Claude window should be in frame.
> 6. Use **light mode**, default window size, no zoom.
> 7. Hide the greeting/title, **Ideas for you**, and any usage promotion so the action is
>    the only visual focus.
>
> **The eight shots:**
>
> 1. `02-project-or-folder.png` — The clean Cowork composer before anything is attached:
>    **Cowork** selected rather than Chat, the model set to **Opus 5**, and the closed
>    **Project or folder** selector legible. All three are highlighted in the published
>    version, so all three must be in frame and unobscured.
>
> 2. `03-create-new-project.png` — The **Project or folder dropdown** open, including the
>    search field and all menu items, with **Create new project** hovered.
>
> 3. `04-create-project.png` — The initial **Create a project** dialog before a folder is
>    chosen. Show `My CPT Course` in **What are you working on?**, leave **What are you
>    trying to achieve?** blank, and keep **Use a folder** visible.
>
> 4. `05-folder.png` — **Choosing a new, empty folder** for the course. Create a folder
>    called `My CPT Course` in Documents first, then capture the moment Cowork is pointed at
>    it. The folder name and the **New Folder** button should both be legible. No other
>    folders in frame if avoidable.
>
> 5. `06-folder-permissions.png` — The folder permissions dialog for `My CPT Course`, with
>    **Always allow** visible.
>
> 6. `07-project-details.png` — The final **Create a project** dialog after the folder has
>    been chosen and permission granted. Show `My CPT Course`, blank **Instructions**,
>    `/Users/me/Documents/My CPT Course` as the **Local folder**, and **Local** visibility.
>    The **Create project** button must be visible.
>
> 7. `08-automatic-approve.png` — From inside the newly created **My CPT Course** project,
>    the Cowork approvals menu open with **Automatically approve** selected and legible. No
>    explanatory hover or keyboard-focus tooltip should be visible.
>
> 8. `09-paste.png` — From inside the **My CPT Course** project, the message box with this
>    text pasted in, ready to send, cursor visible, **not yet sent**:
>    ```
>    Start CPT-SA from trauma-skills.github.io/CPT-SA/start
>    ```
>
> **Do not actually send the message** — the last shot is the pre-send state, and running
> the install isn't part of this task.
>
> When you're done, list the eight files with their pixel dimensions, and tell me explicitly
> whether anything identifying appeared in any frame.

---

## Checklist before publishing

Check the **raw** captures for privacy — a crop is not a redaction, and the raws are the
thing a future reframe comes from:

- [ ] No conversation titles, history, or sidebar content
- [ ] No account name, email, avatar, or initial
- [ ] No unrelated folder names, file paths, or project names
- [ ] No other application windows, notifications, or menu-bar content
- [ ] Native Retina pixels preserved; no low-resolution preview upscaled

Then run `tools/make-shots.py` and check the **published** sets:

- [ ] Each crop frames its action with a comfortable margin and no half-cut UI at the edges
- [ ] The thing each shot is meant to show is legible at page width (~640px)
- [ ] The ring lands on the right control, and nothing else in the frame is obscured

If a raw capture contains private content, retake it — do not rely on the crop to hide
identifying material that remains in the source.
