# Installing Yazi

**Outcome: `yazi` and `ya` are on your
path, and you have seen each one prove it
runs.**
Check: in a real terminal window, run
`yazi --version` and `ya env`. The first
prints the version block (the lab's is
transcript t00); the second prints the
configuration report from chapter 2. The
words *in a real terminal* are load-
bearing, for reasons this chapter ends
with.

## The release archive

The route this guide's lab took, and the
one it can vouch for:

1. From the Yazi project's GitHub releases
   page, download the archive for your
   machine — the lab's was
   `yazi-x86_64-unknown-linux-gnu.zip`
   (about 14 MB) for Yazi **26.9.1**.
2. Unzip it. Inside a single folder you
   get the two programs, `yazi` and `ya`,
   plus shell completion files.
3. Put both programs somewhere on your
   `PATH` (the lab used its own `bin`
   folder) and make sure they are
   executable.

There is nothing else to install: no
service, no runtime, no configuration
wizard. Package managers for most systems
also carry Yazi — the project documents
them — but the lab used the archive, so
the archive is what this guide teaches.

Shell completions for bash, zsh, fish and
friends are in the archive if you want
them; they complete file paths and
options for the `yazi` and `ya` commands,
and are a nicety, not a requirement.

## The font question

Yazi draws file-type icons from a **Nerd
Font** — a font family patched with extra
symbols. With one, the listings in this
guide's transcripts show a little picture
beside every name. Without one, the same
listings show boxes or blanks where the
pictures belong. Nothing else changes:
the names, the keys and the behaviour are
identical. If the boxes annoy you, any
Nerd Font in your terminal's settings
fixes them; chapter 14 lists this under
its own heading so you can find it when
it happens to you.

## The terminal is not optional

Here is the strange part, and the lab has
the receipt (transcript t16). Run
`yazi --help` with no terminal attached —
pipe it to a file, say — and Yazi refuses:

```text
Error: Inappropriate ioctl for device (os error 25)
```

*ioctl* is the operating system's word
for asking a device questions, and Yazi
begins by asking your terminal what it
can do: its size, its graphics protocols,
its colours. No terminal, no answers, no
start — not even for `--help` or
`--version`-style questions. `--version`
itself is the one exception the lab
found: it prints happily anywhere.

The practical lesson is small but worth
having early: Yazi belongs in an
interactive terminal window. Scripts that
call it must give it one (the lab's robot
used a pseudo-terminal, which chapter 7
explains), and if you ever meet that
error, you now know it means "no terminal
here", not "Yazi is broken".

## What `yazi --debug` became

Older guides — and older Yazi versions —
had a `yazi --debug` flag printing a
report about your setup. In 26.9.1 that
flag is gone: the command answers
"unexpected argument '--debug'". The
report itself moved to the companion
program: **`ya env`** prints it now,
config paths, terminal probe and all.
Transcript t02 keeps both halves of that
story, the refusal and the report, side
by side. Chapter 14 returns to this when
an old forum answer sends you looking for
the flag.
