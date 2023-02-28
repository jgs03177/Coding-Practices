import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    *b, = map(int, input().split())
    *c, = map(int, input().split())
    # find missing number in a,b,c
    m = []
    for l in (a, b, c):
        p = [0] * n
        for e in a:
            p[e - 1] = 1
        for i, e in enumerate(p):
            if not e:
                m += [i + 1]
                break
    l = []
    # 4 2 1  4 1 3
    # 4 1 3  4 2 1
    for i in range(n - 1):
        if a[i] != b[i]:
            # 4 2 1  4 2 3
            if (i == n - 2) or a[i + 1] == b[i + 1]:
                if (i != n - 2 and b[i] == c[i] and a[i] == c[i + 1]) or (i != 0 and b[i] == c[i - 1] and a[i] == c[i]):
                    e = [b[i], a[i]]
                else:
                    e = [a[i], b[i]]
                l = a[:i] + e + a[i + 1:]
            else:
                # 4 2 1  2 1 3
                if a[i + 1] == b[i]:
                    l = a[:i + 1] + b[i:]
                else:
                    l = b[:i + 1] + a[i:]
            break

    for i in range(n - 3):
        input()
    print(*l)
