# https://atcoder.jp/contests/abc254/tasks/abc254_d
# see https://atcoder.jp/contests/abc254/submissions/32430343
# mine is slower
import math

n = int(input())

sieve = [1] * (n + 1)
prime = []

for p in range(2, n + 1):
    if sieve[p]:
        prime += [p]
        for i in range(p + p, n + 1, p):
            sieve[i] = 0


def f(n):
    bound = math.isqrt(n) + 1
    result = 0
    for k in range(1, n + 1):
        squarefree = True
        for p in prime:
            if p >= bound:
                break
            if k % (p * p) == 0:
                squarefree = False
                break
        if squarefree:
            result += math.floor((n / k) ** 0.5) ** 2
    return result


print(f(n))