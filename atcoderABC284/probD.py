import sys
import math

input = sys.stdin.readline

lim = 3 * 10 ** 6 + 1
sieve = [0] * lim
primes = []
for i in range(2, lim):
    if sieve[i] == 0:
        primes += [i]
        for j in range(i * i, lim, i):
            sieve[j] = 1

t = int(input())
for _ in range(t):
    n = int(input())
    p0 = 0
    for p in primes:
        if n % p == 0:
            p0 = p
            break
    if (n // p0) % p0 == 0:
        q = n // p0 // p0
        p = p0
    else:
        q = p0
        p = math.isqrt(n // p0)
    print(p, q)
