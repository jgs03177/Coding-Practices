import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,k = map(int,input().split())
    *a, = map(int,input().split())
    cost=0
    rem=[0]*k
    for i in range(n):
        e=a[i]
        cost+=e//k
        rem[e%k]+=1

    lastptr=1
    for i in range(k-1,0,-1):
        lastptr=max(lastptr,k-i)
        while lastptr<i:
            bonus=min(rem[i],rem[lastptr])
            rem[i]-=bonus
            rem[lastptr]-=bonus
            cost+=bonus
            if rem[lastptr]==0:
                lastptr+=1
            if rem[i]==0:
                break
        if lastptr==i:
            bonus=rem[i]//2
            cost+=bonus
            break
    print(cost)