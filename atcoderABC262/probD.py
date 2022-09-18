# see editorial
import sys

input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())

mod = 998244353

tot = 0
for l in range(1, n + 1):  # pick total 1~n numbers
    re = [e % l for e in a]  # remainder mod l
    nr = [[[0] * l for _ in range(l + 1)] for _ in range(n + 1)]
    # nr[j][k][i] number of remainder==i mod l when we picked k numbers in a[:j+1]
    nr[0][0][0] = 1
    for j in range(n):  # picked number idx
        for k in range(l + 1):  # currently picked k numbers.
            for i in range(l):  # remainders
                nr[j + 1][k][i] += nr[j][k][i]  # increase idx
                complement = (i - re[j]) % l
                if k != l:
                    nr[j + 1][k + 1][i] = (nr[j + 1][k + 1][i] + nr[j][k][complement]) % mod
    tot = (tot + nr[n][l][0]) % mod
print(tot)
