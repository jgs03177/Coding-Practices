import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())
    *a, = map(int, input().split())
    b = []
    c = []
    bodd = 0
    codd = 0
    for e in a:
        bi = e//n
        bi = bi * (bi>=2)
        ci = e//m
        ci = ci * (ci>=2)
        bodd |= bi>=3
        codd |= ci>=3
        b += [bi]
        c += [ci]
    sb = sum(b)
    sc = sum(c)
    o = ""
    if (sb >= m and ((m & 1 == 0) or bodd)) or \
        (sc >= n and ((n & 1 == 0) or codd)):
        o="Yes"
    else:
        o="No"
    print(o)
