import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    no = 0
    sa = 0
    o = []
    for i, ai in enumerate(a):
        no += ai & 1
        sa += ai
        if i == 0:
            o += [sa]
        else:
            o += [sa - no // 3 - (no % 3 == 1)]
    print(*o)
