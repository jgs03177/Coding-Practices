# https://atcoder.jp/contests/abc256/tasks/abc256_e

import sys

sys.setrecursionlimit(200100)

n=int(input())
*x,=map(int,input().split())
*c,=map(int,input().split())
visit=[0]*n

tot=0

def dfs(i):
    global tot
    if visit[i]==0:
        visit[i]=1
        v=dfs(x[i]-1)
        v=min(v,c[i])
        if visit[i]==3:
            tot+=v
        visit[i]=2
        return v
    if visit[i]==1:
        visit[i]=3
        return c[i]
    if visit[i]==2:
        return 0

for i in range(n):
    if visit[i]==0:
        dfs(i)

print(tot)