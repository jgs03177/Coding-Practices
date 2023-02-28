# Upsolving problem D with editorial https://codeforces.com/blog/entry/111286
"""Editorial Summary
Create a bipartite graph with a's and p's.
gcd(a_i,a_j) = p_k then we move like a_i -> p_k -> a_j.
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

# prime factor
lim = 3 * 10 ** 5 + 1
sieve = [0] * lim
for i in range(2, lim):
    if sieve[i] == 0:
        sieve[i] = i
        for j in range(i * i, lim, i):
            sieve[j] = i

n = int(input())
*a, = map(int, input().split())
s, t = map(int, input().split())
s -= 1
t -= 1

# factorize
factors = []
for e in a:
    factor = []
    while e != 1:
        p = sieve[e]
        factor += [p]
        e //= p
    factors += [factor]

pgraph = defaultdict(list)  # p -> i
agraph = factors  # i -> p
for i, factor in enumerate(factors):
    for p in factor:
        pgraph[p] += [i]

# bfs with two stacks
q = [s]
avisit = [-1] * n
pvisit = {}
distance = 1  # if distance is odd: a->p
avisit[s] = s
while q:
    newq = []
    while q:
        v = q.pop()
        if distance & 1:  # a->p
            for e in agraph[v]:
                if e in pvisit:
                    continue
                newq += [e]
                pvisit[e] = v
        else:  # p->a
            for e in pgraph[v]:
                if avisit[e] != -1:
                    continue
                newq += [e]
                avisit[e] = v
                if e == t:
                    newq = []
                    break
    q = newq
    distance += 1

if avisit[t] == -1:
    print(-1)
else:
    o = [t+1]
    c = t
    while c != s:
        c = pvisit[avisit[c]]
        o += [c+1]
    print(len(o))
    print(*o[::-1])
