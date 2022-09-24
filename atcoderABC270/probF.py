import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
*x, = map(int, input().split())
*y, = map(int, input().split())

adj = [[] for _ in range(n + 2)]  # n:airport, n+1:harbor
for i in range(m):
    a, b, z = map(int, input().split())
    a -= 1
    b -= 1
    adj[a] += [(z, b)]
    adj[b] += [(z, a)]

mincost = float("inf")

# only road
visited = [0] * (n + 2)
visited[0] = 1
pq = sorted(adj[0])
cost = 0
conn = 1
while pq and conn != n:
    z, v = heapq.heappop(pq)
    if not visited[v]:
        visited[v] = 1
        conn += 1
        cost += z
        us = adj[v]
        for u in us:
            if not visited[u[1]]:
                heapq.heappush(pq, u)
if conn == n:
    mincost = cost

# road + harbor
visited = [0] * (n + 2)
visited[n+1] = 1
pq = sorted([(y[i], i) for i in range(n)])
cost = 0
conn = 1
while pq and conn != n + 1:
    z, v = heapq.heappop(pq)
    if not visited[v]:
        visited[v] = 1
        conn += 1
        cost += z
        us = adj[v]
        for u in us:
            if not visited[u[1]]:
                heapq.heappush(pq, u)

mincost = min(cost, mincost)

# road + airport
visited = [0] * (n + 2)
visited[n] = 1
pq = sorted([(x[i], i) for i in range(n)])
cost = 0
conn = 1
while pq and conn != n + 1:
    z, v = heapq.heappop(pq)
    if not visited[v]:
        visited[v] = 1
        conn += 1
        cost += z
        us = adj[v]
        for u in us:
            if not visited[u[1]]:
                heapq.heappush(pq, u)

mincost = min(cost, mincost)

# road + harbor + airport
for i in range(n):
    adj[n + 1] += [(y[i], i)]
    adj[i] += [(y[i], n + 1)]
    adj[n] += [(x[i], i)]
    adj[i] += [(x[i], n)]

visited = [0] * (n + 2)
visited[0] = 1
pq = sorted(adj[0])
cost = 0
conn = 1
while pq and conn != n + 2:
    z, v = heapq.heappop(pq)
    if not visited[v]:
        visited[v] = 1
        conn += 1
        cost += z
        us = adj[v]
        for u in us:
            if not visited[u[1]]:
                heapq.heappush(pq, u)

mincost = min(cost, mincost)

print(mincost)
