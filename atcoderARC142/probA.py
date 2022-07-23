import sys,math
input=sys.stdin.readline

n,k=map(int,input().split())

if k%10==0:
    if n>=k:
        o=1
    else:
        o=0
else:
    k2=int(str(k)[::-1])
    o=math.floor(max(math.log10(n/k)+1,0))
    if k!=k2:
        if k<k2:
            o+=math.floor(max(math.log10(n/k2)+1,0))
        else:
            o=0
print(o)