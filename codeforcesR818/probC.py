import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    *b, = map(int, input().split())

    if any([a[i]>b[i] for i in range(n)]):
        print("NO")
        continue

    # zero: inf loop
    minb = min(b)
    for i in range(n):
        a[i] = max(a[i], minb)

    minidx = 0
    for i in range(n):
        if b[i] == minb:
            minidx=i
            break

    verd = True
    for i in range(minidx, -1, -1):
        if a[i] == b[i]:
            continue
        if b[i] <= 1 + a[(i+1)%n]:
            a[i] = b[i]
        else:
            verd = False
            break

    if not verd:
        print("NO")
        continue

    for i in range(n-1, minidx, -1):
        if a[i] == b[i]:
            continue
        if b[i] <= 1 + a[(i+1)%n]:
            a[i] = b[i]
        else:
            verd = False
            break

    if not verd:
        print("NO")

    else:
        print("YES")