import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    h,w=map(int,input().split())
    ll=[]
    for i in range(h):
        *l,=map(int,input().split())
        ll+=[l]
    ph,pw=0,0
    p=ll[0][0]
    for i in range(h):
        for j in range(w):
            if p < ll[i][j]:
                ph=i
                pw=j
                p=ll[i][j]
    print((h-min(ph,h-ph-1))* (w-min(pw,w-pw-1)))