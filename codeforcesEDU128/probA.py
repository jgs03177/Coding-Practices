import sys
input=sys.stdin.readline

t = int(input())

for i in range(t):
    l1,r1,l2,r2=map(int,input().split())
    if max(l1,l2)<=min(r1,r2):
        print(max(l1,l2))
    else:
        print(l1+l2)
