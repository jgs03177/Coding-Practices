import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    h,w=map(int,input().split())
    for i in range(h):
        f1=((i>>1)^i)&1
        l=[]
        for j in range(w):
            f2 = ((j >> 1) ^ j) & 1
            l+=[f1^f2]
        print(*l)
