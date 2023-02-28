# Upsolving problem C with editorial https://codeforces.com/blog/entry/111286
"""Editorial Summary
Observation
n and n+1 and ... and m = x
=> n, n+1, ..., m \superset x
<=> n and x = x

Therefore:
If n and x != x, then answer is -1.
If n and x = x, then zerofy bits only in n&(~x).
    For each 1 bit in n (say i-th), find the minimum number (m_i) >= n that makes the bit 0.
    If that bit is in x (i.e. n&x), then m_i > m.
    If not in x (i.e. n&~x), then m_i <= m.
"""

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    # 0 <= n, x <= 10**18 ; m < 5 * 10**18
    # log2(n), log2(x) < 60 ; log2(m) < 63
    if n & x != x:
        print(-1)
        continue
    mask = 0
    m_atmost = 1 << 63  # x has i
    m_atleast = n  # x does not have i
    for i in range(63):
        if n >> i & 1:
            m = n + (1 << i) - (n & ((1 << i) - 1))
            if x >> i & 1:  # x has i
                m_atmost = min(m_atmost, m)
            else:  # x does not have i
                m_atleast = max(m_atleast, m)
    print(m_atleast if m_atleast < m_atmost else -1)
