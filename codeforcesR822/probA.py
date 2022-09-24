import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    o = float("inf")
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                da = abs(a[i] - a[j]), abs(a[j] - a[k]), abs(a[k] - a[i])
                o = min(o, da[0] + da[1], da[1] + da[2], da[2] + da[0])
    print(o)
