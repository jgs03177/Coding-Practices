import sys

input = sys.stdin.readline

mod=1_000_000_007

n, k = map(int, input().split())

def pwrmod(a,b):
    o = 1
    a = a % mod
    mul = a
    while b > 0:
        if b%2:
            o = mul * o % mod
        b >>= 1
        mul = mul * mul % mod
    return o


l = [1]
last = 1
for i in range(500002):
    last = last * (i+1) % mod
    l.append(last)


def nck(n, r):
    if r > n:
        return 0
    k = n - r
    numer = l[n]
    denom1 = l[r]
    denom2 = l[k]
    denom = denom1 * denom2 % mod
    sol = numer * pwrmod(denom,mod-2) % mod
    return sol

print(sum([nck(n,i) for i in range(0,min(k,n)+1)])%mod)
