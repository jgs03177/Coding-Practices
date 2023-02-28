import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, s, r = map(int, input().split())
    maxdice = s - r
    surplus = r - n + 1
    l = [maxdice]
    for i in range(n - 1):
        # surplus >= maxdice -1 -> maxdice
        # between -> 1 + surplus
        # surplus = 0 -> 1
        if surplus >= maxdice - 1:
            d = maxdice - 1
        elif surplus == 0:
            d = 0
        else:
            d = surplus
        surplus -= d
        l += [1 + d]
    print(*l)
