# Moving around

**Outcome: you can walk a folder tree
without thinking about the keys, open a
second tab, and narrow a long listing
down to the file you want in two
different ways.**
Check: the lab's route through this
chapter is transcripts t09, t11 and t12.
Repeat any of them in a folder of your
own and watch the status bar's fraction
change as you move.

## The four walking keys

Everything else is commentary on these:

- `j` / `k` — hover down / up one entry.
- `l` — enter the hovered folder (on a
  file, it opens it — chapter 6).
- `h` — go back to the parent folder.

Add `gg` for the top of the list and `G`
for the bottom, and ordinary folders are
fully covered. The lab's transcript t09
is exactly this: two `j`s to reach
`photos`, `l` in, `h` back out, `G` to
`notes.txt`, `q` to leave — with the
preview pane following every step.

## Prefix keys and their little menus

Some keys do not act at once; they open a
small menu near the bottom of the screen
listing what the *next* key can mean,
then wait. `g` is the one you will use
most — the lab photographed its menu
twice (t12, t13):

- `g` `g` — top of the list
- `g` `h` — your home folder
- `g` `c` — your configuration folder
- `g` `d` — your downloads folder
- `g` `t` — the trash bin itself

The menu is a kindness worth noticing:
you do not have to memorise the second
key, because the program shows you the
choices at the moment you need them.
Chapter 9 adds a row of the lab's own to
that menu.

## Tabs

A tab is a second Yazi inside the first:
same window, its own folder, its own
hover. `t` is another prefix key — press
it and the menu offers, among others,
`t` (create a new tab in the current
folder) and `r` (rename the current tab).
The lab opened a second tab, walked it
into a different folder, and quit; the
first tab had never moved (transcript
t12). Tabs are how you keep a "home base"
folder open while you go digging
somewhere else, and chapter 11's shell
trick reads its final folder from
whichever tab is active when you quit.
Switching between tabs and closing them
are listed by the help key below; the
lab's sessions did not need them.

## Narrowing a listing

Two tools, two different questions:

- **Filter** (`f`) — "show me only the
  entries matching this text." Type a
  fragment, press Enter, and the list
  shrinks to matches; the header wears
  `(filter: notes)` while it lasts, and
  `Esc` brings the full list back. The
  lab filtered a five-entry folder down
  to the one file containing "notes"
  (transcript t11).
- **Find** (`/`) — "jump my hover to the
  entry matching this text." The list
  stays whole; the hover moves. Type
  `ph`, and you are standing on `photos`.
  Enter confirms; `n` and `N` walk to the
  next and previous matches.

Filter when the folder is big and the
target is a kind of thing; find when the
folder is small and the target is one
name.

## The help key, and leaving

Press `~` at any time for a scrollable
list of every keybinding — the lab's
photograph of it (t11) is where several
facts in this chapter were checked,
including the two exits:

- `q` — quit, writing your final folder
  to the cwd file if Yazi was given one
  (chapter 11 lives on this).
- `Q` — quit *without* writing it.

And `Ctrl-C`, which the help describes as
"close the current tab, or quit if it's
last" — inside a prompt or dialog it
also serves as the cancel key, which is
how the lab backed out of every dialog
it photographed.
