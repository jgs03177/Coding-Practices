import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
path = []
for i in range(m):
    a, b, c = map(int, input().split())
    path += [(a - 1, b - 1, c)]
*es, = map(int, input().split())
dist = [float("inf")] * n
dist[0] = 0
for e in es:
    e -= 1
    a, b, c = path[e]
    dist[b] = min(dist[b], dist[a] + c)
print(dist[n - 1] if dist[n - 1] != float("inf") else -1)
