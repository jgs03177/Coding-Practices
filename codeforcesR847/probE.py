# Problem E upsolving with editorial: https://codeforces.com/blog/entry/111948
"""Editorial summary
To always make a^b=x, start from a=x, b=0 (a+b=x, a^b=x).
To make a+b=2x, greedily add bits to both a and b msb first (because its binary),
Which ends to a+=x//2, b+=x//2.
"""

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x = int(input())
    a = x + x // 2
    b = x // 2
    if a + b == 2 * x and a ^ b == x:
        print(a, b)
    else:
        print(-1)
