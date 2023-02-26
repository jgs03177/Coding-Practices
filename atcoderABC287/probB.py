import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for i in range(n):
    s = int(input())
    l += [s]
d = set()
for i in range(m):
    t = int(input())
    d |= {t}
o = 0
for s in l:
    if s % 1000 in d:
        o += 1
print(o)
