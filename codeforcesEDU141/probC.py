import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    *a, = map(int, input().split())
    b = sorted(a)
    times = 0
    lasttime = 0
    wins = 0
    for e in b:
        if times + e <= m:
            times += e
            lasttime = e
            wins += 1
        else:
            break
    bonus = (a[wins] <= m - times + lasttime) if wins < n else 0
    print(n + 1 - wins - bonus)
