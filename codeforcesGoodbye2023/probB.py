import sys
from math import gcd


input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    ga = a // g
    gb = b // g
    if ga == 1:
        print(g * gb * gb)
    else:
        print(g * ga * gb)
