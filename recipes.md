# Recipes

**Outcome: three useful arrangements,
each built only from parts this guide
has already proven.**
Check: each recipe names its proof. Where
a step is the project's documented form
rather than the lab's run, the recipe
says so rather than borrow the lab's
authority.

## Make your shell follow you out

The everyday frustration of terminal file
managers: you browse deep into a tree,
quit — and your shell is still standing
where you launched it. Yazi's answer is
the `--cwd-file` option from chapter 3:
give it a path, and on quitting with `q`
it writes the folder you ended in to that
file. The lab verified the mechanism
directly — quit from a second tab and
the file held that tab's folder
(transcript t12).

The wrapper that turns the mechanism
into a habit is a small shell function,
the one the project itself documents
(this exact function is documented, not
lab-run; the half it depends on is the
half the lab proved):

```bash
function y() {
  local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
  yazi "$@" --cwd-file="$tmp"
  if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
    builtin cd -- "$cwd"
  fi
  rm -f -- "$tmp"
}
```

Start it with `y` instead of `yazi`, and
when you quit, your shell has quietly
moved to wherever you were browsing.
Quit with `Q` and it has not — which is
exactly what `Q` is for.

## Tidy a folder in one pass

For the classic downloads-folder mess,
using only chapter 5 and 6 keys:

1. Open the folder and press `.` if the
   mess includes hidden files.
2. Press `f`, type the fragment the
   keepers share (say, `invoice`), Enter.
3. `Space`-select each entry that goes,
   watching the count your next dialog
   will report.
4. Press `d`, read the dialog's count
   against your own, confirm.
5. `Esc` to drop the filter, and repeat
   for the next fragment.

Everything lands in the trash, so a
mistake is a restore, not a loss. The
lab's dialog counts (1 file, then 2
selected files) are the habit to copy:
the count is the program telling you
what it is about to do, and it takes one
second to check it agrees with you.

## Open a handful of files at once

Select several files with `Space`, then
press `o`. Each is handed to its opener —
in practice, your editor opens them all,
as buffers or tabs depending on the
editor. The lab proved the single-file
handoff with its logging stand-in editor
(t10); the multi-file version is the
same action aimed at a selection, and
behaves the way the opener treats a list
of paths. It is the fastest route from
"these five logs" to reading them side
by side.

## A standing practice folder

If the keys are new, make a practice
folder — a handful of text files and a
subfolder, all invented, like the lab's
`ops` folder — and run chapter 6's whole
session in it: create, mis-rename,
rename properly, copy, cut, trash,
delete. Ten minutes of breaking things
that do not matter buys you the one
thing that does matter in a real folder:
having already seen every dialog before
it counts.
