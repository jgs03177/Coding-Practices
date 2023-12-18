
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    *a, = map(int, input().split())
    l = [(-((a[i] - 1) % k), i) for i in range(n)]
    l.sort()
    print(*[e[1] + 1 for e in l])
