import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())
x -= 1
y -= 1
adj = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u] += [v]
    adj[v] += [u]

# dfs
parent = [-1] * n
parent[x] = -2
q = [x]
found = 0
while q:
    u = q.pop()
    vs = adj[u]
    for v in vs:
        if parent[v] == -1:
            parent[v] = u
            q += [v]
        if v == y:
            found = 1
    if found:
        break

r = y
l = [y + 1]
while r != x:
    r = parent[r]
    l += [r + 1]

print(*l[::-1])
