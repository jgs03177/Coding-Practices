import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

maxsieve = 10_000_001
sieve = [0] * maxsieve
# loop until sqrt(maxsieve) is also possible, but requires a little bit of code change
for i in range(2, maxsieve):
    if sieve[i] == 0:
        sieve[i] = i
        for j in range(i * i, maxsieve, i):
            sieve[j] = i

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    primecounter = defaultdict(int)
    for e in a:
        while e != 1:
            p = sieve[e]
            primecounter[p] += 1
            e //= p

    twos = 0
    rems = 0
    for e in primecounter.values():
        q, r = divmod(e, 2)
        twos += q
        rems += r
    o = twos + rems // 3
    print(o)
