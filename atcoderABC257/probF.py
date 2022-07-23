import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())

adj=[[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u]+=[v]
    adj[v]+=[u]

q=deque([1])
visit=[0]*(n+1)
visit[1]=1
dist1=[float("inf")]*(n+1)
dist1[1]=0
while q:
    v=q.popleft()
    us=adj[v]
    for u in us:
        if visit[u]:
            continue
        visit[u]=1
        q+=[u]
        dist1[u]=dist1[v]+1

q=deque([n])
visit=[0]*(n+1)
visit[n]=1
dist2=[float("inf")]*(n+1)
dist2[n]=0
while q:
    v=q.popleft()
    us=adj[v]
    for u in us:
        if visit[u]:
            continue
        visit[u]=1
        q+=[u]
        dist2[u]=dist2[v]+1

# min: 1->n, 1->v1->0->v2->n, 1->v->0->n, 1->0->v->n
o=[]
m1 = min([dist1[u] for u in adj[0]] + [float("inf")])
m2 = min([dist2[u] for u in adj[0]] + [float("inf")])
for i in range(1,n+1):
    dist=min(dist1[n],m1+2+m2,m2+dist1[i]+1,m1+dist2[i]+1)
    o+=[dist if dist!=float("inf") else -1]
print(*o)