import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())
s = []
for i in range(n):
    si = input().rstrip()
    s += [si]

forward = [float("inf")] * n
backward = [float("inf")] * n
forward[0] = 0
for i in range(n):
    for j in range(1, m + 1):
        if s[i][j - 1] == "1":
            forward[i + j] = min(forward[i + j], forward[i] + 1)

backward[-1] = 0
for i in range(n - 1, -1, -1):
    for j in range(1, m + 1):
        if i - j < 0: continue
        if s[i - j][j - 1] == "1":
            backward[i - j] = min(backward[i - j], backward[i] + 1)

o = []
for i in range(1, n - 1):
    c = float("inf")
    for st in range(1, m):
        for end in range(1, m + 1):
            # i-s -> i-s+e. without visiting i.
            if i - st < 0: continue
            if -st + end <= 0: continue
            if s[i - st][end - 1] == "1":
                c = min(c, forward[i - st] + backward[i - st + end] + 1)
    o += [-1 if math.isinf(c) else c]

print(*o)
