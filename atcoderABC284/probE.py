import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * n
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u] += [v]
    graph[v] += [u]

o = 0
q = [(0, 0)]
while q:
    j, s = q.pop()
    if s == 0:
        visited[j] = 1
        o += 1
        if o >= 10 ** 6:
            break
        for e in graph[j]:
            if not visited[e]:
                q += [(e, 1), (e, 0)]
    else:
        visited[j] = 0

print(o)
