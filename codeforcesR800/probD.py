import sys

input=sys.stdin.readline
sys.setrecursionlimit(300000)

t=int(input())

for _ in range(t):
    n = int(input())
    adj=[[] for i in range(n)]
    *p, = map(int, input().split())
    for i in range(n-1):  # p[0] is the parent of 1st node (idx start from 0)
        adj[p[i]-1]+=[i+1]
    ls=[]
    rs=[]
    for i in range(n):
        l,r=map(int, input().split())
        ls+=[l]
        rs+=[r]

    ops=0
    def dfs(i):
        global ops
        if not adj[i]:
            ops+=1
            return rs[i]
        hi=sum([dfs(e) for e in adj[i]])
        if hi>=ls[i]:
            return min(hi,rs[i])
        else:
            ops+=1
            return rs[i]

    dfs(0)
    print(ops)