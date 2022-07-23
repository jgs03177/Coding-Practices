import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    *s, = map(int,input().split())
    *f, = map(int, input().split())
    l=[]
    for i in range(n):
        d=f[i]-s[i]
        d2=f[i]-f[i-1] if i>0 else f[i]
        l.append(min(d,d2))

    print(*l)
