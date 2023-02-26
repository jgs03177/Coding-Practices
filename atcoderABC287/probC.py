import sys

input = sys.stdin.readline

n, m = map(int, input().split())
c = [0] * n
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    c[u - 1] += 1
    c[v - 1] += 1
    graph[u - 1] += [v - 1]
    graph[v - 1] += [u - 1]

n1 = 0
n2 = 0
for e in c:
    if e == 1:
        n1 += 1
    elif e == 2:
        n2 += 1
o = "No"
if m == n - 1 and n1 == 2 and n2 == n - 2:
    visited = [0] * n
    q = [0]
    visited[0] = 1
    component = 1
    while q:
        v = q.pop()
        for u in graph[v]:
            if visited[u] == 0:
                q += [u]
                visited[u] = 1
                component += 1
    if component == n:
        o = "Yes"
print(o)
