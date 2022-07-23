import sys
input=sys.stdin.readline

n,k,q=map(int,input().split())
*a,=map(int,input().split())
*l,=map(int,input().split())

for e in l:
    e-=1
    if e==k-1:
        nxt=n+1
    else:
        nxt=a[e+1]
    if a[e]+1!=nxt:
        a[e]+=1

print(*a)