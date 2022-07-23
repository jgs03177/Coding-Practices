n, m, k = map(int, input().split())
mod = 998244353

l = [1] * m
if k:
    for i in range(n - 1):
        l2 = [0] * m
        tmp = 0
        for j in range(m - k):
            tmp += l[j]
            tmp %= mod
            l2[j + k] = tmp
        tmp = 0
        for j in range(m - 1, k - 1, -1):
            tmp += l[j]
            tmp %= mod
            l2[j - k] = (l2[j - k] + tmp) % mod
        l = l2
    print(sum(l) % mod)
else:
    print(m ** n % mod)