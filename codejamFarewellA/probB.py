import sys

input = sys.stdin.readline

nt = int(input())
for t in range(nt):
    # road's length, light's radius, #bulbs
    m, r, n = map(int, input().split())
    *x, = map(int, input().split())
    # memorize enlighten area
    # and the position of the next candidate bulb
    la = 0
    cb = None
    nb = 0
    y = 1
    for e in x:
        if e <= la + r:
            cb = e
        elif cb is not None and e <= cb + r + r:
            la = cb + r
            cb = e
            nb += 1
        else:
            y = 0
            break

    if y:
        if la >= m:
            pass
        elif cb + r >= m:
            nb += 1
        else:
            y = 0
    y = str(nb) if y else 'IMPOSSIBLE'
    print(f"Case #{t + 1}: {y}")
