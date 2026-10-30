# Working with files

**Outcome: you can create, rename, copy,
move, select, open, trash and truly
delete files from the keyboard — and you
know how each result was verified, so you
can verify your own.**
Check: this chapter's whole session is
transcript t10. Every operation below
ends with the check the lab ran
afterwards; do the same in a practice
folder of your own before trusting the
keys in a real one.

The stage: a folder holding an empty
folder `archive`, and three files —
`draft-letter.txt`, `measurements.csv`,
`old-notes.txt`.

## Creating

Press `a`. A prompt appears: `Create:`.
Type a name and press Enter, and the
entry exists, hovered, ready to open.
End the name with a slash —
`new-folder/` — and you get a folder
instead of a file. *Check:* the lab's
listing and `ls` both showed the new
entries (`shopping-list.txt`, then
`new-folder`) the moment the prompts
closed.

## Opening

Hover a file and press `o` (or Enter, or
`l`). Yazi hands the file to the program
registered for its kind — for text, your
`$EDITOR`. The lab could not run a real
editor session, so it cheated honestly:
it pointed `EDITOR` at a three-line
script that only writes its arguments to
a log. The log afterwards read:

```text
editor called with: /home/hatch/workspace/yazi-labwork/ops/draft-letter.txt
```

That one line is the proof that opening
works and that the full path is what the
editor receives. On your machine the same
action simply opens your editor.

## Renaming, and the extension trap

Press `r`. The rename prompt opens
pre-filled with the current name — with
the cursor resting **just before the
extension**. That placement is a
deliberate kindness (most renames keep
the extension) and a trap if you do not
know it: the lab's first attempt cleared
the name with backspaces, typed a full
new name *including* `.txt`, and produced
`letter-to-sam.txt.txt`. The prompt had
kept the extension standing the whole
time. Type only the new stem —
`letter-to-sam` — and the result is the
`letter-to-sam.txt` you meant.
*Check:* the listing shows the new name
and `ls` agrees.

## Copying, cutting, pasting

The clipboard keys are the ones your
fingers may expect, minus the Ctrl:

- `y` — copy ("yank") the hovered entry.
- `x` — cut it.
- `p` — paste what you last yanked or
  cut, here.

Paste a copy into the folder it already
lives in and Yazi makes a sibling with a
numbered suffix: `draft-letter.txt`
becomes `draft-letter_1.txt`, and a
copied folder `archive` becomes
`archive_1`. Paste a cut somewhere else
and the file simply moves — the lab cut
`measurements.csv`, stepped into
`archive`, pasted, and found it there,
its contents already showing in the
preview pane. *Check:* `ls` in both
folders; a cut file is gone from the
first and present in the second.

## Selecting several

Tap `Space` on an entry to select it,
move, tap `Space` again on another.
Selected entries are the target of the
next operation, however many there are.
The proof in the lab is indirect and
therefore trustworthy: with two files
selected, the delete dialog asked about
**2** selected files (transcript t10).
Build the habit: select first, act once,
rather than acting entry by entry.

## Deleting: two keys, two meanings

This distinction matters, so the guide
puts it in a heading of its own.

- `d` — **trash.** A dialog names the
  file (or counts the selection) and asks
  before anything happens. Confirm, and
  the file leaves the folder — but it is
  not gone. It is sitting in the desktop
  trash, recoverable like anything else
  you have ever thrown away from a
  graphical file manager. The lab
  confirmed it where it counts:
  `ls ~/.local/share/Trash/files` listed
  the very `old-notes.txt` the dialog had
  named.
- `D` (capital) — **delete permanently.**
  Its dialog says so in words —
  "Permanently delete 1 selected file?" —
  and it means them. After the lab used
  it, the file was in no folder and in no
  trash. There is no third place it could
  be.

The rule of thumb writes itself: `d` for
everyday tidying, because regret is
common and trash is cheap; `D` only when
you would happily say the same sentence
out loud — *this should not exist
anywhere, including the bin.*
