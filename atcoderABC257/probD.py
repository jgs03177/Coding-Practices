import sys
input=sys.stdin.readline

n=int(input())

xs=[]
ys=[]
ps=[]
for i in range(n):
    x,y,p=map(int,input().split())
    xs+=[x]
    ys+=[y]
    ps+=[p]

dist=[]
for i in range(n):
    xi=xs[i]
    yi=ys[i]
    pi=ps[i]
    dist2=[]
    for j in range(n):
        xj=xs[j]
        yj=ys[j]
        dist2+=[(abs(xi-xj)+abs(yi-yj)+pi-1)//pi] # ceil
    dist+=[dist2]

# floyd warshall
for k in range(n):  # include vertice k
    for i in range(n):  # for every vertice i, j
        for j in range(n):
            dist[i][j]= min(dist[i][j], max(dist[i][k], dist[k][j]))  # consider visiting vertice k

l=[]
for i in range(n):
    l+=[max(dist[i])]
print(min(l))