# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's folders hold invented letters, lists and notes.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: it refuses to run without a terminal, its rich
   previews depend on the terminal's graphics, its names and
   flags shift between versions, its trash is only as safe as
   the desktop trash ever is, and its plugins are third-party
   code.
8. **The safety rule is in the text, early.** Yazi's own
   delete key defaults to the trash, and this guide states the
   two-delete distinction — recoverable `d`, permanent `D`,
   each behind its own confirmation — in chapter 2, before any
   procedure depends on it, and repeats it where the keys are
   taught. The matching rule for add-ons — read keymap shell
   commands and plugins before running them, because they act
   with your permissions — is stated where each is introduced.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a shared Ubuntu 24.04 sandbox with **no
interactive terminal and no display**. Yazi **26.9.1** (official
release archive `yazi-x86_64-unknown-linux-gnu.zip`, 14 MB) was
run unmodified. Because the program refuses to start without a
terminal — it probes the terminal even for `--help`, and fails
with "Inappropriate ioctl for device (os error 25)" — the lab
drove it through a **pseudo-terminal** (110x32) with a small
Python harness (`yazi-lab/ptyrun.py`), which sent scripted
keystrokes (the `.scn` files) and rendered the returning screen
with the pyte library. Every screen quoted is that rendering;
every file operation was then re-checked on disk with `ls` and
friends, and the guide believes the disk where the two could
disagree. All transcripts live in `yazi-lab/transcripts/`
(t00–t16).

Run for real, with transcripts as evidence:

- Version for both binaries; `yazi --help` and `ya --help`
  captured under a pseudo-terminal (t00, t01, t03) — and the
  same `--help` failing verbatim without one (t16).
- `yazi --debug` answered with the verbatim "unexpected
  argument" error: the flag no longer exists in 26.9.1. Its
  report was captured from `ya env` instead, both with no
  configuration present and with the lab's configuration folder
  in use (t02, t05).
- Navigation on a planted tree (garden / kitchen / photos,
  budget.csv, notes.txt): j/k movement, l into a folder, h
  back, G to the bottom, q quitting with exit code 0 — with
  the preview pane following each step (t09).
- Previews seen on screen: a folder's listing, plain text
  (a diary page, a letter), CSV rows, and the "Empty file" /
  "No items" notices (t09, t10).
- File operations, each verified on disk afterwards: create a
  file and (with a trailing slash) a folder; open a file, with
  `$EDITOR` pointed at a logging stand-in script that recorded
  the full path it was handed; rename — including the first
  attempt's `letter-to-sam.txt.txt`, which exposed the rename
  prompt's cursor resting before the extension, and the
  corrected rename after it; cut and paste across folders;
  copy and paste in place, producing the `_1` suffix; Space
  selection of two files, counted by the delete dialog;
  `d` trashing, with the file found in
  `~/.local/share/Trash/files`; `D` deleting permanently,
  with the file in no folder and no trash (t10).
- Filter (`f`, "notes") narrowing the listing and Esc
  restoring it; Find (`/`, "ph") jumping the hover; the `~`
  help listing, quoted for the q / Q / Ctrl-C entries (t11).
- Tabs: `t` is a prefix key whose menu offers tab creation;
  `t` then `t` opened a second tab, which was walked into a
  different folder and quit from, while the first tab never
  moved. With `--cwd-file`, the file Yazi wrote on exit held
  the second tab's folder — and an earlier, mistimed run of
  the same session proved the path is resolved at exit time,
  not at launch (t12).
- Configuration, in a redirected `XDG_CONFIG_HOME`: a
  `yazi.toml` with `show_hidden = true` and
  `linemode = "size"` changed the listing in exactly those
  two ways on screen; a `keymap.toml` entry added a
  `g`-prefix menu item under its own description and, when
  pressed, ran its shell command — the touched file was
  confirmed with `ls -la` (t05, t13).
- A deliberately broken `yazi.toml` (`show_hidden = tru`)
  produced the verbatim full-screen parse error — file, line,
  column, caret, expected value — and the offer to continue
  with preset settings (t14).
- Packages over the real network with the real `ya pkg`:
  the `catppuccin-mocha` flavour installed, listed, recorded
  in `package.toml` with its revision and hash, chosen in
  `theme.toml`, and reported as loaded by `ya env` (t06,
  t07; the git clone progress lines in t06 are collapsed
  behind a marked omission). The `full-border` plugin
  installed, listed, switched on with one `init.lua` line,
  and its pane borders visible on screen (t08, t15).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Image previews and every other graphics-protocol preview:
  the lab's pseudo-terminal speaks none of them (`ya env`
  reports the protocols absent and a character-block adapter
  as the fallback). PDF, video and archive previews through
  helper programs are likewise documented, not run.
- The flavour's actual colours: the lab's screens are text
  renderings, so the guide verifies the flavour is loaded
  and offers no judgement of how it looks.
- Search by name and content (`s`, `S`), jump integrations
  (fzf, zoxide), bulk rename, the open-with menu, tab
  switching and closing keys, mouse use, sorting changes and
  the remaining `yazi.toml` options, the shell wrapper
  function in chapter 11 (its `--cwd-file` mechanism is the
  verified half), DDS messaging between instances via
  `ya pub` / `ya sub` / `ya emit`, virtual filesystems, and
  Yazi on Windows and macOS.
- Speed: no benchmark was run. Responsiveness claims in the
  text are attributed to the documented asynchronous design,
  not presented as measurements.
- The neighbour tools of chapter 12 (ranger, lf, nnn,
  Midnight Commander) — characterised, not run or benchmarked.

Fixtures are this guide's own and deliberately generic: a
garden diary, a letter about seedlings, a shopping list, soup
and bread recipes, a small budget — no names, organisations or
real events. Paths in the transcripts are the lab sandbox's
own working folders, kept unedited because the transcripts are
evidence; nothing in them is a reader's or author's real
machine.
