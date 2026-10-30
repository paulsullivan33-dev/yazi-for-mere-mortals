# What Yazi is

**Outcome: you can say what Yazi is, what
its screen shows, and why someone would
choose it over a windowed file manager or
plain shell commands.**
Check: nothing to run yet — hold the three
panes in mind (parent, current, preview)
and test them against the first real
screen in chapter 4.

Yazi is a file manager that runs in a
terminal. You start it with one word,
`yazi`, and your terminal fills with a
view of your folders. You leave with one
key, `q`, and you are back at your shell
prompt, in the same place — or, with a
small wrapper your shell can use, in the
folder you browsed to (chapter 11 shows
that trick and what makes it work).

The screen is always the same three
panes, side by side:

- **Left: the parent folder** — where the
  folder you are in lives.
- **Middle: the current folder** — its
  entries listed, one of them *hovered*
  (highlighted). The hovered entry is the
  one your keys act on.
- **Right: a preview** — the contents of
  the hovered entry. A folder previews as
  its own listing. A text file previews
  as its text. Other files preview as
  whatever can be shown of them, which
  chapter 8 takes up.

That third pane is the idea at the centre
of the program. In a shell, finding out
what a file *is* costs a command: `cat`,
`file`, `head`. In Yazi the answer is
already on the screen, kept current as
you move. Half of file management is
really file *recognising*, and the
preview pane does that half for free.

Everything is driven from the keyboard.
One key moves, one key copies, one key
trashes. Some keys are *prefixes*: press
`g` and a small menu appears listing what
the next key can mean — go to the top,
go home, go to your downloads. The
program teaches you its own keys as you
go, and the `~` key opens a full list of
them. Chapter 5 is built on the subset
this guide's lab pressed for real.

Two design choices sit underneath.
First, Yazi is a single fast program
written in Rust, and it does its slow
work — reading big folders, building
previews — away from the drawing of the
screen, so the keys stay responsive.
This guide did not benchmark that; it is
the documented design, and the lab's
ordinary folders cannot test it anyway.
Second, almost everything about Yazi is
set in plain-text files you can read,
copy and version: what the keys do, what
the screen shows, which colours it uses.
Chapter 9 opens those files.

What Yazi is not: it is not a shell (it
runs inside one, and hands you back to
it), not an editor (it opens your editor
for you), and not a transfer tool (it
will not copy files to another machine —
that is a job for the tools in the
rclone and rsync guides of this series).
It manages the files on the machine it
runs on, from the terminal that is
already open.
