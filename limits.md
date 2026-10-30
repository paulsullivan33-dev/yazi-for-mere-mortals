# Limits

**Outcome: you can name what Yazi cannot
do, what it will not do without help, and
which of its facts expire as versions
change — before any of them surprises
you.**
Check: the first limit below can be
reproduced in ten seconds — pipe
`yazi --help` into a file and read
transcript t16's error in your own
terminal's output.

- **A real terminal, or nothing.** Yazi
  interrogates the terminal before it
  does anything at all, and without one
  it stops with an ioctl error — `--help`
  included. It cannot be driven from a
  plain pipe, a cron job, or a script
  that does not give it a terminal (the
  lab's robot exists precisely because of
  this). SSH sessions and terminal
  multiplexers are fine; nothing-at-all
  is not.
- **Previews stop at your terminal's
  graphics.** Text and listings preview
  anywhere. Images need a graphics
  protocol your terminal must speak;
  PDFs, videos and archives lean on
  outside tools. A minimal terminal gets
  a minimal third pane, and no setting
  inside Yazi changes that.
- **Deleting is safe, not magical.** The
  trash is the desktop trash: it follows
  that system's rules, lives on the same
  disk, and protects you from accidents,
  not from disk failure or from `D`,
  which is permanent the moment it is
  confirmed. Yazi also works on the
  machine it runs on — it is not a
  backup, sync, or transfer tool.
- **Names change between versions.** This
  guide's own evidence caught two:
  `yazi --debug` is gone (the report is
  `ya env` now), and `ya pack` became
  `ya pkg`. Yazi is young and moving
  quickly; expect the occasional renamed
  door, and trust `ya env` and the `~`
  help — which describe *your* build —
  over any fixed text, including this
  guide's, when they disagree.
- **Add-ons are other people's code.**
  Plugins run inside the program with
  your permissions. The package system
  records exact revisions, which helps
  you know *what* you are running; it
  cannot tell you whether you should.
  That judgement — read first, or stay
  with the project's own collection — is
  a limit of the arrangement, not of
  your diligence.
- **The keyboard is the interface.** A
  mouse can click and scroll in Yazi, but
  everything this guide teaches assumes
  keys. If your workflow is
  mouse-centred, a windowed manager will
  fit it better, and chapter 12's
  neighbours include one that meets you
  there.
- **One machine's files.** Remote and
  virtual filesystems exist in Yazi's
  world (the untouched `vfs.toml` of
  chapter 2) but are beyond this guide's
  verification, and the everyday story —
  browse, preview, rearrange this
  machine's folders — is the whole of
  what the lab can stand behind.
