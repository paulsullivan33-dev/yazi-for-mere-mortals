#!/usr/bin/env python3
"""PTY driver for the Yazi lab.

Runs a command on a pseudo-terminal of a fixed size, feeds it a
timed script of keystrokes, renders what a terminal would show
with pyte, and saves screen snapshots at marked points.

Scenario file format (one action per line, # starts a comment):
  wait <seconds>        pause
  send <text>           send text; backslash escapes (\r, \x1b, \t) decoded
  snap <name>           save the current screen to snapshots/<name>.txt

Usage:
  ptyrun.py --cols 110 --rows 32 --snapdir DIR --log RAWLOG \
            --scenario FILE -- command [args...]

Environment for the child is inherited; set TERM etc. outside.
The child's exit code is printed at the end as CHILD_EXIT=<n>.
"""
import argparse
import codecs
import fcntl
import os
import pty
import select
import signal
import struct
import subprocess
import sys
import termios
import time

import pyte

# pyte (0.8.x) handlers do not accept the `private` keyword the parser
# passes for CSI ? ... sequences, which Yazi sends (device status, SGR).
# Wrap every Screen method so the flag is dropped before dispatch.
import types as _types

for _name, _fn in list(vars(pyte.Screen).items()):
    if isinstance(_fn, _types.FunctionType):

        def _make(fn):
            def wrapper(self, *a, **k):
                k.pop("private", None)
                return fn(self, *a, **k)

            return wrapper

        setattr(pyte.Screen, _name, _make(_fn))


def set_winsize(fd, cols, rows):
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cols", type=int, default=110)
    ap.add_argument("--rows", type=int, default=32)
    ap.add_argument("--snapdir", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--scenario", required=True)
    ap.add_argument("--timeout", type=float, default=30.0)
    ap.add_argument("cmd", nargs=argparse.REMAINDER)
    args = ap.parse_args()
    cmd = args.cmd
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]

    os.makedirs(args.snapdir, exist_ok=True)
    master, slave = pty.openpty()
    set_winsize(slave, args.cols, args.rows)
    proc = subprocess.Popen(
        cmd,
        stdin=slave,
        stdout=slave,
        stderr=slave,
        close_fds=True,
        start_new_session=True,
    )
    os.close(slave)

    screen = pyte.Screen(args.cols, args.rows)
    stream = pyte.ByteStream(screen)
    rawlog = open(args.log, "wb")

    def pump(duration):
        """Read output for `duration` seconds (or until EOF)."""
        end = time.time() + duration
        while True:
            left = end - time.time()
            if left <= 0:
                return True
            r, _, _ = select.select([master], [], [], min(left, 0.2))
            if master in r:
                try:
                    data = os.read(master, 65536)
                except OSError:
                    return False
                if not data:
                    return False
                rawlog.write(data)
                rawlog.flush()
                stream.feed(data)
            if proc.poll() is not None:
                # drain whatever is left
                try:
                    while True:
                        r, _, _ = select.select([master], [], [], 0.1)
                        if master not in r:
                            break
                        data = os.read(master, 65536)
                        if not data:
                            break
                        rawlog.write(data)
                        stream.feed(data)
                except OSError:
                    pass
                return False

    def snap(name):
        path = os.path.join(args.snapdir, name + ".txt")
        with open(path, "w") as f:
            for line in screen.display:
                f.write(line.rstrip() + "\n")
        print(f"[snap] {name} -> {path}")

    with open(args.scenario) as f:
        actions = [ln.rstrip("\n") for ln in f]

    pump(0.5)
    for ln in actions:
        if not ln or ln.startswith("#"):
            continue
        verb, _, rest = ln.partition(" ")
        if verb == "wait":
            pump(float(rest))
        elif verb == "send":
            text = codecs.decode(rest, "unicode_escape")
            os.write(master, text.encode())
            pump(0.35)
        elif verb == "snap":
            snap(rest.strip())
        else:
            print(f"unknown action: {ln}", file=sys.stderr)

    # final grace period, then clean up
    deadline = time.time() + 3.0
    while proc.poll() is None and time.time() < deadline:
        if not pump(0.3):
            break
    if proc.poll() is None:
        proc.send_signal(signal.SIGTERM)
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=3)
    snap("final")
    rawlog.close()
    os.close(master)
    print(f"CHILD_EXIT={proc.returncode}")


if __name__ == "__main__":
    main()
