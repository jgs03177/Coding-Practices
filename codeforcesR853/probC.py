import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    *a, = map(int, input().split())  # pairwise distinct (unique elems)
    appear = [0] * (n + m)
    for e in a:
        appear[e - 1] = m + 1
    for i in range(m):
        # i-th change-> m-i appearances
        p, v = map(int, input().split())  # a[p]=v, always unique elems
        appear[a[p - 1] - 1] -= m - i
        appear[v - 1] += m - i
        a[p - 1] = v
    o = 0
    for e in appear:
        o += e * m - e * (e - 1) // 2
    print(o)
