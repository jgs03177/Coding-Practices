import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    mat = []
    for i in range(n * n // 2):
        mat += [i + 1, n * n - i]
    if n & 1:
        mat += [n * n // 2 + 1]
    for i in range(n):
        print(*mat[i * n:i * n + n][::-1 if i & 1 else 1])
