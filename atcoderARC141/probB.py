import sys,math
input=sys.stdin.readline

n,m=map(int,input().split())
mod = 998244353

nd = int(math.log(m,2))
twoi=[1<<i for i in range(nd+1)]
dp=[(m-twoi[nd]+1) % mod]
for i in range(nd):
    dp+=[twoi[nd-1-i] % mod]
if n>60:
    print(0)
else:
    for i in range(n-1):
        dp2=[]
        pf = 0
        for i in range(nd+1):
            dp2 += [pf * twoi[nd-i] % mod]
            pf = (pf + dp[i]) %mod
        dp=dp2
    print(sum(dp)%mod)