import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    s=input().rstrip()
    c1=0
    t=len(s)
    prv=s[0]
    for c in s:
        if c!=prv:
            t+=c1
        c1+=1
        prv=c
    print(t)