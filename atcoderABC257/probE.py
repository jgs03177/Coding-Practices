import sys
input=sys.stdin.readline

n=int(input())
*c,=map(int,input().split())

minv=c[8]
minidx=8
for i in range(7,-1,-1):
    if c[i] < minv:
        minv=c[i]
        minidx=i

length=n//minv
remain=n-length*minv

o=[]
for i in range(8,-1,-1):
    if minidx >= i:
        break
    dv = c[i]-minv
    length1 = remain//dv
    o+=[i+1]*length1
    remain-=length1*dv

o+=[minidx+1]*(length-len(o))
print(*o,sep="")
