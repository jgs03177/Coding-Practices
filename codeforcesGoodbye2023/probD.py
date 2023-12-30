import sys
from math import isqrt

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    i10 = 10 ** (n - 1)
    o = []
    j10 = 1
    for j in range(n - 2):
        k10 = j10
        for k in range(j + 1, n - 1):
            k10 *= 10
            for a, b, c in [(1, 6, 9), (1, 9, 6), (6, 1, 9), (6, 9, 1), (9, 1, 6), (9, 6, 1)]:
                candidate = a * i10 + b * j10 + c * k10
                if isqrt(candidate) ** 2 == candidate:
                    o += [candidate]
        j10 *= 10
    print(*o[:n])

from collections import defaultdict


def observation(n):
    storage = defaultdict(set)
    for i in range(10 ** (n // 2), int(10 ** (n // 2) * 3.2) + 1):
        e = i ** 2
        if e > 10 ** n:
            break
        se = str(e)
        counter = [0] * 10
        for c in se:
            counter[ord(c) - ord('0')] += 1
        storage[tuple(counter)].add(e)
    print(storage)
    for k, v in storage.items():
        if len(v) >= n:
            print(v)
