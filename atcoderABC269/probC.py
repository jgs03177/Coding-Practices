import sys

input = sys.stdin.readline

n = int(input())
n2 = n
d = 0
ds = []
while n2:
    if n2 & 1:
        ds += [d]
    n2 >>= 1
    d += 1

for i in range(2 ** len(ds)):
    o = 0
    d = 0
    while i:
        if i & 1:
            o += 2 ** ds[d]
        i >>= 1
        d += 1
    print(o)
