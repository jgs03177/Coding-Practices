import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nm = n + m
nm1 = nm + 1
coord = []
for i in range(nm):
    x, y = map(int, input().split())
    coord += [(x, y)]
coord += [(0, 0)]

dist = [[0] * nm1 for _ in range(nm1)]
for i in range(nm1):
    xi, yi = coord[i]
    for j in range(i + 1, nm1):
        xj, yj = coord[j]
        d = ((xi - xj) * (xi - xj) + (yi - yj) * (yi - yj)) ** 0.5
        dist[i][j] = d
        dist[j][i] = d

speed = 1

path = [[float("inf")] * nm for _ in range(1 << nm)]

for i in range(nm):
    path[1 << i][i] = dist[nm][i]


def flag2list(flag):
    state = [[], [], 0]
    for i in range(n):
        state[flag & 1] += [i]
        flag >>= 1
    for i in range(n, nm):
        state[flag & 1] += [i]
        state[2] += flag & 1
        flag >>= 1
    return state


# tsp
flags = [1 << i for i in range(nm)]
for ns in range(1, nm):
    newflags = set()
    for flag in flags:
        s0, s1, boost = flag2list(flag)
        speed = 1 << boost
        for i in s0:
            newflag = flag | (1 << i)
            path[newflag][i] = min(path[newflag][i], min([path[flag][j] + dist[j][i] / speed for j in s1]))
            newflags.add(newflag)
    flags = newflags

allflag = (1 << n) - 1
cost = []
for i in range(1 << m):
    flag = i << n | allflag
    s0, s1, boost = flag2list(flag)
    speed = 1 << boost
    currentcost = min([path[flag][i] + dist[i][nm] / speed for i in s1])
    cost += [currentcost]

print(min(cost))
