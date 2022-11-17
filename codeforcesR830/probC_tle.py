import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    *a, = map(int, input().split())
    csum = 0
    psum = [0]
    cxor = 0
    pxor = [0]
    for e in a:
        csum += e
        cxor ^= e
        psum += [csum]
        pxor += [cxor]
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        maxf = -1
        maxi = 0
        maxj = 0
        minlen = 1
        for i in range(n):  # a[i~j] inclusive
            for j in range(i + 1, n + 1):
                f = psum[j] - psum[i] - (pxor[j] ^ pxor[i])
                if (f, -j + i) > (maxf, -minlen):
                    minlen = j - i
                    maxf = f
                    maxi = i
                    maxj = j
        print(f"{maxi + 1} {maxj}")
