import sys

input=sys.stdin.readline

t=int(input())
for i in range(t):
    a=int(input())
    a2=a
    min0 = None
    min1 = None
    n1s=0
    d=0
    while a:
        b=a&1
        if b:
            min1=min(min1,d) if min1 is not None else d
            n1s+=1
        else:
            min0=min(min0,d) if min0 is not None else d
        a>>=1
        d+=1
    if min0 is None:
        min0=min1+1
    if n1s==1:
        print((1<<min1)+(1<<min0))
    else:
        print((1<<min1))
#비트1개: 가장작은1비트+가장작은0비트
#비트2개: 가장작은1비트
