import sys
from math import gcd

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0 if a[0] == 1 else 1)
        continue
    if gcd(*a) == 1:
        print(0)
        continue

    b = a[:]
    b[-1] = gcd(n,b[-1])
    if gcd(*b) == 1:
        print(1)
        continue

    b = a[:]
    b[-2] = gcd(n-1,b[-2])
    if gcd(*b) == 1:
        print(2)
        continue

    print(3)
