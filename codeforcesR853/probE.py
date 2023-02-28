# Problem E upsolving with editorial and other competitor's code: https://codeforces.com/blog/entry/113246
"""Editorial rephrase
Problem
f(x) is the number of i that p_i, q_i exists where s_i = p_i floor(s_n/x) + q_i ceil(s_n/x).
find sum_{x=1}^{s_n} x f(x) mod 998_244_353.

Editorial
We define f_i(x) = 1 if p_i, q_i exists where s_i = p_i floor(s_n/x) + q_i ceil(s_n/x), else 0.
Then f(x) = sum_{i=1...n} f_i(x).
o = sum_{x=1...s_n} x f(x) mod p
  = sum_{x=1...s_n} x sum_{i=1...n} f_i(x) mod p

To find x such that f_i(x)=1, let k = s_n // x.
Suppose f_i(x)=1. Divide two cases:

1. x !| s_n -> s_i = a_i * k + b_i  (b_i <= a_i)
Since a_i = s_i // k, b_i = s_i % k, we know s_i // k >= s_i % k
If s_i is in the interval ( [(j-1)k + i , jk - 1] for j in range(k), both inclusive ), then a_i, b_i does not exist.
To calculate f(x), count s_i in the interval using prefix sum of presence of s_i.

2. x | s_n -> let s_n = x * k. then s_i = a_i * k, therefore k | s_i and k | s_n.
Count s_i for k*j, j=1,2,... .
"""
import sys

input = sys.stdin.readline

mod = 998244353

t = int(input())

for _ in range(t):
    n = int(input())
    *s, = map(int, input().split())
    m = s[-1]
    pref = [0] * (m + 2)
    for e in s:
        pref[e+1] += 1        # Due to MLE, use in-place prefix sum
    for i in range(m+1):
        pref[i+1] += pref[i]  # pref[j] - pref[i] = sum(s_freq[i:j])
    prv = -1, -1
    c = 0
    o = 0
    for x in range(1, m + 1):
        v1, v2 = m // x, (m - 1) // x + 1  # v1 = floor(m/x), v2 = ceil(m/x)
        if prv != (v1, v2):  # caching
            if v1 == v2:  # x | m
                c = 0
                for j in range(v1, m+1, v1):
                    c += pref[j+1] - pref[j]
            else:  # x !| m
                c = pref[m+1] - pref[min(v1 * v2 + 1, m+1)]  # sum(s_freq[v1*v2+1:])
                k = 1
                for j in range(v2, v1 * v2 + 1, v2):
                    c += pref[min(j+1, m+1)] - pref[min(j-k, m+1)]  # sum(s_freq[j-k:j])
                    k += 1
            prv = v1, v2  # memoize!
        o = (o + c * x) % mod
    print(o)
