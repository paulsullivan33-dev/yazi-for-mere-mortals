# Troubleshooting

**Outcome: the failures this guide met —
and the ones its readers most predictably
will — each matched to its cause and its
check.**
Check: every entry below either quotes a
transcript in `yazi-lab/transcripts/` or
names the command that settles it.

## "Error: Inappropriate ioctl for device"

**Cause:** Yazi was started with no
terminal attached — piped, redirected, or
launched by a script that gave it none.
It asks the terminal questions before
anything else, `--help` included
(transcript t16).
**Fix:** run it in an interactive
terminal window. If a script must drive
it, the script owes it a pseudo-terminal,
which is what the lab's `ptyrun.py`
does.

## Yazi opened, but all my settings are gone

**Cause:** almost always, a configuration
file it cannot parse. Yazi then starts on
its built-in presets — after showing a
full-screen error naming the file, the
line, and the column (transcript t14).
If you blinked past that screen, the
symptom is exactly this one.
**Check:** `ya env`. It lists each
configuration file as found or missing —
but a *found* file can still be the
broken one. Reproduce the error by
starting Yazi and reading the first
screen slowly, then fix the named line.

## The icons are little boxes

**Cause:** your terminal's font is not a
Nerd Font, so the glyphs Yazi draws have
no pictures to draw with.
**Fix:** set a Nerd Font in your
terminal's own settings. Nothing inside
Yazi changes, and nothing else is broken
— names and behaviour are identical with
or without the pictures.

## A key does not do what a guide said

**Cause:** usually one of two things.
The write-up is for another version —
this guide watched `t` turn out to be a
prefix key with a menu, not a one-press
tab button, and watched `--debug` and
`ya pack` retire within the project's
recent history. Or your own `keymap.toml`
has a binding in front of the built-in
one.
**Check:** press the key and read the
little menu if one appears; press `~`
for your build's own binding list; and
read your keymap file before blaming the
program.

## The preview pane is empty or useless for this file

**Cause:** three ordinary possibilities.
The thing is genuinely empty — the pane
says "Empty file" or "No items", and it
is telling the truth. The file's kind
needs a graphics protocol your terminal
does not speak (images, chapter 8). Or
the preview needs an outside helper —
an archiver, a thumbnailer — that is not
installed.
**Check:** `file <name>` in the same
folder tells you what the file is, which
decides which of the three you are
looking at.

## Delete did not free any space

**Cause:** `d` trashes; it does not
delete. The file moved to the desktop
trash, which lives on the same disk
(transcript t10 found it there with
`ls`).
**Fix:** empty the trash by your usual
desktop route — or, next time, use `D`
if you truly mean permanent, having read
its dialog as carefully as it was
written.

## Still stuck

Turn on the log: set `YAZI_LOG=debug`,
start Yazi again, and read the newest
log under the state folder `ya env`
points you towards (`~/.local/state/
yazi/` by default). Then `ya env`'s full
report — version, configuration paths,
terminal probe — is the page to have in
front of you, or to attach, when you go
looking for help.
