import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()

p = 0, 0
d = {(0, 0)}

order = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
for c in s:
    dx, dy = order[c]
    p = p[0] + dx, p[1] + dy
    d |= {p}

print("Yes" if len(d) < n + 1 else "No")
