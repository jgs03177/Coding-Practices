import sys
input=sys.stdin.readline

n=int(input())

l=[]
for i in range(3,n+1):
    print(f"? {1} {i}", flush=True)
    d1=int(input())
    assert(d1!=-1)
    print(f"? {2} {i}", flush=True)
    d2=int(input())
    assert(d2!= -1)
    l+=[d1+d2]

dmin=min(l)
li=[]
count=0
for i in range(n-2):
    if l[i]==dmin:
        count+=1
        li+=[i+3]

if dmin==3:
    if count==2:
        print(f"? {li[1]} {li[0]}", flush=True)
        d3=int(input())
        assert (d3!=-1)
        if d3==1:
            o=3
        else:
            o=1
    else:
        o=1
else:
    o=dmin
print(f"! {o}")