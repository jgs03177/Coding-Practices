import sys

input = sys.stdin.readline

n, q = map(int, input().split())
ls = []
for i in range(n):
    _, *l, = map(int, input().split())
    ls += [l]
for i in range(q):
    s, t = map(int, input().split())
    print(ls[s - 1][t - 1])
