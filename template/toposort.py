# https://www.acmicpc.net/problem/1766

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

dep = [0] * n

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())  # a->b
    a -= 1
    b -= 1
    graph[a] += [b]
    dep[b] += 1

q = []
for i in range(n):
    if dep[i] == 0:
        q += [i]

o = []
while q:
    a = heapq.heappop(q)  # if priority is not determined, queue or stack can be used instead
    o += [1 + a]
    for b in graph[a]:
        dep[b] -= 1
        if dep[b] == 0:
            heapq.heappush(q, b)

print(*o)
