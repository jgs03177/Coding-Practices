import sys

input = sys.stdin.readline

ntc = int(input())

for t in range(ntc):
    m, n, p = map(int, input().split())
    s = []
    john = None
    for i in range(1, m + 1):
        *ss, = map(int, input().split())
        if i == p:
            john = ss
        else:
            s += [ss]
    o = sum([max(max([s[i][j] for i in range(m - 1)]) - john[j], 0) for j in range(n)])
    print(f"Case #{t + 1}: {o}")
