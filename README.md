# Yazi for Mere Mortals

Most file managers live in a window of
their own: you leave the terminal, click
through folders with a mouse, and come
back when you are done. **Yazi** does the
same job without the leaving. It is a file
manager that runs *in* the terminal,
shows you three folders' worth of truth
at once — the folder above, the folder
you are in, and a preview of whatever you
are pointing at — and moves at the speed
of your keyboard. No account, no mouse
required, and nothing about your files
leaves the machine.

This guide explains how Yazi lays out the
screen, how to install it, and how to do
the everyday work: looking, moving,
copying, renaming, deleting, and opening.
Then it does something most tool guides
skip: it **proves** the program did what
it claims. The lab that wrote this guide
had no terminal of its own to type at —
so it drove the real Yazi through a
pseudo-terminal with a small robot,
pressed the actual keys, photographed
the screen, and then checked on disk
with plain shell commands that every
file operation had really happened.
A screenshot can be staged. A trash
folder with the file in it cannot.

The lab behind this guide ran the real
thing: **Yazi 26.9.1**, the official
release build, on a small Linux machine.
Against it the lab navigated a planted
folder tree, read text previews off the
screen, created, renamed, cut, copied and
trashed files — checking each result with
`ls` afterwards — ran two tabs at once,
filtered and searched a listing, changed
the configuration and watched the listing
change, broke the configuration and read
the error, and installed a colour scheme
and a plugin from the project's own
package system, including the plugin's
visible effect on the screen.

What the lab could not do, it did not
fake. Its pseudo-terminal speaks no
graphics protocol, so it cannot show you
an image preview the way a modern
terminal can — that whole family of
previews is taught from the documentation
and labelled as such wherever it appears.
The lab also never benchmarked Yazi's
famous speed: it reports what the design
does — work happens off the drawing
thread, so listings stay responsive —
and leaves stopwatches to you.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What Yazi is**](what-yazi-is.md) —
  the mental model: three panes, one
  keyboard, and a preview that answers
  "what is this?" before you open it
- [**The moving parts**](the-moving-parts.md) —
  the two programs you install, the
  configuration folder and its files,
  and the helper tools Yazi borrows
- [**Installing Yazi**](installing-yazi.md) —
  the release download, what is inside
  it, and the strange error you get when
  there is no terminal
- [**Your first look**](your-first-look.md) —
  reading the screen: header, three
  panes, the status bar, and why the
  count never matches `ls`
- [**Moving around**](moving-around.md) —
  the movement keys, prefix keys that
  open little menus, tabs, filter, and
  find
- [**Working with files**](working-with-files.md) —
  creating, renaming (mind the
  extension), copying, cutting, trashing
  and deleting for real, each checked
- [**Proving it worked**](proving-it-worked.md) —
  how this guide knows any of it
  happened: the robot, the rendered
  screens, and the disk checks that
  outrank them
- [**Previews**](previews.md) — what the
  third pane can show for folders, text
  and everything else, and where the
  terminal itself draws the line
- [**Making it yours**](making-it-yours.md) —
  the plain-text configuration files,
  two settings changed and proven, and
  what a typo does
- [**Plugins and packages**](plugins-and-packages.md) —
  `ya pkg`, colour schemes called
  flavours, Lua plugins, and one plugin
  whose effect you can see
- [**Recipes**](recipes.md) — make your
  shell follow Yazi out the door, tidy a
  folder in one pass, and open a handful
  of files at once
- [**The neighbours**](the-neighbours.md) —
  ranger, lf, nnn, Midnight Commander,
  and the plain shell: what each does
  that Yazi doesn't, and vice versa
- [**Limits**](limits.md) — a real
  terminal or nothing, previews that
  depend on your terminal's graphics,
  names that changed between versions,
  and third-party plugins to read before
  you run
- [**Troubleshooting**](troubleshooting.md) —
  the ioctl error, the full-screen config
  complaint, boxes instead of icons, and
  the keys that are not where older
  guides say they are
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Scripting Yazi as a platform — writing
your own Lua plugins is a project with
its own documentation; this guide
installs and runs other people's, and
reads one before trusting it. The remote
and virtual-filesystem features, and
Yazi on Windows and macOS, are pointed
at, not taught: the lab ran on Linux,
and says so. Turning Yazi into your
only file interface inside other
programs (editors, shells' completion)
is likewise pointed at, not covered.

## How to use this guide

Read chapter 1 for the model, and
chapter 2 before installing anything —
knowing which file holds what turns
later confusion into a named problem.
Chapters 3 and 4 get you a running
program and the ability to read its
screen; chapter 5 puts your hands on
the keys, and chapter 6 does real work
with them. Chapter 7 is the one to read
slowly even if you trust the program:
its habits — check the disk, not the
screen — are how you catch a file
operation that quietly did something
else. The lab's transcripts live in
`yazi-lab/transcripts/`; its driving
robot is `yazi-lab/ptyrun.py` and the
keystroke scripts it followed are the
`.scn` files beside it.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Finding Files for Mere Mortals](https://paulsullivan33-dev.github.io/finding-files-for-mere-mortals/)
- [Bash for Mere Mortals](https://paulsullivan33-dev.github.io/bash-for-mere-mortals/)
- [tmux for Mere Mortals](https://paulsullivan33-dev.github.io/tmux-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/yazi-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/yazi-for-mere-mortals/blob/main/LICENSE-CODE).
