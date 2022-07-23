import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a]+=[b]
    graph[b]+=[a]

nq=int(input())
for i in range(nq):
    x,k=map(int,input().split())
    q=deque([(x-1,0)])
    visit=set()
    while len(q):
        v,lvl= q.popleft()
        if v+1 in visit:
            continue
        visit.add(v+1)
        if lvl >= k:
            continue
        for v2 in graph[v]:
            q+=[(v2,lvl+1)]
    print(sum(visit))