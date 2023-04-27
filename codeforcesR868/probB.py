import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    *p, = map(int, input().split())
    mismatch = 0
    for i in range(n):
        if (p[i] - (i + 1)) % k:
            mismatch += 1
    o = 0
    if mismatch > 2:
        o = -1
    if mismatch == 2:
        o = 1
    print(o)
