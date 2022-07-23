import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    ll=[]
    for i in range(n):
        *l,=map(int,input().split())
        ll+=[l]
    if (n&1)^(m&1)==0:
        print("NO")
        continue

    minl1 = [0]*m
    maxl1 = [0]*m
    pref=0
    for j in range(m):
        pref = pref + ll[0][j]
        minl1[j] = pref
        maxl1[j] = pref
    for i in range(1,n):
        minl2 = [0]*m
        maxl2 = [0]*m
        minpref=minl1[0]
        maxpref=maxl1[0]
        for j in range(m):
            minpref=min(minpref,minl1[j])+ll[i][j]
            minl2[j]=minpref
            maxpref = max(maxpref, maxl1[j]) + ll[i][j]
            maxl2[j]=maxpref
        minl1=minl2
        maxl1=maxl2
    print("YES" if minl1[-1]<=0<=maxl1[-1] else "NO")

