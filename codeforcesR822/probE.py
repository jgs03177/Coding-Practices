import sys

input = sys.stdin.readline

n = int(input())
*b, = map(int, input().split())

for i in range(n):
    print(*[(b[i] + i * j - j * j) % n for j in range(n)])
