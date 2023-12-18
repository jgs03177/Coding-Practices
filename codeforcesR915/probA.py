import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    print(max(h, w))
