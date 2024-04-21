# https://www.acmicpc.net/problem/1647

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edge = []
for i in range(m):
    a, b, c = map(int, input().split())
    edge += [(c, a - 1, b - 1)]

nv = n
# class union-find
gparent = list(range(nv))
grank = [0] * nv
gsize = [1] * nv


def find(x):
    # returns root node. with path compression
    if gparent[x] != x:
        gparent[x] = find(gparent[x])
    return gparent[x]


def union(x, y):
    # union by rank.
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return rx
    sx = grank[rx]
    sy = grank[ry]
    # merge small rank into large rank.
    if sx > sy:
        ry, rx = rx, ry
    elif sx < sy:
        pass
    else:
        grank[ry] += 1
    # rx merge into ry
    gparent[rx] = ry
    gsize[ry] += gsize[rx]
    gsize[rx] = 0
    return ry


# end class


# end class union-find

edge.sort()
cost = 0
nedge = n - 2
for c, a, b in edge:
    if nedge == 0:
        break
    ga = find(a)
    gb = find(b)
    if ga == gb:
        continue
    cost += c
    nedge -= 1
    union(a, b)

print(cost)
