import sys

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[0] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u][v] = 1
    adj[v][u] = 1

tot = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            tot += adj[i][j] == adj[j][k] == adj[i][k] == 1
print(tot)
