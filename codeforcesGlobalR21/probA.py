import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,z=map(int,input().split())
    *a,=map(int,input().split())

    l=[]
    for e in a:
        l+=[e|z]

    print(max(l))
