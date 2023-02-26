import sys

input = sys.stdin.readline

n = int(input())
o = [0] * n
originptr = [None]
ss = []
for _ in range(n):
    s = input().rstrip()
    ss += [s]
l = list(range(n))
l.sort(key=lambda i: ss[i])  # sort index of ss, dictionary order
invl = [0] * n
for i, e in enumerate(l):
    invl[e] = i

lcp = []
for i in range(n - 1):
    t1 = ss[l[i]]
    t2 = ss[l[i + 1]]
    clcp = min(len(t1), len(t2))
    for j in range(clcp):
        if t1[j] == t2[j]:
            pass
        else:
            clcp = j
            break
    lcp += [clcp]
for i in range(n):
    t = invl[i]
    o = []
    if t >= 1:
        o += [lcp[t - 1]]
    if t <= n - 2:
        o += [lcp[t]]
    print(max(o))
