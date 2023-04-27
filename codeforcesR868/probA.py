import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    o = 0
    a = 0
    b = 0
    for i in range(n):
        a = i
        b = n - i
        if a * (a - 1) // 2 + b * (b - 1) // 2 == k:
            o = 1
            break
    if o:
        print("YES")
        print(*([1] * a + [-1] * b))
    else:
        print("NO")
