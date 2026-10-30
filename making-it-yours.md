# Making it yours

**Outcome: you can change how Yazi
behaves by editing a plain-text file, you
have seen two changes take effect and a
third one fail safely, and you know how
to prove Yazi read your file at all.**
Check: after any edit, run `ya env`. Its
Config section names your file with its
size in characters beside it, instead of
"No such file" (transcript t05). If it
still says "No such file", you are
editing a file Yazi is not reading, and
the rest of this chapter will wait while
you find the right one.

## Where the files live

Everything sits in one folder —
`~/.config/yazi/` by default, and
`ya env` will tell you if yours is
elsewhere. You create the files yourself;
until you do, Yazi runs on its built-in
presets. Chapter 2 lists the full set.
This chapter works with two of them:

- `yazi.toml` — behaviour and display.
- `keymap.toml` — the keys.

## Two changes, proven

The lab's `yazi.toml` for this chapter
was four lines:

```toml
[mgr]
show_hidden = true
linemode = "size"
```

(`[mgr]` is the section that holds the
manager's settings — the pane this whole
guide has been looking at.) Restart Yazi
and the listing tells on itself, as
transcript t13's screen shows: the
hidden `.hidden-note.txt` is simply
*there*, and every row now carries its
size at the right edge, because
`linemode` decides what extra fact each
row wears — here, sizes; folders report
their item count instead. Set it back,
restart, and both changes are gone. That
restart-and-compare loop is the whole
method of this chapter: change one thing,
look, decide.

Other settings in the same file follow
the same pattern — the sort order and
direction, whether folders sort first,
the pane ratios from chapter 8, scroll
margins. The project's configuration
reference lists them all; the lab
verified the two above and presents the
rest as documented options, not results.

## A key of your own

`keymap.toml` can add bindings in front
of the built-in ones. The lab added a
two-key command behind the `g` prefix:

```toml
[[mgr.prepend_keymap]]
on = ["g", "x"]
run = 'shell "touch /home/hatch/workspace/yazi-labwork/keymap-proof.txt"'
desc = "Touch the proof file"
```

Three things happened, all checkable.
The `g` menu grew a line — "x → Touch
the proof file" — listed under the
description the lab gave it, among the
built-in entries (transcript t13).
Pressing `g` then `x` ran the shell
command. And the shell itself confirmed
the result: a brand-new, empty
`keymap-proof.txt` with that minute's
timestamp. Read the shape of the entry
and you can write your own: `on` is the
key sequence, `run` is the action —
Yazi's own actions, or a shell command —
and `desc` is what the menu will call it.
The absolute path in the command is the
lab's, kept so the transcript's `ls`
points at a real file; yours would name
your own folder.

A warning that belongs with the power:
a keymap `shell` binding runs its command
with your full permissions, the moment
the keys are pressed, with no further
asking. Write these entries yourself, or
read every line of anyone else's before
it goes in the file — the same rule
chapter 10 applies to plugins.

## When you make a typo

The lab's last experiment in this chapter
was breaking the file on purpose:
`show_hidden = tru`. Yazi refused to
start on it — and the refusal is the
instructive part (transcript t14,
verbatim):

```text
Failed to parse config ".../yazi.toml"
Caused by:
TOML parse error at line 2, column 15
  |
2 | show_hidden = tru
  |               ^^^
invalid boolean, expected `true`
Press any key to continue with preset settings...
```

File, line, column, the offending text
underlined, the expected value named —
and then the merciful part: press any key
and Yazi starts anyway, on its built-in
presets. A typo costs you your settings,
never the program. Two consequences worth
remembering: a Yazi that "lost all my
configuration" is usually a Yazi that
could not parse it, and the error screen
is the first place to look; and because
it starts on presets, a broken file can
hide for a while behind a working
program, with only your missing settings
as the clue.
