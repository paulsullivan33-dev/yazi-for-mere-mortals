# Your first look

**Outcome: you can read Yazi's screen —
the header, the three panes, and the
status bar — and explain why the entry
count is smaller than the number of files
`ls` would show you.**
Check: start `yazi` in any folder you
know well. Compare the middle pane's
count (bottom right of the screen, in the
form `1/5`) with `ls -A` in the same
folder. The difference is this chapter's
last section.

The lab's first screen is transcript t09,
and this chapter is a guided tour of it.

## The header

One line at the top: the full path of the
folder you are in. It changes as you
move, and it picks up annotations —
chapter 5 shows it wearing `(filter:
notes)` when a filter is active. When you
have more than one tab open, the tabs
live up here too.

## The three panes

**Left — the parent.** The folder that
contains yours, with yours highlighted.
It answers "where did I come from?" and
gives `h` somewhere visible to go.

**Middle — the current folder.** Its
entries, one per line, each with a small
icon. One entry is drawn highlighted end
to end: that is the **hovered** entry,
the target of almost every key you
press. By default the order is folders
first, then alphabetical — the lab's
playground shows `garden`, `kitchen`,
`photos`, then `budget.csv`, `notes.txt`.

**Right — the preview.** Whatever the
hovered entry *contains*. Hover a folder
and you see its listing. Hover a text
file and you see its text — in the lab's
first screen the diary entry is simply
there, unasked. Hover an empty folder
and the pane says so ("No items"); hover
an empty file and it says "Empty file".
Chapter 8 takes the preview pane apart.

## The status bar

The bottom line is dense and worth
learning once:

- **Mode**, at the far left: `NOR` for
  normal. Selecting and other states have
  their own labels.
- **The hovered entry's size** — a file's
  size in bytes, or a folder's total where
  Yazi shows one.
- **The hovered entry's name and its
  permissions**, in the familiar
  `drwxrwx---` style.
- **Position**: `Top`, `Bot`, or a
  percentage for how far down the list
  the hover sits, and the fraction —
  `1/5` means "first of five entries".

## The missing files

Five entries — but the playground folder
on disk holds six things. The sixth is
`.hidden-note.txt`, and Yazi does not
show it. Files whose names begin with a
dot are **hidden** by default, exactly as
`ls` hides them without `-a`. There are
two ways to see them, both proven in the
lab: press `.` to toggle them for the
session (transcript t10's addendum), or
set `show_hidden = true` in the
configuration to see them always
(chapter 9, transcript t13). Neither is
better; they answer different questions —
"just this once" and "on this machine,
always".
