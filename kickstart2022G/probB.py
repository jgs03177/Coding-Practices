import sys

input = sys.stdin.readline

ntc = int(input())

for t in range(ntc):
    rs, rh = map(int, input().split())
    r2 = (rs + rh) * (rs + rh)
    q = []
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        d2 = x * x + y * y
        if d2 <= r2:
            q += [(d2, 0)]  # 0 means red team
    m = int(input())
    for _ in range(m):
        z, w = map(int, input().split())
        d2 = z * z + w * w
        if d2 <= r2:
            q += [(d2, 1)]  # 1 yellow
    q.sort()
    scores = [0, 0]
    winner = -1
    if q:
        winner = q[0][1]
    for e in q:
        if e[1] != winner:
            break
        scores[winner] += 1
    y, z = scores
    print(f"Case #{t + 1}: {y} {z}")
