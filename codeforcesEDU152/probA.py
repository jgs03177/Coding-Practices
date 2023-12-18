import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    b, c, h = map(int, input().split())
    o = min(b - 1, c + h) * 2 + 1
    print(o)
