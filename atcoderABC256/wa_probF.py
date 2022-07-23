# https://atcoder.jp/contests/abc256/tasks/abc256_f

import sys
input=sys.stdin.readline

mod = 998244353
n,nq=map(int,input().split())
*a,=map(int,input().split())
prvd=0
d=lambda i: i*(i+1)*(i+2)//6

for i in range(n):
    prvd=(prvd+a[i]*d(n-i))%mod

for _ in range(nq):
    *q,=map(int,input().split())
    if q[0]==1:
        i=q[1]-1
        b=q[2]
        prvd=(prvd+a[i]*d(n-i))%mod

