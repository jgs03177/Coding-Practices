import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    o = 1
    s0 = input().rstrip()
    for i in range(n - 1):
        s = input().rstrip()
        if s == s0: o += 1
    print(o)
