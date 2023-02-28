# Problem D upsolving with editorial: https://codeforces.com/blog/entry/111783
"""Memo
Problem
Find 0<=x<=10**18 that maximizes the number of square numbers in {a_1+x, ... a_n+x}.
(we will call the number of square numbers as squareness)
a_i is sorted. a<=10**9, n<=50.

Brute force approach
For all 0<=x<=10**18, calculate a_1+x, a_2+x, ..., a_n+x is a square number. O(nx)

Editorial summary
We can guarantee there exists x such that the squareness is at least 1.
We search only x that the squareness can be at least 2.

Detail
Check x s.t both a[i]+x, a[j]+x becomes perfect square.
Let a[i]+x=p**2, a[j]+x=q**2.
d_ij = a[i]-a[j] = p**2-q**2 = (p-q)(p+q).
let
p-q=c, p+q=d_ij/c  (c is a factor of d_ij)
then
p = (c + d_ij/c)/2
q = (-c + d_ij/c)/2
x = p**2-a[i]
"""

import sys
from math import isqrt

input = sys.stdin.readline

t = int(input())

# precompute sieve 10**9 -> MLE and TLE
# fast factorization is possible with pollard's rho

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    o = 1
    cand = set()
    for i in range(n):
        for j in range(i):  # i>j
            d = a[i] - a[j]
            for c in range(1, isqrt(d) + 1):
                p = (c + d // c) // 2
                q = (-c + d // c) // 2
                if (p + q) * (p - q) != d:
                    continue
                x = p ** 2 - a[i]
                y = q ** 2 - a[i]
                if 0 <= x <= 10 ** 18:
                    cand.add(x)
                if 0 <= y <= 10 ** 18:
                    cand.add(y)
    for e in cand:
        nc = 0
        for k in range(n):
            ai = a[k] + e
            sq = isqrt(ai)
            nc += sq * sq == ai
        o = max(o, nc)
    print(o)
