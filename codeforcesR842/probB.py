import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    *p, = map(int, input().split())
    target = 1
    re = 0
    for e in p:
        if e == target:
            target += 1
        else:
            re += 1
    print(math.ceil(re / k))
