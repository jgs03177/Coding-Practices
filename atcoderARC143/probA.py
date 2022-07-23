import sys
input=sys.stdin.readline

*a,=map(int,input().split())

a.sort()
a,b,c=a

# 1 2 3
nex=0
d2 = min(b-a,c-b)
c-=d2
b-=d2
nex+=d2

if c==b:
    # 1 2 2
    nex+=c
else:
    # 1 1 2
    d1 = c-b
    if a<d1:
        nex=-1
    else:
        nex+=c
print(nex)




