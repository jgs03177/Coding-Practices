# Problem E upsolving via other's code

import sys

input = sys.stdin.readline

# factor
lim = 2 * 10 ** 5 + 1
factor = [[] for _ in range(lim)]
for i in range(1, lim):
    for j in range(i, lim, i):
        factor[j] += [i]

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    *b, = map(int, input().split())

    # if bi<ai, then the k should be higher than the difference, and ceil(ai/k) == ceil(bi/k)
    # if ai<=bi, then ignore safely.
    # mark the "skip area" using imos
    check1 = [0] * (n + 1)
    for ai, bi in zip(a, b):
        if bi < ai:
            check1[bi] += 1
            check1[ai] -= 1
    for i in range(1, n + 1):
        check1[i] += check1[i - 1]

    # mark impossible k's
    check2 = [0] * (n + 1)
    for i in range(n):
        if check1[i]:
            for e in factor[i]:
                check2[e] = 1

    o = []
    for i in range(1, n + 1):
        if check2[i] == 0:
            o += [i]
    print(len(o))
    print(*o)
