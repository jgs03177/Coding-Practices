import sys, heapq
input=sys.stdin.readline

n,m=map(int,input().split())
iadj=[[] for _ in range(n)]  # inverted road
nadj=[0]*n
dist=[n+1]*n
cost=[float("inf")]*n
visit=[0]*n

for _ in range(m):
    v,u=map(int,input().split())
    v-=1
    u-=1
    iadj[u]+=[v]
    nadj[v]+=1

q = [(0,n-1)]
cost[n-1]=0
while q:
    d,v=heapq.heappop(q)
    if visit[v]:
        continue
    visit[v]=1
    for u in iadj[v]:
        nadj[u]-=1
        if cost[v] + nadj[u] + 1 < cost[u]:
            cost[u]=cost[v]+nadj[u] + 1
            heapq.heappush(q, (cost[u], u))

print(cost[0])