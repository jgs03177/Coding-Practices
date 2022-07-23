import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    *la,=map(int,input().split())
    *lb,=map(int, input().split())
    d=[la[i]-lb[i] for i in range(n)]
    common=None
    verdict=True
    for i in range(n):
        if d[i]<0:
            verdict=False
            break
        if lb[i]!=0:
            if common is None:
                common=d[i]
            if common!=d[i]:
                verdict=False
                break
    if (common is None) or (verdict == False):
        pass
    else:
        for i in range(n):
            if lb[i]==0 and d[i]>common:
                verdict=False
                break
    print("YES" if verdict else "NO")