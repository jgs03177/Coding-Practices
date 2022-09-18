import sys
import heapq

input = sys.stdin.readline

t = int(input())
for ntc in range(t):
    d, n, x = map(int, input().split())
    li1 = []
    for i in range(n):
        q, l, v = map(int, input().split())
        li1 += [(l, q, v)]
    li1.sort()
    pq = []
    o = 0
    for i in range(n):
        l, q, v = li1[i]
        heapq.heappush(pq, (-v, q))
        if i == n - 1:
            day_interval = max(d - l, 0)
        else:
            day_interval = li1[i + 1][0] - l
        n_seed = day_interval * x
        while n_seed:
            if not len(pq): break
            v, q = heapq.heappop(pq)
            v = -v
            c_seed = min(n_seed, q)
            o += c_seed * v
            q -= c_seed
            n_seed -= c_seed
            if q:
                heapq.heappush(pq, (-v, q))
    print(f"Case #{ntc + 1}: {o}")
