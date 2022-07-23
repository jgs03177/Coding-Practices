import sys
input=sys.stdin.readline

n,x=map(int,input().split())
a=[]
b=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a+=[ai]
    b+=[bi]

t=float("inf")
cm=float("inf")
cc=0
for i in range(min(n,x)):
    cc+=a[i]+b[i]
    cm=min(cm,b[i])
    t=min(cc+(x-i-1)*cm,t)
print(t)