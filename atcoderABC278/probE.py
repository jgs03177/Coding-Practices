import sys

input = sys.stdin.readline

h, w, n, th, tw = map(int, input().split())
a = []  # a[h][w]
for i in range(h):
    *aa, = map(int, input().split())
    a += [aa]

dp = []
for i in range(h):
    state = [0] * n
    dp2 = [state[:]]
    for j in range(w):
        state[a[i][j] - 1] += 1
        dp2 += [state[:]]
    dp += [dp2]

tstate = [0] * n
for i in range(h):
    for k in range(n):
        tstate[k] += dp[i][w][k]

out = []
for j in range(w - tw + 1):
    state = tstate[:]
    val = 0
    for k in range(n):
        for i in range(th):
            state[k] -= dp[i][j + tw][k] - dp[i][j][k]
        val += state[k] != 0
    out2 = [val]
    for i in range(th, h):
        val = 0
        for k in range(n):
            state[k] += dp[i - th][j + tw][k] - dp[i - th][j][k]
            state[k] -= dp[i][j + tw][k] - dp[i][j][k]
            val += state[k] != 0
        out2 += [val]
    out += [out2]

for i in range(h - th + 1):
    for j in range(w - tw + 1):
        print(out[j][i], end=" ")
    print()
