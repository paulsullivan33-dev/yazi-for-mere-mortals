# The moving parts

**Outcome: you can name the two programs
in the box, find the folder where all of
Yazi's settings live, and say which jobs
Yazi hands to outside helpers.**
Check: after installing (next chapter),
run `ya env`. Its Config section lists
every file Yazi looks for, with "No such
file" beside the ones you have not made
yet — the lab's printout is transcript
t02, and t05 shows the same list once two
of the files exist.

Installing Yazi gives you **two**
programs, and knowing which is which
clears up most early confusion:

- **`yazi`** — the file manager itself:
  the full-screen interface you type at.
- **`ya`** — a command-line companion.
  It talks to a running `yazi` (sending it
  commands, asking it questions) and it
  manages Yazi's add-on packages. You
  will meet it in chapter 10 as
  `ya pkg ...`, and whenever this guide
  needs a fact about your setup, as
  `ya env`.

**The configuration folder** holds
everything you can change. By default it
is `~/.config/yazi/`, and `ya env` will
confirm the exact paths on your machine.
The files, none of which exist until you
create them:

- `yazi.toml` — behaviour: sorting, what
  is shown, how previews run.
- `keymap.toml` — what the keys do.
- `theme.toml` — colours and icons,
  including which *flavour* (a ready-made
  colour scheme) to use.
- `init.lua` — a small Lua program Yazi
  runs at startup; this is where plugins
  are switched on.
- `package.toml` — the list of installed
  plugins and flavours. You never edit
  this one by hand; `ya pkg` writes it.
- `vfs.toml` — virtual filesystems, for
  remote and archived locations. This
  guide does not use it.

**State and logs** live separately, under
the XDG state folder (typically
`~/.local/state/yazi/`). Set the
environment variable `YAZI_LOG` to a
level such as `debug` and Yazi writes a
log file there — chapter 14 points at it
when something misbehaves.

**Borrowed tools.** Yazi does some jobs
by calling programs you may already have:
the system `file` command to identify
what it is previewing, and — when you
install them — `fd` for name searches,
`ripgrep` for searching inside files,
`fzf` and `zoxide` for jumping, and
`ffmpeg`, ImageMagick and archive tools
for richer previews. None of that is
required for the core of this guide: the
lab's Yazi ran with none of them
installed, and everything in chapters 4
to 7 worked anyway. Where a feature
needs a helper, the text says so.

**The trash.** Deleting inside Yazi is
not an immediate shredding: the ordinary
delete key moves files to your desktop
trash folder (on Linux, the freedesktop
trash under `~/.local/share/Trash`),
from which they can be recovered.
Chapter 6 proves that with `ls`, and
shows the separate, sterner key that
deletes for real. This is a safety
property worth knowing before your first
session, not after.
