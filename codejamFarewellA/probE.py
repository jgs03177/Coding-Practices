import sys

input = sys.stdin.readline

nt = int(input())
for t in range(nt):
    c = input().rstrip()
    # dp-memorize prv rps
    dp = [[0, 1001, 1001], [1001, 0, 1001], [1001, 1001, 0]]

    # dp[i][j] stores current min val of [j], and must end with [i].
    for e in c:
        newdp = []
        for l in dp:
            r, p, s = l
            nr = min(p, s) + (e != "R")
            np = min(r, s) + (e != "P")
            ns = min(r, p) + (e != "S")
            newdp += [[nr, np, ns]]
        dp = newdp
    y = min(dp[0][0], dp[1][1], dp[2][2])
    print(f"Case #{t + 1}: {y}")
