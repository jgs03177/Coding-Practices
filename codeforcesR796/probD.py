import sys

input=sys.stdin.readline

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    *as_,=map(int,input().split())
    maxseq=0
    timebonus=0
    if n>k:
        pref=[0]
        tot=0
        for a in as_:
            tot+=a
            pref+=[tot]
        for i in range(k,n+1):
            seq=pref[i]-pref[i-k]
            maxseq=max(seq,maxseq)
        timebonus=k*(k-1)//2
    else:
        maxseq=sum(as_)
        timebonus=(2*k-1-n)*n//2  #(k-1)+...+(k-n)
    print(maxseq+timebonus)