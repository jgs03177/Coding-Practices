import sys

input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    *as_,=map(int,input().split())
    nodd=0
    ors=0
    for a in as_:
        nodd += a&1
        ors |= a
    nops=0
    if nodd==0:
        while ors&1==0:
            ors>>=1
            nops+=1
        nops-=1
    nops+=n-nodd
    print(nops)

    # 홀수 존재: 짝수를 다 더함
    # 다 짝수: 가장낮은 비트를 찾는다 (or), >>op 사용한다, 다 더한다.