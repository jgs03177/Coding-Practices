import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    *a, = map(int, input().split()) #unhappiness
    c = []
    nc = [0] * n
    for _ in range(m):
        x, y = map(int, input().split())
        x-=1
        y-=1
        c += [(x,y)]
        nc[x]+=1
        nc[y]+=1
    if m&1:
        o = []
        for i in range(n):
            if nc[i]&1:
                o+=[a[i]]
        for x,y in c:
            if ((nc[x]&1) | (nc[y]&1)) == 0:
                o+=[a[x]+a[y]]
    else:
        o = [0]
    print(min(o))