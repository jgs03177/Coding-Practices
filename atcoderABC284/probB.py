import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    o = 0
    n = int(input())
    *a, = map(int, input().split())
    for e in a:
        o += e & 1
    print(o)
