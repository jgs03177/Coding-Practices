import sys

input = sys.stdin.readline

n, k = map(int, input().split())
*a, = map(int, input().split())

print(*(a[min(k, n):] + [0] * min(k, n)))
