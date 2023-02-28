# Problem D upsolving with editorial: https://codeforces.com/blog/entry/113246
"""Editorial summary
If a==0==b or a!=0!=b then the solution exists.
Match the LSB/MSB of b with a by shift. Use msb of a and lsb of a to recreate b.
"""

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().rstrip()
    b = input().rstrip()
    aa = 0
    bb = 0
    for i in range(n):
        aa += (a[i] == "1") << (n - i - 1)
        bb += (b[i] == "1") << (n - i - 1)

    mask = (1 << n) - 1


    def ixsh(x, i):
        """in-place xor shift"""
        x ^= ((x << i) & mask) if i > 0 else x >> -i
        return x


    if aa == 0 == bb:
        print(0)
    elif aa != 0 != bb:
        o = []
        # find lsb of a and b
        lsbb = 0
        for i in range(n):
            if (bb >> i) & 1:
                lsbb = i
                break
        lsba = 0
        for i in range(n):
            if (aa >> i) & 1:
                lsba = i
                break
        # set aa[lsbb]=1  # aa[i] means i-th rightmost bit (0-based idx) of aa
        if (aa >> lsbb) & 1 == 0:
            aa = ixsh(aa, lsbb - lsba)
            o += [lsbb - lsba]
            if lsba > lsbb:
                lsba = lsbb
        # copy aa[n-1:lsbb] = bb[n-1:lsbb] with lsba # aa[i:j] means aa[i]...aa[j+1]
        for i in range(lsbb + 1, n):
            if ((aa >> i) & 1) != ((bb >> i) & 1):
                aa = ixsh(aa, i - lsba)
                o += [i - lsba]
        # find msb of a
        msba = 0
        for i in range(n - 1, -1, -1):
            if (aa >> i) & 1:
                msba = i
                break
        # zerofy aa[lsbb-1:-1] with msba
        for i in range(lsbb - 1, -1, -1):
            if (aa >> i) & 1:
                aa = ixsh(aa, i - msba)
                o += [i - msba]
        print(len(o))
        if o:
            print(*o)
    else:
        print(-1)
