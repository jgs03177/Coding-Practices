import sys

input=sys.stdin.readline

n,m=map(int,input().split())
q = [0] * m
li = []
for i in range(m):
    if i>0:
        q[i-1]=0
    q[i]=1
    print(f"? {''.join([str(e) for e in q])}", flush=True)
    a=int(input())
    li+=[(a,i)]

li.sort(key=lambda x:x[0])
a,i=li[0]

q=[0]*m
q[i]=1
prv=a
for j in range(1,m):
    a,i=li[j]
    q[i]=1
    print(f"? {''.join([str(e) for e in q])}", flush=True)
    b=int(input())
    if b!=prv+a:
        q[i]=0
    else:
        prv=b

print(f"! {prv}")

    # 더했는데 조금만 더해진경우: 거름
    # 더했는데 안더해진경우: 없앰
