import sys
input=sys.stdin.readline

n=int(input())
lrs=[]
for i in range(n):
    *lr,=map(int,input().split())
    lrs+=[lr]

lrs.sort(key=lambda x:x[0])

li,ri=lrs[0]
lastl=li
lastr=ri
o=[]
for i in range(1,n):
    li,ri=lrs[i]
    if li<=lastr:
        lastr=max(lastr,ri)
    else:
        o+=[(lastl,lastr)]
        lastl=li
        lastr=ri
o+=[(lastl,lastr)]
for e in o:
    print(*e)