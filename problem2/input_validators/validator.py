import sys

lines = sys.stdin.read().split("\n")
if lines[-1] != "":
    sys.exit(1)
lines = lines[:-1]
if not lines[0].isdigit() or str(int(lines[0])) != lines[0]:
    sys.exit(1)

n = int(lines[0])
if not 1 <= n <= 100000:
    sys.exit(1)
    
idx = 1
for _ in range(n):
    parts = lines[idx].split(" ")
    if len(parts) != 2:
        sys.exit(1)
    msg = parts[0]
    cnt_str = parts[1]
    if not 1 <= len(msg) <= 20 or not msg.islower() or not msg.isalpha():
        sys.exit(1)
    if not cnt_str.isdigit() or str(int(cnt_str)) != cnt_str:
        sys.exit(1)
    cnt = int(cnt_str)
    if not 1 <= cnt <= 1000000:
        sys.exit(1)
    idx += 1
    
if not lines[idx].isdigit() or str(int(lines[idx])) != lines[idx]:
    sys.exit(1)

q = int(lines[idx])
if not 1 <= q <= 100000:
    sys.exit(1)
idx += 1
for _ in range(q):
    phrase = lines[idx]
    if not 1 <= len(phrase) <= 20 or not phrase.islower() or not phrase.isalpha():
        sys.exit(1)
    idx += 1
if idx != len(lines):
    sys.exit(1)
sys.exit(42)
