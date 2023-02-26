import sys

input = sys.stdin.readline

n, m = map(int, input().split())

const = [0] * n
adj = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    adj[x - 1] += [y - 1]
    const[y - 1] += 1

# len(q) always should be 1.
q = []
for i, e in enumerate(const):
    if e == 0:
        q += [i]

o = []
while q:
    if len(q) > 1:
        break
    v = q.pop()
    o += [v]
    us = adj[v]
    for u in us:
        const[u] -= 1
        if const[u] == 0:
            q += [u]

if len(o) == n:
    print("Yes")
    oo = [0] * n
    for i, e in enumerate(o):
        oo[e] = i + 1
    print(*oo)
else:
    print("No")
