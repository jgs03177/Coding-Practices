t=int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d = set()
    n0 = 0
    for e in a:
        n0 += 0 if e else 1  # count #0s
        d.add(e)  # count uniques
    d.discard(0)
    nd = len(d)
    if nd == n:
        print(n+1)
    else:
        print(n-n0)
