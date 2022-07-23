import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    *a,=map(int,input().split())
    k = int(input())
    *b, = map(int, input().split())

    abase = []
    cp=0
    cq=0
    for e in a:
        q=1
        while e%m==0:
            e//=m
            q*=m
        if cp==0 or cp!=e:
            if cp!=0: abase+=[(cp,cq)]
            cp=e
            cq=q
        else:
            cq+=q
    if cp!=0: abase+=[(cp,cq)]

    bbase = []
    cp=0
    cq=0
    for e in b:
        q=1
        while e%m==0:
            e//=m
            q*=m
        if cp==0 or cp!=e:
            if cp!=0: bbase+=[(cp,cq)]
            cp=e
            cq=q
        else:
            cq+=q
    if cp!=0: bbase+=[(cp,cq)]

    out=False
    if len(abase)==len(bbase):
        for i in range(len(abase)):
            if abase[i]!=bbase[i]:
                break
        else:
            out=True

    print(["No","Yes"][out])