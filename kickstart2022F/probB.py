import sys
input=sys.stdin.readline

t=int(input())

for ntc in range(t):
    n,q=map(int,input().split())
    graph=[[] for _ in range(n)]
    for _ in range(n-1):
        i,j=map(int,input().split())
        i-=1
        j-=1
        graph[i]+=[j]
        graph[j]+=[i]
    stk = [0]
    visit = [0] * n
    lvl = []
    visit[0]=1
    while stk:
        new_stk=[]
        lvl+=[len(stk)]
        while stk:
            u = stk.pop()
            vs = graph[u]
            for v in vs:
                if visit[v]:
                    continue
                visit[v]=1
                new_stk+=[v]
        stk=new_stk
    for _ in range(q):
        input()
    o=0
    for e in lvl:
        if e<=q:
            o+=e
            q-=e
        else:
            break
    print(f"Case #{ntc+1}: {o}")