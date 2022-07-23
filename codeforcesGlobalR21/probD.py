# https://codeforces.com/blog/entry/103479
# sol 1

import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    *a,=map(int,input().split())

    fmin=[]
    fmax=[]
    cmin=n
    imin=1
    cmax=1
    imax=1
    for i in range(n):
        v=a[i]
        if v<=cmin:
            cmin=v
            imin=i
        if v>=cmax:
            cmax=v
            imax=i
        fmin+=[imin]
        fmax+=[imax]

    bmin=[]
    bmax=[]
    cmin=n
    imin=1
    cmax=1
    imax=1
    for i in range(n-1,-1,-1):
        v=a[i]
        if v<=cmin:
            cmin=v
            imin=i
        if v>=cmax:
            cmax=v
            imax=i
        bmin+=[imin]
        bmax+=[imax]

    idx = fmax[n-1]
    bmin=bmin[::-1]
    bmax=bmax[::-1]

    tlist = ((fmin, fmax), (bmin, bmax))

    res=0

    ismax=0
    isback=0
    idx1=idx
    while idx1!=0:
        res+=1
        idx1 = tlist[isback][ismax][idx1]
        ismax^=1

    ismax=0
    isback=1
    idx1=idx
    while idx1!=n-1:
        res+=1
        idx1 = tlist[isback][ismax][idx1]
        ismax^=1

    print(res)
