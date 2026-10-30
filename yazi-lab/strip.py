import re, sys
data = sys.stdin.buffer.read().decode("utf-8", "replace")
# drop kitty graphics and other APC/DCS/OSC payloads, then CSI sequences
data = re.sub(r"\x1b_[^\x1b]*\x1b\\", "", data)
data = re.sub(r"\x1bP[^\x1b]*\x1b\\", "", data)
data = re.sub(r"\x1b\][^\x07\x1b]*(\x07|\x1b\\)", "", data)
data = re.sub(r"\x1b\[[0-9;?><!$% ]*?[A-Za-z@~]", "", data)
data = re.sub(r"\x1b[()][0-9A-B]", "", data)
data = re.sub(r"\x1b.", "", data)
data = data.replace("\r\n", "\n").replace("\r", "\n")
lines = [ln.rstrip() for ln in data.split("\n")]
out = []
for ln in lines:
    if ln or (out and out[-1]):
        out.append(ln)
sys.stdout.write("\n".join(out).strip("\n") + "\n")
