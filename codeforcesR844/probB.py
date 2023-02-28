import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    c = [0] * n
    for e in a:
        c[e] += 1
    go = 0
    o = 1
    acc = 0
    for i in range(n):
        if i <= go:  # at least i people already go
            go += c[i]
        elif i < go + acc + c[i]:  # currently less than i people go, but if i go, then at least i+1 people go
            go += c[i] + acc
            acc = 0
            o += 1
        else:
            acc += c[i]
    print(o)
