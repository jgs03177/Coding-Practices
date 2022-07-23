import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    *l1,=map(int,input().split())
    t=0
    l2=[]
    result=True
    zero=False
    for e in l1:
        t+=e
        if t<0:
            result=False
            break
        if zero and t>0:
            result=False
            break
        if t==0:
            zero=True
    if t:
        result=False
    print(["No","Yes"][result])