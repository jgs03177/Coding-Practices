# Upsolving problem B with hint in comments.

"""Summary
Let c = [c1,c2,...,cn], c[i][k]:= k-th bit in c[i]

exists a,b s.t or(*c[a])=or(*c[b]) and a!=b
<=> exists i such that or(*c[{1...n}])=or(*c[{1...n}-{i}])
<=> then i exists such that for all k s.t c[i][k]=1, add(*c[{1...n}])[k]>=2

bitfield->tle, list->tle, dict->ac
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    check = defaultdict(int)
    ps = []
    for i in range(n):
        # p-th digit is 1
        k, *p = map(int, input().split())
        ps += [p]
    for p in ps:
        for e in p:
            check[e] += 1
    for p in ps:
        all2 = True
        for e in p:
            all2 &= check[e] >= 2
        if all2:
            print("Yes")
            break
    else:
        print("No")
