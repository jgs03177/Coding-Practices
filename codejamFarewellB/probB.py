import sys

input = sys.stdin.readline
from math import gcd


def ext_gcd(a, b):
    # r0 > r1 > .... >= 0
    r0, r1 = (a, b) if a > b else (b, a)
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q, r2 = divmod(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    gcd = r0
    x, y = (s0, t0) if a > b else (t0, s0)
    return gcd, x, y  # gcd(a,b) = ax+by


def inv(a, n):
    g, x, y = ext_gcd(a, n)
    if g != 1:
        return -1
    return x % n


t = int(input())
for case in range(t):
    w, n, d = map(int, input().split())
    *x, = map(int, input().split())
    impossible = False
    o = 0
    for a, b in zip(x[:w // 2], x[::-1][:w // 2]):
        # a=b+dk (mod n)
        # (a-b)/d=k (mod n)
        c = a - b
        if c == 0:
            continue
        f1 = gcd(d, n)
        f2 = gcd(c, n)
        # f1 must divide f2
        if f1 != gcd(f1, f2):
            impossible = True
            break
        newd = d // f1
        newn = n // f1
        winv = inv(newd, newn)
        k = (c // f1) * winv % newn
        o += min(k, abs(newn - k))
    if impossible:
        o = "IMPOSSIBLE"
    print(f"Case #{case + 1}: {o}")
