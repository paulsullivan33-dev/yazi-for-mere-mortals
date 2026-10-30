# Proving it worked

**Outcome: you understand how this guide
can claim, chapter after chapter, that a
key press did something — and you can
repeat the whole proof yourself with the
tools in the `yazi-lab` folder.**
Check: `yazi-lab/ptyrun.py` and the `.scn`
keystroke scripts are in this repository.
Point the robot at a folder of your own
and it will retake every photograph in
the guide.

Most software guides show you a
screenshot and say *this is what you will
see*. This guide's lab had a problem with
that approach: it has no terminal. It
runs in a sandbox with no interactive
screen at all, so it could not simply
open Yazi, type, and look. Anything it
claimed about Yazi's behaviour had to be
earned some other way.

The way it chose has three parts, and all
three are in the repository:

1. **A robot typist.** A small Python
   harness (`ptyrun.py`) opens a
   *pseudo-terminal* — the operating
   system's way of giving a program a
   terminal to talk to when no physical
   one exists — starts Yazi on it, and
   sends keystrokes from a script (the
   `.scn` files: `wait`, `send j`,
   `send l`, and so on). Yazi cannot tell
   the difference; as far as it knows, a
   person is typing slowly and
   predictably.
2. **A rendered screen.** What comes back
   down the pseudo-terminal is a stream of
   drawing instructions. The harness feeds
   them to `pyte`, a library that
   simulates a terminal screen, and saves
   what a person would have seen. Those
   renderings are the screens in
   transcripts t09 to t15.
3. **Disk checks that outrank the
   screens.** After every operation the
   lab left the terminal and asked the
   shell: `ls` the folder, read the
   editor's log, list the trash. The
   screen says the file was renamed; the
   disk is where renaming actually
   happens. Whenever the two could have
   disagreed, this guide would have
   believed the disk.

The method earned its keep twice, and
both times are still in the text. The
robot's first rename produced
`letter-to-sam.txt.txt` — the screen had
looked fine at every step, but the disk
check exposed the rename prompt's
extension behaviour that chapter 6 now
teaches. And the robot's first attempt
at the `--cwd-file` transcript quit from
a different folder than intended, which
the written file reported faithfully —
and which turned into chapter 5's
understanding of tabs, and the note in
transcript t12 about when the path is
resolved.

Two honest limits of the method. The
rendered screens show text and layout,
not colour: when chapter 10 installs a
colour scheme, the proof is that Yazi's
own report names it as loaded, not that
the lab saw the colours. And a
pseudo-terminal offers none of the
graphics protocols a real terminal has,
so image previews never happened here at
all — chapter 8 marks them documented-
only, because they are.

Read the transcripts the way the lab
wrote them: the screens are evidence of
what Yazi *showed*, and the shell
commands after each session are evidence
of what Yazi *did*. A guide that keeps
those two apart can be wrong, but it
cannot easily lie to you.
