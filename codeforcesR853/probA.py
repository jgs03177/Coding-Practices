import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    o = 0
    for i in range(1, n):
        for j in range(i):
            o |= math.gcd(a[i], a[j]) <= 2
    print("YES" if o else "NO")
