# The neighbours

**Outcome: you can place Yazi among the
other terminal file managers, and say in
one sentence what each would give you
that Yazi does not, and the reverse.**
Check: nothing to run. This chapter is
characterisation from each project's own
documentation — none of the neighbours
was installed in the lab, and none is
benchmarked or ranked on speed here.

**ranger** is the elder of this family,
written in Python, and the source of the
three-pane layout Yazi wears — parent,
current, preview was ranger's idea first.
It is slower, endlessly configurable in
Python itself, and its preview tradition
runs through external tools. If you
already live in ranger, Yazi reads as
the same room rebuilt with faster
materials.

**lf** (list files) is a single small
binary in Go, deliberately minimal: one
pane by default, no previews until you
wire a previewer yourself, configuration
as plain commands. It is the choice for
someone who wants the smallest possible
thing and enjoys assembling the rest.

**nnn** is smaller still — a tiny C
program, famously fast, with its features
deliberately pushed out into a plugin
ecosystem of shell scripts. Where Yazi
builds previews and panes in, nnn builds
almost nothing in, and its devotees
consider that the point.

**Midnight Commander** (`mc`) is the
classic two-pane manager in the Norton
Commander tradition, older than most of
its users' careers, with menus, a mouse
it is happy to use, built-in viewer and
editor, and network filesystems. It is
the least keyboard-arcane of the group
and the one your muscle memory may
already know from other systems.

**The plain shell, honestly considered,**
is the neighbour everyone already has:
`cd`, `ls`, `cp`, `mv`, plus this series'
own companions — `fzf` for finding,
`eza` for listings, `bat` for looking at
files, and the *Finding Files* guide for
searching properly. Yazi's case against
it is not capability but friction: the
preview pane and the hover replace a
steady drizzle of small commands, and
the trash-backed delete is kinder than
`rm`. If your folder work is rare and
simple, the shell you have is a perfectly
defensible answer, and this guide's
existence is not an argument otherwise.

What Yazi gives back against the whole
street: the preview-first layout with a
modern terminal's graphics when the
terminal offers them, the asynchronous
design that keeps big folders responsive,
one configuration folder with readable
files, and a package system for its
add-ons. What it asks in return is a
real terminal, a Nerd Font if you want
the icons, and a little unlearning if
your fingers expect a mouse.
