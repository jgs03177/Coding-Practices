import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    *x, = map(int, input().split())
    *c, = map(int, input().split())

    # xyzxyz... is not a palindrome
    o = "xyz"
    idx = 0
    xp, cp = 3, 3
    for i in range(k):
        xi, ci = x[i], c[i]
        xd, cd = xi - xp, ci - cp
        if xd < cd:
            o = None
            break
        o += chr(ord("a") + i) * cd
        rem = xd - cd
        while rem > 0 and idx != 0:
            o += "xyz"[idx]
            rem -= 1
            idx = (idx + 1) % 3
        # naively extending o gives TLE, so...
        o += "xyz" * (rem // 3)
        rem %= 3
        while rem > 0:
            o += "xyz"[idx]
            rem -= 1
            idx = (idx + 1) % 3
        xp, cp = xi, ci
    if o is not None:
        print("YES")
        print(o)
    else:
        print("NO")
