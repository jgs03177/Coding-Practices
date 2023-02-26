import sys

input = sys.stdin.readline

mod = 998244353

n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a += [ai]
    b += [bi]

c = 1, 1
for i in range(1, n):
    c1 = 0
    c2 = 0
    if a[i - 1] != a[i]:
        c1 += c[0]
    if a[i - 1] != b[i]:
        c2 += c[0]
    if b[i - 1] != a[i]:
        c1 += c[1]
    if b[i - 1] != b[i]:
        c2 += c[1]
    c = c1 % mod, c2 % mod
print(sum(c) % mod)
