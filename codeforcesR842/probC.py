import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    arr = [0] * n
    pos = [[] for _ in range(n)]
    for i in range(n):
        e = a[i]
        arr[e - 1] += 1
        pos[e - 1] += [i]
    free = 0
    verdict = True
    for e in range(n):
        free += 1
        if arr[e] > 2 or arr[e] > free:
            verdict = False
            break
        free -= arr[e]
    if not verdict:
        print("NO")
        continue
    # if arr[e-1]==2: place e on q side, place x on p side where arr[x]==0.
    # if arr[e-1]==1: place e on p side, place x on q side where arr[x]==1 or 0.
    p = [0] * n
    q = [0] * n
    pfree = []  # 0
    qfree = []  # 1 or 0
    for e in range(n):
        if arr[e] <= 1:
            qfree += [e + 1]
        if arr[e] == 0:
            pfree += [e + 1]
    for e in range(n - 1, -1, -1):
        if arr[e] == 2:
            q[pos[e][1]] = e + 1
            p[pos[e][1]] = pfree.pop()
        if arr[e] >= 1:
            p[pos[e][0]] = e + 1
            q[pos[e][0]] = qfree.pop()
    print("YES")
    print(*p)
    print(*q)
