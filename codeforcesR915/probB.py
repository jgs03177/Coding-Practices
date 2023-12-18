import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    deg = [0] * n
    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        deg[u] += 1
        deg[v] += 1
    leaves = 0
    for e in deg:
        if e == 1:
            leaves += 1
    print((leaves + 1) // 2)
