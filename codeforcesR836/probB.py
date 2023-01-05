import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    if n & 1:
        print(*[n] * n)
    else:
        print(*[n + 1] * (n - 1), 1)
