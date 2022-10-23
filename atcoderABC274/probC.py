import sys

input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())
l = [0] * (2 * n + 2)
for i, e in enumerate(a, 1):
    l[i * 2] = l[e] + 1
    l[i * 2 + 1] = l[e] + 1
print(*l[1:], sep="\n")
