import sys

input = sys.stdin.readline

n = int(input())
aa = []
for i in range(n):
    *a, = map(int, input().split())
    aa += [a]

visit = [dict() for _ in range(n)]
for i in range(2 ** (n - 1)):
    c = aa[0][0]
    x, y = 0, 0
    for j in range(n - 1):
        v = i & 1
        i = i >> 1
        if v:
            x += 1
        else:
            y += 1
        c ^= aa[x][y]
    visit[x].setdefault(c, 0)
    visit[x][c] += 1
o = 0
for i in range(2 ** (n - 1)):
    c = 0
    x, y = n - 1, n - 1
    for j in range(n - 1):
        c ^= aa[x][y]
        v = i & 1
        i = i >> 1
        if v:
            x -= 1
        else:
            y -= 1
    v = visit[x].setdefault(c, 0)
    o += v
print(o)
