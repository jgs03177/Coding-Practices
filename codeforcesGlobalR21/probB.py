import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    *a,=map(int,input().split())

    no0_cluster=0
    prv=0
    for e in a:
        if e!=0 and prv==0:
            no0_cluster+=1
        prv=e
    print(min(2,no0_cluster))
    # 0 if all 0
    # 1 if 1 continuous no-0 seq
    # 2 otherwise
