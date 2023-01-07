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
for i in range(n):
    if not visited[i]:
        o += 1
        q = [i]
        visited[i] = 1
        while q:
            j = q.pop()
            for e in graph[j]:
                if not visited[e]:
                    visited[e] = 1
                    q += [e]
print(o)
