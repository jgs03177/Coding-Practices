import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    l="01"*min(a,b)
    if a<b:
        l+="1"*(b-a)
    else:
        l+="0"*(a-b)
    print(l)