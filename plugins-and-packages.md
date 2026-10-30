# Plugins and packages

**Outcome: you can install a ready-made
colour scheme and a plugin from Yazi's
own package system, see where they are
recorded, and switch a plugin on — with
proof at each step, including one effect
visible on the screen itself.**
Check: `ya pkg list` prints what you have
installed, split into Plugins and
Flavors. The lab's lists are transcripts
t06 and t08.

## The package manager in `ya`

Yazi's add-ons — **plugins** (Lua code
that changes behaviour) and **flavours**
(colour schemes, spelled the project's
way) — are distributed as Git
repositories and managed by the companion
program. In Yazi 26 the subcommand is
**`ya pkg`**; older versions and older
write-ups call it `ya pack`, and chapter
14 notes the rename in case an old answer
sends you to the wrong word.

Installing takes one line:

```text
ya pkg add yazi-rs/flavors:catppuccin-mocha
```

Underneath, `ya` clones the repository,
deploys the package into place, and
records it in `package.toml` — the file
from chapter 2 that you never edit by
hand. After the lab's install, that file
held the scheme's name, the exact
revision, and a hash:

```toml
[[flavor.deps]]
use = "yazi-rs/flavors:catppuccin-mocha"
rev = "1183892"
hash = "ce320f877fe709b189433941aba747c4"
```

Naming the revision is what makes this
more than a download: everyone reading
that file can fetch exactly the same
code. `ya pkg list` then shows the
scheme under **Flavors**, and the clone
itself is cached under
`~/.cache/yazi/packages/` if you ever go
looking for it.

## Using a flavour

Installing a scheme does not apply it.
`theme.toml` chooses:

```toml
[flavor]
dark = "catppuccin-mocha"
```

The check is `ya env` again: its Config
section gains a line the lab captured —
`Dark/light flavor` naming
`catppuccin-mocha` as loaded (transcript
t07). What the lab cannot honestly add
is an opinion about the colours: its
screens are text renderings, and the
guide leaves the judging of Mocha versus
any other scheme to your eyes, in your
terminal.

## A plugin, switched on and seen

Plugins install the same way:

```text
ya pkg add yazi-rs/plugins:full-border
```

— and then need one line in `init.lua`,
the startup file from chapter 2, to
switch them on:

```lua
require("full-border"):setup()
```

This plugin's job is small and visible:
it draws a complete box border around
each pane, where the standard layout
uses plain dividers. Transcript t15 is
the same folder as transcript t09 with
the plugin on, and the borders are
simply there. Small as it is, it proves
the whole chain — install, record, load,
run — with your eyes instead of a log
file, which is why the lab chose it.

Each plugin documents its own
`require(...)` line and options; that
line, and not the install, is what makes
a plugin part of your Yazi.

## The trust rule

A plugin is someone else's Lua code
running inside your file manager, with
your permissions, on your files. The
collection under the `yazi-rs`
organisation is the project's own and is
the natural place to start — both
packages in this chapter come from it.
For anything from elsewhere, the rule is
the one you already met for keymap shell
commands: read it before you run it, or
do not run it. `ya pkg` will fetch
whatever it is pointed at; deciding
whether it should is the part that stays
yours.
