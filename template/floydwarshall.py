# boj prob11404
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float("inf")] * n for _ in range(n)]  # dist[i][j] : min dist from i->j

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], c)

for i in range(n):
    dist[i][i] = 0

for k in range(n):  # include vertice k
    for i in range(n):  # for every vertice i, j
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # consider visiting vertice k

for i in range(n):
    for j in range(n):
        if dist[i][j] == float("inf"):
            dist[i][j] = 0

for i in range(n):
    print(*dist[i])
