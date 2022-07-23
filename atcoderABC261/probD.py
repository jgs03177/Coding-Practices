import sys
input=sys.stdin.readline

n,m=map(int,input().split())

*xs,=map(int,input().split())

ys=[0]*5001
for i in range(m):
    c,y=map(int,input().split())
    ys[c]=y

dp=[0]

for i in range(n):
    x = xs[i]
    dp2 = [max(dp)]
    dp+=[0]
    for j in range(i+1):
        dp2 += [max(dp[j+1], dp[j] + x + ys[j+1])]
    dp = dp2
print(max(dp))