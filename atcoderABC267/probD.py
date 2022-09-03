import sys

input = sys.stdin.readline

n,m = map(int, input().split())
*a, = map(int, input().split())

# dp[k][l] selecting 0,1,...,k elems in a[0:l]
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(m): # select
    dp[i+1][i+1] = sum([(e+1)*a[e] for e in range(i+1)])
    for j in range(i+1,n): # elem
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j] + (i+1)*a[j])
print(dp[m][n])