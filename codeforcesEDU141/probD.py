import sys

input = sys.stdin.readline

n = int(input())
a0, *a = map(int, input().split())

mod = 998244353
p = 90000
dp = [0] * (2 * p + 1)
dp[a[0] + p] = 1
dp2 = [0] * (2 * p + 1)
dp3 = [0] * (2 * p + 1)
for e in a[1:]:
    for i in range(2 * p + 1):
        dp2[i] = dp[i - e] % mod if 0 <= (i - e) else 0
        dp3[i] = dp[i + e] % mod if (i + e) <= 2 * p else 0
    for i in range(2 * p + 1):
        dp[i] = (dp2[i] + dp3[i]) % mod if i != p + e else dp3[i]
print(sum(dp) % mod)
