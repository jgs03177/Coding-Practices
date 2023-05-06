import sys

input = sys.stdin.readline

nt = int(input())
for t in range(nt):
    n = int(input())
    # 1 -> 26 * 1 chrs.
    # 2 -> 26 * 2 chrs. 26 * 3 chrs total
    # i -> 26 * i(i+1)//2 chrs total
    l, r = 1, 10 ** 7
    while l != r:
        m = (l + r) // 2
        fm = 13 * m * (m + 1)
        if n <= fm:
            r = m
        else:
            l = m + 1
    m = l
    n -= 13 * m * (m - 1)
    y = chr(ord('A') + (n - 1) // m)

    print(f"Case #{t + 1}: {y}")
