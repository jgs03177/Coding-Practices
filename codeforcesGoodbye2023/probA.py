import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, a = map(int, input().split())
    *b, = map(int, input().split())
    s = 1
    for e in b:
        s *= e
    r = 2023 // s
    if r * s != 2023:
        print("NO")
    else:
        print("YES")
        print(r, *[1] * (a - 1))
