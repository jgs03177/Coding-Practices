import sys

input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    *d, = map(int, input().split())
    *c, = map(int, input().split())
    for i in range(n):
        d[i] -= 1
    constraint = [0] * n
    for e in d:
        constraint[e] += 1
    r = [0] * n  # current car
    q = []
    for i in range(n):
        if constraint[i] == 0:
            q += [i]
    o = 0
    while q:
        e = q.pop()
        o += max(0, c[e] - r[e])
        next = d[e]
        r[next] += c[e]
        constraint[next] -= 1
        if constraint[next] == 0:
            q += [next]
    for i in range(n):
        if constraint[i] != 0:  # loop
            order = [i]
            rs = [r[i]]
            cs = [0, c[i]]
            p = d[i]
            constraint[i] = 0
            while p != i:
                rs += [r[p]]
                cs += [c[p]]
                constraint[p] = 0
                order += [p]
                p = d[p]
            cs[0] = cs[-1]
            within = []
            without = []
            for i in range(len(rs)):
                without += [max(0, cs[i + 1] - rs[i])]
                within += [max(0, cs[i + 1] - (cs[i] + rs[i]))]
            minstart = min((without[i] - within[i]) for i in range(len(rs)))
            o += sum(within) + minstart

    print(f"Case #{case + 1}: {o}")
