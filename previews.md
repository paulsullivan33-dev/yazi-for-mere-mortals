# Previews

**Outcome: you know what the right-hand
pane can show for the files you actually
have, which of those the lab proved, and
where the boundary sits between Yazi's
ability and your terminal's.**
Check: hover three things in any folder —
a subfolder, a plain text file, and an
empty file — and match the pane against
the first section below. All three are
transcript evidence, not promises.

## What the lab saw

The preview pane reacts to the hovered
entry, and in the lab's transcripts it
did these things, repeatedly and on cue:

- **A folder** previews as its own
  listing — names and icons, the same
  view the middle pane would give you if
  you stepped in (t09, first screen).
- **A text file** previews as its text,
  line-wrapped to the pane. A diary page,
  a letter, a CSV file — the CSV showed
  its rows (`row,length` / `1,12` /
  `2,9`) plainly enough to read the data
  off the screen (t09, t10).
- **An empty file** says "Empty file".
  **An empty folder** says "No items".
  Small sentences, but they mean you are
  never left guessing whether the pane
  failed or the thing is genuinely empty.

Which previewer handles a file is decided
from what the file *is* — its media type,
checked with the system `file` machinery
— not merely from its name, so a text
file wearing the wrong extension still
previews as text.

## Where the terminal draws the line

An image cannot be drawn in characters
the way text can. For pictures, Yazi
speaks one of the terminal graphics
protocols — Kitty's graphics protocol,
sixel, iTerm2's inline images — and the
*terminal* paints the pixels inside the
pane. Whether you get image previews is
therefore a question about your terminal
first and Yazi second. Modern terminals
mostly can; a plain or old one cannot,
and Yazi falls back to what it can do,
down to rendering images as coloured
character blocks with the Chafa tool
(which is the adapter `ya env` reported
on the lab's bare pseudo-terminal, where
it also reported the graphics protocols
as absent — t02).

The lab's pseudo-terminal speaks no
graphics protocol at all, so **image
previews are documented-only in this
guide**: described from the project's
documentation, never shown, and never
claimed as tested. The same applies to
the richer previews Yazi offers through
helper programs — PDF pages and video
thumbnails via external tools, archive
listings via an archiver. They are real
features; they are simply not this lab's
evidence, and the text treats them that
way.

## Tuning the pane

Two settings from chapter 9's file are
worth knowing exist even if you never
touch them: the pane ratio between the
three columns can be changed (the default
gives the preview roughly half the
width), and previews of very large files
are capped by size so that hovering a
huge log does not stall your browsing.
Both live in `yazi.toml`, documented in
the project's configuration reference;
the lab left them at their defaults.
