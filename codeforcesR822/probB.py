import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(n):
        o = [0] * (i + 1)
        o[0] = 1
        o[-1] = 1
        print(*o)
