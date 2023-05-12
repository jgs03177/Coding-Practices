import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n % 2 == 1:
        print(-1)
    else:
        print(*[e for l in zip(range(2, n + 1, 2), range(1, n + 1, 2)) for e in l])
