# Upsolving with editorial
# https://codeforces.com/blog/entry/115586
# Summary: greedily dump in-between numbers in a non-increasing sequence

import sys

input = sys.stdin.readline

n, q = map(int, input().split())
*a, = map(int, input().split())
dump = [0] * n

for i in range(1, n):
    flag1 = a[i - 1] < a[i]
    if flag1 == 1:
        dump[i - 1] = 0
    if flag1 == 0:
        dump[i] = 1
dump[n - 1] = 0

c = 0
pfdump = [c]
for e in dump:
    c += e
    pfdump += [c]

for _ in range(q):
    l, r = map(int, input().split())  # 1-based, inclusive i.e. a[l-1:r]
    special = (pfdump[r] - pfdump[l - 1] - dump[r - 1] - dump[l - 1])
    if r - 1 == l - 1:
        special += dump[r - 1]
    print(r - l + 1 - special)
