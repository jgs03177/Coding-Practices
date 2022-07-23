import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    *a,=map(int,input().split())
    determined=False
    win=True
    mikedt=10**9+1
    mikeidx=0
    joedt=10**9+1
    joeidx=0
    for i in range(n):
        if i%2==0:
            if mikedt > a[i]:
                mikedt=a[i]
                mikeidx=i
        else:
            if joedt > a[i]:
                joedt=a[i]
                joeidx=i
        if a[i]==0:
            determined=True
            win=i%2
            break
    if not determined and n%2==1:
        win=1
    else:
        if mikedt >joedt or (mikedt==joedt and mikeidx > joeidx):
            win=1
        else:
            win=0
    print("Mike" if win else "Joe")