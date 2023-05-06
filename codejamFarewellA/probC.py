import sys

input = sys.stdin.readline

nt = int(input())
for t in range(nt):
    n = int(input())
    *s, = map(int, input().split())
    prv = None
    q = []
    mem = set()
    y = 1
    for e in s:
        if prv != e:
            if e in mem:
                y = 0
                break
            prv = e
            mem.add(e)
            q += [e]
    y = ' '.join(map(str, q)) if y else 'IMPOSSIBLE'
    print(f"Case #{t + 1}: {y}")
